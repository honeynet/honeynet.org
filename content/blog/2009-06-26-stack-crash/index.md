---
title: "stack crash?"
date: "2009-06-26"
tags: 
  - "qebek-windows"
---

This phenomenon is first observed when I tried the NtReadFile test last week, sometimes when the postNtReadFile is called, the handle value, buffer address and buffer size got from the stack is quite different from values got in preNtReadFile. I didn't pay much attention to this problem that time, but, when I tried to debug the NtSecureConnectPort API with WinDBG today, this phenomenon appeared again. So I did a further study on it.

  

  

First, I set a break point at nt!NtSecureConnectPort:

  

  

kd> bp nt!NtSecureConnectPort  
kd> bl  
 0 e 80599128     0001 (0001) nt!NtSecureConnectPort  
kd> g  
Breakpoint 0 hit  
nt!NtSecureConnectPort:  
80599128 6884000000      push    84h  
kd> r esp  
esp=f5f3ed14  
kd> dd esp  
f5f3ed14  805999b8 001532f0 00aef5c8 00aef5d0  
f5f3ed24  00000000 00000000 00000000 00000000  

  

  

Then I set a break point at the return address 0x80599b8:

  

  

kd> bp 805999b8  
kd> g  
Breakpoint 1 hit  
nt!NtConnectPort+0x24:  
805999b8 5d              pop     ebp  

  

  

But this time when I tried to view the stack information, it seems that the stack has been crashed:

  

  

kd> r esp  
esp=f5f3ed3c  
kd> dd f5f3ed14  
f5f3ed14  ffffffff 00000030 f5f3ed64 00aef5b8  
f5f3ed24  80599994 f5f3ed3c 00000000 805999b9  
f5f3ed34  00000008 00000246 f5f3ed64 8053d648  

  

  

This is so strange. So I set a write break point at the place where the handle pointer is saved:

  

  

kd> ba w 4 f5f3ed18  
kd> g  
Breakpoint 2 hit  
nt!KiTrap03+0xf:  
8053e703 bb30000000      mov     ebx,30h  

  

  

I don't know what nt!KiTrap03 is, and there is no useful call stack information. Luckily, the Google result leaded me to this [book](http://books.google.com/books?id=aimxHAHHe1IC&pg=PA148&lpg=PA148&dq=nt!KiTrap03&source=bl&ots=eEPeTDcZzk&sig=rR_0cYxZr9UdrfbQcDuQeWB1EuU&hl=en&ei=zf9ESsbeLdOBkQWKv9S1Dw&sa=X&oi=book_result&ct=result&resnum=1), which told me this function is the interrupt handler for `int 3`. So I followed the book's guide.

  

  

kd> dds esp esp+100  
f5f3ed18  00150030  
f5f3ed1c  f5f3ed64  
f5f3ed20  00aef5b8  
f5f3ed24  80599994 nt!NtConnectPort  
f5f3ed28  f5f3ed3c  
f5f3ed2c  00000000  
f5f3ed30  805999b9 nt!NtConnectPort+0x25  
f5f3ed34  00000008  
f5f3ed38  00000246  
f5f3ed3c  f5f3ed64  
f5f3ed40  8053d648 nt!KiFastCallEntry+0xf8  
...  

  

  

Still didn't get much useful information. However, one interesting thing caught my sight: the original call stack is like following when NtSecureConnectPort is called.

  

  

kd> k  
ChildEBP RetAddr    
f5f3ed10 805999b8 nt!NtSecureConnectPort  
f5f3ed3c 8053d648 nt!NtConnectPort+0x24  
f5f3ed3c 7c90e514 nt!KiFastCallEntry+0xf8  
00aef58c 7c90d05a ntdll!KiFastSystemCallRet  
00aef644 7c91150e ntdll!NtConnectPort+0xc  
00aef6b8 77ea19ef ntdll!RtlpAllocateDebugInfo+0x49  

  

  

This means the NtSecureConnectPort is not directly called by KiFastCallEntry, the system service dispatcher, but is called by NtConnectPort. So I checked the disassembled code of NtConnectPort.

  

  

nt!NtConnectPort:  
80599994 8bff            mov     edi,edi  
80599996 55              push    ebp  
80599997 8bec            mov     ebp,esp  
80599999 ff7524          push    dword ptr \[ebp+24h\]  
8059999c ff7520          push    dword ptr \[ebp+20h\]  
8059999f ff751c          push    dword ptr \[ebp+1Ch\]  
805999a2 ff7518          push    dword ptr \[ebp+18h\]  
805999a5 6a00            push    0  
805999a7 ff7514          push    dword ptr \[ebp+14h\]  
805999aa ff7510          push    dword ptr \[ebp+10h\]  
805999ad ff750c          push    dword ptr \[ebp+0Ch\]  
805999b0 ff7508          push    dword ptr \[ebp+8\]  
805999b3 e870f7ffff      call    nt!NtSecureConnectPort (80599128)  
805999b8 5d              pop     ebp  
805999b9 c22000          ret     20h  

  

  

So this system service really doesn't do much things besides calls NtSecureConnectPort which requires one more parameter, ServerSid. So I checked the stack when NtSecureConnectPort returns.

  

  

kd> g  
Breakpoint 1 hit  
nt!NtConnectPort+0x24:  
805999b8 5d              pop     ebp  
kd> dd esp  
f5f3ed3c  f5f3ed64 8053d648 001532f0 00aef5c8  
f5f3ed4c  00aef5d0 00000000 00000000 00000000  
f5f3ed5c  00aef5f8 00aef5e0 00aef6b8 7c90e514  

  

  

Compares with the stack when NtSecureConnectPort is called, these values seems to be fine.

  

  

### Conclusion

  

  

Although I still didn't figure out why the stack is crashed, at least I know this phenomenon seems only appears when a system service is called directly inside the kernel. When NtSecureConnectPort is called directly by KiFastCallEntry, the stack is fine when it returns. This won't happen when we use SSDT hook like the original Windows version Sebek. But if we switch to use kernel inline hook to improve the invisibility, we are very likely to have the same problem.

  

  

And the solution for Qebek is simple -- collects the parameter values in the precall callback function and store them in the user\_data (the new break point framework, will be introduced in another post).
