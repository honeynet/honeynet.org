---
title: "Dionaea Installation"
authors: ["Oguz Yarimtepe"]
date: "2011-05-09"
tags: 
  - "debian"
  - "dionaea"
  - "log-record"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

This summer, I will be dealing with the malware analysis distribution from a visualization perspective at a timeline and geographic basis. To collect data related with malwares, I installed the [Dionaea](http://dionaea.carnivore.it), which is a successor of Nepenthes. The documentation of the Dionaea is plain and easy to follow. I chosed Debian Squeeze to install the honeypot on it. Installing the base system from netinstall CD and following the documentation was enough till i got an error message during the compiling process of Dionaea. "common" from the irc channel of Nepenthess was helpful about the solution of the problem. The problem was defined at http://sourceforge.net/mailarchive/message.php?msg\_id=27441025. It was because of the wrong Cython version usage with a makefile error.  
  
After fixing them, the installation was successful. Now, i am ready to open the honeypot to the public.
