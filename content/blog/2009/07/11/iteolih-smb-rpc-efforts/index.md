---
title: "Iteolih: SMB/RPC efforts"
date: "2009-07-11"
tags: 
  - "iteolih-samba-dcerpc-python"
---

During the last weeks I have been working on SMB and specifically DCERPC support for the [Dionaea](http://dionaea.carnivore.it/ "dionaea homepage") next generation low-interaction honeypot (buzz!).

  
  

SMB / CIFS is a huge protocol with several protocol versions and a lot of message types. The [CIFS technical reference](http://www.snia.org/tech_activities/CIFS/) and the [Implementing CIFS](http://ubiqx.org/cifs/) book have been constant companions for me since the beginning of the project.

  
  

What we basically want to achieve is having a stable base for registering certain known-to-be vulnerable RPC calls in modules to detect exploits and thus be able to collect malware. This way one can easily write a new module if a new patch or exploit gets released for yet another vulnerability without going through the hassle of implementing all SMB message types in each module. In the past we had to manually implement each one in a C++ module for the nepenthes honeypot.

  
  

To overcome the limitations of the old design the new honeypot Dionaea consists of a beautiful C core with lots of funtionalities and has the ability to load vulnerability modules written in Python. Choosing a scripting language like Python makes life easier for the developers of modules, **like me :)**.

  
  

Although the support is not yet stable and complete, we already can detect a subset of exploitations. Here is an example (stripped for better readability) debug output of the ms08-067 module registering the according RPC call and detecting a request:

  
`[11072009 17:14:32] connection: connection 0x828f20 type -> none->accept  
[11072009 17:14:32] connection: connection 0x828f20 state accept 127.0.0.1:5001 -> 127.0.0.1:32848 none->connected  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Negociate_Protocol_Request  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_Negociate_Protocol_Response  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Sessionsetup_AndX_Request  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_Sessionsetup_AndX_Response  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Treeconnect_AndX_Request  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_Treeconnect_AndX_Response  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_NTcreate_AndX_Request  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_NTcreate_AndX_Response  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Write_AndX_Request / SMB_Data  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_Write_AndX_Response  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Write_AndX_Request / SMB_Data  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_Write_AndX_Response  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Read_AndX_Request  
[11072009 17:14:32] SMB: Found UUID of SRVSVC. Accepting Bind.  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_Read_AndX_Response / SMB_Data  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Read_AndX_Request  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_Read_AndX_Response / SMB_Data  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Write_AndX_Request / SMB_Data  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_Write_AndX_Response  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Write_AndX_Request / SMB_Data  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_Write_AndX_Response  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Write_AndX_Request / SMB_Data  
[11072009 17:14:32] SMB: response: NBTSession / SMB_Header / SMB_Write_AndX_Response  
[11072009 17:14:32] SMB: packet: NBTSession / SMB_Header / SMB_Read_AndX_Request  
[11072009 17:14:32] SMB: got the DCERPC request for NetprPathCanonicalize. MS08-067 exploit?  
[11072009 17:14:32] SMB: drop dead!  
[11072009 17:14:32] SMB: process() returned None.  
[11072009 17:19:17] connection: connection 0x828d10 state accept 127.0.0.1:5001 -> 127.0.0.1:32848 connected->close  
`  
  

Developing for this new honeypot is really fun and the SMB protocol is challenging. We will continue improving the support and detection during the course of the project. **Stay tuned!**

  
  

Mark
