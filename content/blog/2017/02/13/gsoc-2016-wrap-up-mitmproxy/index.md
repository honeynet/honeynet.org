---
title: "GSoC 2016 Wrap Up: Mitmproxy"
authors: ["Maximilian Hils"]
date: "2017-02-13"
categories: 
  - "gsoc"
tags: 
  - "gsoc"
  - "mitmproxy"
coverImage: "mitmweb_1_0.png"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

With Google Summer of Code (GSoC) 2017 being around the corner, we’d like to do a short flashback to 2016, our most successful GSoC year for mitmproxy so far! GSoC 2016 was mitmproxy’s fourth time participating in the program under the umbrella of the Honeynet Project. For the first time, we were able to mentor three students over the summer to work on both our Python core and the brand new web interface. As a major milestone, mitmproxy is now a Python 3 project and has a fantastic user interface that even works on Windows. With these improvements in, we finally decided to pull the trigger and called it the [mitmproxy 1.0 release](https://corte.si/posts/code/mitmproxy/announce_1_0/index.html)!

![mitmweb screenshot](images/mitmweb_1_0.png)

_Mitmproxy is an interactive TLS-capable man-in-the-middle proxy. It can be used to intercept, inspect, modify and replay HTTP, HTTP/2, HTTPS, WebSockets, and raw TCP traffic. The open source tool can be used with any device or program to see how it communicates on the network. Mitmproxy is used by software developers, penetration testers, privacy advocates and researchers to fix bugs, find vulnerabilities, uncover privacy violations, conduct empirical research, and more._

We asked Clemens Brunner about his GSoC student experience with mitmproxy and Honeynet:

> I first heard about GSoC in March 2016, which was quite late but there still were some weeks to the end of the application period, so I immediately decided to give my best and write a good proposal. After some coding and design challenges as well as a very early morning Skype interview with my prospective mentor, the application phase was over and I was accepted as a GSoC student to work with Maximilian Hils as my mentor to improve mitmweb, the web UI for mitmproxy. The first challenge was to get familiar with ReactJS, a Javascript framework which was developed by Facebook and is used in mitmweb. I started developing right away and Max helped me to write good code which fits into the mitmweb project. We designed and then built the menus for the most important options (anticache, stickycookie,…) and for specific flow actions. After this we developed the functionality to save flows and load them again in a later session. We also made HTTP message bodies editable in mitmweb, so the user can modify the bodies directly in an editor in mitmweb or upload a file, which replaces the flow content. Last but not least, we also integrated the different content view modes from the mitmproxy console UI. It was a great experience to work and be part of an international open source developer team, and it is fantastic to see my code being used by thousands of users already. Thank you for the great summer!

We had a great time mentoring our students on their projects last year, thank you all! We would also like to thank Google for the fantastic opportunity that they have provided as well as the Honeynet Project for hosting us under their umbrella.

For 2017, we have prepared [two project ideas](https://honeynet.org/gsoc2017/ideas#mitmproxy) for mitmproxy and we’re keeping our fingers crossed that Honeynet will once again be part of the lucky selected mentoring organizations announced on February 27th!
