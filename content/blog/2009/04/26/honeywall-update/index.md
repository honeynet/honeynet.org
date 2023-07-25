---
title: "Honeywall update"
date: "2009-04-26"
tags: 
  - "honeywall"
---

Finally updated the roo-base rpm to point at http://yum.honeynet.org/roo/repo-1.4/ for the location of the yum repository.  Once I have access to the server, someone with an old deployment of roo 1.4, will be able to upgrade their honeywall as follows:

  

  
2. rpm -i http://yum.honeynet.org/roo/repo-1.4/roo-base-5-36.hw.noarch.rpm
  
4. yum update
  

  

This will update the honeywall with all updated system rpms effective 25 April 2009.

  

  

I also placed a new iso with updated rpms on: https://projects.honeynet.org/honeywall/attachment/wiki/WikiStart/roo-1.4.hw-20090425114542.iso.
