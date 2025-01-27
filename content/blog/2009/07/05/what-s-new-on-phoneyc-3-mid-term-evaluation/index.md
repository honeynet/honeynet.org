---
title: "What's new on phoneyc (3)--- Mid-term Evaluation"
authors: ["Zhijie Chen"]
date: "2009-07-05"
categories: 
  - "gsoc"
tags: 
  - "gsoc"
  - "libemu"
  - "phoneyc"
  - "shellcode"
  - "spidermonkey"
---

### Mid-term Report on [PHoneyC](http://code.google.com/p/phoneyc/) GSoC project 1

| Info        | See [https://www.honeynet.org/gsoc/project1](https://www.honeynet.org/gsoc/project1) for project details. |
|-------------|----------------------------------------------------------------------------------------------------------|
| Author      | Zhijie Chen (Joyan) [czj.pub@gmail.com](mailto:czj.pub@gmail.com)                                         |
| Mentor      | Jose Nazario                                                                                             |
| Description | Mid-term Report on [PHoneyC](http://code.google.com/p/phoneyc/) GSoC project 1. This report describes what I have done on the PHoneyC's libemu integration for shellcode and heapspray detection during the first half of the GSoC. Till now, the main ideas on this feature have been fast-implemented (actually I mean poor coding style) and the whole flow works well, with some code rewriting and performance optimization needed in the future. |

### **Introduction**

PHoneyC is a low-interaction honeyclient written by Jose Nazario. The  
shellcode (SC for short) and heapspray (HS for short) detection module  
for PHoneyC is listed on the GSoC this year and I feel lucky to be  
chosen to implement it. This report is the main idea about how to  
detect SC/HS in PHoneyC and how to build and run this version of  
PHoneyC. Note that this module (I call it honeyjs) is far from  
complete currently and this report is only for midterm evaluation. So  
it is possible that the way to build and run it won't work in the  
future.

As for the introduction to PHoneyC, I think I'd better quote what the  
original developer said in his paper 'PhoneyC: A Virtual client  
Honeypot':

This paper presents PhoneyC, a honeyclient tool that can  
provide visibility into new and complex client-side attacks.  
PhoneyC is a virtual honeyclient, meaning it is not a real  
application but rather an emulated client. By using dynamic  
analysis, PhoneyC is able to remove the obfuscation from many  
malicious pages. Furthermore, PhoneyC emulates specific  
vulnerabilities to pinpoint the attack vector. PhoneyC is a  
modular framework that enables the study of malicious HTTP  
pages and understands modern vulnerabilities and attacker  
techniques.

### **My Approach**

My approach to detection shellcode and heapspray can be simply  
described as:

1. Firstly I have modified the python-spidermonkey v0.0.1a  
(written in Pyrex) to let the Javascript Virtual Machine  
interrupted on each assignment.
1. Then I check if the r-value of this assignment is a string.  
If so, I use libemu to check for shellcodes in this string. If  
there are shellcode within the string, it will append an alert  
message into the alert list.
1. A series of shellcode alerts relating to one variable will  
be summarized into a potential heapspray alert.
1. After the execution of the Javascripts, phoneyc will  
analyze the shellcodes for mal-download URLs and other  
information using libemu.

Also there are some optimizations such as mal-value hash table to  
avoid duplicate check to the same value and dataflow tracking (e.g.  
the concatenation of a mal-string (string that contains shellcodes)  
with any other string will result in a mal-string).

The above is all I have done in the first half of this GSoC, and the  
python module I implemented is named **honeyjs**.

### **How to Install**

#### Requirements

To successfully compile the honeyjs module, the following  
software/library is required:

**Pyrex**

"Pyrex - a Language for Writing Python Extension Modules."  
<[http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/](http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/)\>. I use version 0.9.8.5.
 
**Spidermonkey(libjs)**

"SpiderMonkey is the code-name for the Mozilla's C  
implementation of JavaScript."  
<[http://www.mozilla.org/js/spidermonkey/](http://www.mozilla.org/js/spidermonkey/)\>. I use version 1.8.0 pre-release 1.

**Libemu**

"libemu is a small library written in c offering basic x86  
emulation and shellcode detection using GetPC heuristics."  
<[http://libemu.carnivore.it/](http://libemu.carnivore.it/)\>. I use the version from the CVS.

#### Configuration

For the reason that I will rewrite the pyrex code in C to use the  
latest version of python-spidermonkey, it's meaningless to write any  
automatic install scripts this moment. So you have to confirm the  
packages above are correctly installed and manually change the path to  
the libraries and header files in _./lib/setup,py_ and run the command  
_make_ to build it.

#### Run it!

To test this branch of PHoneyC, change the **LINK** variable in  
_honeyclient.py_ to your URL and run it. The shellcode/heapspray  
alerts will be printed, the shellcode will be analyzed and the  
URLs will be stored in a python list if it is a download-and-exec  
shellcode.

_NOTE_: The deobfuscating module is developed by another GSoCer so the  
current deobfuscating ability is limited. We will merge together at  
the end of the GSoC.

For example, running the honeyclient.py on the test sample 2448.html  
will prints like this:

\## The outputs are all messed up in this blog, so I delete them. To view a complete version of this report, try [http://joyan.appspot.com/2009/07/5/Whats\_new\_phoneyc\_3\_Mid-term\_Evaluation.html](http://joyan.appspot.com/2009/07/5/Whats_new_phoneyc_3_Mid-term_Evaluation.html)  or the svn [http://code.google.com/p/phoneyc/source/browse/phoneyc#phoneyc/branches/phoneyc-joyan-branch/doc/other/phoneyc\_libemu\_on\_GSoC\_mid-term\_evaluation](http://code.google.com/p/phoneyc/source/browse/phoneyc#phoneyc/branches/phoneyc-joyan-branch/doc/other/phoneyc_libemu_on_GSoC_mid-term_evaluation)##  

### What to Do in the Future

There are some known problems with the current implementation, which  
includes:
1. The 'strange' behavior of libemu's shellcode analyzing  
    function. Sometimes the shellcode can't be profiled thoroughly,  
    for example, the download-and-exec shellcode in  
    ssreader\_0day.html sometimes can only finish the LoadLibrary  
    and GetprocAddress calls in the emulation, and won't go on to  
    invoke GetSystemDirectory and URLDownloadToFile APIs, as seen  
    from the shellcode profile.  
2. It costs too much time to check a heapspray sledge for  
    shellcode. Some optimization is needed.

Things I will do next:

1. Read the source code of the latest python-spidermonkey module  
    (v0.0.8).
2. Rewrite the whole honeyjs module in C. The current version of  
    honeyjs is based on python-spidermonkey v0.0.1a, which is  
    written in pyrex, but the latest version of python-spidermonkey  
    (v0.0.8) is written in C and has less bugs. And also another  
    PHoneyC GSoC project is also based on the latest version of  
    python-spidermonkey, so it's necessary for me to implement  
    honeyjs based on python-spidermonkey 0.0.8, too.
3. Write a more user-friendly install script for release.
4. Document the implementation.
5. Merge in Geng Wang's DOM simulation codes. 
6. Try some new features, for example, hooking more APIs which  
    will be called in the shellcode.

### Following Milestones

_July 12_:

Finish Source Reading (Step 3).

_July 26_:

Finish the rewriting stuff (Step 4).

_August 2_:

Finish writing the install script and merging in Geng's DOM  
simulation codes. (Step 5 and 7).

_August 10_

Finish documentation and tests.
