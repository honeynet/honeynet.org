---
title: "LEET09 Paper: PhoneyC: A Virtual Client Honeypot"
authors: ["Jose Nazario"]
date: "2009-04-24"
categories: 
  - "analysis"
  - "honeypot"
tags: 
  - "phoneyc"
  - "paper"
  - "leet09"
  - "honeyclient"
---

Earlier this week I had the good fortune to be in Boston for [LEET09](http://usenix.org/events/leet09/tech/tech.html), a workshop on exploits, malware, and large-scale trends. I presented on PhoneyC, the Python honeyclient I've been working on. The paper describes the architecture and features of the tool and a real world evaluation and test. The talk was well received, and many thanks to the organizers of the conference and the PC for their helpful reviews.  
Usenix has made the full paper available to all for free.  

> The number of client-side attacks has grown significantly in the past few years, shifting focus away from defendable positions to a broad, poorly defended space filled with vulnerable clients. Just as honeypots enabled deep research into server-side attacks, honeyclients can permit the deep study of client-side attacks. A complement to honeypots, a honeyclient is a tool designed to mimic the behavior of a user driven network client application, such as a web browser, and be exploited by an attacker’s content. These systems are instrumented to discover what happened and how. This  
> paper presents PhoneyC, a honeyclient tool that can provide visibility into new and complex client-side attacks. PhoneyC is a virtual honeyclient, meaning it is not a real application but rather an emulated client. By using dynamic analysis, PhoneyC is able to remove the obfuscation from many malicious pages. Furthermore, PhoneyC emulates specific vulnerabilities to pinpoint the attack vector. PhoneyC is a modular framework that enables the study of malicious HTTP pages and understands modern vulnerabilities and attacker techniques.  

Source: [PhoneyC: A Virtual Client Honeypot](http://usenix.org/events/leet09/tech/full_papers/nazario/nazario.pdf) \[PDF\] by Jose Nazario, presented at [LEET09](http://usenix.org/events/leet09/tech/tech.html).
