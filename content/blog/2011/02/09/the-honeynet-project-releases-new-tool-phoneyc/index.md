---
title: "The Honeynet Project Releases New Tool: PhoneyC"
authors: ["Anton Chuvakin"]
date: "2011-02-09"
tags: 
  - "tool"
---

Here is another new release from the Project: a release of a new tool called [PhoneyC](https://www.honeynet.org/project/PhoneyC), a virtual client honeypot.  
PhoneyC is a virtual client honeypot, meaning it is not a real application (that can be compromised by attackers and then monitored for analysis of attacker behavior), but rather an emulated client, implemented in Python. The main thing it does is scour web pages looking for those that attack the browser.  
It can be run, for example, as: _$ python phoneyc.py -v_ [_www.google.com_](http://www.google.com/url?sa=D&q=www.google.com)  
By using dynamic analysis, [PhoneyC](https://honeynet.org/project/PhoneyC) is able to remove the obfuscation from many malicious pages. Furthermore, PhoneyC emulates specific vulnerabilities to pinpoint the attack vector. PhoneyC is a modular framework that enables the study of malicious HTTP pages and understands modern vulnerabilities and attacker techniques.  
Download version 0.1 (a contained readme contains installation instructions) here: [phoneyc\_v0\_1\_rev1631.tar\_.gz](https://www3.honeynet.org/wp-content/uploads/attachments/phoneyc_v0_1_rev1631.tar.gz)  
v0.1 feature highlights include:  

  

\* Interpretation of useful HTML tags for remote links

  

\- hrefs, imgs, etc ...

\- iframes, frames, etc

  

\* Interpretation of scripting languages

  

\- javascript (through spidermonkey)

\- supports deobfuscation, remote script sources

  

\* ActiveX vulnerability "modules" for exploit detection

  

\* Shellcode detection and analysis (through libemu)

  

\* Heap spray detection

  

  
PhoneyC is hosted on [http://code.google.com/p/phoneyc/](http://code.google.com/p/phoneyc/) from which the newest development version can be obtained via SVN. For any issues turn to the Google Group dedicated to the project: [http://groups.google.com/group/phoneyc](http://groups.google.com/group/phoneyc).
