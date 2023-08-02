---
title: "Thug and the art of web client tracking inspection"
authors: ["Angelo Dellaera"]
date: "2015-01-27"
tags: 
  - "honeyclient-d3"
  - "thug-d25"
---

A few months ago I read the paper "Technical analysis of client identification mechanisms" \[1\]. The paper is really interesting and it is really worth investing your time and reading. Just a brief excerpt from the abstract:  
  
_"In common use, the term “web tracking” refers to the process of calculating or assigning unique and reasonably stable identifiers to each browser that visits a website. In most cases, this is done for the purpose of correlating future visits from the same person or machine with historical data. Some uses of such tracking techniques are well established and commonplace. For example, they are frequently employed to tell real users from malicious bots, to make it harder for attackers to gain access to compromised accounts, or to store user preferences on a website. In the same vein, the online advertising industry has used cookies as the primary client identification technology since the mid-1990s. Other practices may be less known, may not necessarily map to existing browser controls, and may be impossible or difficult to detect. Many of them - in particular, various methods of client fingerprinting - have garnered concerns from software vendors, standards bodies, and the media."_  
  
A few weeks ago I had a private chat with a dear friend of mine currently involved in the Trackography project \[2\] and developing his own tool for such purposes \[3\]. During the conversation, the idea of using Thug for analyzing if a website makes use of some of the techniques described in \[1\] and to which extent emerged. The idea of using an honeyclient for a so complete different and useful purpose was really exciting for me and so I started thinking about the best way to do it. In order to do it I had to replace httplib2 with requests at first since requests allows me to collect more details about a typical HTTP session. After that I started a new branch (which is still not public) which right now implements just a first single test as shown below.  
  
**$ python thug.py --web-tracking http://www.google.com  
\[2015-01-27 11:39:36\] \[MongoDB\] Analysis ID: 54c76ae8d637083631c9a7ea  
\[2015-01-27 11:39:36\] \[window open redirection\] about:blank -> http://www.google.com  
\[2015-01-27 11:39:37\] \[PRIVACY\] Cookie expiring at 2017-01-26 11:39:37 (more than 365 days from now)  
\[..\]**  
  
Right now it's not that useful but it will be once all the metrics will be implemented. Stay tuned because Thug is turning to be an honeyclient with steroids in the next weeks!  
  
\[1\] [Technical analysis of client identification mechanisms](http://www.chromium.org/Home/chromium-security/client-identification-mechanisms)  
\[2\] [Trackography project](https://myshadow.org/trackography)  
\[3\] [Trackmap](https://github.com/vecna/trackmap)  
\[4\] [Thug](https://github.com/buffer/thug)
