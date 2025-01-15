---
title: "Heralding - the credentials catching honeypot"
authors: ["Johnny Vestergaard"]
date: "2016-03-23"
tags: 
  - "heralding"
  - "honeypot"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

Sometimes (actually, most times) you don’t need advanced deception technology, but rather just a simple tool to answer some simple questions. I was recently in that situation, and needed the answers to the following questions:

  

  
- Which protocols does my adversary try to brute-force?
  
- Which username and password did he use?
  
- At which speed did he brute-force?
  
- From where did he proxy from?
  
- What time of day did he brute-force?
  

  

To answer these questions, I needed a tool that would output something similar to:  
  
`2016-03-12 20:35:02.258198,192.168.2.129,51551,23,telnet,bond,james  
2016-03-12 20:35:09.658593,192.168.2.129,51551,23,telnet,clark,P@SSw0rd123  
2016-03-18 19:31:38.521047,192.168.2.129,53416,22,ssh,guest,guest  
2016-03-18 19:31:39.376768,192.168.2.129,53416,22,ssh,HundeMad,katNIPkat  
2016-03-18 19:33:07.064504,192.168.2.129,53431,110,pop3,charles,N00P1SH  
2016-03-18 19:33:12.504483,192.168.2.129,53431,110,pop3,NektarManden,mANDENnEktar  
2016-03-18 19:36:56.077840,192.168.2.129,53445,21,ftp,Joooop,Pooop  
`

  

  

To fulfill my requirements I forked and modified an [existing](http://www.beeswarm-ids.org) open source project to facilitate the creation of a new simplistic honeypot: 

  

  
[Heralding - the credentials catching honeypot](https://github.com/johnnykv/heralding).  
  
The source code and install instructions can be found in the [Github repo here](https://github.com/johnnykv/heralding).  
  
Key points: Simplicity works, open source rocks!

  

  

Regards,

  

Johnny Vestergaard

  

[LinkedIN](https://www.linkedin.com/in/johnnykv)

  

[Mail](mailto:jkv@unixcluster.dk)
