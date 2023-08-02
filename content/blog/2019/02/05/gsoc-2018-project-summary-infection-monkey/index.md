---
title: "GSoC 2018 Project Summary: Infection Monkey"
authors: ["Daniel Haslinger"]
date: "2019-02-05"
categories: 
  - "gsoc"
tags: 
  - "2018"
  - "gsoc"
  - "gsoc2018"
  - "infection-monkey"
  - "project"
  - "student"
coverImage: "infectionmonkey.png"
---

### The Infection-Monkey team for GSoC 2018 wrote this post as a project summary of their GSoC 2018 experience

### Team:

**Student:** Vakaris Žilius

**Mentor:** Daniel Goldberg

### Introduction

During GSOC 2018, Vakaris worked with me on the Infection Monkey.

 

The Infection Monkey is an open source security tool for testing a data center's resiliency to perimeter breaches and internal server infection. The Monkey uses various methods to self propagate across a data center and reports success to a centralized Monkey Island server.

 

As part of the project, Vakaris implemented a new framework for web vulnerabilities and added multiple new exploit methods using this framework. This makes it far easier for other contributors to add new exploits and gives the Infection Monkey some serious power in older networks.

 

### Features coded during GSOC

- - A remote exploit for Struts2 jakarta multiparser RCE exploit ( CVE-2017-5638 ) [PR #179](https://github.com/guardicore/monkey/pull/179)
        

- - A remote exploit for Oracle WebLogic REST API (CVE-2017-10271) [PR #180](https://github.com/guardicore/monkey/pull/180)
        

- - And Remote code execution on HADOOP server with YARN and default settings [PR #182](https://github.com/guardicore/monkey/pull/182)
        

- - A new framework that all these exploits use to easily develop new web attacks [PR #159](https://github.com/guardicore/monkey/pull/159)
        

- - SSH key stealing, allowing the Monkey to propagate in networks that use SSH keys for authentication. [PR #138](https://github.com/guardicore/monkey/pull/138)
        

 

As part of this work, Vakaris identified and fixed dozens of small bugs spread across multiple features. From this work we identified issues we’d like to solve in the future like

- - It’s still really hard to add new exploits, as it requires adding code to multiple ancillary files like the report generation mechanism.
        

- - Python 2.7 is going to die and new useful libraries are Python 3 only, so we’ll need to migrate the code
        

### Challenges and learning experiences (Written by Vakaris)

I can’t say that any task was particularly more challenging than the rest, because my competence grew at the same pace as task difficulty did.

- - Small bugfix and ssh key stealing: Most challenging thing was the codebase. Python, NoSQL database and network communications were topics where I had none real-world experience.
        

- - Struts2: The most challenging thing there was setting up exploitable environment.
        

- - Web RCE exploit implementation framework: It was challenging to predict and prepare for all possible implementations of these types of exploit. A lot of refactoring and discussions about code happened until the final pull request was merged.
        

- - Weblogic: This vulnerability was harder to implement, because it was a blind exploit, meaning no feedback in case of success.
        

- - Hadoop: Setting up hadoop on windows was notably harder than any other vulnerable server I’ve done.
        

**What I learned:**

- - Solid introduction to python
        

- - Basics of network and web server debugging
        

- - Code quality
        

- - Improved my knowledge of git
        

- - A bit about web security
