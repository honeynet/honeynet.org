---
title: "Long-term distributed honeypot network deployment logistics"
authors: ["David Pisano"]
date: "2026-01-14T11:00:06+01:00"
tags: ["Tpot"]
---
## Overview
For several years The Honeynet Project has operated a network of distributed honeypots. While operating a sensor network over multiple years, we’ve improved our ability to leverage orchestration to deploy in a variety of environments, manage the various sensors, and improve them over time.

## Challenges
An early problem was simply how to manage honeypots running the same sensor software but deployed in very different environments. Further, the sensors needed to be lightweight and require as few resources as possible (so that we could deploy as many as possible). Luckily this effort didn’t require very much net-new orchestration and started out by relying on what had already been developed for tpot. Putting it all together, Ansible has really served as the backbone for bringing up new systems, and making it very easy to customize the sensors and deploy changes. Better yet, the effort into orchestration efforts make the individual sensors semi-disposable; their data is valuable but the sensors themselves are disposable and easily replaced by spinning up more instances.

## Deployment evolution
Sensor orchestration began with tpot’s bash installer which was converted to an Ansible role. Since the initial conversion, tpot has migrated to its own Ansible installer and work is underway to convert the new tpot Ansible installer into roles. 

Initially sensors relied on elastic logstash for transmitting data, but this quickly proved antithetical to the design goal of requiring as few resources as possible. Logstash was soon replaced with filebeat which is not only lighter weight, but more sensible given the uniformity of the data collection and there being no requirement to process any data on the sensors themselves. Instead, the elastic cluster in which data is collected runs logstash and all log munging, mastication, and wrangling occurs there.

## Outstanding work
Work is continuing on the distributed honeypot network project including how to leverage an ever-growing, distributed repository of malware samples and to really leverage them in other Honeynet Project research efforts. Initial considerations include cloud object storage and serverless interactive query services (e.g. S3 and Athena). Additionally, there are better options for some of the functions currently performed by the sensors and replacing p0f and fatt wtth tools still under active development such as Zeek. Adding some queueing for logging rather than the current filebeat mechanism would better support the distributed nature of the entire platform as well as create an interface for future research efforts. Finally, making the entire distributed honeypot network more robust with better defenses and more encryption is a topic returned to often.

## Stay tuned
The distributed honeypot project provides Honeynet researchers a view into data for research and will surely fuel some future research and blogging/writing projects. There are also plans underway to release more of the tooling used in this project so don’t forget to visit The Honeynet Project website and github repositories.

## Acknowledgements
Special thanks to DigitalOcean without whose support this project would not have been possible.