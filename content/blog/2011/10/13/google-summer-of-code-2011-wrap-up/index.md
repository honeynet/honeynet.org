---
title: "Google Summer of Code 2011- Wrap up"
authors: ["Christian Seifert"]
date: "2011-10-13"
categories: 
  - "gsoc"
tags: 
  - "gsoc"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

In 2011, the Honeynet Project had once again the opportunity to participate in the Google Summer of Code program. In the last few weeks, we wrapped up all projects, beta tested the code, wrote documentation, and prepared releases.  

To quickly recap: GSoc (Google Summer of Code) is an annual summer program sponsored by Google, in which Google pairs up students with organizations committed to open-source. Google supports each project with 5000USD of which the students receive the lion's share. The Honeynet Project has participated in GSoc since 2009. Visit https://honeynet.org/gsoc2009 and https://honeynet.org/gsoc2010 to get an idea on what we have accomplished through this program in the last couple of years.  

This year, we were able to spin up and execute 12 projects! While there are still a couple of projects that are preparing their release as part of the larger underlying project, we would like to point you to the following links that provide a summary and references to the projects that already resulted in releases:  

- [cHook - The new CuckooBox Hooking Engine](https://honeynet.org/node/755) and [cHide](https://honeynet.org/node/772) 
- [AxMock is released for your review](https://honeynet.org/node/759)
- [Webviz is out for your reviews](https://honeynet.org/node/758)
- [APKInspector BETA Release & Demo Video](https://honeynet.org/node/761)
- [HoneyViz demo is out for your viewing pleasure](https://honeynet.org/node/763)
- [Beta release of libemu qemu extension](https://honeynet.org/node/765)
- [DroidBox: beta release](https://honeynet.org/node/771)
- [HoneySink: beta release](https://honeynet.org/node/773)
- [SIP Module for Dionaea](https://honeynet.org/node/776)
- [Extending Wireshark Analysis](https://honeynet.org/node/716)

These projects address a wide array of security problems. APKInspector and DroidBox greatly simplify mobile malware analysis; Webviz and HoneyViz explore the space of visualization of data for the security analyst; HoneySink is the first open-source sinkhole solution available; sip module for dionaea extends the capability of this honeypot into the VoIP area; cHook & cHide makes the malware analysis platform Cuckoobox more resilient against detection & evasion; AxMock is a ActiveX emulation/detection module which can be used - for example to detect drive-by-download attacks with client honeypots, such as Capture-HPC - ; the libemu extension made shellcode analysis & execution much more performant; and the wireshark plugins extend the wireshark network monitoring tool with additional forensic and analysis capabilities, such as the integration with rules from the popular intrusion detection system Snort.  
  
This is a really impressive list of projects!  
  
The credit really goes to our awesome students that participated in GSoc this year. We want thank them for participating in this program and choosing the Honeynet Project as their mentoring organization. They all did a great job and I very impressed with their dedication and professionalism. I think the projects speak for themselves and some of the students will continue to be involved with these projects and our community long term! The students this year were:  

- Youzhi Bao (AxMock)
- György Kohut (Honeeebox)
- Lucas McDaniel (HoneyViz)
- Oguz Yarimtepe (WebViz)
- Patrik Lantz (DroidBox)
- Cong Zheng (APKInspector)
- Adam (Sinkhole)
- Jakub Zawadzki (Wireshark Plugins)
- Dario Fernandes (Cuckoobox)
- Brandon Marken (HyperVisor)
- PhiBo (VoIP module for dionaea)
- Florian Schmitt (libemu qemu extension)

Also, we would like to thank the mentors and technical advisors who volunteered their time to support and mentor the students to be successful over the summer....  

- Ian Welch from the New Zealand Chapter (AxMock)
- David Watson from the UK Chapter (Honeeebox)
- Kara Nance from the Alaska Chapter (HoneyViz)
- Ben Reardon from the Australian Chapter (WebViz)
- Anthony Desnos from the French Chapter (DroidBox)
- Ryan Smith from the RoT-1 Chapter (APKInspector)
- Shaun Vlassis from the Australian Chapter (Sinkhole)
- Guillaume Arcas from the French Chapter (Wireshark Plugins)
- Claudio Guarnieri from the Global Chapter (Cuckoobox)
- Brian Hay from the Alaska Chapter (HyperVisor)
- Sjur Usken from the Norwegian Chapter (VoIP module for dionaea)
- Markus Koetter, HP alumni (dionaea)
- Felix Leder from the Giraffe Chapter (libemu qemu extension)

... and last but not least, we thank Google. The program greatly supports organizations like ours that are committed to open-source and trying to make a positive difference. We hope to be back next year :)  

Christian Seifert  
CEO, The Honeynet Project  
