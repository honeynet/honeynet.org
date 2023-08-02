---
title: "Revitalizing a Centralised Honeypot Framework"
authors: ["Rogier Spoor"]
date: "2015-11-19"
tags: 
  - "framework-honeypot"
---

  

_Bringing the dead back to life_

  

  

In early 2005 the SURFids Framework, later renamed to SURFcert IDS, was developed ([http://ids.surfnet.nl/wiki/doku.php](http://ids.surfnet.nl/wiki/doku.php)). The unique concept was the centralised detection approach, based on honeypots, with decentralised sensors running OpenVPN. From a marketing perspective ‘IDS’ was chosen in the name, in that age a popular term. Many organisations worldwide have used this open-source framework, however with a last update on the code in 2011, the project slowly died.

  

In early 2015, several members of the HoneyNED project ([https://www.honeyned.nl/](https://www.honeyned.nl/)), being part of HoneyNet ([https://www.honeynet.org/](https://www.honeynet.org/)), decided to revitalize SURFids under a new name: **Anansi  
**

  
  

>   
> 
> **Anansi** is an African folktale character. He often takes the shape of a spider and is considered to be the spirit of all knowledge of stories. He is also one of the most important characters of West African and Caribbean folklore.
> 
>   

  

With the interest of different parties such as SURFnet (the Dutch National Research Network), a commercial organization and a governmental body, our HoneyNED chapter aims at providing the Honeypot community with a new state-of-the-art open source, centralised honeypot framework. The key concept is to create ‘dumb’ sensors that tunnel attacks through VPN to a centralised server, which runs multiple honeypots and/or analysing algorithms. The centralised server also includes a management interface to administer all sensors, honeypots and detection algorithm. The analysis part will be based on Elastic Search, Logstash and Kibana. Deploying a first proof-of-concept is scheduled for December 2015.

  

  

In order to have a sustainable base for Anansi a project board has been founded in which participating organisations collaborate with HoneyNED. All participants stress the importance to put the Anansi open-source code under the umbrella of an independent respectable and known foundation in order to facilitate third parties to join this project. Any third party that wishes an additional Anansi feature can contribute in-kind or will be able to make a financial donation to the foundation. The roadmap and development effort will be governed from this foundation.

  

  

Anansi is not intended to re-invent the wheel and therefore we’re looking forward to collaborate with existing projects like T-pot, Arakis and others. Please feel free to contact us if you see opportunities for collaboration.

  

  

**HoneyNED** will keep you updated on the Anansi developments.

  

  

_Tommy & Rogier (email myname@honeyNED.nl)  
_
