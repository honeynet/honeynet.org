---
title: "HoneyWeb, a web interface to manage client honeypots"
authors: ["Thibaut Gadiolet"]
date: "2009-05-26"
categories: 
  - "gsoc"
  - "honeypot"
tags: 
  - "client"
  - "gsoc"
  - "honeypot"
  - "honeyweb"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

Hi folks !  

As the GSoC started, this blog entry will introduce to you, myself and my project.

My name is Thibaut, I am still a student like all GSoC participants I guess and I belong to the ENSI of Bourges (France). I took one year off for doing research at the university of Maryland (USA) in the IT security field, especially in honeypots.

About my GSoC project, here is a short description of it:  

Honeyweb allows everyone who possess one or several honeypot clients to manage them via a friendly-user web interface.  
I am in charge of developing this java-based web application that we can divide in three parts:

- The front-end, providing a user-friendly, standardized interface for a large kind of client honeypots.
- A business layer, communicating with a java wrapper (already developed by David Stirling for Capture).
- A back-end, providing the data persistence to collect, store and aggregate client honeypots results.
