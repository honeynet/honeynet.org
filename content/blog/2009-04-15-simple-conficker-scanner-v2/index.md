---
title: "Simple Conficker Scanner v2"
date: "2009-04-15"
tags: 
  - "conficker-d40"
  - "detection"
  - "network"
  - "scan"
---

Today we released version 2 of our [Simple Conficker Scanner](http://four.cs.uni-bonn.de/conficker/) (SCSv2). It contains a new scanning method which allows for detection of machines infected with the recent Conficker version (D or E, depending on the naming scheme - the tool calls it D). Although the patch to the vulnerable function NetpwPathCanonicalize() was updated in the new variant, the RPC response codes for specially crafted requests are still different for infected machines. This enabled us to write a network scanner to distinguish Conficker zombies from clean hosts. The scanning results look like this:

  

  
`  
$ ./scs2.py 10.0.0.1 10.0.0.5  
Simple Conficker Scanner v2 -- (C) Felix Leder, Tillmann Werner 2009  
[UNKNOWN] 10.0.0.1: No response from port 445/tcp.  
[UNKNOWN] 10.0.0.2: Unable to run NetpwPathCanonicalize.  
[CLEAN] 10.0.0.3: Windows Server 2003 R2 3790 Service Pack 2 [Windows Server 2003 R2 5.2]: Seems to be clean.  
[INFECTED] 10.0.0.4: Windows 5.1 [Windows 2000 LAN Manager]: Seems to be infected by Conficker D.  
[INFECTED] 10.0.0.5: Windows 5.1 [Windows 2000 LAN Manager]: Seems to be infected by Conficker B or C.  
done  
`

  

The code was released under the GNU General Public License. Get it from [here](http://four.cs.uni-bonn.de/uploads/media/scs2.zip), feel free to adopt and please use it in your scanner tool.

  
  

**Update:** Florian Roth has compiled a Windows version which is available for download from [his website](http://www.bsk-consulting.de/download/scs2-win32.zip).
