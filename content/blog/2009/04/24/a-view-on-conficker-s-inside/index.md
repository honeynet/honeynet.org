---
title: "A view on Conficker's inside"
authors: ["Felix Leder"]
date: "2009-04-24"
tags: 
  - "conficker-d40"
  - "control-flow"
  - "dependencies"
  - "malware-d38"
  - "visualization-d89"
---

Many people have asked us, how Conficker looks like. That's a tough question for something that's hidden and tries to be as stealthy as possible. The last time somebody asked me: "Can you show me Conficker?", I decided to visualize Conficker. Here is [a little video that shows the evil core of Conficker.C](http://iv.cs.uni-bonn.de/uploads/media/video.avi "Conficker.C video").

  

  

The video is a 3D animation of the functions inside Conficker.C and their functional relationships. Yellow balls are functions found inside Conficker. Green loops are functions imported from Dlls and red boxes are jump holes into other functions. The video shows the way our tools analyze Conficker and the derivation of dependencies among the control flow graph.

  

  

The video can be downloaded from our Conficker-page: [http://four.cs.uni-bonn.de/conficker](http://four.cs.uni-bonn.de/conficker "University of Bonn, Conficker page") or directly accessed via [http://four.cs.uni-bonn.de/uploads/media/video.avi](http://four.cs.uni-bonn.de/uploads/media/video.avi "Conficker.C video")

  

  

Have fun :)

  

  

Tillmann & Felix
