---
title: "Introducing Conpot"
authors: ["Lukas Rist"]
date: "2013-05-11"
tags: 
  - "honeypot-d9"
  - "ics-d114"
  - "scada-d51"
---

We proudly announce the first release of our Industrial Control System honeypot named [Conpot](http://conpot.org).  
  
Until now setting up an ICS honeypot required substantial manual work, real systems which are usually either inaccessible or expensive and lecture of quite tedious protocol specifications. With implementing a master server for a larger set of common industrial communication protocols and virtual slaves which are easy to configure, we provide an easy entry into the analysis of threats against industrial infrastructures and control systems.  
  
Conpot by itself provides a rather small attack surface. But even without additional efforts to promote your back yard nuclear reactor, you will see connections scanning your system for information. If you are interested in larger amounts of data, we recommend to deploy a Human Machine Interface connecting to Conpot. This way adversaries will be able to find your sensor using search engines and specially crafted keywords.  
  
So far we support two major ICS protocols: Modbus and SNMP (jokingly refer to it as “Security is Not My Problem”). Both are de facto standards when it comes to communication between industrial systems and their controllers. When these protocols got defined in the 80s and 90s, there was no inevitable need for security as one expected the systems where only connected to an internal network or a local console, literally air gapped to the internet. Since every aspect of a company gets connected, the once isolated control systems appear in the public network. No matter if it’s on purpose, to be able to lower the fuel rods from home, or by accident, recent reports show that the gap, everyone was expecting, isn’t there anymore. With industrial espionage on the rise this also caught the attention of the less friendly tempered.  
  
The default configuration of Conpot simulates a basic [Siemens SIMATIC S7-200](http://www.automation.siemens.com/mcms/programmable-logic-controller/en/simatic-s7-controller/s7-200/pages/default.aspx) PLC with an input/output module and a [CP 443-1](https://www.automation.siemens.com/mcms/industrial-communication/en/ie/system-interfacing/simatic-s7-sinumerik-o/s7-400/pages/cp443-1.aspx) which would be needed in a real setup to provide network connectivity.
