---
title: "Thug 0.6 released!"
authors: ["Angelo Dellaera"]
date: "2015-01-05"
tags: 
  - "honeyclient"
  - "thug"
---

Thug 0.6 was released just a few hours ago. The most important change introduced during the 0.5 branch was a complete redesign of the logging infrastructure which is now completely modular. This makes adding (or removing) new logging modules extremely easy.  
  
I did this change for a couple of reasons. The first one is that the logging code before Thug 0.5 was developed without a proper design but just adding the modules as soon as I needed them. I usually hate this approach so it would be enough to justify a complete redesign. But there was one more reason. I was aware that a few persons out there were implementing their own logging modules and binding them in some really awful ways to the main code (someone said plugins?). I spent a lot of time in documenting such changes. For these reason I will not dive into details in this post. But trust me. Extending Thug logging with your own modules should be an easy task now. Hopefully. Let me add that additional logging modules would be really appreciated so if you think your cool module should be included in the source tree please feel free to contact me.  
  
Moreover I worked a lot in order to improve the reliability and the performances of the analyses. Sometimes this required just little changes, sometimes not. But I am really satisfied about such changes and the improvements they produced.  
  
I have great plans for the 0.6 branch. First of all I will continue focusing on reliability and performance improvements (probably I never stopped doing it from the first release). Moreover I would love working on the distributed analysis approach which we started experimenting during the Google Summer of Code 2013 and on the client tracking mechanisms detection.  
  
Stay tuned because I just started having fun!  
  
[https://github.com/buffer/thug](https://github.com/buffer/thug)  
[http://buffer.github.com/thug/](http://buffer.github.com/thug/)
