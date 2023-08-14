---
title: "Get STIX Reports from ICS Honeypot Conpot"
authors: ["Lukas Rist"]
date: "2014-08-06"
categories: 
  - "honeypot"
tags: 
  - "conpot"
  - "honeypot"
  - "ics"
  - "scada"
  - "stix"
  - "taxii"
---

The team working on the ICS/SCADA honeypot [Conpot](http://conpot.org), just merged in a more mature support for [STIX](https://stix.mitre.org/) (Structured Threat Information eXpression) formatted reporting via [TAXII](https://taxii.mitre.org/) (Trusted Automated eXchange of Indicator Information) into the master branch on [Github](https://github.com/glastopf/conpot).  

STIX allows us to represent event sessions captured by the honeypot in a structured format, which eases the integration of Conpot into existing consumer (e.g. SIEM) infrastructures.  

By transforming an arbitrary honeypot event into a schema defined format, we are able to communicate an incident in a language, which is also understandable by someone not trained in interpreting industrial protocol messages.  

The TAXII client allows us to transport the STIX reports to any TAXII service. By adopting this additional transporting capability, we are able to push the collected data live to interested parties, event manager applications and incident responders.  

[STIX](https://stix.mitre.org/)™ is a collaborative community-driven effort to define and develop a standardized language to represent structured cyber threat information. The STIX Language intends to convey the full range of potential cyber threat information and strives to be fully expressive, flexible, extensible, automatable, and as human-readable as possible.  

[TAXII](https://taxii.mitre.org/)™ is the main transport mechanism for cyber threat information represented as STIX. Through the use of TAXII services, organizations can share cyber threat information in a secure and automated manner.  

[Conpot](http://conpot.org) is a low interactive server side Industrial Control Systems honeypot designed to be easily deployed, modified and extended. By providing a range of common industrial control protocols, we created the basics to build your own system, capable to emulate complex infrastructures to convince an adversary that he just found a huge industrial complex.
