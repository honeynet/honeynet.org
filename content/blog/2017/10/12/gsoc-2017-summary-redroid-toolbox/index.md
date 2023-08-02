---
title: "GSoC 2017 Summary: ReDroid toolbox"
authors: ["Roberto Tanara"]
date: "2017-10-12"
categories: 
  - "android"
  - "gsoc"
tags: 
  - "gsoc"
  - "gsoc2017"
---

This is a contribution by GSoC student Ziyue Yang, find him on Github [yzygitzh](https://github.com/yzygitzh).

  

  
My project for GSoC 2017 is [Android Sandbox Detection and Countermeasure](https://summerofcode.withgoogle.com/projects/#4820206829436928), which came out to be the **ReDroid** toolbox. This post was presented for the final evaluation of my GSoC 2017 project.

  

ReDroid is a toolbox for **automatically detecting and countering** anti-sandbox behaviors in Android apps. You can:

  

  
- [View source on GitHub](https://github.com/yzygitzh/ReDroid)
  
- [Download as zip file](https://github.com/yzygitzh/ReDroid/archive/master.zip)
  
- [View usage example](https://yzygitzh.github.io/android/2017/08/29/redroid-usage.html)
  

  

Before GSoC 2017 begins, my GSoC mentor Yuanchun Li discussed with me about the proposal for the GSoC project. Generally our goal was to develop some mechanism that can **counter anti-sandbox techniques presented in Android apps**.

  

First, We raised three related research questions to solve:

  

  
2. What sandbox-detection techniques are applied in Android apps, and how and to what extent are they applied?
  
4. Is there a method capable of detecting such sandbox-detection techniques given a sample app?
  
6. Is there an app analysis solution undetectable by common sandbox-detection methods?
  

  

After that, we came out with a plan with three stages:

  

  
2. _Investigating and collecting sandbox-detection techniques used in Android app_ (especially malware), and implementing a sample app using those techniques.
  
4. _Implementing a **detection-aware system**_, which can identify whether an Android app has sandbox-detection techniques inside.
  
6. _Implementing an **undetectable system**_. Such undetectable system is able to automatically find the detection activities inside an Android app, and convey countermeasures for them using data collected from 2). In such a system, an app would believe that it’s running on as a real device.
  

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

| Tasks |     Status     | Comments |
| --- | --- | --- |
|   
Investigating and collecting sandbox-detection techniques used in Android app |   
Done |   
Investigated [anti-emulator](https://github.com/yzygitzh/anti-emulator), [DenDroid](https://github.com/yzygitzh/dendroid_apk) and a malware dataset provided by [contagiominidump.blogspot.com](http://contagiominidump.blogspot.com/) |
|   
Implementing a detection-aware system |   
Done |   
Modified Android source to enable robust and automatic trace collection; Implemented a runtime trace collecting system based on [DroidBot](https://github.com/honeynet/droidbot) and a heuristic trace difference detection system |
|   
Implementing an undetectable system |   
Partly  
Done |   
Implemented a dynamic control flow correction system based on JDWP and [Xposed](https://forum.xda-developers.com/showthread.php?t=3034811), which is capable for modifying method return values; Modified Android source to enable dynamic control flow correction without known by apps |

  

  
For more details, please visit [this page](https://yzygitzh.github.io/gsoc/2017/06/01/gsoc-2017-progress.html)

  

# Future work:

  

  
2. _Support more complex method return types_: currently ReDroid only supports return values of primitive types and `String` type.
  
4. _Support more advanced method hooking_: currently ReDroid only supports hacking methods according to stack trace, and the methods hacked can have only one return value.
  
6. _Wrap ReDroid to make it usable for most people_: to run ReDroid, one has to configure real device and emulators, which is much too complicated for normal users. ReDroid can be wrapped into a cloud service in the future.
