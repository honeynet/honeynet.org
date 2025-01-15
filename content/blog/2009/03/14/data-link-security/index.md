---
title: "Data Link Security"
authors: ["Sami Guirguis"]
date: "2009-03-14"
tags: 
  - "arp-spoof"
  - "data-link-layer-attacks"
  - "dhcp-starvation"
  - "layer-2"
  - "mac-flood"
  - "stp-manipulation"
  - "vlan-hopping"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

  

Buffer overflow, cross site scripting and sql injection have had their share of the spotlight,  

I have recently decided to give more attention to layer two issues and share my findings.

  

  

  

Some of the reasons that attracted me to layer two security is that there is a high percentage of 

  

insiders attacks by employees, the threat is under estimated and what is within the LAN is 

  

considered "trusted". Also more broadband providers deploy network access based exclusively on 

  

layer two (for fast recovery, the average convergence time for RSTP is far greater than OSPF and EIGRP ).

  

A DOS attack takes another damaging dimension in the data link layer than network layer.

  

  

The OSI layer was built to allow different layers to work without

  

 the knowledge of each other, that means that if a layer is compromised the other layers will not be aware.

  

It is finally worth mentioning that the boundaries of the LAN are no longer physical as wireless networks 

  

are used in the environment.

  

  

  

The first attack time that you might be familiar with is MAC flood A.K.A CAM table overflow,

  

(do not confuse CAM table <MAC Vs port> and ARP table <IP Vs MAC>) using tools such as macof

  

(available since 1998) it can generate 155,000 MAC/min. the average switch CAM table range between 16 to 128Kb, 

  

even with a auto refresh of the CAM table the default in most switches is generally around 5 min. 

  

Mitigating this attack would be limiting the amount of MAC addresses learned per port.   

  

  

  

ARP spoof (ARP poisoning) this attack targets the ARP table and basically takes advantage 

  

of the fact that any machine can claim to be any IP,  ettercap tool is very easy to launch 

  

this attack.Mitigation of this attack can be using static arp entries (an administrative burden for large 

  

networks) or using DHCP snooping  and dynamic ARP inspection that builds a binding table and when new gratuitous

  

arp entries are received they are compared to that table.

  

  

  

VLAN Hopping -- Switch spoofing this is a straightforward attack for ports that are configured for trunking 

  

or negotiate trunking and yet users are  connected to them, the attacker can spoof a switch using ISL or 802.1q

  

and as trunk ports have access to all VLANs Voila!, a tool that can enumerate a switch is Yersinia or if you are familiar

  

with brctl. Mitigation is secure configuration disabling unused ports, setting used ones to access mode only.

  

  

  

VLAN Hopping -- double tagging this attack is more complex and requires specific setup and has its limitations

  

It only works on 802.1q trunking standard it works even if the port is set to access only, as the switches do only one level of untagging when the attacker double tags a packet the switch forwards it to the other switch with a tag, the attack is limited to being unidirectional, and cannot work on a target on the same switch as the attacker and the attacker and trunk must have the same native VLAN.

  

  

  

STP manipulation the spanning tree protocol prevents layer 2 loops from being formed when switches 

  

are interconnected via multiple paths for redundancy, switches exchange BPDU messages to elect a root bridge,

  

elect a per VLAN designated bridge and in the case of topology change.

  

The pitfalls of STP/RSTP is the lack of authentication in the BPDU messages, if an attacker impersonates a switch and keep sending topology change BPDUs the other switches will enter an infinite loop of recomputing the algorithm.

  

Mitigation of this type of attack is by enforcing the placement of root bridges in the network (Root guard) or disabling the use of priority zero on users port (BPDU guard).

  

  

  

  

  

Private VLANs to create multiple LANs on the switch VLANs was the solution, to restrict communication between ports in the same VLAN, Private VLANs was the solution is uses port roles (Isolated, Promiscuous and community) to restrict communication between ports. this can be bypassed used a layer 2 proxy attack in which a packet is sent with the destination of the target IP address and the MAC address of the gateway, since switches are working in the MAC level and routers are on the  IP level.

  

this attack is unidirectional and can be prevented by configuring an access list on the router to prevent communication between the IPs of its LAN.

  

  

  

DHCP starvation is done by sending DHCP requests with spoofed MAC addresses to exhaust the DHCP server IP pool, according to RFC 2131 a hacker can introduce a rogue DHCP server assigning IPs to clients while the real DHCP server is up and running,

  

allowing a MITM attack.RFC 3118 defines DHCP authentication but there has not been an implementation of it.

  

  

  

Configuration best practices 

  

  

  

  

  
- Use dedicated PVLAN ports for trunk ports.
  
- Avoid VLAN 1.
  
- Deploy port security on switches.
  
- Set users ports to access mode only.
  
- Use ARP security options.
  
- Disable unused ports or put them in unused VLAN or Honeypot vlan,
  
- Be aware of DHCP attacks.
  

  

  

  

  

  

  

  

Sami Kamel Guirguis
