---
title: "Export Address Table Filtering (EMET v2)"
authors: ["Guido Landi"]
date: "2010-08-31"
tags: 
  - "eat-filtering"
  - "emet"
  - "shellcode"
---

I'll tell you the truth: Export Address Table Filtering, the feature of the [upcoming release of EMET](http://blogs.technet.com/b/srd/archive/2010/07/28/announcing-the-upcoming-release-of-emet-v2.aspx), "designed to break nearly all shell code in use today", intrigued me a bit.  
  
Since I wasn't able to find docs about the actual implementation, I started to think about how that could be done and I wrote a simple POC that uses [VirtualProtect](http://msdn.microsoft.com/en-us/library/aa366898(VS.85).aspx) to flag the relevant pages of the .data section of ntdll and kernel32 with [PAGE\_GUARD](http://msdn.microsoft.com/en-us/library/aa366549(VS.85).aspx) to intercept read operations over the [PEB.Ldr](http://undocumented.ntinternals.net/UserMode/Undocumented%20Functions/NT%20Objects/Process/PEB.html). A [Vectored Exception Handler](http://msdn.microsoft.com/en-us/library/ms681420(VS.85).aspx) is then used to handle the exception and to check if the faulting address is within the code section of a module([MEMORY\_BASIC\_INFORMATION.Type](http://msdn.microsoft.com/en-us/library/aa366775(VS.85).aspx) == MEM\_IMAGE). Here is the pseudo-code:  
  
`  
BOOL WINAPI DllMain(...)  
{  
[...]  
AddVectoredExceptionHandler(1, VectoredHandler);  
VirtualProtect(PLDR,  
PAGE_SIZE,  
PAGE_READWRITE|PAGE_GUARD,  
&old_protect);  
[...]  
}  
LONG CALLBACK VectoredHandler(  
__in PEXCEPTION_POINTERS ExceptionInfo)  
{  
[...]  
if(ExceptionInfo->ExceptionRecord->ExceptionCode ==  
STATUS_GUARD_PAGE_VIOLATION)  
{  
VirtualQueryEx(GetCurrentProcess() ,  
(LPVOID)ExceptionInfo->ExceptionRecord->ExceptionAddress,  
&lpMemInfo,  
sizeof(MEMORY_BASIC_INFORMATION)))  
  
if(lpMemInfo.Type != MEM_IMAGE)  
ShellcodeDetected();  
[...]  
`  
Yesterday I found [this .doc](http://www.microsoft.com/presspass/events/blackhat/docs/BlackHatEMETFS.docx). It explains pretty much everything: they use hardware breakpoints to intercept read operations and a Vectored Exception Handler to check if the faulting address belongs to a module.... pretty much the same thing, isn't it?  
  
Then I started to think about how EAT filtering could be bypassed, obviously there are many ways to find the address of a function without touching the EAT, but I was looking for a quick way to just fix existing shellcodes and make them working under EMET. Since EMET is going to use hardware breakpoints it will be probably faster than the PAGE\_GUARD approach because while you can put a breakpoint on a single DWORD using debug registers, the granularity of VirtualProtect is PAGE\_SIZE.  
  
But hardware registers can be zeroed out, disabling the protection, by taking advantage of the Structured Exception Handling and without even using a single API. And so, I thought, you can easily add to a metasploit shellcode something like this:  
  
`  
START:  
call +0 // poor's man get_pc()  
mov eax, [esp]  
add eax, HANDLER_OFFSET  
push eax // install SEH handler  
push fs:[0]  
mov fs:[0], esp  
xor eax, eax  
mov byte [eax], 1 // oops  
[...]  
  
HANDLER:  
xor eax, eax  
mov ebx, [esp+0xc] // context  
add [ebx+0xb8], 3 // eip += len("mov byte [eax], 1")  
mov [ecx+0x4], EAX // clean debug registers  
mov [ecx+0x8], EAX  
mov [ecx+0xc], EAX  
mov [ecx+0x10], EAX  
mov [ecx+0x14], EAX  
mov [ecx+0x18], EAX  
ret  
`  
right? Well, not quite really! Because this is not gonna work with SAFESEH enabled! :)  
  
Btw, is there a way to **quickly** disable PAGE\_GUARD using only position independent code and without touching EAT?
