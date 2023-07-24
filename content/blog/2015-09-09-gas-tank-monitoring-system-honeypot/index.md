---
title: "Gas Tank Monitoring System Honeypot"
date: "2015-09-09"
categories: 
  - "honeypot"
tags: 
  - "conpot-d32"
  - "honeypot-d9"
  - "ics-d114"
---

The [Conpot](http://conpot.org) team is following closely the latest developments in Honeypot research and the methods and technologies used. If you look at the topics presented on security conferences, you might have also noticed an increased interest in ICS security and honeypot technologies in the last two years. One presentation from this years Blackhat’15 conference caught my attention also knowing previous research done by Kyle and Stephen: “The little pump gauge that could: Attacks against gas pump monitoring systems” \[[link](https://www.blackhat.com/us-15/briefings.html#the-little-pump-gauge-that-could-attacks-against-gas-pump-monitoring-systems)\] If you are interested in their findings, I recommend their white paper: “The GasPot Experiment: Unexamined Perils in Using Gas-Tank-Monitoring Systems“ \[[link](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/the-gaspot-experiment), [pdf](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_gaspot_experiment.pdf)\] by [Kyle Wilhoit](https://twitter.com/lowcalspam) and [Stephen Hilt](https://twitter.com/sjhilt) from Trend Micro’s Forward-Looking Threat Research team.  
  
So we had the great idea to add exactly that feature to Conpot...  
  
Adding the capability to Conpot to emulate this gas pump monitoring system was a rather easy exercise considering [GasPot]( https://github.com/sjhilt/GasPot) published by the before mentioned researchers. Embedding their implementation into Conpot gives me the advantage of the honeypots mature framework, its logging capabilities, session tracking, template system and the possibility to combine it with other protocols. It goes without saying that, as with all the templates provided with the factory version of Conpot, you should modify the gas pump template so it can’t be fingerprinted and your gas station and product names match the geolocation of your honeypot. It is also unlikely that the IP address of a gas pump monitoring system belongs to the Amazon Web Services range or its nmap OS fingerprint matches that of an iPhone (not suggesting that you should try to run Conpot on an iPhone).  
  
If you are interested in the details of this feature, the initial feature pull request can be found [here](https://github.com/mushorg/conpot/commit/61ee0f5881ef1ed127181450057cf049b5487905).  
  
Conpot is a modular honeypot providing various protocols and a templating system to emulate complex industrial systems. The project is open source and available on [GitHub](https://github.com/mushorg/conpot). For more details check out our [web page](http://conpot.org/) get in contact on [gitter]("https://gitter.im/mushorg/conpot) or write me [directly](https://twitter.com/glaslos).
