---
title: "SIP Module for Dionaea"
authors: ["Guillaume Arcas"]
date: "2011-09-27"
categories: 
  - "gsoc"
tags: 
  - "gsoc"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

The Honeynet Project had mentored 12 projects this year for the Google Summer  
of Code (GSoC). The 11th project was to extend the SIP module for  
Dionaea to handle SIP udp, tcp and even tls. With the TLS part, the  
Dionaea can even emulate a Microsoft Lync server. The TLS part was not  
part of the original scope, but the hard work made that possible as  
well!  
  
\[[Dionaea](http://dionaea.carnivore.it/)\] intention is to trap malware  
exploiting vulnerabilities exposed by services offered to a network,  
the ultimate goal is gaining a copy of the malware. With the SIP  
module, you can answer the SIP attacks, record the information. It is  
also possible to make "real" users, so the attacker will get different  
answers depending on which accounts he tries to hack. If you would  
fake a Microsoft Lync installation, you could add some of the real  
user names from your server and see if somebody is doing a targeted  
attack towards you. (but of course, don't use the same passwords.... )  
  
Dionaea is meant to be a nepenthes successor, embedding python as  
scripting language, using libemu to detect shellcodes, supporting ipv6  
and tls  
  
This year student was Phibo, which did a great job on extending the  
SIP module. Markus Koetter, the author of Dionaea was of great help on  
the coding and a quote from him: "Working with him was fun, I think  
both of us have learned something and - even more important - the code  
written exceeded my expectations."  
  
Test out [Dionaea](http://dionaea.carnivore.it/) for yourself today!  
  
The Honeynet Project would like to thank Phibo and especial Markus  
Koetter for the great job done on this project. This could not have  
been done without you! Thank you!  
  
\[Blog entry's author: Sjur Eivind Usken\]
