---
title: "Capture HPC Client for Linux released!"
date: "2012-08-19"
---

I'm proud to announce the release of new Capture HPC client module.  
  
The new version - 0.9 beta implements totally new system monitoring method. The old one - strace - was replaced by kernel module that intercepts some system calls to record events for later analysis.  
  
The communication between kernel and userland is done via proc file. It means that module might be easily used with other applications. File output has a format that is simple to parse and by writing to the file one can modify module behaviour.  
  
More details are available on [projects wiki](http://redmine.honeynet.org/projects/linux-capture-hpc/wiki) .  
Client is available for download [here](http://redmine.honeynet.org/projects/linux-capture-hpc/files) and supported servers (2.5.1 and 3.0.0) [here](https://projects.honeynet.org/capture-hpc/wiki/Releases).  
  
This version is beta as I had no opportunity to run it on production system. After many tests I ran, it seems to be stable so the beta suffix will be removed after successfull usage on production.  
  
I'd like to thank Adam Kozakiewicz - my mentor and father of the idea, Paweł Jacewicz - backup mentor and two kind strangers from the internet who gave me some very useful hints about kprobes - Prasanna Panchamukhi and Quentin Casasnovas.  
  
Have fun hunting drive-by attacks for linux and don't hesitate to ask if the documentation isn't enough.  
  
Maciej Szawlowski
