---
title: "Bison/Flex parser"
authors: ["Robin Berthier"]
date: "2009-06-27"
tags: 
  - "honeybrid-gsoc-parser"
---

This week I completed an important step which is to integrate a parser in Honeybrid. There are now two new files in the source code:

  

  
- _rules.l_ which defines the different tokens to analyze,
  
- _rules.y_ which defines the configuration language and the different subroutines to call when a specific combination of tokens is detected.
  

  

[Flex](http://dinosaur.compilertools.net/flex/manpage.html) and [Bison](http://dinosaur.compilertools.net/bison/manpage.html) compile these two files and generate _rules.c_ and _rules.h_ which are then used by honeybrid to parse its configuration. The great advantages of having a parser are to have a flexible configuration file and to better handle configuration errors with a short volume of code.

  

The configuration of Honeybrid is now defined in a single file _honeybrid.conf_, which is divided in three sections:

  

  
2. _Configuration parameters_: to define the general parameters of Honeybrid (logging level, log output files, network behavior, network timeouts...).
  
4. _Module definition_: to define the parameters of each decision modules. Note that a module can be defined multiple times with different parameters. A unique name is assigned to each module definition.
  
6. _Target definition_: to define the IP spaces covered by honeybrid and the behavior of honeybrid when receiving packets to these IP spaces.
  

  

The goal with the _target_ section is to precisely control the behavior of the honeynet at each stage of an attack: during initialization (_frontend_), during the attack itself (_backend_), and after the attack, when the honeypot is compromised (_outbound control_). So the _target_ section is made of four keywords:

  

  
- _filter_: a pcap filter expression (similar to tcpdump filter syntax) to define the network traffic that this target should cover.
  
- _frontend_: a honeypot IP address followed by a sequence of decision modules, to define which frontend honeypot should first answer to requests sent to this target, and which decision criteria to apply to accept request packets.
  
- _backend_: a honeypot IP address followed by a sequence of decision modules, to define which backend honeypot should take over the network sessions initiated between attackers and the frontend, and which decision criteria to apply to start the redirection.
  
- _control_: a sequence of decision modules, to define how to limit outgoing packets from network sessions initiated by honeypots.
  

  

An example of the final configuration file is attached to this blog post.
