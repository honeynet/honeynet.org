---
title: "A new and improved version of Rumal"
authors: ["Roberto Tanara"]
date: "2016-09-05"
categories: 
  - "gsoc"
tags: 
  - "gsoc"
  - "gsoc2016"
  - "rumal"
  - "thug"
---

Thug is a client honeypot that emulates a real web browser, fetches and executes any internal or external JavaScript, follows all redirects, downloadable files just like any browser would do, and collects the results in a mongodb collection. The purpose of this tool is to study, analyse and locate exploit kits and malicious websites. Thug’s analysis can be difficult to navigate or understand and this is where Rumal comes in. Rumal’s function is to be Thug’s GUI, providing users with trees, graphs, maps, tables and intuitive representations of Thug’s data.

If this is the first time you hear of Rumal or Thug or just want to read more about them, then we suggest you take a look at some of the following resources:

- Thug [https://github.com/buffer/thug](https://github.com/buffer/thug)
- Rumal, a web GUI for Thug [https://www.honeynet.org/node/1312](https://www.honeynet.org/node/1312)
- GSoC 2015: Introducing Thug’s Rumal [https://sysenterhoneynet.wordpress.com/2015/03/06/gsoc-2015-introducing-thugs-rumal/](https://sysenterhoneynet.wordpress.com/2015/03/06/gsoc-2015-introducing-thugs-rumal/)
- GSoC 2016 project [https://honeynet.org/gsoc/ideas#project8](https://sysenterhoneynet.wordpress.com/2015/03/06/gsoc-2015-introducing-thugs-rumal/)
- Rumal’s Documentation [http://thugs-rumal.github.io/](http://thugs-rumal.github.io/)
    

The Rumal GSOC 2016 project assigned to Dennis Parchkov adds features and improvements to the previous 2015 GSoC Rumal project that was in its early alpha stage.

During the GSoC program, running from May to August 2016, the following tasks have been completed:

[A dockerized version](https://github.com/thugs-rumal/rumal_docker)[i](https://github.com/thugs-rumal/rumal_docker)savailable[,](https://github.com/thugs-rumal/rumal_docker) to make installation and testing even simpler.

A working version of rumal\_docker can now be easily installed to test this tool. This only requires you to have Docker installed on your system. To aid in the installation, we created a Github page for this project with a guide on building and running rumal with docker [http://thugs-rumal.github.io/docker.html](http://thugs-rumal.github.io/docker.html).

The backend daemon run\_thug used the subprocess Python module to launch Thug in a dockerized environment. Docker-py is a python library used to control containers and may be a viable alternative to sub process.

Subprocess popen module that was originally used for launching docker scans is currently the most viable option. Docker-py has limitations in controlling docker containers as certain options cannot be used, such as --rm. It is not officially supported by docker and lacks clear and up to date documentations. Error messages can sometimes be very vague. More information about docker-py’s limitation can be found here:[http://blog.bordage.pro/avoid-docker-py/](http://blog.bordage.pro/avoid-docker-py/)

Communication between front-end and back-end happened via rest APIs, now a communication system based on RabbitMQ is available

A prototype communication system has been implemented using RabbitMQ and the pika python library. This communication system has been developed to handle the issues with distributed multiple backend/frontends, and specifically these problems:

- Is it possible to have multiple consumers (backends) and a single frontend?
- Is it possible to choose what backend you want to use?
- Would it be possible to have multiple publishers (frontends) as well?

 When running a new scan you can now select which backend you want to run the scan on, which will send this scan via a private queue to the backend you specified. If you have no preference on which backend to run the scan you can select ANY option which will place it on a public queue and it will be picked up by the 1st available backend.

A list of backends and the location of the public ANY queue is specified on the frontend backend.conf file. Some sort of auto discovery needs to be implemented in the future. More information about this architecture can be found on Rumal’s documentation: [http://thugs-rumal.github.io/architecture.html](http://thugs-rumal.github.io/architecture.html)

Robust communication between front-end and back-end

The back-end currently runs a consumer daemon which only handles receiving, saving and replying to messages. Work was done on  making the new communication system more robust and able to handle disconnects, timeouts and uncommon situations that may results in the daemon crashing.

A possible future development would be to combine run\_thug and consumer into one daemon.

Rumal Docker with RabbitMQ

Rumal Docker was modified to use the new RabbitMQ communication system. This involved adding all the requirements to run RabbitMQ and starting all the new daemons. Using RabbitMQ removed the dependency to run the back-end web server (previously used for the TastyPie Rest API), thus the back-end web server is no longer required and has been removed from this docker version and documentation.

Rumal known issues fixed

Known Github issues were resolved. Rumal report panels were redesigned. The basic info panel is constantly open to view the information on the selected node, while other panels need to be hovered over to display their contents. More information about issues that have been fixed can be found on Rumal’s github page [https://github.com/thugs-rumal/rumal/issues](https://github.com/thugs-rumal/rumal/issues).

Advanced scan search using a complex search language

 As we know the analysis returned by Thug can be time consuming to look at, understand or find specific patterns. This feature was developed to help users in finding scans with a certain pattern within the fields of Thug’s data.

The advanced search was implemented to build complex queries used to filter and find scans with specific behaviors. This feature is built using pyparsing, that parses a string into a syntax tree that is then converted into a MongoDb query that is able to fetch all analyses that satisfy the query. Unit tests have been made for testing the behaviors of both processes (string to syntax tree and syntax tree to mongo query).  
  

Building a Social Platform

 Rumal can be run on a single machine, but its potential power can be fully exploited with collaborating  users collecting and sharing multiple perspectives.

Rumal now supports the use of public, private and group scans with the ability to comment and tag:

- Groups (just like on Facebook) will provide users a private area where they can run scans, comment and tag, all within a group of collaborators. Only authorized collaborators can see and access the group. Groups can be modified at any time by the owner (removing/adding users). 
- Public scans allow anyone to view, comment and tag your scan, while a private scan is only for yourself to view. Owners can modify the sharing model of their scan at any time.
- Commenting will give users the ability to show their perspective and ideas about results of a public scan (or within a group). Comments are attached to nodes (url and IP address) within the analysis tree and can be switched by selecting a node.
- Tags allow you to show to other users what is important in a public or group scan. Tags are attached to the entire scan and are saved within the mongo database. They can be used within the advanced search to find scans with specific tags. 
    

 A concept we had in mind while developing the social aspects for Rumal was to let users give their understanding about scan results. The more people share their ideas, the more information we have on the scan, with of course some sort algorithm to filter incorrect data (which can be difficult).

Want to learn more or try out the tool? We have one location with all the necessary information.

Using Github pages, Rumal now has its own documentation site that contains information about installation, architecture, usage and development([http://thugs-rumal.github.io/](http://thugs-rumal.github.io/)). If you have any issues or ideas please do not hesitate and contact a Rumal developer or get involved yourself. 

**  
A couple of future developments that we have in mind:**

Combining run\_thug and consumer daemons on the backend

Plugin development: the current plugin architecture allows developers to create their own enrichment of Thug’s data but no way of displaying them. There needs to be a way of providing a way for developers to decide how to display their enriched data.

Auto discovery of back-ends: Some sort of auto discovery needs to be implemented so that you can link back-ends to front-ends.

Similar Comments: When viewing comments on a node (URL, IP address), a feature that might be useful would be displaying comments from a similar URL or exact IP address. In the case where multiple scans for the same url exist, allowing comments to be shared between them (if authorized), will allow ideas to be broadcasted.
