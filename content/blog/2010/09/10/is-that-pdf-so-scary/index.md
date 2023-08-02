---
title: "Is that PDF so scary?"
authors: ["Guido Landi"]
date: "2010-09-10"
tags: 
  - "aslr-d63"
  - "dep-d89"
  - "exploit-d27"
  - "pdf-d64"
  - "rop-d27"
---

  
  

>   
> \- "it bypasses DEP and ASLR using impressive tricks and unusual methods" - [Vupen](http://www.vupen.com/blog/)  
>   

  

>   
> \- "it uses a previously unpublished technique to bypass ASLR" - [Metasploit Blog](http://blog.metasploit.com/2010/09/return-of-unpublished-adobe.html)  
>   

  

>   
> \- "exploit uses the ROP technique to bypass the ASLR and DEP" - [ZDnet/Kasperky](http://www.zdnet.com/blog/security/adobe-pdf-exploits-using-signed-certificates-bypasses-aslrdep/7303)  
>   

  

>   
> \- "it's so scary I ran away screaming" - anonymous  

  
  
  
  
Is that PDF so scary? I don't think so.  
  
  
  
  
DEP is an hardware feature that prevents execution of **data**, it obviously works if software sets the execution flag only on memory pages containing **code**.  
  
  
  
If you VirtualAlloc all of your memory with PAGE\_EXECUTE\_READWRITE DEP can't help.  
If you opt-out, it can't help.  
If you disable it system-wide.. guess what.  
  
  
Is "directly executing injected data" the only way to get "arbitrary code execution"? Answer is: nope.  
  
It is possible to get "arbitrary code execution" by taking advantage of the call/return mechanism of x86. This was called [ret2libc](http://en.wikipedia.org/wiki/Return-to-libc_attack) **more than ten years ago** and it works by injecting fake stack frames instead of code. The return addresses of those stack frames are used to jump to code already in memory that belongs to main executable or libraries. By chaining stack frames, if enough functions are present in memory, you can achieve "arbitrary code execution".  
  
  
  
Since windows is pretty happy to give you memory with write and execution permissions and there are even a few api to programmatically disable DEP, there's no really need to use ret2libc to implement the entire shellcode. Instead you use it to call just a couple of functions or "pieces of functions"(gadgets) to ask for +RWX memory, copy the shellcode there, jump to it. All you need is the addresses of those functions/gadgets.  
  
  
  
Is that a DEP bypass? nope. but it's smart and convenient, isn't it?  
Is it something new, at least in the wild? nope.  
ret2what? ret2libc, but cool guys now call it ROP.  
  
  
  
ASLR is a software feature that randomizes memory allocations and should stop ret2libc because it makes hard to guess the location of a piece of code. It works if software does not give the attacker too much control over memory allocations.  
  
  
  
If software does leak pointers ASLR can't help.  
**If you don't opt-in, it can't help.**  
  
  
  
How that scary exploit works? It uses heap-spray to fill the memory with fake stack frames and ret2libc to "bypass" DEP as describe above, **the addresses of functions/gadgets used to put the shellcode in an +rwx area come from a DLL that does not opt-in to ASLR**.  
  
  
  
Is that an ASLR bypass? nope, it's sounds to me like bypassing ASLR when ASLR is disabled.
