---
title: "Beta Release of DroidBox for Android 2.3 and APIMonitor"
authors: ["Kun Yang"]
date: "2012-08-23"
categories: 
  - "android"
  - "gsoc"
tags: 
  - "android-d70"
  - "apimonitor-d69"
  - "dalvik-d65"
  - "droidbox"
  - "dynamic-d12"
  - "gsoc-d20"
---

I'm announcing the new features of Android dynamic analysis tool DroidBox as GSoC 2012 approaches the end. In this release, I would like to introduce two parts of my work: DroidBox porting and APIMonitor.

  
  

### DroidBox for Android 2.3

  
Based on TaintDroid 2.3, I've ported DroidBox to support Android 2.3 and fixed some bugs.  

  
- Download bata version: [http://droidbox.googlecode.com/files/DroidBox23.tar.gz](http://droidbox.googlecode.com/files/DroidBox23.tar.gz)
  
- Source code repository: [https://github.com/kelwin](https://github.com/kelwin)
  

  
Usage is same with the previous version. You can check the [project page](https://code.google.com/p/droidbox/).  
  

### DroidBox APIMonitor for all versions of Android

  
  
Android is upgrading in a fast speed. To avoid endless porting of DroidBox, we changed the way to do dynamic analysis. Instead of hooking systems, we interpose APIs in APK files and insert monitoring code. By running the repackaged APK, we can get API call logs and understand APK's behavior. To find more details, please check the links below:  

  
- APIMonitor wiki page: [http://code.google.com/p/droidbox/wiki/APIMonitor](http://code.google.com/p/droidbox/wiki/APIMonitor)
  
- Download bata version: [http://droidbox.googlecode.com/files/APIMonitor-beta.tar.gz](http://droidbox.googlecode.com/files/APIMonitor-beta.tar.gz)
  
- Source code repository: [https://github.com/kelwin/apkil](https://github.com/kelwin/apkil)
  
- Slides that introduce how APIMonitor works: [http://www.slideshare.net/KelwinYang/improving-droidbox](http://www.slideshare.net/KelwinYang/improving-droidbox)
