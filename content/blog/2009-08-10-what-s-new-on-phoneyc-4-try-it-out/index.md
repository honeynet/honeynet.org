---
title: "What's new on PHoneyC (4): Try it out!"
date: "2009-08-10"
tags: 
  - "gsoc-d20"
  - "libemu-d34"
  - "phoneyc-d89"
  - "shellcode-d49"
  - "spidermonkey"
---

Hi all:

  

       I have finished almost all the coding stuff of Project #1, now you can try out the new PHoneyC with shellcode/heapspray detection here:

  

  

[http://code.google.com/p/phoneyc/source/browse/phoneyc#phoneyc/branches/phoneyc-honeyjs](http://code.google.com/p/phoneyc/source/browse/phoneyc#phoneyc/branches/phoneyc-honeyjs)

  

  

        Please feel free to report any bug or suggestion on shellcode/heapspray detection to me.

  
  

  

        As Geng and his partner is still working on the DOM simulation of PHoneyC (Project #2), I will do more test and write an overall introduction to the ideas and structure of the new PHoneyC after merging in his final commit.

  

  

NOTICE: The DOM simulation part of PHoneyC in the svn may change a lot in the following days, so please checkout revision 1433 of the for a stable version.

  

  

Here is the current installation manual, you can also find it in the README file:

  

  

\===========================================================

  

Requirements:

  

  
    libemu-svn

  

    http://libemu.carnivore.it/

  

  
    curl

  

    http://curl.haxx.se/

  

  
  
Compile the modules:

  

  
    cd modules

  

    make

  

    make install

  

  
NOTE: Don't need to have root privilege when running make install.

  

  
  
Run it:

  

  
   PYTHONPATH=lib/python python main.py URL-you-what-to-examine

  

  
\===========================================================
