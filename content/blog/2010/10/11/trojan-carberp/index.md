---
title: "Trojan Carberp"
authors: ["Guido Landi"]
date: "2010-10-11"
tags: 
  - "carberp"
  - "trojan"
  - "zeus"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

I'm interested in infostealers and specifically in banking-trojans so I didn't want to miss [this one](http://www.trustdefender.com/blog/2010/10/06/carberp-%E2%80%93-a-new-trojan-in-the-making/). Samples of Carberp are floating around at least since last spring but in late September we saw such numbers increasing.  
  
Taking a look at how Carberp hooks API it looks like yet another Zeus "clone". What I found interesting is how it hooks system calls. This is how a normal syscall looks like  
`  
MOV EAX,0xce // ZwResumeThread syscall id  
MOV EDX,0x7FFE0300 // pointer to KiFastSystemCall  
CALL DWORD PTR DS:[EDX]  
RETN 0x8  
`  
And this is how the hooked syscall looks like  
`  
MOV EAX,0xce  
MOV EDX,0x00152958 // pointer to fake KiFastSystemCall  
CALL DWORD PTR DS:[EDX]  
RETN 0x8  
`  
Instead of overwriting the first instruction(s) with a JMP/CALL to redirect the execution flow to the hook, Carberp substitutes the pointer to KiFastSystemCall. This is nothing new but it is actually enough to hide such hook from most of the "anti-rootkit" products out there (including rkunhooker).
