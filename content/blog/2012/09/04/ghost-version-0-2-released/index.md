---
title: "Ghost version 0.2 released"
date: "2012-09-04"
tags: 
  - "ghost-d68"
---

We've just released version 0.2 of the Ghost USB honeypot for Windows XP and Windows 7 with a lot of great new features. You can download the new version from [the project page](http://code.google.com/p/ghost-usb-honeypot/). In this post, I'm going to give an overview of the changes.  
  
Let's start with what you usually do first: install Ghost. Installing the honeypot has been tedious in the past, so we've built an installer that handles most of the work for you. Just run it and enjoy.  
  
Another issue that we've dealt with is the interface that Ghost provides. Version 0.1 featured a basic command-line tool to control the honeypot's operation. We've added a graphical frontend that can check for USB malware periodically and display the results in a user-friendly way. Also, Ghost 0.2 features a library that you can link to from any application in order to control the honeypot. Thus, integrating Ghost into your custom setup becomes very easy. See my [previous blog post](https://honeynet.org/node/908) for details.  
  
The third important piece of news is that we're now able to find out a lot about processes that infect the emulated device. Besides the process and thread IDs, Ghost provides you with a list of modules (executables and DLLs) that are loaded in the process. So if you observe write access to the emulated device from svchost.exe, for example, then you can browse the list of loaded DLLs to possibly identify the one containing malicious code.  
  
Those are the most interesting features of the new version. If you're curious now, [download Ghost 0.2](http://code.google.com/p/ghost-usb-honeypot/downloads/list) and see for yourself!  
  
Finally, let me add a word on contribution. If you're willing to contribute to the project (e.g. writing code or documentation, providing suggestions for new features, etc.), please send me an email (sebastian dot poeplau at gmail dot com). You don't have to be an expert in Windows kernel development to help - as long as you're interested, we'll get you introduced to everything you need for development!
