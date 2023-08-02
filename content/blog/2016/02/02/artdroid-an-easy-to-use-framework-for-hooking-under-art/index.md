---
title: "ARTDroid: an easy-to-use framework for hooking under ART"
authors: ["Cong Zheng"]
date: "2016-02-02"
categories: 
  - "android"
tags: 
  - "android-d70"
  - "art"
  - "dynamic-analysis-d29"
  - "gsoc-d20"
  - "hook-d81"
  - "malware"
---

During Google Summer of Code 2015, in the Honeynet Project open-source org, Valerio Costamagna and Cong Zheng (mentor) worked on ARTDroid, an easy-to-use framework for hooking virtual-method under latest Android runtime (ART).

  

**Introduction**  
We propose ARTDroid, a framework which allows to analyze Android apps without modifications to both Android framework and apps. The core technology is the library injection and virtual methods hooking by vtable tampering after getting the root privilege.

  

ARTDroid supports real devices as well. With the advantage of not modifying app’s codes, it can analyze benign apps that have the integrity checking ability. Because, all modifications are finished in app’s virtual memory. For malicious apps, they often use anti-emulator techniques, so applying dynamic analysis with ARTDroid on real devices can detect this kind of advanced malicious apps.

  

To the best of our knowledge, ARTDroid is the first framework for hooking virtual-methods under ART runtime.

  

**Description**  
In Java programming, all non-static methods are "virtual” functions by default. Only “final” methods (cannot be overridden) and “private” methods (cannot be not inherited), are non-virtual. Basically, virtual methods are treated differently at runtime.

  

Imagine you want to hook the virtual-method "X" ("original method") and detour control flow to virtual-method "Y" ("patch method"). ARTDroid allows you to define your own method "Y" in Java and override the target method "X" with the method "Y". ARTDroid further supports loading "patch" code from DEX file. This allows to write the "patch" code in Java and thus simplifies interacting with the target app and the Android framework (Context, etc...).

  

Dynamic analysis using hooking techniques has a long history, regarding Android there are various tools, like: "DroidBox", "Cuckoo-Droid", "Xposed", "Frida". While these tools are valuable, they usually fail to running at all different Android versions under ART runtime.

  

Last but not least, ARTDroid is able to intercept virtual-method called using both JNI and Java reflection, moreover it supports integration with "frida" framework for hooking native functions.

  

**How to use**

  

ARTDroid aims to allow users to build their own Android app dynamic analysis environment. The following is a not complete list of examples uses of ARTDroid:

  

\- enforcing security policies at runtime  
\- tracing methods execution  
\- finding vulnerabilities  
\- analyzing and tampering with method's arguments  
\- etc...

  

We have a pretty detailed setup guide for you here [ARTDroid-tutorial](https://vaioco.github.io/)

  

You can look at the following [ARTDroid-Demo](https://vimeo.com/138221439):

  

<iframe src="https://player.vimeo.com/video/138221439" width="500" height="375" frameborder="0" webkitallowfullscreen mozallowfullscreen="" allowfullscreen=""></iframe>

  

  
For any questions or suggestions, please go to our Google Group: [ARTDroid-Google-Group-Q&A](https://groups.google.com/forum/#!forum/artdroid)

  

**Acknowledgements**  
I'd like to thank my Honeynet mentor Cong Zheng for his sincere contribute, @marcograss and @emd3l for all the nights without sleep but always funny ;)

  

I hope you will enjoy this framework, and it still is under ongoing development. Next release will support direct-methods hooking and other interesting features, stay tuned!

  

Happy Hacking!
