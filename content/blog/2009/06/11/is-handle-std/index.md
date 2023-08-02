---
title: "Is Handle Std"
authors: ["Chengyu Song"]
date: "2009-06-11"
tags: 
  - "qebek-d19"
  - "qemu-d52"
  - "sebek-d10"
  - "windows-d101"
---

Sebek Windows client has two keystroke sources, one is read or write std stream, the other is csrss port. In the callback function of NtReadFile and NtWriteFile, Sebek will check if the given file handle match one of the three standard stream handles. if matches, it then logs the given data of keystrokes:

  

\_\_asm {  
  mov EAX, FS:\[18h\]  
  mov \[pTIB\], EAX  
}  
if(FileHandle == pTIB->pPEB->ProcessParameters->StandardOutput ||   
  FileHandle == pTIB->pPEB->ProcessParameters->StandardInput ||   
  FileHandle == pTIB->pPEB->ProcessParameters->StandardError)  
{ //log data }  

  

Today I'm going to show how to get these handles in QEMU. The process can be show in one statement, take stdout as an example:

  

stdout = KPRC.KPCRB->KTHREAD->TEB->PEB->ProcessParameters->StandardOutput

  

In the blog posted previously, I already showed how to get KTHREAD:  

  

kd> kd> dd 0xffdff124  
ffdff124  8177d3c8  

  

The pointer to TEB (thread environment block) is at the offset of 0x20 in KTHREAD structure under Windows XP SP3:

  

kd> dt nt!\_kthread  
   +0x000 Header           : \_DISPATCHER\_HEADER  
   +0x010 MutantListHead   : \_LIST\_ENTRY  
   +0x018 InitialStack     : Ptr32 Void  
   +0x01c StackLimit       : Ptr32 Void  
   +0x020 Teb              : Ptr32 Void  
   +0x024 TlsArray         : Ptr32 Void  
   +0x028 KernelStack      : Ptr32 Void  
   +0x02c DebugActive      : UChar  
   ...   
kd> dd 0x8177d3e8  
8177d3e8  7ffdb000  

  

The pointer to the PEB (process environment block) is at the offset of 0x30 in TEB structure:

  

kd> dt nt!\_teb  
   +0x000 NtTib            : \_NT\_TIB  
   +0x01c EnvironmentPointer : Ptr32 Void  
   +0x020 ClientId         : \_CLIENT\_ID  
   +0x028 ActiveRpcHandle  : Ptr32 Void  
   +0x02c ThreadLocalStoragePointer : Ptr32 Void  
   +0x030 ProcessEnvironmentBlock : Ptr32 \_PEB  
   +0x034 LastErrorValue   : Uint4B  
   ...  
kd> dd 0x7ffdb030  
7ffdb030  7ffd4000  

  

The pointer to ProcessParameters is at the offset of 0x10 in PEB structure:

  

kd> dt nt!\_peb  
   +0x000 InheritedAddressSpace : UChar  
   +0x001 ReadImageFileExecOptions : UChar  
   +0x002 BeingDebugged    : UChar  
   +0x003 SpareBool        : UChar  
   +0x004 Mutant           : Ptr32 Void  
   +0x008 ImageBaseAddress : Ptr32 Void  
   +0x00c Ldr              : Ptr32 \_PEB\_LDR\_DATA  
   +0x010 ProcessParameters : Ptr32 \_RTL\_USER\_PROCESS\_PARAMETERS  
   +0x014 SubSystemData    : Ptr32 Void  
   +0x018 ProcessHeap      : Ptr32 Void  
   ...  
kd> dd 0x7ffd4010  
7ffd4010  00020000  

  

Then we can read the handle value from the RTL\_USER\_PROCESS\_PARAMETERS structure:

  

kd> dt nt!\_RTL\_USER\_PROCESS\_PARAMETERS  
   +0x000 MaximumLength    : Uint4B  
   +0x004 Length           : Uint4B  
   +0x008 Flags            : Uint4B  
   +0x00c DebugFlags       : Uint4B  
   +0x010 ConsoleHandle    : Ptr32 Void  
   +0x014 ConsoleFlags     : Uint4B  
   +0x018 StandardInput    : Ptr32 Void  
   +0x01c StandardOutput   : Ptr32 Void  
   +0x020 StandardError    : Ptr32 Void  
   +0x024 CurrentDirectory : \_CURDIR  
   +0x030 DllPath          : \_UNICODE\_STRING  
   +0x038 ImagePathName    : \_UNICODE\_STRING  
   +0x040 CommandLine      : \_UNICODE\_STRING  
   +0x048 Environment      : Ptr32 Void  
   +0x04c StartingX        : Uint4B  
   +0x050 StartingY        : Uint4B  
   +0x054 CountX           : Uint4B  
   +0x058 CountY           : Uint4B  
   +0x05c CountCharsX      : Uint4B  
   +0x060 CountCharsY      : Uint4B  
   +0x064 FillAttribute    : Uint4B  
   +0x068 WindowFlags      : Uint4B  
   +0x06c ShowWindowFlags  : Uint4B  
   +0x070 WindowTitle      : \_UNICODE\_STRING  
   +0x078 DesktopInfo      : \_UNICODE\_STRING  
   +0x080 ShellInfo        : \_UNICODE\_STRING  
   +0x088 RuntimeData      : \_UNICODE\_STRING  
   +0x090 CurrentDirectores : \[32\] \_RTL\_DRIVE\_LETTER\_CURDIR  

  

Check if the process leads to correct value:

  

kd> !peb  
PEB at 7ffd4000  
    InheritedAddressSpace:    No  
    ReadImageFileExecOptions: No  
    BeingDebugged:            No  
    ImageBaseAddress:         01000000  
    Ldr                       00191e90  
    Ldr.Initialized:          Yes  
    Ldr.InInitializationOrderModuleList: 00191f28 . 00195288  
    Ldr.InLoadOrderModuleList:           00191ec0 . 00195278  
    Ldr.InMemoryOrderModuleList:         00191ec8 . 00195280  
            Base TimeStamp                     Module  
         1000000 48025c30 Apr 14 03:17:04 2008 C:\\WINDOWS\\Explorer.EXE  
        7c900000 49901d48 Feb 09 20:10:48 2009 C:\\WINDOWS\\system32\\ntdll.dll  
        7c800000 49c4f482 Mar 21 22:06:58 2009 C:\\WINDOWS\\system32\\kernel32.dll  
        77dd0000 49901d48 Feb 09 20:10:48 2009 C:\\WINDOWS\\system32\\ADVAPI32.dll  
    ...  
    WindowTitle:  'C:\\WINDOWS\\Explorer.EXE'  
    ImageFile:    'C:\\WINDOWS\\Explorer.EXE'  
    CommandLine:  'C:\\WINDOWS\\Explorer.EXE'  
    DllPath:      'C:\\WINDOWS;C:\\WINDOWS\\system32;C:\\WINDOWS\\system;C:\\WINDOWS;.;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem'  
    Environment:  00010000  
    ...  

  

Check if we can get the right WindowTitle from the ProcessParameters we got:

  

kd> dd 0x00020070   
00020070  0030002e  
kd> dd 0x00020074  
00020074  000205e4  
kd> dc 0x000205e4  
000205e4  003a0043 0057005c 004e0049 004f0044  C.:.\\.W.I.N.D.O.  
000205f4  00530057 0045005c 00700078 006f006c  W.S.\\.E.x.p.l.o.  
00020604  00650072 002e0072 00580045 00000045  r.e.r...E.X.E...  
00020614  00690057 0053006e 00610074 005c0030  W.i.n.S.t.a.0.\\.  
00020624  00650044 00610066 006c0075 00000074  D.e.f.a.u.l.t...  
00020634  003a0043 0057005c 004e0049 004f0044  C.:.\\.W.I.N.D.O.  
00020644  00530057 0045005c 00700078 006f006c  W.S.\\.E.x.p.l.o.  
00020654  00650072 002e0072 00580045 00000045  r.e.r...E.X.E...  

  

Correct & Cheers
