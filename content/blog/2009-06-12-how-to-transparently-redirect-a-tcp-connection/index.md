---
title: "How to transparently redirect a TCP connection"
date: "2009-06-12"
tags: 
  - "honeybrid-gsoc-redirection"
coverImage: "redirection_diagram_20090611.jpg"
---

TCP was built to allow 2 hosts to exchange a stream of packets reliably. Honeybrid must add a third host to this operation when it decides to investigate further a connection. The keys for this process to work are: 1) a replay process that gets the high interaction honeypot to the same state than the low interaction honeypot; and 2) a forwarding process that translates not only IP addresses but also TCP sequence and acknowledgement numbers. Here is how things work in detail:

  

  
2. An external source _S_ initiates a TCP connection with an IP address _D1_ belonging to a honeynet instrumented with Honeybrid. Honeybrid is configured so that _D1_ is a low interaction honeypot that will complete the TCP handshake with _S_.
  
4. Packets sent by _S_ and carrying data are analyzed by the Decision Engine of Honeybrid. If a packet payload matches a decision rule, then Honeybrid decides to investigate further this connection by forwarding it to a high interaction honeypot _D2_.
  
6. Before this forwarding process to start, Honeybrid has first to get _D2_ to the same state than _D1_. This is achieved by replaying the beginning of the connection between _S_ and _D1_ to _D2_.
  
8. When _D2_ is ready to take over the connection, Honeybrid starts the forwarding process between _S_ and _D2_. The source IP of packets sent by _D2_ are replaced with the address of _D1_, and the destination IP of packets sent by _S_ are replaced with the address of _D2_. TCP sequence and acknoweldgement numbers as well as TCP options are also translated, otherwise packets would be discarded by the TCP/IP stacks of _S_ and _D2_. 
  

  

The main challenge with this process it to prevent the source _S_ from noticing that the destination of the connection has been changed from _D1_ to _D2_. Therefore, the replay phase should go as fast as possible so that it does not add a latency that could be fingerprinted by _S_. The fact that _S_ is an external host while _D1_ and _D2_ are on the local network reduces such risk.

  

The diagram attached illustrates the entire mechanism with a short TCP connection of 13 packets.

  

From an implementation perspective, Honeybrid uses [libnetfilter queue](http://www.netfilter.org/projects/libnetfilter_queue/index.html "lbnetfilter queue") to be able to process packets in user land. The decision engine of Honeybrid was previously working on a separate thread to prevent the decision process from delaying the main packet processing queue. The problem was that the decision thread and the main thread had to concurrently access the same data structure. This could create severe instability issue when a large volume of packets were handled. This week I added a #define statement to Honeybrid so that the thread can be easily disabled. I will now test with and without the thread to precisely measure the efficiency drop and the stability gain.
