---
title: "Conficker Online Detection"
date: "2009-04-02"
tags: 
  - "conficker-d40"
  - "detection"
---

Joe Stewart from the Conficker Working Group has created an [eye chart](http://www.confickerworkinggroup.org/infection_test/cfeyechart.html "CWG Eye Chart") that allows for online identification of Conficker B and C infections. The idea of trying to load content from sites that are blocked by Conficker is really smart. We wrote our [own page](http://iv.cs.uni-bonn.de/fileadmin/user_upload/werner/cfdetector/ "Conficker Online Infection Indicator") based on their method with the goal to make the results as clear as possible (note this only requires a substring match on a pattern in Conficker's blacklist, rather than a complete domain name match). This detection method should be more reliable than network scanning based tests. Happy scanning!

  

Felix & Tillmann
