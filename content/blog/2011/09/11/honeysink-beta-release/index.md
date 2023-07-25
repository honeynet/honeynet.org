---
title: "HoneySink: Beta Release"
date: "2011-09-11"
categories: 
  - "gsoc"
tags: 
  - "beta-d90"
  - "gsoc-d20"
  - "honeypot-d9"
  - "honeysink"
  - "sink"
  - "sinkhole-d45"
---

The Beta version of HoneySink is out!  
  
**What is HoneySink?**  
  
HoneySink is an open source network sinkhole that provides a mechanism for detection and prevention of malicious traffic on a given network.  
  
Able to be deployed both internally and externally it is designed to log and respond to incoming requests for a number of network protocols.  
  
With configuration and scalability in mind, HoneySink was designed from the ground up with a non-blocking architecture to handle extremely large amounts of traffic while being able to perform customised interactions and logging.  
  
**Where can I get it?**  
  
You can download the Beta from [Here](http://redmine.honeynet.org/projects/sinkhole)  
  
All install and configuration information is available inside the package.  
  
**What does it do?**  
  
Currently HoneySink allows its user to sinkhole any number of domains to it and configure logging for the following set of protocols:  
\- DNS  
\- HTTP  
\- FTP  
\- IRC  
  
For each of the above protocol/domain combination you are able to specify the actions on when an infected computer makes a connection to HoneySink.  
  
HoneySink currently has the following mechanisms available for logging:  
\- flat file  
\- MySQL  
\- MQueue  
  
**How can it be used?**  
  
There are many use cases for HoneySink but the two main ones are as follows:  
  
1) HoneySink can be deployed on an internal network where there may not be security appliances used to protect internal staff members from browsing the Internet. By using HoneySink and an internal DNS server a security engineer would be able to redirect all known malicious domains, from public blacklists, to the internal deployment of HoneySink. This would allow for the detection of internal infected machines as well as preventing the infected PC from communicating with the C&C server.  
  
2) HoneySink can be deployed facing the Internet and configured to respond, using its own DNS server software, to respond to requests for malicious domains that have been taken over by Security Researchers, CERT's, Law Enforcement to detect infected PC's and prevent criminal groups from maintaining control of their botnets.  
  
**So What?**  
HoneySink is the first 'Open Source' Network Sinkhole software to be released. There is no other, at this time, freely available equivalent that provides the same level of protocol emulation and logging with the requirement for scalability to handle potentially massive amounts of traffic.  
  
I would like to thank Adam, the GSOC (Google Summer Of Code) 2011 student, that wrote this system literally from scratch. He has done an excellent job and without him you wouldn't have another tool to use against malware.  
  
It was no easy task writing the code and definitely not easy listening to my mentoring during the course for GSOC 2011 :)  
  
If you find any Bugs (or have feature requests) please let us know through the project site (redmine) so that we can get them fixed.
