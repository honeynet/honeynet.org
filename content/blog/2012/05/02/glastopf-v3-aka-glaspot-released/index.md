---
title: "Glastopf v3 released"
authors: ["Lukas Rist"]
date: "2012-05-02"
categories: 
  - "gsoc"
tags: 
  - "botnet-monitoring"
  - "glastopf"
  - "google-summer-of-code"
  - "gsoc"
  - "hpfeeds"
  - "release"
  - "sandbox"
  - "web-server-botnet"
---

We where glad to announce yet another tool during our annual workshop in San Francisco. Glaspot is the third version of the web application honeypot [Glastopf](http://glastopf.org "Glastopf") and it come with some very powerful new features:  

- A build-in PHP sandbox for code injection emulation, allowing us to bring vulnerability emulation to a new level
- Hooked up to the [HPFeeds](http://hpfeeds.honeycloud.net/ "HPFeeds") generic data feed system for centralized data collection and tight integration into our sandbox and web server botnet monitoring system
- Modular implementation: Turn your web application into a honeypot with a few easy steps
- Runs in his own lightweight Python server or as a WSGI module in common web server environments
- Automated attack surface generation and expansion

In the next three months we are working on even more exciting new features and a much stronger integration into our web thread analysis platform.  
Additionally Phani Vadrevu got accepted as a Google Summer of Code student to help us with additional improvements like request classification based on attacker profiling, hardening the internal sandbox and extending the attack surface. Details can be found in his project description: [Glastopf Improvements](https://honeynet.org/gsoc/slot14 "Glastopf Improvements").  

How you could integrate the honeypot in a web threat oriented attack analysis framework is described in a recent presentation by Lukas Rist: [Feasible Solution for the Web Threat Jigsaw](http://www.youtube.com/watch?v=kipxPRXKlXY "Feasible Solution for the Web Threat Jigsaw").  
  
As usual code and documentation can be found in our [repository](http://dev.glastopf.org/projects/glaspot/ "Glaspot Repository").
