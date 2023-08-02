---
title: "GSoC2011-THP Project 1 - Improve our high interaction client honeypot Capture-HPC"
authors: ["Youzhi Bao"]
date: "2011-05-05"
categories: 
  - "gsoc"
  - "honeypot"
tags: 
  - "capture-hpc-d18"
  - "gsoc-d20"
---

Project Description:  
[Proposed Capture-HPC Description](https://honeynet.org/gsoc/ideas#project1)  
  
Capture-HPC is a high-interaction client honeypot that is capable of seeking out and identifying client-side attacks. It identifies these attacks by driving a vulnerable client to open a file or interact with a potentially malicious server. As it processes the data, Capture-HPC monitors the system for unauthorized state changes that indicate a successful attack has occurred. It is regularly used in surveys of malicious websites that launch drive-by-download attacks.  
  
Capture-HPC has been widely used and been described as the state-of-art high interaction client honeypot system in many academic papers, but has several area that can be improved:  
  
It does not contain fine grained attack detection mechanism, i.e. Capture-HPC cannot tell us which vulnerability is exploited, or is likely being exploited  
Capture-HPC can only detect attacks that are successful. If, for instance, a web page attacks an ActiveX component that is not installed on the system, Capture-HPC is unable to detect it.  
The community would benefit from more regularly updated Capture-HPC Exclusion Lists, particularly for modern browser versions (and greater community sharing).  
The goal of this project is to address these issues by extending Capture-HPC to monitor a web page’s interaction with ActiveX controls installed on the system. This will allow Capture-HPC to identify which vulnerability is being exploited.  
  
Furthermore, ideally Capture-HPC should be able to emulate ActiveX controls that are not presently installed on the system. This project will investigate this in the second part of the project.  
  
We believe that continuing to improve Capture-HPC will encourage more automated analysis of malicious websites, helping to detect new generations of client focused attacks and further improve web browser security and safety for Internet users.
