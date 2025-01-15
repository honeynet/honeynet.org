---
title: "What's new in phoneyc's shellcode detection (1)--- Tracing spidermonkey"
authors: ["Zhijie Chen"]
date: "2009-05-25"
categories: 
  - "gsoc"
tags: 
  - "gsoc"
  - "phoneyc"
  - "shellcode"
  - "spidermonkey"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

## 1. Overview

As I wrote in my project outline ([https://www.honeynet.org/gsoc/project1](/gsoc/project1)) . I should have done some basic  enhancement and experiments on python-spidermonkey for a more fine-granted tracing on spidermonkey. So till now what I have done on it includes:                                                                                

a. Implemented the _get\_globj_ method in the Context class, which enables one to 'pull' all the properties of the global object inside spidermonkey ( namely the **global variables,** because all the global variables are properties of the global object ) into python context.

b. Implemented the _hook\_setname_ method in the Runtime class. 'setname' is an opcode in the spidermonkey js  bytecodes. In most cases an assignment to a global variable will be compiled into a series of bytecodes and the last one is a setname 'instruction'(or opcode) to set the value of a given name. I have traced the spidermonkey vm and make it print the argument of the setname opcode whenever the setname opcode is executed.                

c. Seeking a way to hook the creation of each atom in spidermonkey. As all strings and other immutable things  are stored as an atom in spidermonkey, I'm trying to hook this event using js\_TraceAtomState.                   

Here is some details about the implementation and experiment results:                                           

## 2 Details
          
### A. get\_globj Method
          
As we know, python-spidermonkey didn't provide any API to get all the global vaiables at a time by now. But the approach is simple, for the reason that all the global vaiables are actually the properties (attributes) of the global object. So all we should do is to convert the global object in js into a dict in python, and it's keys are the global variables' names and the values are the values of those global variables accordingly. So I just added another method in Context called get\_globj, which simply invokes 'Py\_from\_JS' and translate the global   object into python context. 

NOTE: I haven't figured it out if the strings stored in python context will stay exactly the same as in javascript. So I don't know if the shellcodes in js strings are still valid in the python context. 

### B hook\_setname and js\_intterupt\_handler.                                                                 
The hook\_setname method in 'Runtime' simply calls the spidermonkey C API 'JS\_SetInterrupt(self.rt,js\_intterupt\_handler,NULL)' to make the jsvm(javascript virtual machine) step-traced and register the 'js\_intterupt\_handler' as the callback function at each step. Thus we can examine each bytecode in the runtime. 

The js\_intterupt\_handler function first checks if the bytecode is setname. If so, print it's arguments,  otherwise continue. We can call the libemu detection API at this point to check the arguments in the furture.   
More details about the spidermonkey opcodes can be found in **jsopcode.tbl** of the mozilla spidermonkey source code version 1.80. To know what those opcodes can do, you should refer to **jsinterp.c**. In the furture, more opcodes should be hooked to audit all the assignments (such as assignments to local variables by setvar, and also some stuff like setarg, setprop, etc.) 

NOTE: I have used some APIs and structs neither declared in jsapi.h nor jsdbgapi.h. I know it's dirty but, emmm.., I can't find any alternatives :p.

### C. Censoring Atom Creations
            
As far as I know, all the shellcodes are stored in the atoms in Spidermonkey. So I'm thinking that if we can interrupt on the creation of each atom and let libemu to detect shellcodes in it. But I haven't know how to use the related API 'js\_TraceAtomState', because there are no documents about these APIs including most of them in section B. I have to read the spidermonkey's source myself. And I think I should fully implement features mentioned in Section B first, which I think is enough for shellcode detection. 

## 3. Solutions

So I currently have two approaches on the shellcode detection:

**3.1** Steptrace the jsvm, and perform the shellcode detection only on the argument of the assignment opcodes. And all these works are implemented in C, or at least in Pyrex (but Pyrex does not support C macros as far as I know, which may be a problem in the furture.)

The shellcode or other variables to be examined will travel through: JS Context->C Context in spidermonkey->C Context in libemu, which is efficient.

**3.2** Wrap the opcode tracing APIs into python as methods provided by spidermonkey module. And also wrap libemu into a python module.

The shellcode then will be pass through: JS Context->C Context in spidermonkey->Python Context->C Context in libemu.

## 4. Problems

Solution 3.1 and solution 3.2 both have advantages and disadvantages. Approach 3.2 is cleaner and more flexable. I mean both the hooked spidermonkey module and pylibemu module can be used in other ways or even other applications. But it is more difficult for me because I currently have no idea about how to expose APIs into python and make the two module cooperate well in python context. What's more, there is a big overhead on   
the shellcode transforming and invoking python method at each step of the jsvm.

In contrast, solution 3.1 is more efficient, and easier to implement, because both spidermonkey and libemu are written in C originally. What's more, actually all my ideas in GSoC about the shellcode detection are inside spidermonkey, and almost have nothing to do with other parts of phoneyc such as the HTML parser, so I think I'd better wrap spidermonkey and libemu inside one module (I call it honeyjs). The honeyjs module will inherit all the methods and classes in python-spidermonkey so honeyclient.py can use this module the same way as spidermonkey, all the shellcode detection stuff are inside honeyjs. So in my opinion, solution 3.1 is preferable. But I haven't decided how to expose those shellcode detection and emulation and also URL extraction APIs, either.

PS:All the codes along with this post is available in my svn branch of phoneyc([http://code.google.com/p/phoneyc/source/browse/phoneyc#phoneyc/branches/phoneyc-joyan-branch](http://code.google.com/p/phoneyc/source/browse/phoneyc#phoneyc/branches/phoneyc-joyan-branch)).

PSS:This post is also available on my personal blog:

[http://joyan.appspot.com/?p=15402](http://joyan.appspot.com/?p=15402)
