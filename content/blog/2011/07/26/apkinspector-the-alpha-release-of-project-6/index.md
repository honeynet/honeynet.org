---
title: "APKinspector : the alpha release of project 6."
date: "2011-07-26"
categories: 
  - "android"
  - "gsoc"
tags: 
  - "apkinspector-android-malware-static-analysis"
  - "gsoc-d20"
---

The GUI tool for static analysis of Android malware is ready for an alpha release. For more details regarding this project, check [here](https://www.honeynet.org/gsoc/slot6).  
  
In the alpha release, the following features have been finished.  
  
(1) Show the CFG (control flow graph) for a given method  
  
(2) Show the smali codes for a given method.  
  
(3) Show the Java codes for a given java file.  
  
(4) Show the betecodes for a given method.  
  
(5) Show all strings, methods and classes.  
  
(6) Show the APK's related information.  
  
(7) Drag and zoom in/out the CFG.  
  
(8) Modify the content of nodes in the CFG.  
  
And now, I add additional features in the latest codes, such as syntax highlighting, editors with line numbers, searching and filtering.  
  
I will improve the CFG's module and pay more attention to the beautiful and concise graph view. For each node, It should be smaller to make the whole graph more compact. In addition, it will show the hint for each node when the user move the mouse over it.  
  
To continue the user's interaction module, I will start to add some signals and slots on some widgets. This would be the most important work in the next phase.  
  
To experience our tool, go to [apkinspector](https://bitbucket.org/ryanwsmith/apkinspector)
