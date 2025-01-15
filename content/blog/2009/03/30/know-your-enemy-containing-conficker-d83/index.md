---
title: "Know Your Enemy: Containing Conficker"
authors: ["Lance Spitzner"]
date: "2009-03-30"
categories: 
  - "kye"
tags: 
  - "kye"
  - "conficker"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

The Honeynet Project is excited to announce the release of [Know Your Enemy: Containing Conficker](/papers/conficker/).    In this paper we present several potential methods to contain Conficker. The approaches presented take advantage of the way Conficker patches infected systems, which can be used to remotelydetect a compromised system. Furthermore, we demonstrate various methods to detect and remove Conficker locally and a potential vaccination tool is presented. Finally, the domain name generation mechanism for all three Conficker variants is discussed in detail and anoverview of the potential for upcoming domain collisions in version .C is provided. Tools for all the ideas presented  are freely available for download including source code.  This paper was authored by Tillmann Werner and Felix Leder.

In addition, as a result of this paper and the hard work of Dan Kaminsky, most vulnerability scanning tools (including Nmap) should now have a plugin or signatures that allow you to remotely detect infected Conficker systems on your networks.  Finally, we would like to recognize and thank the tremendous help and input of the [Conficker Working Group.](http://www.confickerworkinggroup.org)
