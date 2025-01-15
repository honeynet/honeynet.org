---
title: "Dissecting the SotM Attack Trace Pcap"
authors: ["Tillmann Werner"]
date: "2010-02-19"
tags: 
  - "forensic-challenge-2010"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

Hi everybody,  
  

our first [Scan of the Month Challenge](https://honeynet.org/node/504) in 2010 is over! We received 91 submissions in total, and some parts of the solutions are so interesting that I would like to publicly highlight them in this post. Now that the winners are announced (Congratulations Ivan, Franck, and Tareq!), I think I also owe you an explanation why we asked the specific questions and what we expected as answers. I am sure you will be surprised how many pieces of information you can dig up in a plain pcap - I was indeed when I had a look at the solutions we received. Enjoy!

  
  
  

We received 91 submissions in total. A maximum of 40 points was possible, and we awarded up to 2 additional points for cool explanations and smart approaches. Here is a chart that shows the score distribution for all solutions.

  
  

I skip the **first 3 questions** as they are really trivial, and I think almost everybody provided the correct answers. Just one thing, we said in the announcement of the challenge that the victim IP address has been changed to hide the true location. It was **not** a box at Adobe Systems Inc. that was targeted. We changed the address to a random one to protect the box the trace was recorded on. Maybe we should have changed it to something like 127.8.9.10 to make it more obvious.

  
  

The right answer to **question 4** (How long did it take to perform the attack?) is: _The attack lasted 16.219218 seconds._ The pcap format supports nanosecond granularity, so why round this value up instead of giving the exact answer?

  
  

I must admit that **question 5** is not as easy as it seems. Which operating system was targeted by the attack? And which service? Which vulnerability? OK, the service can easily be determined by taking a look at the TCP stream that carries the actual exploit. It's a SMB session over which the LSASS service is accessed, and the `DsRoleUpgradeDownlevelServer` call is executed. The vulnerability is obviously the [MS04-011](http://www.microsoft.com/technet/security/Bulletin/MS04-011.mspx) one (or [CVE-2003-0533](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-0533) if you prefer CVE numbers) that was discovered by [eEye](http://research.eeye.com/html/advisories/published/AD20040413C.html) in 2003.

  
  

What remains is the operating system targeted by the attack. And that's tricky one. Wireshark does the SMB dissection for us, and it shows that in packet 16 we have the unicode string `Windows 5.1`, which means the system is a Windows XP box (if you don't know which number belongs to which Windows version, do a web search, there are plenty of resources). But can we also find out the service pack? The [advisory](http://www.microsoft.com/technet/security/Bulletin/MS04-011.mspx) tells us that XP SP2 and later is not vulnerable to this particular attack, so it must be either SP0 or SP1. We can confirm that the exploit is designed for Windows XP by taking a look at its internal structure. The exploit fraction in packet 31 has the double-word `0x00460001` at offset 0x2aa. If we convert that number to x86 host byte order, we get `0x01004600`, which is a known [opcode](http://www.metasploit.com/opcodedb) commonly used in LSASS exploits, e.g. the one from [House of Dabus](http://downloads.securityfocus.com/vulnerabilities/exploits/HOD-ms04011-lsasrv-expl.c) (HOD).

  
  

I have to anticipate and tell you that the victim was a honeypot system - in fact, it was [honeytrap](http://honeytrap.carnivore.it/) running in mirror mode, so everything was sent back to the attacker (we excluded the mirror connections from the trace file). Now that we know that what we see is actually an attacker talking to his own machine, we can use Michal Zalewski's [`p0f`](http://lcamtuf.coredump.cx/p0f.shtml) to determine its OS:

  
  
$ p0f -qls ./attack-trace.pcap | head -1  
98.114.205.102:1821 - Windows XP SP1+, 2000 SP3 -> 192.150.11.111:445 (distance 15, link: ethernet/modem)  
  

Putting it all together we now know that the exploit was targeting a Windows XP SP1.

  
  
Please check out the winner solutions for great answers to the other questions. Thanks to everybody who participated.  
  
Tillmann
