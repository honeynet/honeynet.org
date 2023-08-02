---
title: "Beta release of libemu qemu extension"
authors: ["Florian Schmitt"]
date: "2011-08-30"
tags: 
  - "libemu-d34"
  - "qemu-d52"
  - "shellcode-d49"
---

As part of this year’s Summer of Code, I programmed an extension for the shellcode detection and analysis library [libemu](http://libemu.carnivore.it/). The main goal of the project was to increase the performance when executing shellcode, with the help of a virtualizer. Prior to this extension, libemu made use of a custom emulator, which supported only instructions mostly used in shellcode. With this extension, libemu utilizes a full-blown, completely functioning virtualizer, which executes code presumably the same way a real CPU does.  
  
The project consists of two parts. The first is qemulib, which is a modified version of the virtualizer [qemu](http://www.qemu.org/). The main modification is that it gets linked as a dynamic library, which can be used in libemu. In addition, several instructions are hooked in order to detect API-calls.  
  
The second part of the project is an extended version of libemu. If set, it utilizes qemulib and not the build in emulator to execute shellcode. Shellcode detection is done by a brute-force approach instead of instruction tracking.  
  
An installation guide is included in the readme. The commands of the sctest-program have been slightly changed. Beforehand, instructions were always processed stepwise. Now, by default, code is executed in non-single step mode. This means, if you need instruction wise assembler code or you want to create a call graph, single step mode must be turned on by the -T flag.  
  
Drawback of the extension is, that qemu was not designed to be thread-safe. So, libemu is not thread-safe anymore either. Additionally, the beta is known not to work with 64-bit Linux. This will likely be fixed later.  
  
The beta release can be found [here]( http://redmine.honeynet.org/projects/scemuperf/files).
