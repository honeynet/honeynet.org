---
title: "Ghost USB honeypot released"
authors: ["Sebastian Poeplau"]
date: "2012-06-14"
categories: 
  - "honeypot"
tags: 
  - "ghost"
  - "usb"
---

I'm very pleased to announce that we have released the first public version of the Ghost USB honeypot.  

Ghost is a honeypot for malware that uses USB storage devices for propagation. It is able to capture such malware without any further knowledge - especially, it doesn't need signatures or the like to accomplish its task.  

Detection is achieved by emulating a USB flash drive on Windows systems and observing the emulated device. The assumption is that on an infected machine the malware will eventually copy itself to the removable device.  

Ghost was first presented to the public at the Honeynet Project's 2012 workshop in the San Francisco Bay Area (video availabe at [the workshop's website](https://honeynet.org/SecurityWorkshops/2012_SF_Bay_Area/Mar_19/Workshop_Program_Agenda#Sebastian_Poeplau)). Development will be continued as a Honeynet Project summer of code.  

You can find a binary release and the source code, as well as instructions for compiling the source and installing the honeypot, at [the project's website](http://code.google.com/p/ghost-usb-honeypot/). A detailed plan of intended future development is available at [the HP summer of code project page](https://honeynet.org/hpsoc/slot1).
