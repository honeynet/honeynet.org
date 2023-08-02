---
title: "GlastopfNG release"
authors: ["Lukas Rist"]
date: "2010-10-15"
tags: 
  - "glastopf-d23"
  - "glastopng-d53"
  - "web-honeypot-d19"
---

Before we are getting worse than [Duke Nukem Forever](http://en.wikipedia.org/wiki/Duke_Nukem_Forever), we decided to finally release the next generation of the web application honeypot Glastopf, aka GlastopfNG!  
  
Today we find web applications in every environment independent of company size and even in home networks. Over web attack vectors like SQL Injections and Remote File Inclusions, criminals can overtake web servers which than become part of a botnet or even a command and control server. Web servers are specially interesting for such tasks as they normally have bigger bandwidth than client computers and mostly an uptime of nearly 24 hours, seven days a week. This makes a hacked web server a dangerous weapon in the hands of a criminal.  
  
**Note**  
The new GlastopfNG is a fork of our [current version](http://dev.glastopf.org/projects/glastopf). This means, it is currently not fully compatible with infrastructures that already use the old version. This is the case because not all modules from the old version have already been ported to the new one but due to its superior design, we will merge features from the old Glastopf as fast as possible.  
  
**Introduction**  
GlastopfNG is a honeypot specialized on simulating a vulnerable web server/application to become a target of automated and even manual attacks. Instead of trying to block these attacks GlastopfNG tries to get as much information as possible about the attacker and the used attack itself. This gathered information can then be used in different ways to protect real applications in the future against such attacks. Today it's for example already used by hosting providers to inform owners of servers, which are attacking other servers on the Internet, that it's very likely, that their server has been hacked. This is a great additional service for their customers and can be done in a mainly automated way.  
  
**Project**  
If you don't know what attacks to expect, it's nearly impossible to block any of them. This is why it is so important to gather information about the latest attacks on the Internet. There was already a honeypot called Glastopf but unfortunately, it had some shortcomings and this is why this bachelor thesis was dedicated to a complete rewrite of the Glastopf honeypot including the way it internally works, it's module concept, it's configuration approach and all used data structures.  
  
**Result**  
GlastopfNG does not have any of the shortcomings of the original Glastopf anymore, which makes it the most advanced web attack honeypot. The sophisticated architecture of GlastopfNG makes it really easy for developers and even interested non-developers to extend it with modules. Overall, GlastopfNG is now one of the most flexible honeypots available. In the tests during the thesis, it was already possible to analyze thousands of attacks and gather information about them like the attack source and their payloads.  
  
**Links**  
The project page:  
[http://dev.glastopf.org/projects/show/glastopfng](http://dev.glastopf.org/projects/show/glastopfng "The project page")  
Get Svens thesis on GlastopfNG:  
[http://dev.glastopf.org/wiki/glastopfng/Thesis](http://dev.glastopf.org/wiki/glastopfng/Thesis "Thesis on GlastopfNG")  
Get GlastopfNG:  
[http://dev.glastopf.org/wiki/glastopfng/Binary](http://dev.glastopf.org/wiki/glastopfng/Binary "GlastopfNG binary")
