---
title: "Project 6 - IPv6 attack detector Report"
date: "2012-08-28"
categories: 
  - "gsoc"
tags: 
  - "gsoc-d20"
---

1 Introduction  
  
As the end of GSoC 2012 will come in the next few days, i am proud to announce IPv6-guard. IPv6-guard is an IPv6 attack detector tool including some defense mechanisms to protect against most of recent attacks on ipv6 protocol suite.  
  
2 IPv6-Guard  
  
2.1 How it works  
  
At first, the tool will gather “genuine” informations of connected network. Those information includes IP and MAC address of neighbors and routers on the network.After first time run, IPv6-guard will save this information to use later, if anything has change,it will ask for confirmation ( User can edit “/data/genuine.info” to add more interface if need). If the network is under attack, some invalid information might be detected and it will ask you to verify what information is “genuine”. IPv6-Guard will use collected information and signatures against every received packet to detect and mitigate IPv6 attacks from the network.  
  
Output:  
\[code\]  
Trusted ? \[Y/n\] y Got fe80::9c4e:a8a4:c6b9:7e6c / 6c:62:6d:07:7e:8c  
\[/code\]  
2.2 Examples  
  
• flood\_advertise6  
  
Output:  
\[code\]  
\[FLOOD PACKET\]  
Time : 2012-08-22 08:27:12  
From : 00:18:18:a5:65:5b (Cisco Systems)  
To : 33:33:00:00:00:01 (Unknow)  
Desc : flood\_advertise6  
\[/code\]  
This feature detect flood on a target with random neighbor advertisements. It is based on configured packet rate and a few heuristic algorithms.  
  
• flood\_solicitate6  
  
Output:  
  
\[code\]  
\[FAKE NEIGHBOR SOLICITATION\]  
Time : 2012-08-22 08:22:14  
From : 90:84:0d:84:b7:b2 (Apple, Inc)  
To : 33:33:ff:00:00:09 (Unknow)  
Desc : parasite6  
\[/code\]  
• fake\_router6 or flood\_router6  
  
Output:  
\[code\]  
\[FAKE ROUTER ADVERTISMENT\]  
Time : 2012-08-22 08:28:42  
From : 00:18:ab:36:4d:ac (BEIJING LHWT MICROELECTRONICS INC.)  
To : 33:33:00:00:00:01 (Unknow)  
Desc : fake\_router6  
\[/code\]  
This is an example to detect fake\_router6 attack by announcing a host as a router on the network with the highest priority. To protect host against this attack, the tool will send a packet with routerlifetime=0 to reset that fake router and invalid route in routing table.  
  
Also, when this attack is occured, the tool will also clean up host interface using “genuine” information collected earlier.  
  
Before  
\[code\]  
eth0: flags=4163 mtu 1500  
inet 192.168.56.1 netmask 255.255.255.0 broadcast 192.168.56.255  
inet6 2a01:9c11:db7e:d849:800:27ff:fe00:0 prefixlen 64 scopeid  
inet6 2a01:99ac:6b62:841a:800:27ff:fe00:0 prefixlen 64 scopeid  
inet6 2a01:b5ab:3408:9545:800:27ff:fe00:0 prefixlen 64 scopeid  
inet6 2a01:43c1:e2c6:6d96:800:27ff:fe00:0 prefixlen 64 scopeid  
inet6 fe80::800:27ff:fe00:0 prefixlen 64 scopeid 0x20  
\[/code\]  
Cleaning up  
\[code\]  
Clean ip 2a01:9c81:e745:eef2:800:27ff:fe00:0  
Mon Aug 20 21:16:44 2012  
Delete an ipv6 address of interface eth0 from 2a01:9c81:e745:  
eef2:800:27ff:fe00:0  
\[/code\]  
After  
\[code\]  
eth0: flags=4163 mtu 1500  
inet 192.168.56.1 netmask 255.255.255.0 broadcast 192.168.56.255  
inet6 fe80::800:27ff:fe00:0 prefixlen 64 scopeid 0x20  
ether 0a:00:27:00:00:00 txqueuelen 1000 (Ethernet)  
\[/code\]  
• smurf6  
  
Output:  
\[code\]  
\[FLOOD NEIGHBOR SOLICITATION\]  
Time : 2012-08-22 08:28:42  
From : 00:18:ab:36:4d:ac (BEIJING LHWT MICROELECTRONICS INC.)  
To : 33:33:00:00:00:01 (Unknow)  
Desc : rsmurf6 | sendpees6  
\[/code\]  
Detect smurf6 attack in which using our ip address with another MAC address.  
  
2.3 Supported Attack Detections  
  
Currently, this tool could detect various IPv6 attacks including:  
  
• parasite6: icmp neighbor solitication/advertisement spoofer  
  
• fake\_router6: fake router address (mitm)  
  
• flood\_router6: flood router advertisement packet  
  
• flood\_advertise6: flood neighbor advertisement packet  
  
• fake\_advertiser6: fake neighbor ip (mitm)  
  
• smurf6: flood icmp echo packet  
  
• rsmurf6: remote smurfer  
  
• fuzz\_ip6: flood ipv6 packet  
  
• fake\_mld6: fake multicast group  
  
• sendpees6: Generates a neighbor solicitation requests with a lot of CGAs.  
  
For protection, some simple methods are being implemented such as  
  
• Reset routerlifetime to delete fake route in routing table  
  
• Clear all invalid entries on attacked interface  
  
2.4 Synopsis  
\[code\]  
\# python2 6shield.py -i \-c  
\- interface interface to sniffing and detect attack  
\- config configuration file  
ex:  
\# python2 6shield.py -i eth0  
\[/code\]  
2.5 Configuration  
  
This tool includes a configuration file to detect attacks from thc-ipv6 tool. If another tool using similar techniques with different packet rate, you could add a new section for it  
\[code\]  
\[generic\]  
manuFile=manuf ; mac/manufacturer file  
; attack tool ( command line option)  
\[thc-ipv6\]  
routerLifetime=9999 ; router lifetime that attack using  
naLimit=10 ; Neighbor Advertisement packet/second limitation  
raLimit=10 ; Router Advertisement packet/second limitation  
icmpLimit=10 ; ICMP Echo packet per second limitation  
limitRate=20 ; IPv6 control packet per second limitation  
\[/code\]  
2.6 Future Works  
  
• Improve detection method to lower false positive chance  
  
• Improve protection method  
3.Requirements:  
\-Python2  
\-scapy: www.secdev.org/projects/scapy/  
\-Check out at: http://code.google.com/p/ipv6-guard/  
4\. Final words  
  
• Thanks Google for such a program for student  
  
• Thanks Honeynet Project for this cool project  
  
• Thanks Thanh Nguyen for help me finish this project
