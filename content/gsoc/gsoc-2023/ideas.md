---
title: "Google Summer of Code 2023 Project Ideas"
date: "2023-02-09"
url: "/gsoc/gsoc-2023/google-summer-of-code-2023-project-ideas"
---

### Getting Started

This page contains a list of potential project ideas that we are keen to develop during GSoC 2023. If you would like to apply as a GSoC student, please follow these two steps to get started:

1. Read through this page and identify the project ideas you find interesting. Play around with our tools!
2. Join us on Slack and talk to your potential mentors at [https://gsoc-slack.honeynet.org/](https://gsoc-slack.honeynet.org/)

If there are any questions, please don’t hesitate and get in touch! 🙂

### GSoC and The Honeynet Project

During the previous years of GSoC, the Honeynet Project's students have created a wide range of very successful open source security projects, many of which have gone on to become the industry standard open source tools in their respective fields.

We are also always interested in hearing any ideas for additional relevant computer security and honeynet-related R&D projects (although remember that to qualify for receiving GSoC funding from Google your project deliverables need to fit in to [GSoC's project timescales](//developers.google.com/open-source/gsoc/faq)!). If you have a suitable and interesting project, we will always try and find the right resources to mentor it and support you.

Please note - even if you aren't an [eligible GSoC participant](//developers.google.com/open-source/gsoc/faq), we are also always looking for general volunteers who are enthusiastic and interested in getting involved in honeynet R&D.

Each sponsored GSoC 2023 project will have one or more mentors available to provide a guaranteed contact point to students, plus one or more technical advisors to help applicants with the technical direction and delivery of the project (often the original author of a tool or its current maintainer, and usually someone recognised as an international expert in their particular field). Our Google Summer of Code organisational administrators will also be available to all sponsored GSoC students for general advice and logistical support. We'll also provide hosting for project infrastructure, if required.

For all questions about the Honeynet Project, the GSoC program or our projects, please contact us on **[gsoc-slack.honeynet.org](//gsoc-slack.honeynet.org/) (preferred)** or email us at [project@honeynet.org](mailto:project@honeynet.org).

**Application template**

If you are considering applying to participate with us in GSoC 2023 please find our [application template here]({{< ref "application.md" >}}). Use it when you are preparing your application on the official GSoC site and don't hesitate to ask your mentors for feedback before submitting!

* * *

# GSoC 2023 Project Ideas Overview

- [GSoC 2023 Project Ideas Overview](#gsoc-2023-project-ideas-overview)
  - [#1 - Hack on Mitmproxy!](#1---hack-on-mitmproxy)
  - [#2 - Honeyscanner: a vulnerability analysis tool for honeypots](#2---honeyscanner-a-vulnerability-analysis-tool-for-honeypots)
  - [#3 - Riotpot: improving the IoT/OT honeypot](#3---riotpot-improving-the-iotot-honeypot)
  - [#4 - HosTaGe: the swiss-army knife mobile honeypot](#4---hostage-the-swiss-army-knife-mobile-honeypot)
  - [#5 - WhisperPot: a medium interaction honeypot for SIP/VOIP attacks](#5---whisperpot-a-medium-interaction-honeypot-for-sipvoip-attacks)
  - [#6 - Add a summary of malware behavior to DRAKVUF Sandbox](#6---add-a-summary-of-malware-behavior-to-drakvuf-sandbox)
  - [#7 - Ochi – Honeypot Live Event Feed UI](#7---ochi--honeypot-live-event-feed-ui)
  - [#8 - IntelOwl: General improvements and new features](#8---intelowl-general-improvements-and-new-features)

* * *

## #1 - Hack on Mitmproxy!

**Mentor:** Maximilian Hils

**Project URL:** [https://mitmproxy.org](https://mitmproxy.org)

**Project type**: Improving an existing tool

**Project hours:** 350

mitmproxy is your swiss-army knife for debugging, testing, privacy measurements, and penetration testing. It can be used to intercept, inspect, modify and replay web traffic such as HTTP/1, HTTP/2, HTTP/3, WebSockets, DNS, UDP, or any other SSL/TLS-protected protocols. You can prettify and decode a variety of message types ranging from HTML to Protobuf, intercept specific messages on-the-fly, modify them before they reach their destination, and replay them to a client or server later on.

mitmproxy is a large project with a huge number of interesting areas to explore, down from low-level protocol work up to UX improvements. If you are motivated and know what you’re interested in, why not get in touch with us and map out a custom GSoC project? Below are some ideas with a rough project size estimations – an enterprising student should be able to complete one large or 3 or more small tasks in a 350h GSoC project.

Potential Tasks: https://github.com/mitmproxy/mitmproxy/issues/5850

* * *

## #2 - Honeyscanner: a vulnerability analysis tool for honeypots

**Mentor:** Manolis

**Project type**: New tool

**Project hours:** 350

Several honeypots have been developed over the last decade. A common problem with many of them is that they have been implemented as part of ephemeral academic research or open-source projects that did not gain the expected community support. As a result, many honeypots may have potential undiscovered vulnerabilities and security issues.

With this project, honeyscanner, we propose an open-source vulnerability scanner for honeypots. The tool will use a penetration testing strategy, with different levels of attacks, starting from reconnaissance (i.e., identifying the honeypot nature of a system) to more advanced ones. The first level will include exploiting already known vulnerabilities of software libraries used from the honeypot. The second level will utilize more advanced techniques like fuzzing.

* * *

## #3 - Riotpot: improving the IoT/OT honeypot

**Mentor:** Manolis

**Project type**: Improving existing tool

**Project hours:** 350

RIoTPot is a modern open-source hybrid interaction OT/IoT honeypot written in Go. The honeypot has been presented in both academic conferences as well as in Black Hat Europe 2021. The goal of this project is to enhance RIoTPot’s capabilities by adding new protocol emulation support in the form of device profiles, work on existing problems and improve the project’s documentation. In addition, the project can explore how the honeypot is handling fingerprinting (e.g., via Nmap) and how it can trick such systems and hide its honeypot nature.

For further reading have a look at the GIT repo: https://github.com/aau-network-security/riotpot -research paper: https://www.researchgate.net/publication/353794760\_RIoTPot\_a\_modular\_hybrid-interaction\_IoTOT\_honeypot\

Last year’s GSoC: https://ricyaben.github.io/blog/projects/gsoc_2022_riotpot/

* * *

## #4 - HosTaGe: the swiss-army knife mobile honeypot

**Mentor:** Emmanouil Vasilomanolakis, Shreyas Srinivasa

**Project type**: Improving existing tool

**Project URL**: https://github.com/aau-network-security/HosTaGe

**Project hours:** 175

HosTaGe (Honeypot To Go) is a lightweight, low-interaction, portable, and generic honeypot for mobile devices that aims on the detection of malicious, wireless network environments. As most malware propagate over the network via specific protocols, a low-interaction honeypot located at a mobile device can check wireless networks for actively propagating malware. We envision such honeypots running on all kinds of mobile devices, e.g., smartphones and tablets, to provide a quick assessment on the potential security state of a network. HosTaGe is developed in android and contains wrappers in python, c and c++ languages. We aim to improve HosTaGe by developing new features that enhance its deception abilities, fix bugs, and improve the UI.

Further reading: HosTaGe PlayStore Link: https://play.google.com/store/apps/details?id=dk.aau.netsec.hostage

* * *

## #5 - WhisperPot: a medium interaction honeypot for SIP/VOIP attacks

**Mentor:** Emmanouil Vasilomanolakis, Shreyas Srinivasa

**Project type**: New tool

**Project hours:** 350

This project aims to create Whisperpot: a honeypot that can simulate the SIP and VoIP protocols. The aim of this project is to develop a new honeypot system that can essentially simulate phones and VoIP devices and log incoming traffic for further analysis. The honeypot will be developed as a medium or high interaction honeypot where most the simulation includes the protocol emulation and device profile. We welcome ideas and suggestions from the students. This also entails the students get an opportunity to be involved in the project right from its idea phase. The student will be primarily involved in the development of the honeypot.

Some of the tasks are:

Coming up with a potential architecture for the honeypot system

Implementation of the honeypot, including protocols SIP, VoIP and optionally other proprietary device protocols

Evaluation and testing of the honeypot system

* * *

## #6 - Add a summary of malware behavior to DRAKVUF Sandbox

**Mentor:** CERT.pl team

**Project type**: Improving existing tool

**Project URL:** https://github.com/CERT-Polska/drakvuf-sandbox

**Project hours:** 175

DRAKVUF Sandbox is an open source automated black-box malware analysis system using virtual machine introspection (VMI) with DRAKVUF (https://drakvuf.com) engine under the hood.

As DRAKVUF Sandbox monitors behavior of malware samples it collects a lot of detailed data, like API calls, syscalls, network traffic, etc., however it lacks a summary of the most important characteristics of the analyzed sample, for example if any anti-analysis tricks are used, files are downloaded, code injected into another process, persistence methods and more.

The goal of this project is to add an overview of the most important behaviors of the malware to the results view based on the information already present in the logs collected by the sandbox, so an analyst can quickly see main properties of the sample. See https://github.com/CERT-Polska/drakvuf-sandbox/issues/70.

Other existing sandboxing solutions can serve as an inspiration for the design of the feature. Examples – TODO

The scope of this project includes design of the interface that will be used to present the overview, selection of heuristics to extract interesting features from logs (possibly by embedding the CAPA tool: https://github.com/fireeye/capa and implementation of the new view in DRAKVUF Sandbox.

* * *

## #7 - Ochi – Honeypot Live Event Feed UI

**Mentor:** Lukas Rist

**Project type**: Improving existing tool

**Project URL:** https://github.com/glaslos/ochi

**Project hours:** 350

Ochi is a web interface for live Honeypot events to correlate, filter and annotate. In this project we would like to add the ability to filter the events using a version of the Wireshark query syntax as a DSL. Queries should be persistent and the backend should calculate metrics how often a query is matched.

Furthermore the backend should support perma-links to events so they can be shared.

Primary skills required are HTML/CSS/JavaScript. Secondary would be Golang but this can also be covered by the mentor of the project.

* * *

## #8 - IntelOwl: General improvements and new features

**Mentor:** Matteo Lodi

**Project type**: Improving existing tool

**Project URL:** [https://github.com/intelowlproject/intelowl](https://github.com/intelowlproject/intelowl)

**Project hours:** 350

**Skills required**: Cyber Threat Intelligence and OSINT knowledge, Docker, Python (Django), JavaScript (React.js), Object-Oriented Programming

All the projects proposed by the [IntelOwl Project](https://github.com/intelowlproject/IntelOwl) Organization will be run under The Honeynet Project Umbrella during the GSoC 2023.

Please check the [dedicated repo](https://github.com/intelowlproject/gsoc) and the [ideas list](https://github.com/intelowlproject/gsoc/tree/main/2023) for further information.
