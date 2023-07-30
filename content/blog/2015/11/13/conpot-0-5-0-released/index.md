---
title: "Conpot 0.5.0 released"
date: "2015-11-13"
authors: ["Lukas Rist"]
tags: 
  - "conpot"
  - "honeypot"
  - "ics"
  - "scada"
---

The [Conpot](http://conpot.org) development team is proud to announce the [0.5.0 release](https://github.com/mushorg/conpot/blob/master/Changelog.txt). Highlights of this release are the support for two new protocols and one additional device. Peter Soóky did a major contribution with support for the [BACnet](https://en.wikipedia.org/wiki/BACnet) protocol, which is used for building automation and control networks, and support for [IPMI](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface), which is used an interface to a computer subsystem that provides management and monitoring capabilities independently of the host system's CPU, firmware and operating system (consider the insights you can get from someone [exploiting this](https://community.rapid7.com/community/metasploit/blog/2013/07/02/a-penetration-testers-guide-to-ipmi)). As mentioned in an [earlier blog post](https://honeynet.org/node/1269), we also added support to emulate a Guardian AST device. This is based on [the research](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/the-gaspot-experiment) from Kyle Wilhoit and Stephen Hilt.  
Another goal of this release was to improve the ease of deployment. Therefore we added a Docker container template. Thanks to our contributors, we also have documentation on how to run Conpot on CentOS.  
To avoid some easy fingerprinting, we added the feature to modify the MAC address of the interface Conpot is listening on. So now your hardware address can match the device manufacturer you are intending to emulate.  
As with every other release, we tried to improve our test coverage and code quality in order to increase the honeypots stability.  
  
If you are enjoying Conpot, please consider [enabling](https://github.com/mushorg/conpot/blob/master/conpot/conpot.cfg#L32-L38) HPFeeds in order to share data with us. We are also looking for new developers to join, so don’t be shy and get in touch!
