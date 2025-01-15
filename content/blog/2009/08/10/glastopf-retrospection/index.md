---
title: "Glastopf retrospection"
authors: ["Lukas Rist"]
date: "2009-08-10"
tags: 
  - "glastopf"
  - "webhoneypot"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

Today I make a retrospection on my work on the Glastopf Web Honeypot during the Google Summer of Code Program. My goal was to push forward the development on a Honeypot for an attack vector in web security which is really underestimated in current discussions. The main objectives could be merged into one intention: Increasing our attractiveness and answering every request as close as possible to a real world system. This got achieved with the new PHP file parser and the dynamic Google dork list which we provide for the Google crawler.  
Since the past three months, we also collected a lot of attacks. Actually we have around 1.27 million unique attacker IP and requested vulnerability combinations in our database. In total we have something above 14 million hits on our three deployed sensors. We also collected the vulnerabilities which got triggered by the attacker. Currently we have more than 30 thousand different vulnerabilities in the database! So there is a lot of noise out there to catch :)  
For the coming months after the Google Summer of Code program I'm looking forward to finish the integration of Glastopf in the [SURFids](http://ids.surfnet.nl/) environment (a plugin is already done), and further steps into the improvement of the PHP file parser. There are also plans on analyzing the collected PHP bots and botnets.  
So the program was real fun and I've learned a lot during this summer. I'm looking forward to increase the already existing knowledge from the Honeynet Project on web app security and the methods used by the attackers!
