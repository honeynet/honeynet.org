---
title: "Improving Glastopf"
authors: ["Lukas Rist"]
date: "2009-06-15"
categories: 
  - "analysis"
tags: 
  - "glastopf-d23"
  - "new-version"
  - "web-honeypot-d19"
---

Last saturday I've finally released a new Glastopf version. There are some new features and many changes under the hood.

  
  

_New implemented features:_

  

**LFI** (Locale File Inclusion) handler: He is back! I have lost him somehow during coding and now he has his own handler. I am looking forward to get some data for attack method comparison. Furthermore he is one possible first layer for RCE (Remote Code Execution) attacks. So I am also curious if I'm catching some of those attacks.

  

**IRC** logging module: This is a request/response bot. The request gets translated into a MySQL query whose results are replied to the requester.

  

**Twitter** logging module: Now the Twitter module is integrated into Glastopf. It's fun to lean back and [watch him](http://twitter.com/glastopf "Glastopf Twitter Page") doing his work!

  

  

_Important changes in existing modules:_

  

**Dynamic dork list**: I am collecting unknown dorks from attacks against the Honeypot since a while and someday I thought it would be fun to serve them all to the search engine crawlers. So I generated a list containing 17k (a still growing number) dorks. This noticeably raised the number of hits against the Honeypot.

  

  

_Plans for the next two weeks:_

  

The **central database** lacks an easy to handle and public shareable interface.

  

The **vulnerability database** needs some cleanup and the collected data should be analyzed.

  

I am planning some **geolocation analysis** of the attacker IPs.

  

Glastopf's **vulnerability emulator** is one of the central parts when handling attacks. I've improved the concept and a first version is finished and will be implemented during the next weeks.
