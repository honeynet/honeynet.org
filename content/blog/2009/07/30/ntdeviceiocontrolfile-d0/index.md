---
title: "NtDeviceIoControlFile"
authors: ["Chengyu Song"]
date: "2009-07-30"
tags: 
  - "qebek-windows-socket-network"
---

As the console spy is almost finished, the next stage is mainly for network activities. Sebek Win32 version uses TDI hook to get this done. However, since getting driver object in virtualization layer is hard and TDI is TDI is on the path to deprecation, I need to find another way. The best solution seems to be hooking NtDeviceIoControlFile, the API Windows uses to do network related stuff and has been widely mentioned in malware behavior analysis papers. After some days of searching, I encounter a very useful resources today, a master thesis from TTAnalyze team:

  

  

**Understanding and Replaying Network Traffic in Windows XP for Dynamic Malware Analysis**

  

  

Anyone who is interested in related topic should find this useful as I do. Thank Petritsch for summarizing this great work.

  

  

\[2009-08-03\] Update1: The IoControlCode of recvfrom is 0x1201b, at the offset 0x10 of the InputBuffer is the address of the sockaddr, in which the remote ip (offset <del>0x10</del> 0x04) and port (offset <del>0x08</del> 0x02) is stored.  

  

  

\[2009-08-01\] Update2: The IoControlCode of accept is 0x1200c, at the offset 0x0C of the OutputBuffer is the remote port and at the offset of 0x0E is the remote ip.
