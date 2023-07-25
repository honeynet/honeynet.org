---
title: "Glastopf"
date: "2009-10-17"
---

## About Glastopf

* * *

Web sites are hacked all the time. Web application, database, and cross-site scripting vulnerabilities expose a large attack surface that can be exploited to, among others, deface the web site, send spam, convert web site into bots, and serve drive-by-download attacks. Glastopf is a low-interaction honeypot that emulates a vulnerable web server hosting many web pages and web applications with thousands of vulnerabilities. Glastopf is easy to setup and once indexed by search engines, attacks will pour in by the thousands daily. Glastopf has been developed as part of the 2009 Google of Summer Code by student Lukas Rist (and mentored by Thorsten Holz of the German Honeynet Project Chapter).

Glastopf is a Python web application honeypot. We use vulnerability type emulation instead of vulnerability emulation. Popular attack type emulation is already in place: Remote File Inclusion via a build-in PHP sandbox, Local File Inclusion providing files from a virtual file system and HTML injection via POST requests.

 

## Download

* * *

It can be downloaded from the Glastopf trac site at [https://github.com/mushorg/glastopf](https://github.com/mushorg/glastopf)

More information on Glastopf can be found on the project site at [http://mushmush.org/](http://mushmush.org/)

There is KYT paper about Glastopf available on [here](/publications/whitepapers/glastopf-a-dynamic-low-interaction-web-application-honeypot/).
