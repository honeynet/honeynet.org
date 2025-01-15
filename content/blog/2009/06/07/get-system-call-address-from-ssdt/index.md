---
title: "Get system call address from SSDT"
authors: ["Chengyu Song"]
date: "2009-06-07"
categories: 
  - "analysis"
tags:
  - "qebek"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

One difference in Qebek from other existing virtualization based honeypot monitoring tool is that I want to 'hook' the function of system service instead of the dispatcher, more precisely, the 'sysenter' or 'int 2e' instruction. This is similar to the difference between SSDT (System Service Descriptor Table) hook and kernel inline hook. However, doing it this way must face a problem: how to get the function address? One way is get it directly from SSDT. Under Windows, since SDT (Service Descriptor Table) can be referenced by the exported symbol 'KeServiceDescriptorTable', this is a very simple task. So the problem for me is how to get the SDT address in QEMU without any 'symbol'.
### A Brief Introduction of SSDT and SDT

SSDT is the data structure Windows uses to store system service information.

  
```
struct SystemServiceDescriptorTable {  
        PULONG\_PTR ServiceTableBase;  
        PULONG ServiceCounterTableBase;  
        ULONG NumberOfServices;  
        PUCHAR ParamTableBase;  
};
```

It contains four elements, the first one is a pointer to the system service function address table indexed by the system service number; the second one is not used  in free build; the third one indicates the number of services and is used to check whether the given service number is valid; the last one points to the table containing the parameter size information of each system service.

SDT is then constructed with four SSDT:

```
struct ServiceDescriptorTable {  
        SystemServiceDescriptorTable ntoskrnl;  
        SystemServiceDescriptorTable used\_or\_win32k.sys;  
        SystemServiceDescriptorTable iis\_spud;  
        SystemServiceDescriptorTable unused;  
;
```

In fact, there are two SDT in Windows, the primary default one, KeServiceDescriptorTable, and another one exported by KeServiceDescriptorTableShadow. The first SSDT in both table defines the core system services, also called Native APIs, implemented in ntoskrnl.exe. The difference come in the second SSDT, which is unused in KeServiceDescriptorTable, but defines kernel-mode part ot the Windows USER and GDI services in KeServiceDescriptorTableShadow. The third SSDT is occupied by IIS SPUD driver under Windows 2000. The fourth SSDT is free to use, so one can load his own SSDT by calling KeAddSystemServiceTable to fool monitor tools depending on system service number.

About the system service number, when making system calls, the caller stores the required service number in EAX. The 13 and 14 bit of system service number indicates which SSDT to use and the last 12 bits is used as the index to access the ServiceTable and ParameterTable in the chosen SSDT.

### SDT Pointer in Thread Structure

The KTHREAD structure includes one entry (offset 0xE0) points to the SDT used by the thread. This pointer points to KeServiceDescriptorTable by default, but once the thread calls the USER or GDI service, Windows kernel changes this pointer to point to KeServiceDescriptorTableShadow. However, in my experience, the ServiceTableBase of the first SSDT (i.e. the Native API) in both SDT is the same, though the address of this two SSDT is definitely different.

### nt!KiFastCallEntry

KiFastCallEntry is the service routine (service dispatcher) for 'sysenter' instruction. There is a good article analysis the internal of this function [here](http://bbs.pediy.com/showthread.php?p=630730), though in Chinese :) Basically, what it does is save the context, load the service function address into EBX and call it. Following is the key steps to load the address, aka, how to get the service function address in QEMU.

```
mov ecx,23h  
mov ds,cx //load the new dsmov ebx,dword ptr ds:\[0FFDFF01Ch\] //EBX=KPCR.SelfPcr, ie, KPCR itselfmov esi,dword ptr \[ebx+124h\] //ESI=KTHREADmov edi,eax //EDI=system service numbershr edi,8  
and edi,30h //EDI=SSDT indexadd edi,dword ptr \[esi+0E0h\] //EDI=SSDTmov edi,dword ptr \[edi\] //EDI=SSDT->ServiceTableBasemov ebx,dword ptr \[edi+eax\*4\] //EBX=service function address  
```

So my strategy is to follow the same procedure when the first 'sysenter' instruction is issued.
