---
title: "Google Summer of Code 2022 Project Ideas"
date: "2022-02-09"
url: "/gsoc/gsoc-2022/google-summer-of-code-2022-project-ideas"
---

### Getting Started

This page contains a list of potential project ideas that we are keen to develop during GSoC 2022. If you would like to apply as a GSoC student, please follow these two steps to get started:

1. Read through this page and identify the project ideas you find interesting. Play around with our tools!
2. Join us on Slack and talk to your potential mentors at [https://gsoc-slack.honeynet.org/](https://gsoc-slack.honeynet.org/)

If there are any questions, please don’t hesitate and get in touch! 🙂

### GSoC and The Honeynet Project

During the previous years of GSoC, the Honeynet Project's students have created a wide range of very successful open source security projects, many of which have gone on to become the industry standard open source tools in their respective fields.

We are also always interested in hearing any ideas for additional relevant computer security and honeynet-related R&D projects (although remember that to qualify for receiving GSoC funding from Google your project deliverables need to fit in to [GSoC's project timescales](//developers.google.com/open-source/gsoc/faq)!). If you have a suitable and interesting project, we will always try and find the right resources to mentor it and support you.

Please note - even if you aren't an [eligible GSoC participant](//developers.google.com/open-source/gsoc/faq), we are also always looking for general volunteers who are enthusiastic and interested in getting involved in honeynet R&D.

Each sponsored GSoC 2022 project will have one or more mentors available to provide a guaranteed contact point to students, plus one or more technical advisors to help applicants with the technical direction and delivery of the project (often the original author of a tool or its current maintainer, and usually someone recognised as an international expert in their particular field). Our Google Summer of Code organisational administrators will also be available to all sponsored GSoC students for general advice and logistical support. We'll also provide hosting for project infrastructure, if required.

For all questions about the Honeynet Project, the GSoC program or our projects, please contact us on **[gsoc-slack.honeynet.org](//gsoc-slack.honeynet.org/) (preferred)** or email us at [project@honeynet.org](mailto:project@honeynet.org).

**Application template**

If you are considering applying to participate with us in GSoC 2022 please find our [application template here](https://www.honeynet.org/gsoc/gsoc-2022/gsoc-2022-application-template). Use it when you are preparing your application on the official GSoC site and don't hesitate to ask your mentors for feedback before submitting!

* * *

# GSoC 2022 Project Ideas Overview

- [GSoC 2022 Project Ideas Overview](#gsoc-2022-project-ideas-overview)
  - [#1 - Hack on Mitmproxy!](#1---hack-on-mitmproxy)
  - [#2 - IoT linux sandbox](#2---iot-linux-sandbox)
  - [#3 - Securing the Open Source Supply Chain](#3---securing-the-open-source-supply-chain)
  - [#4 - Finding hijacked Software](#4---finding-hijacked-software)
  - [#5 - Qiling Improvements](#5---qiling-improvements)
  - [#6 - Quark-Engine: strengthen Quark with both the depth and the breadth of the technology](#6---quark-engine-strengthen-quark-with-both-the-depth-and-the-breadth-of-the-technology)
  - [#7 - RIoTPoT: the IoT/OT honeypot](#7---riotpot-the-iotot-honeypot)
  - [#8 - HosTaGe: the swiss-army knife mobile honeypot](#8---hostage-the-swiss-army-knife-mobile-honeypot)
  - [#9 - WhisperPot: a medium interaction honeypot for SIP/VOIP attacks](#9---whisperpot-a-medium-interaction-honeypot-for-sipvoip-attacks)
  - [#10 - HTTP requests evaluation in TANNER](#10---http-requests-evaluation-in-tanner)
  - [#11 - Give a face to the GreedyBear!](#11---give-a-face-to-the-greedybear)
  - [#12 - Give power to the GreedyBear!](#12---give-power-to-the-greedybear)
  - [#13 - IntelOwl: Go client (go-intelowl)](#13---intelowl-go-client-go-intelowl)
  - [#14 - IntelOwl: General improvements and new features](#14---intelowl-general-improvements-and-new-features)
  - [#15 - Add a summary of malware behavior to DRAKVUF Sandbox](#15---add-a-summary-of-malware-behavior-to-drakvuf-sandbox)
  - [#16 - Implement a log browser in DRAKVUF Sandbox web interface](#16---implement-a-log-browser-in-drakvuf-sandbox-web-interface)
  - [#17 - Add graph representing malware execution to DRAKVUF Sandbox](#17---add-graph-representing-malware-execution-to-drakvuf-sandbox)
  - [#18 - TANNER Web Improvement](#18---tanner-web-improvement)

* * *

## #1 - Hack on Mitmproxy!

**Mentor:** Maximilian Hils

**Project URL:** [https://mitmproxy.org](https://mitmproxy.org)

**Project type**: Improving an existing tool

**Project hours:** 350

mitmproxy is your swiss-army knife for debugging, testing, privacy measurements, and penetration testing. It can be used to intercept, inspect, modify and replay web traffic such as HTTP/1, HTTP/2, WebSockets, or any other SSL/TLS-protected protocols. You can prettify and decode a variety of message types ranging from HTML to Protobuf, intercept specific messages on-the-fly, modify them before they reach their destination, and replay them to a client or server later on.

mitmproxy is a large project with a huge number of interesting areas to explore, down from low-level protocol work up to UX improvements. If you are motivated and know what you’re interested in, why not get in touch with us and map out a custom GSoC project? Below are some ideas with a rough project size estimations – an enterprising student should be able to complete one large or 3 or more small tasks in a 350h GSoC project.

Potential Tasks: [https://github.com/mitmproxy/mitmproxy/issues/5048](https://github.com/mitmproxy/mitmproxy/issues/5048)

* * *

## #2 - IoT linux sandbox

**Mentor:** Hugo Glez

**Project type**: New tool

**Project hours:** 175

With the increase of malware IoT dissemination in multiple platforms, a sandbox for IoT common platforms its a "nice to have" tool for analysts. This project should include other open source components such as QEMU. The first stage and the main goal of this project is to instrument a linux system running on MIPS and ARM platforms, that report the findings to a central console. It is possible to re-use cuckoo sandbox architecture, or work directly over it to support this new platforms. Also documentation is extremly important to allow other members to expand or comment on the project.

A lot of integration and documentation is needed alongside programming.

* * *

## #3 - Securing the Open Source Supply Chain

**Mentor:** Felix Leder

**Project type**: New tool

**Project hours:** 350

Open source code is used everywhere from free software to commercial products in top 500 companies. This creates interesting dependencies and risks. More and more attackers try to "hack" their way into companies and projects by modifying open source libraries. In this project, we want You to help securing the dependencies = open source supply chain.

* * *

## #4 - Finding hijacked Software

**Mentor:** Felix Leder

**Project type**: New tool

**Project hours:** 350

With examples like SolarWinds and MeDoc, it becomes apparent that attackers like to infiltrate organization by releasing backdoors through the software supply chain. This can be a hacked build server or a modified open source library. It is impossible for the average user to identify and find such backdoors in legitimate programs.  
This project is about smart ways to analyze compiled software and spot unwanted modifications. We want the student to come up with cool ideas. It can involve static (binary) analysis or dynamic analysis during execution, like network traffic.

* * *

## #5 - Qiling Improvements

**Mentor:** Simone Berni, Ziqiao Kong, Chenxu Wu, Zheng Yu, Eli Cohen Nehemia

**Project type**: Improving existing tool

**Project URL:** [https://github.com/qilingframework/qiling](https://github.com/qilingframework/qiling)

**Project hours:** 175-350 based on contributor proposal and complexity

**Skills required:** Python, Binary Analysis

Qiling is an advanced binary emulation framework, that aims to support a variety of operating system, file formats and architecture, written entirely in Python.  
Malware have been emulated and studied thanks to Qiling, and at the moment it supports even the analysis of rootkit thanks to the merge with the Demigod project. Morever, we put a lot of effort to integrate Qiling with other tool, like the plugin with IdaPro, that allows to use the power of Qiling emulation while using Ida.  
Fuzzing have been one of the community focus point in the latest period, and at the moment Qiling can be used together with AFL++ to fuzz over the emulation layered offered by Qiling.

We propose the following ideas, but we will consider even other proposals:

\- Improve project robustness and resilience of the project: test coverage, unit test, documentation for both users and developers, improve CI pipeline, add linters  
\- Bridge with other reverse engineering tools ( r2, ghidra)  
\- Allow emulation of a xv6 kernel  
\- MacOS/Windows/Android Improvements  
\- Allow emulation of network connections for malware analysis  
\- Emulate Pong, on the first game ever made, on Qiling DOS mode!

A more thorough description is present here: [https://github.com/qilingframework/qiling/discussions/1083](https://github.com/qilingframework/qiling/discussions/1083)

* * *

## #6 - Quark-Engine: strengthen Quark with both the depth and the breadth of the technology

**Mentor:** Shaun Dang, Yu-Shiang Dang, Sheng-Feng Lu

**Project type**: Improving existing tool

**Project URL:** [https://github.com/quark-engine/quark-engine](https://github.com/quark-engine/quark-engine)

**Project hours:** 350

Quark is one of the most popular analysis engines for hunting threat intelligence inside the Android APK files. With ideas decoded from criminal law, Quark has its unique angles for malware analysis. Since it is rule-based, you can use the ones built-in or customize as needed. We developed a Dalvik bytecode loader that has tainted analysis inside but also defeats the obfuscation techniques used against reverse engineering. And surprisingly, the loader matches perfectly the design of our malware scoring system.

Last year, our primary goals were to make Quark everywhere among the open-source projects, rewrite the core library of Quark, and also improve the performance of rule generation. During 2021 GSoC, our two contributors, Sheng-Feng Lu and Yu-Shiang Dang helped us reach the milestones.  
Here is the link for more detail: [https://quark-engine.github.io](https://quark-engine.github.io)

This year, our primary goal is to strengthen Quark-Engine with both the depth and the breadth of the technology. To strengthen the depth of the technology, we believe that understanding the fundamentals and building everything from the ground up is good for tool developers’ souls. As for strengthening the breadth of the technology, innovation through what we have adds possibilities to the Quark community. Please read the following description for more details.

\- Depth: To clearly understand how the Android system works and make Quark analyze APK more comprehensively, our goal is to emulate a Dalvik Virtual Machine (DVM). Any implementation of the emulation (e.g., APK parsing, Android API calling, etc) is welcome to contribute.

\- Breadth: Innovate based on the current technology of Quark. For example, make YARA Rule available for Quark-Engine. This helps to make Quark a more widely used tool and the most important of all, the Yara Rule integration provides new possibilities for malware hunting.

* * *

## #7 - RIoTPoT: the IoT/OT honeypot

**Mentor:** Emmanouil Vasilomanolakis, Shreyas Srinivasa

**Project type**: Improving existing tool

**Project URL:** [https://github.com/aau-network-security/riotpot](https://github.com/aau-network-security/riotpot)

**Project hours:** 350

RIoTPot is a modern open-source medium interaction OT/IoT honeypot written in Go. The goal of this project is to enhance RIoTPoT’s capabilities by adding new protocol emulation support in the form of device profiles. In addition, the project can explore how the honeypot is handling fingerprinting (e.g., via Nmap) and how it can trick such systems and hide its honeypot nature.

The student can decide to follow one or more of the following options: i) OT device profile creation (e.g., devices using DNP3, Fieldbus, Profibus), ii) IoT device profile creation (e.g., devices using AMQP, CoAP, M2M), iii) OT-based dynamic response system, iv) Attack signature export, v) Anti-fingerprinting response generation

* * *

## #8 - HosTaGe: the swiss-army knife mobile honeypot

**Mentor: ** Emmanouil Vasilomanolakis, Shreyas Srinivasa

**Project type**: Improving existing tool

**Project URL:** [https://github.com/aau-network-security/HosTaGe](https://github.com/aau-network-security/HosTaGe)

**Project hours:** 175

HosTaGe (presented at the Blackhat Europe Arsenal 2020) is a lightweight, low-interaction, portable, and all around honeypot for mobile devices that aims on the detection of malicious, wireless network environments. As most malware propagate over the network via specific protocols, a low-interaction honeypot located at a mobile device can check wireless networks for actively propagating malware. We envision such honeypots running on all kinds of mobile devices, e.g., smartphones and tablets, to provide a quick assessment on the potential security state of a network.

HosTaGe is developed for Android and contains wrappers in Python, C and C++ languages. We aim to improve HosTaGe by developing new features that enhance its capabilities. The student along with the mentors will discuss potential new features and improvements. These include: i) new protocol simulation, ii) improvement of existing protocol simulation, iii) new system (so-called profiles) simulation, iv) improvement on the stealthiness of the honeypot, v) Kotlin migration.

* * *

## #9 - WhisperPot: a medium interaction honeypot for SIP/VOIP attacks

**Mentor: ** Emmanouil Vasilomanolakis, Shreyas Srinivasa

**Project type**: New tool

**Project hours:** 350

The COVID19 pandemic significantly increased the amount of online calls and virtual meetings via various SIP/VoIP systems. We propose WhisperPot, a honeypot that can simulate the SIP and VoIP protocols. The aim of this project is to develop a new honeypot system that can essentially simulate phones and VoIP devices and log incoming traffic for further analysis. The honeypot will be developed as a medium-interaction honeypot where most the simulation includes the protocol emulation and device profile. WhisperPot is to be implemented in Python, support SIP and be able to emulate different types of devices (via a profile setting component).

* * *

## #10 - HTTP requests evaluation in TANNER

**Mentor:** Evgeniia Tokarchuk

**Project type**: Improving existing tool

**Project URL:** [https://github.com/mushorg/tanner](https://github.com/mushorg/tanner)

**Project hours:** 350

**Skill required**:  
\- Python 3  
\- Experience in Machine Learning (any)  
\- Optional: experience with (and/or) pytorch/scikit-learn/xgboost/other ML lib

TANNER is a remote data analysis and classification service to evaluate HTTP requests. However, the evaluation and classification are built upon handcrafted heuristics. That leads to the adaptation and generalization problem while classifying for attacks. With the advances of machine learning algorithms nowadays and the availability of various datasets, it is potentially promising to build a more reliable classification system. Moreover, after years of running TANNER, there are multiple available TANNER logs, which can be used for training.  
This project will include several steps:  
\- Analyzing current error rates for classifications (setting the baseline)  
\- Data preparation/cleaning  
\- Designing and implementing the prototype of the ML-based classification system  
\- Incorporating a new system into the TANNER (only in case of successful outcome)

* * *

## #11 - Give a face to the GreedyBear!

**Mentor:** Matteo Lodi, Daniele Rosetti, Shubham Pandey

**Project type**: Improving existing tool

**Project URL:** [https://github.com/honeynet/GreedyBear](https://github.com/honeynet/GreedyBear)

**Project hours:** 175

The recently born project GreedyBear needs a face! The contributor will provide a Graphical User Interface to this application, based on ReactJS and the updated interface of the upcoming IntelOwl 4 version ([https://github.com/intelowlproject/IntelOwl/pull/856](https://github.com/intelowlproject/IntelOwl/pull/856))

Starting point: [https://github.com/honeynet/GreedyBear/issues/11](https://github.com/honeynet/GreedyBear/issues/11)

(Please note: if the potential contributor would like to invest more time in GreedyBear, he can propose a 350 hours project composed of “Give a face to the GreedyBear!” and “Give power to the GreedyBear!” requirements together)

* * *

## #12 - Give power to the GreedyBear!

**Mentor:** Matteo Lodi, Daniele Rosetti, Shubham Pandey

**Project type**: Improving existing tool

**Project URL:** [](https://github.com/honeynet/GreedyBear)[https://github.com/honeynet/GreedyBear](https://github.com/honeynet/GreedyBear)

**Project hours:** 175

**Skills required**: Web development, Docker, Python (Django)

The recently born project GreedyBear needs new features! The contributor will work to solve the existing issues in the project regarding:

- creation of an authenticated API enrichment service
- integrate the platform with other Honeypots
- create tests and documentation

We strongly encourage proposals for other general improvements for this project.

(Please note: if the potential contributor would like to invest more time in GreedyBear, he can propose a 350 hours project composed of “Give a face to the GreedyBear!” and “Give power to the GreedyBear!” requirements together)

* * *

## #13 - IntelOwl: Go client (go-intelowl)

**Mentor:** Eshaan Bansal, Shubham Pandey

**Project type**: Improving existing tool

**Project URL:** [https://github.com/intelowlproject/go-intelowl](https://github.com/intelowlproject/go-intelowl)

**Project hours:** 175

**Skills required**: good programming skills in Go, unit-testing, familiarity with IntelOwl’s API  

IntelOwl ([https://github.com/intelowlproject/IntelOwl](https://github.com/intelowlproject/IntelOwl)) is an open-source OSINT tool written in Django that exposes a RESTful API. PyIntelOwl ([https://github.com/intelowlproject/pyintelowl](https://github.com/intelowlproject/pyintelowl)) is an SDK/library in Python that allows developers to easily interface with IntelOwl’s API, write automation scripts and integrate IntelOwl with their own tools and services.

We wish to build a similar SDK/package in Go programming language as it has become a famous choice nowadays for building security tools and services. The aim of go-intelowl is to provide an easy-to-use interface to IntelOwl’s API that would allow integration of IntelOwl into many more projects.

The project is to be written from scratch (See [https://github.com/intelowlproject/go-intelowl/issues/16](https://github.com/intelowlproject/go-intelowl/issues/16) issue) and your proposal should include writing the library code for all API endpoints along with unit-tests that work with and without mock data, CI integrations (uni tests and linting) and package publish pipelines.

(Note: Since this is a new project with no existing codebase, familiarity with IntelOwl’s codebase (for e.g, previous contributions to IntelOwl, pyintelowl, IntelOwl-ng repositories) will be taken into consideration)

* * *

## #14 - IntelOwl: General improvements and new features

**Mentor:** Eshaan Bansal, Matteo Lodi

**Project type**: Improving existing tool

**Project URL:** [https://github.com/intelowlproject/intelowl](https://github.com/intelowlproject/intelowl)

**Project hours:** 350

**Skills required**: Cyber Threat Intelligence and OSINT knowledge, Docker, Python (Django), JavaScript (React.js), Object-Oriented Programming

IntelOwl has been in development for 2 years now. Over the last 2 GSoCs, the students proposed working on adding new features and refactoring legacy code. The project summaries can be found [here](https://github.com/intelowlproject/IntelOwl#the-honeynet-project)

We use the GSoC period to explore new ideas, add new features, introduce breaking changes and essentially serve it all to the users at the end of the GSoC program with a new major release of IntelOwl. This year is no different with the scheduled v4.0.0 release. We want the candidate to pick some issues from the v4.0.0 milestone ([https://github.com/intelowlproject/IntelOwl/milestone/2](https://github.com/intelowlproject/IntelOwl/milestone/2)), preferably the following ones:

- Playbooks (automated scripts) - [https://github.com/intelowlproject/IntelOwl/issues/628](https://github.com/intelowlproject/IntelOwl/issues/628)
- Investigations (combination of playbooks) - [https://github.com/intelowlproject/IntelOwl/issues/680](https://github.com/intelowlproject/IntelOwl/issues/680)
- Allow managing plugin keys and configurations from the GUI - [https://github.com/intelowlproject/IntelOwl/issues/433](https://github.com/intelowlproject/IntelOwl/issues/433)
- Bulk analysis - [https://github.com/intelowlproject/IntelOwl/issues/732](https://github.com/intelowlproject/IntelOwl/issues/732)
- Option to run only “free” analyzers - [https://github.com/intelowlproject/IntelOwl/issues/733](https://github.com/intelowlproject/IntelOwl/issues/733)

Given this list of priority issues, the ideal candidate for this project is someone who is strongly familiar with IntelOwl and has knowledge of cyber threat intelligence analysis and automation.

* * *

## #15 - Add a summary of malware behavior to DRAKVUF Sandbox

**Mentor:** CERT.pl team

**Project type**: Improving existing tool

**Project URL:** [https://github.com/CERT-Polska/drakvuf-sandbox](https://github.com/CERT-Polska/drakvuf-sandbox)

**Project hours:** 175

DRAKVUF Sandbox is an open source automated black-box malware analysis system using virtual machine introspection (VMI) with DRAKVUF [(https://drakvuf.com](https://drakvuf.com)) engine under the hood.

As DRAKVUF Sandbox monitors behavior of malware samples it collects a lot of detailed data, like API calls, syscalls, network traffic, etc., however it lacks a summary of the most important characteristics of the analyzed sample, for example if any anti-analysis tricks are used, files are downloaded, code injected into another process, persistence methods and more.

The goal of this project is to add an overview of the most important behaviors of the malware to the results view based on the information already present in the logs collected by the sandbox, so an analyst can quickly see main properties of the sample. See [https://github.com/CERT-Polska/drakvuf-sandbox/issues/70](https://github.com/CERT-Polska/drakvuf-sandbox/issues/70).

Other existing sandboxing solutions can serve as an inspiration for the design of the feature.  
Examples:  
[https://cuckoo.cert.ee/analysis/2745362/summary](https://cuckoo.cert.ee/analysis/2745362/summary)  
[https://www.vmray.com/analyses/guloader-delivering-azorult/report/overview.html](https://www.vmray.com/analyses/guloader-delivering-azorult/report/overview.html)  
[https://www.joesandbox.com/analysis/347016/0/html](https://www.joesandbox.com/analysis/347016/0/html)

The scope of this project includes design of the interface that will be used to present the overview, selection of heuristics to extract interesting features from logs (possibly by embedding the CAPA tool: [https://github.com/fireeye/capa](https://github.com/fireeye/capa)) and implementation of the new view in DRAKVUF Sandbox.

* * *

## #16 - Implement a log browser in DRAKVUF Sandbox web interface

**Mentor:** CERT.pl team

**Project type**: Improving existing tool

**Project URL:** [https://github.com/CERT-Polska/drakvuf-sandbox](https://github.com/CERT-Polska/drakvuf-sandbox/issues/70)

**Project hours:** 175

DRAKVUF Sandbox is an open source automated black-box malware analysis system using virtual machine introspection (VMI) with DRAKVUF ([https://drakvuf.com](https://drakvuf.com)) engine under the hood.

Most of the analysis results generated by DRAKVUF Sandbox are available as plain NDJSON files, which can be significant in size. The goal of this project is to implement an interactive log browser that would allow analysts to easily browse and search the results, including filtering (by process, DRAKVUF plugin, text pattern, etc.). The log browser should also automatically collapse sequences of similar log lines to reduce excessive output that is generated when certain APIs are called in a loop for example.

The project includes creating a design of the search user interface for individual analyses, proposal of heuristics for collapsing similar log lines and implementing the feature in DRAKVUF Sandbox.

* * *

## #17 - Add graph representing malware execution to DRAKVUF Sandbox

**Mentor:** CERT.pl team

**Project type**: Improving existing tool

**Project URL:** [https://github.com/CERT-Polska/drakvuf-sandbox](https://github.com/CERT-Polska/drakvuf-sandbox/)

**Project hours:** 175

DRAKVUF Sandbox is an open source automated black-box malware analysis system using virtual machine introspection (VMI) with DRAKVUF ([https://drakvuf.com](https://drakvuf.com)) engine under the hood.

As DRAKVUF Sandbox monitors behavior of malware samples it collects a lot of detailed data, like API calls and syscalls that were used. Currently the data is available as a big log file, which makes it difficult to get a high-level understanding of the malware activities.

The goal of this project is to provide an analyst with a graph that would illustrate all important activities of the sample, for example process creation or code injection, based on the logs available.

Graph visualisations offered by existing solutions can serve as an inspiration for designing the feature. Examples: [https://www.joesandbox.com/analysis/347016/0/html#behaviorGraph](https://www.joesandbox.com/analysis/347016/0/html#behaviorGraph) [https://www.vmray.com/analyses/303ad8c115d9/report/behavior\_grouped.html](https://www.vmray.com/analyses/303ad8c115d9/report/behavior_grouped.html) [https://procdot.com/](https://procdot.com/)

The scope of the project includes proposing a design of the visualization for a limited set of activities (at least process creation, termination, code injection), evaluation of open source JavaScript visualization libraries for graph layout and rendering (D3.js, Dagre, ELK, etc.) and implementing the feature in DRAKVUF Sandbox.

* * *

## #18 - TANNER Web Improvement

**Mentor:** Mehtab Zafar

**Project type**: Improving existing tool

**Project URL:** [https://github.com/mushorg/tanner](https://github.com/mushorg/tanner)

**Project hours:** 175

TANNER has support for both an API and a WEB application. API is responsible for performing search operations and web application shows the data inconvenient way. Even though the current system allows to search and filter based on session attributes, there is a lack of visual representation for aggregated metrics. Right now TANNER returns the session information in a table view, however, designing API requests and improving visualization might give the user a more appealing tool to work with the collected data. So it would be a great addition if we improve the frontal view of that data. Also, add support for graphical presentation such as pie/line/bar charts visualizing all the data stored in the database.
