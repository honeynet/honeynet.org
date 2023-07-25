---
title: "Google Summer of Code 2018 Project Ideas"
date: "2018-08-28"
url: "/gsoc/gsoc-2028/google-summer-of-code-2018-project-ideas"
---

![GSoC Logo](images/GSoC-logo-horizontal-800.png)

#### Getting Started

This page contains a list of potential project ideas that we are keen to develop during [GSoC 2018](https://summerofcode.withgoogle.com/). If you would like to apply as a GSoC student, please follow these three steps to get started:

1. Read through this page and identify the project ideas you find interesting. Play around with our tools!
2. Check out our [application tips](https://honeynet.org/node/1308) page.
3. Join us on Slack and talk to your potential mentors:  
    [  
      
    ](https://gsoc-slack.honeynet.org/)

If there are any questions, please don’t hesitate and get in touch! 🙂

#### GSoC and The Honeynet Project

During the previous years of GSoC, the Honeynet Project's students have created a wide range of very successful open source security projects, many of which have gone on to become the industry standard open source tools in their respective fields. Examples for these include:

- [Cuckoo Sandbox](https://www.cuckoosandbox.org/) (2010+)
- [Mitmproxy](https://mitmproxy.org/) (2012+)
- [Thug Client Honeypot](https://buffer.github.io/thug/) (2012+)
- [DroidBox Android Sandbox](https://github.com/pjlantz/droidbox) (2011+)
- [ConPot ICS/SCADA Honeypot](http://conpot.org/) (2013+)
- [Glastopf Web Application Honeypot](http://glastopf.org/) (2009+)
- [Dionaea](http://dionaea.carnivore.it/) (2009+)
- [Holmes Processing](https://www.holmesprocessing.com/) (2017+)

If you can't find something to immediately interest you, please take a look at [GSoC 2009](https://www.honeynet.org/gsoc2009/ideas), [GSoC 2010](https://www.honeynet.org/gsoc2010/ideas), [GSoC 2011](https://www.honeynet.org/gsoc2011/ideas), [GSoC 2012](https://www.honeynet.org/gsoc2012/ideas), [GSoC 2013](https://www.honeynet.org/gsoc2013/ideas), [GSoC 2014](https://www.honeynet.org/gsoc2014/ideas), [GSoC 2015](https://www.honeynet.org/gsoc2015/ideas), [GSoC 2016](https://www.honeynet.org/gsoc2016/ideas) and [GSoC 2017](https://www.honeynet.org/gsoc2017/ideas) project ideas pages for other inspiration.

We are also always interested in hearing any ideas for additional relevant computer security and honeynet-related R&D projects (although remember that to qualify for receiving GSoC funding from Google your project deliverables need to fit in to [GSoC's 3-month project timescales](https://developers.google.com/open-source/gsoc/faq)!). If you have a suitable and interesting project, we will always try and find the right resources to mentor it and support you.

Please note - even if you aren't an [eligible GSoC student](https://developers.google.com/open-source/gsoc/faq), we are also always looking for general volunteers who are enthusiastic and interested in getting involved in honeynet R&D.

Each sponsored GSoC 2018 project will have one or more mentors available to provide a guaranteed contact point to students, plus one or more technical advisors to help applicants with the technical direction and delivery of the project (often the original author of a tool or its current maintainer, and usually someone recognised as an international expert in their particular field). Our Google Summer of Code organisational administrators will also be available to all sponsored GSoC students for general advice and logistical support. We'll also provide hosting for project infrastructure, if required.

For all questions about the Honeynet Project, the GSoC program or our projects, please contact us on **[gsoc-slack.honeynet.org](https://gsoc-slack.honeynet.org/) (preferred)** or email us at [project@honeynet.org](mailto:project@honeynet.org).

# GSoC 2018 Project Ideas Overview

**New Projects**

- [Honeypot Detection Tool](https://www.honeynet.org/gsoc2018/ideas#honeypot-detection): Create an open-source honeypot detection tool that detects whether a system is a honeypot.
- [Trusted Execution Environment-Based Dynamic Analysis on ARM](https://www.honeynet.org/gsoc2018/ideas#tea): Construct a TEE-based dynamic behavior monitor.

**Mitmproxy - HTTPS interception proxy**

- [New Sans I/O Proxy Core](https://www.honeynet.org/gsoc2018/ideas#mitmproxy-sansio): Teach mitmproxy new protocols, sans-io style.
- [Pick-Your-Tasks Project](https://www.honeynet.org/gsoc2018/ideas#mitmproxy-core): New features for mitmproxy's Python 3 core.

**Honeytrap - Advanced Honeypot framework**

- [IoT QEMU Director](https://www.honeynet.org/gsoc2018/ideas#honeytrap-iot): Implement a new director that will allow running Qemu images as target.
- [Core Improvements](https://www.honeynet.org/gsoc2018/ideas#honeytrap-core): Implement new services such as an elasticsearch simulator service.

**DRAKVUF - Black-Box Binary Analysis System**

- [Hardening Against Memory Probes](https://www.honeynet.org/gsoc2018/ideas#drakvuf-hardening): Implement cloaking zero-page for shadow pages.
- [Injector Enhancements](https://www.honeynet.org/gsoc2018/ideas#drakvuf-injector): Implement process cloaking techniques using VMI.
- [Support for Dynamic Malware Analysis on ARM](https://www.honeynet.org/gsoc2018/ideas#drakvuf-arm): Add ARM support to the dynamic malware analysis framework.

**Holmes Processing - Cyber threat intelligence at scale**

- [Automated Malware Relationship Mining](https://www.honeynet.org/gsoc2018/ideas#holmes-relationships): Automatically learn the relationship of malware samples at scale using deep learning techniques.
- [Expand Holmes-Storage v2](https://www.honeynet.org/gsoc2018/ideas#holmes-storage): Improve Holmes-Storage v2 by adding more storage solutions and finishing a general API that can be used via HTML and AMQP.

**Android-Related Projects**

- [DroidBot/DroidBox web service](https://www.honeynet.org/gsoc2018/ideas#android-webservice): Implement a web frontend for DroidBot and DroidBox.
- [DroidBot with AI](https://www.honeynet.org/gsoc2018/ideas#android-ai): Improve DroidBot coverage using machine learning / deep learning techniques.
- [Android Instrumented Sandbox](https://www.honeynet.org/gsoc2018/ideas#android-sandbox): Run malware analyses on real physical Android devices.

**Capstone/Unicorn/Keystone Projects**

- [Capstone Disassembler](https://www.honeynet.org/gsoc2018/ideas#capstone): Fix bugs & update LLVM.
- [Unicorn Emulator](https://www.honeynet.org/gsoc2018/ideas#unicorn): Fix bugs & update QEMU.
- [Keystone Assembler](https://www.honeynet.org/gsoc2018/ideas#keystone): Fix bugs & update LLVM.

**Independent Projects**

- [LibVMI](https://www.honeynet.org/gsoc2018/ideas#libvmi): Add support for the Bareflank research hypervisor to LibVMI.
- [Conpot](https://www.honeynet.org/gsoc2018/ideas#conpot): Extend Conpot protocol stacks, intercommunication and internal features.
- [Cuckoo Sandbox](https://www.honeynet.org/gsoc2018/ideas#cuckoo): Improve the Longterm Analysis Functionality in Cuckoo Sandbox.
- [Thug](https://www.honeynet.org/gsoc2018/ideas#thug): Port Thug to Python 3 and replace PyV8 with a modern alternative.
- [SNARE/TANNER](https://www.honeynet.org/gsoc2018/ideas#snare): Improve SNARE/TANNER's architecture, logging system, and session storage and analysis.
- [D2 Environment Builder](https://www.honeynet.org/gsoc2018/ideas#d2): Add new security-related or data analytic open source  
    components to an existing automated deployment environment.
- [Infection Monkey](https://www.honeynet.org/gsoc2018/ideas#infection-monkey): Add new exploiters to detect and attack targets.

* * *

# New Projects

## #1 - Honeypot Detection Tool

Mentor Marcin SzymankiewiczBackup Mentor Adel KarmiSkills required

- Python (strong)
- Linux (good)
- Common network protocols (good)

Project type New toolProject goal Create a honeypot detection toolDescription Many researchers fail deploying honeypots that are easily detectable. There are trivial mistakes people can make when deploying a honeypot like leaving the default settings or templates. On the other hand there are some non-direct indicators of a honeypot including but not limited to running both Windows and Linux services on the same box or having two different ssh servers listening on the same IP. The goal of this project would be to create a simple and open source honeypot detection tool that would scan an IP looking for any traces of a honeypot and create a report with findings and their severity. Using this tool a researcher can scan their system before putting it online or in production and based on the report perform the necessary tuning.  

## #2 - Trusted Execution Environment-Based Dynamic Analysis on ARM

Mentor Peng XuBackup Mentor Yue ChenSkills required C, operating systems, dynamic analysisProject type New toolProject goal Construct a TEE-based dynamic behavior monitorDescription

Hardware virtualization based monitoring, like libvmi and DRAKVUF, is a good approach to provide the out-of-the-box dynamic code analysis and offer a stealthy guest instrumentation. However, the overhead of this type of monitoring is extreme high, mostly over several times. Alternatively, nearly all of the modern ARM and Intel architectures provide trusted execution environment (TEE) to offer isolated storage and execution environment, entitled as “normal world” and “secure world”. The purpose of this project is to constructure a monito(like eBPF in the latest version linux kernel) in the “secure world” which can collect sensitive data from the rich operating system( locating in the “normal world”) and create a stealthy monitor since program in “normal world” cannot access “secure world” directly. In our project we choose the trustzone on ARM (op-tee) as our TEE basement.

\[0\] [http://www.brendangregg.com/perf.html#eBPF](http://www.brendangregg.com/perf.html#eBPF)  
  
\[1\] [https://github.com/OP-TEE](https://github.com/OP-TEE)

* * *

# Projects for Mitmproxy

![mitmproxy logo](images/logo-brand-inverted.png)

Mitmproxy is an interactive TLS-capable man-in-the-middle proxy. It can be used to intercept, inspect, modify and replay HTTP, HTTP/2, HTTPS, WebSockets, and raw TCP traffic. Think of it as a mix of WireShark and the Chrome developer tools - you can hook up any device or program and see how it communicates on the network. Mitmproxy is used by software developers, penetration testers, privacy advocates and researchers to fix bugs, find vulnerabilities, uncover privacy violations, conduct empirical research, and more.

**Getting started for GSoC:** [https://github.com/mitmproxy/mitmproxy/issues/2812](https://github.com/mitmproxy/mitmproxy/issues/2812)   
**Project page:** [https://mitmproxy.org/](https://mitmproxy.org/)   
**Code repository:** [https://github.com/mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)

## #3 - Mitmproxy: New Sans I/O Proxy Core

Mentor Maximilian HilsBackup Mentor Aldo CortesiSkills required

- Python 3 (strong)
- Networking Fundamentals

Project type Improve existing toolProject goal Spend the summer rewriting mitmproxy’s core proxy functionality!Description

A major feature on mitmproxy’s roadmap is the replacement of our proxy core with an implementation that separates I/O and protocol logic (“sans I/O”). As you can guess this is a major undertaking, but we’re determined to tackle it for a whole bunch of reasons. There are a couple of places where we would be happy to have help here:

- We're interested in trialling the sans-I/O core with non-web protocols. There are a huge number of protocols that make use of TLS and could usefully be intercepted. Common protocols that are not overly complicated - SMTP, POP, and IMAP spring to mind - might find a home within the mitmproxy project itself. A stretch goal here might be SSH interception, which will require a somewhat lower-level approach. You could also explore some more exotic protocols like RDP - these might use the core but remain external to mitmproxy. The project here would be to extend the set of protocols we implement, and solidify the sans-I/O APIs to ensure that they're general-purpose and fit for use.
- Students up for a challenge may want to work on the sans-I/O TLS core directly, and help solidify the HTTP, HTTP/2, and WebSockets implementations that will power a future version of mitmproxy. Writing a TLS or HTTP implementation that is used by thousands of users is an exciting and amazing challenge. We’d love to have a student with us on that quest, but be warned it’s a very steep and stony path that requires very strong software engineering skills to be successful.

Further Resources:

- [https://github.com/mitmproxy/mitmproxy/issues/1775](https://github.com/mitmproxy/mitmproxy/issues/1775)
- [https://sans-io.readthedocs.io/](https://sans-io.readthedocs.io/)
- [https://www.youtube.com/watch?v=7cC3\_jGwl\_U](https://www.youtube.com/watch?v=7cC3_jGwl_U)
- [https://github.com/mitmproxy/mitmproxy/tree/sans-io](https://github.com/mitmproxy/mitmproxy/tree/sans-io) (`python3 -m mitmproxy.proxy2.server`)
- `mitmproxy.proxy` on master, `mitmproxy.proxy2` on the sans-io branch.
- [https://github.com/citronneur/rdpy](https://github.com/citronneur/rdpy)
- [https://github.com/SySS-Research/Seth](https://github.com/SySS-Research/Seth)
- [https://github.com/ronf/asyncssh](https://github.com/ronf/asyncssh)
- [https://github.com/paramiko/paramiko](https://github.com/paramiko/paramiko)

See [here](https://www.honeynet.org/gsoc2018/ideas#mitmproxy) for details on how to get started.

## #4 - Mitmproxy: Pick-Your-Tasks Project

Mentor Thomas KriechbaumerBackup Mentor Maximilian HilsSkills required

- Python 3 (strong)
- HTTP (familiar)

Project type Improve existing toolProject goal Spend the summer improving mitmproxy and work on addons and the core proxy!Description

![mitmproxy screenshot](images/mitmproxy-small.png)

Mitmproxy is a large project with a huge number of interesting areas to explore. If you are motivated and know what you're interested in, why not get in touch with us and map out a custom GSoC project? Below are some ideas with a rough project size estimations - an enterprising student should be able to complete one large or 3 or more small projects during the GSoC period.

- **\[large\]** Ecosystem germination: Mitmproxy's addon mechanism has undergone a complete revolution in the last year. We can now write powerful, isolated addons that reach into almost any facet of mitmproxy's operation. We're now ready to take the next step, and work out how to foster an addon ecosystem outside of the core. This involves planning and implementing methods for addon distribution, considering the thorny problem of how to manage addons with third-party dependencies, setting up an addon registry, and solidifying our APIs to make the third-party addon experience even better. This is an opportunity to have a huge impact on the future of mitmproxy as a project.
- **\[large\]** Mitmproxy urgently needs a new built-in primitive: sessions. Sessions will hold information related to a given capture session, keep a spool of captures on-disk, and allow users to annotate flows and save hot configuration without affecting their global config files. This will solve some large outstanding issues for mitmproxy and pave the way for us to take the next step in our interactive tooling. \[[2175](https://github.com/mitmproxy/mitmproxy/issues/2175)\]
- **\[large\]** Mitmproxy's current serialization format has served us well, but has a number of shortcomings. It's hard to maintain, has impedance mismatches with the structure of our data, and is hard to use from other languages. Your task will be to grow a clean, lean serialization format based on Google protobufs - at first as an exporter addon, and then to migrate it into mitmproxy's core. As part of this, you will also map out the protobuf-generated language bindings for the capture format that will make mitmproxy's data accessible from other programming universes. \[[2660](https://github.com/mitmproxy/mitmproxy/issues/2660)\]
- **\[medium/large\]** We’d love to improve mitmproxy’s performance. It’s a well-known fact that you can’t improve what you can’t measure, and at the moment mitmproxy is flying blind. Your mission, should you choose to accept it, would be to set up a benchmarking suite for mitmproxy to measure our key indicators, work out how to run this reliably in the cloud, and create a performance dashboard that will be linked to from our website. As a next step, you may choose to fix some of the performance issues you discovered.
- **\[medium\]** Many mitmproxy users want to use mitmproxy to just see all traffic of their current device without configuring individual applications, but that requires a complicated iptables configuration or undocumented scripts on Windows. You can make tremendous improvements to mitmproxy onboarding experience here! \[[1261](https://github.com/mitmproxy/mitmproxy/issues/1261)\]
- **\[medium\]** Extend mitmproxy's console UI to support WebSockets and raw TCP mode. These protocols are well-supported and mature in the core, but we haven't found the time to expose them to users in the UI. We need YOUR help!
- **\[small/medium\]** Improved Contentviews \[[1662](https://github.com/mitmproxy/mitmproxy/issues/1662)\]
- **\[small/medium\]** Importers and Exporters for related file formats, such as HAR. \[[1477](https://github.com/mitmproxy/mitmproxy/issues/1477)\]
- **\[small\]** Support for upstream SOCKS proxies \[[211](https://github.com/mitmproxy/mitmproxy/issues/211)\]
- **\[small\]** "Map Remote Editor": Other proxies have a feature which maps one URL to another, e.g. one can map [https://example.com/foo.js](https://example.com/foo.js) to a local file that is served to the client instead. It is easy to write a mitmproxy script that does this, but we want this to be a built-in feature! Fun fact: This task was initially proposed by a GSoC student in \[[1454](https://github.com/mitmproxy/mitmproxy/issues/1454)\]!

See [here](https://www.honeynet.org/gsoc2018/ideas#mitmproxy) for details on how to get started. We encourage you to also think beyond what is listed above - what would \*you\* do to improve mitmproxy?

* * *

# Projects for Honeytrap

Honeytrap is an extensible and opensource system for running, monitoring and managing honeypots.

**Getting started for GSoC:** [https://github.com/honeytrap/honeytrap/issues/](https://github.com/honeytrap/honeytrap/issues/)   
**Project page:** [http://docs.honeytrap.io/docs/home/](http://docs.honeytrap.io/docs/home/)   
**Code repository:** [https://github.com/honeytrap/honeytrap/](https://github.com/honeytrap/honeytrap/)

## #5 - Honeytrap: IoT QEMU Director

Mentor Remco VerhoefBackup Mentor (to be done)Skills required

- Golang (strong)
- QEMU (familiar)

Project type Improve existing toolProject goal Spend the summer implementing Qemu support for HoneytrapDescription

Honeytrap is an advanced honeypot framework where listeners, directors, services and events are extensible. Existing honeypots can be used, but new simulated services can be implemented also.

Implement a new director that will allow running Qemu images as target. Each attacking IP will run get its own Qemu process, preserving all information and data. Eventually existing services can be extended to facilitate low- to high interaction, where depending on the first commands we’ll pick another qemu image.

Honeytrap has been built modular, so you’ll only need to work on the director itself, the services and listener already facilitate running connections to other targets.

Currently we support proxying traffic to remote hosts (eg a real host, another honeypot) , experimental firejail containers or individual per-attacker lxc containers. Protocols will have a -proxy variant, with protocol knowledge that will take care of sending events. Honeytrap has an advanced event mechanism, filtering and sending events to Slack, Elasticsearch, Kafka, File and Console.

See [here](https://www.honeynet.org/gsoc2018/ideas#honeytrap) for details on how to get started.

## #6 - Honeytrap: Core Improvements

Mentor Remco VerhoefBackup Mentor (to be done)Skills required

- Golang (strong)
- Protocol knowledge (familiar)

Project type Improve existing toolProject goal Spend the summer implementing new services for HoneytrapDescription

Honeytrap is an advanced honeypot framework where listeners, directors, services and events are extensible. Existing honeypots can be used, but new simulated services can be implemented also.

Implement new services (like an elasticsearch simulator service), fix issues, improve the docs or other great ideas you’ll have.

Honeytrap has been built modular, so you’ll only need to work on the director, listener, service or channel itself.

See [here](https://www.honeynet.org/gsoc2018/ideas#honeytrap) for details on how to get started.

* * *

# Projects for DRAKVUF

DRAKVUF is a virtualization based agentless black-box binary analysis system. DRAKVUF allows for in-depth execution tracing of arbitrary binaries (including operating systems), all without having to install any special software within the virtual machine used for analysis.

## #7 - DRAKVUF: Hardening Against Memory Probes

Mentor Tamas LengyelBackup Mentor Balint Varga-PerkeSkills required CProject type Improve existing toolProject goal DRAKVUF hardening against memory probesDescription

Currently DRAKVUF uses a memory cloaking technique in which shadow memory pages are direct mapped to a dummy zero-filled pages at the end of the guest physical memory. While this technique protects against discovery that simply reads from memory, a knowledgeable attacker can probe these pages by writing to them a canary and observing all other pages where the canary appears. To avoid this information leak, shadow pages where a canary gets written needs to get their own cloaking zero-page (similar to deduplicating a page when performing copy-on-write).

- Ticket: [https://github.com/tklengyel/drakvuf/issues/309](https://github.com/tklengyel/drakvuf/issues/309)
- More background: [https://www.youtube.com/watch?v=86EvJK2Ef\_U](https://www.youtube.com/watch?v=86EvJK2Ef_U), [https://blog.xenproject.org/2016/04/13/stealthy-monitoring-with-xen-altp2m/](https://blog.xenproject.org/2016/04/13/stealthy-monitoring-with-xen-altp2m/)

## #8 - DRAKVUF: Injector Enhancements

Mentor Tamas LengyelBackup Mentor Balint Varga-PerkeSkills required CProject type Improve existing toolProject goal DRAKVUF injector enhancementsDescription

The current process injection mechanism used by DRAKVUF sets up the stack for creating a call to ntdll.dll!CreateProcessA. Thus, the process created by this mechanism will reflect the executable name as found in the disk, which may result in information leak malware could use to detect DRAKVUF. There are process cloaking techniques (usually used by malware) to hide the process in the shell of another: process hollowing and process doppelgänging. Implementing these techniques using VMI will improve the resiliency of DRAKVUF against potential malware trying to detect the environment.

- Ticket: [https://github.com/tklengyel/drakvuf/issues/332](https://github.com/tklengyel/drakvuf/issues/332), [https://github.com/tklengyel/drakvuf/issues/290](https://github.com/tklengyel/drakvuf/issues/290)
- More background: [https://www.blackhat.com/docs/eu-17/materials/eu-17-Liberman-Lost-In-Transaction-Process-Doppelganging.pdf](https://www.blackhat.com/docs/eu-17/materials/eu-17-Liberman-Lost-In-Transaction-Process-Doppelganging.pdf), [http://www.autosectools.com/process-hollowing.pdf](http://www.autosectools.com/process-hollowing.pdf)

## #9 - DRAKVUF: Support for Dynamic Malware Analysis on ARM

Mentor Sergej ProskurinBackup Mentor Tamas LengyelSkills required C, C++Project type Improve existing toolProject goal Add ARM support to the dynamic malware analysis framework DRAKVUFDescription

Recent efforts in the development of a foundation for the dynamic malware analysis framework DRAKVUF on the ARM architecture have extended the Xen hypervisor to establish the means for stealthy guest instrumentation. More precisely, one of the implementation efforts of Google Summer of Code in 2016 resulted in the Xen altp2m subsystem for ARM \[0,1\] that allows to maintain multiple second level address translation tables, each representing a specific view on the guest's physical memory. As to close the circle, the GSoC 2018 student is expected to tackle the problem from the opposite side and extend DRAKVUF itself as to provide ARM support. This project will close the circle in providing the foundation for DRAKVUF on ARM and thus establish a solid ground for dynamic malware analysis for mobile devices.

\[0\] [https://www.holmesprocessing.com/gsoc/#portfolioModal1](https://www.holmesprocessing.com/gsoc/#portfolioModal1)  
  
\[1\] [https://summerofcode.withgoogle.com/archive/2016/projects/6408159388237824/](https://summerofcode.withgoogle.com/archive/2016/projects/6408159388237824/)

* * *

# Projects for Holmes Processing

Holmes Processing was born out of the need to rapidly process and analyze large volumes data in the computer security community. At its core, Holmes Processing is a catalyst for extracting useful information and generate meaningful intelligence. Furthermore, the robust distributed architecture allows the system to scale while also providing the flexibility needed to evolve.

## #10 - Holmes Processing: Automated Malware Relationship Mining

Mentor Huang XiaoBackup Mentor Bojan KolosnjajiSkills required Python, Numpy, Tensorflow or other deep learning framework, JavaScriptProject type Improve existing toolProject goal Automatically learn the relationship of malware samples at scale using deep learning techniquesDescription

The Holmes Project has recently acquired a large dataset of labeled malware artifacts, which can be used for deep learning based malware relationship mining. This labeled dataset of over 20k samples should be a big help for students attempting to do Malware Relationship Detection. Besides, as a result of the previous GSoC’17, we also have an efficient data model for the malware relationships. New potential GSoC students can immediately start with the machine learning part without concerns for optimal data modeling and distributed storage. As a follow-up project, students are expected to come up with decent learning model to detect malware relationship and create better visualisation frontend. In order to visualize the relationship properly, the model needs to learn to aggregate relationships from different malware analysis services.

Ticket: [https://github.com/HolmesProcessing/gsoc\_relationship/issues/22](https://github.com/HolmesProcessing/gsoc_relationship/issues/22)

## #11 - Holmes Processing: Expand Holmes-Storage v2

Mentor Christian von PentzBackup Mentor Ryan HarrisSkills required Very solid Scala with akka, knowledge about various database and storage solutionsProject type Improve existing toolDescription

Improve Holmes-Storage v2 by adding more storage solutions and finishing a general API that can be used via HTML and AMQP.

At the end of the project Holmes-Storage should be an akka based, scalable application that supports data storage via MongoDB, Cassandra, and Elastic as well as object storage via S3, Minio, and the local file system (testing).

The second part of this should be the implantation of a general API that can be used to interact with both selected storage solutions. A user should be able to connect to this API via a simple RESTful HTTP web server based on akka http as well a dedicated AMQP queue with optional callback queue for replies if necessary.

More Details: [https://github.com/HolmesProcessing](https://github.com/HolmesProcessing)  

* * *

# Android-Related Projects

## #12 - DroidBot/DroidBox web service

Mentor Hanno LemoineBackup Mentor Yuanchun LiSkills required

- Python (strong)
- HTML/JavaScript
- Docker

Project type Improve existing toolProject goal Implement a web frontend for DroidBot and DroidBoxDescription

DroidBot \[1\] and DroidBox \[2\] are dynamic analysis tools for Android apps. However, installing and configuring such tools are difficult for analyzers. So we already setup a docker container for using DroidBox \[3\]. But we want to make these tools easier to use by having a web service as frontend and a small backend that runs analysis in DroidBox and save the results. Some wanted features include:

1. The ability to upload an app for analysis, monitor the analysis process and see the results. Similar to \[4\] and \[5\].
2. The ability to interact with the app during analysis. Using VNC \[6\] should be fine.
3. A UI to add and change scripts for droidBot scripting language e.g. \[7\]
4. The web service should be easy to deploy (better to be deployable with Docker/Compose).
5. A database for storing and searching previous analysis results .

\[1\] [https://github.com/honeynet/droidbot](https://github.com/honeynet/droidbot)  
  
\[2\] [https://github.com/pjlantz/droidbox](https://github.com/pjlantz/droidbox)  
  
\[3\] [https://hub.docker.com/r/honeynet/droidbox/](https://hub.docker.com/r/honeynet/droidbox/)  
  
\[4\] [https://www.hybrid-analysis.com/](https://www.hybrid-analysis.com/)  
  
\[5\] [http://sanddroid.xjtu.edu.cn/](http://sanddroid.xjtu.edu.cn/)  
  
\[6\] [https://github.com/oNaiPs/droidVncServer](https://github.com/oNaiPs/droidVncServer)  
  
\[7\] [https://github.com/honeynet/droidbot/tree/master/script\_samples](https://github.com/honeynet/droidbot/tree/master/script_samples)  

## #13 - DroidBot with AI

Mentor Yuanchun LiBackup Mentor Hanno LemoineSkills required

- Python (strong)
- Deep learning

Project type Improve existing toolProject goal Improve DroidBot coverage using machine learning / deep learning techniquesDescription

DroidBot \[1\] is a dynamic analysis tool that tries to trigger sensitive behaviors of Android apps by sending random test input. Similar to many other test input generation tools, the key challenge of DroidBot is to improve test coverage (i.e. letting the generated test input execute more code, thus trigger more sensitive behaviors). However, the random test strategy only have limited performance. We want to make use of the technical advances in AI to help DroidBot generate more reasonable and meaningful test input. For example, using AI to detect similar UI views in order to avoid redundant input, and using AI to understand the dependency between UI views in order to generate targeted input. We have a lot of training data (DroidBot results for thousands of Android apps) or you can use open dataset like Rico.

\[1\] [https://github.com/honeynet/droidbot](https://github.com/honeynet/droidbot)  
  
\[2\] [http://interactionmining.org/rico](http://interactionmining.org/rico)  
  
\[3\] [https://arxiv.org/pdf/1709.00928.pdf](https://arxiv.org/pdf/1709.00928.pdf)  
  
\[4\] [http://drops.dagstuhl.de/opus/volltexte/2016/6695/pdf/dagrep\_v006\_i004\_p161\_s16172.pdf](http://drops.dagstuhl.de/opus/volltexte/2016/6695/pdf/dagrep_v006_i004_p161_s16172.pdf)  

## #19 - Android Instrumented Sandbox in a Real Device

Mentor Hugo GonzálezBackup Mentor TBASkills required

- Python
- JavaScript
- Bash
- Android Basics

Project type New toolProject goal Integrate/expand existing tools to offer an instrumented sandbox for Android analysis on real devicesDescription

There are great tools like droidbot and cuckoo droid to  
perform Android malware analysis. We want to offer a new tool to  
perform these analyses on real devices. We need to automatize as much  
as possible to reset a real device to a clean state. Restore a backup  
of the device, so it looks like a normal device. This should include  
instrumentation software as Xposed and/or Frida. Then the process of  
installing the malware and run it, and run other apps also. Capture  
the network traffic. Finally recover all data from the device and  
process it to offer a comprehensive report about the malware. Then  
start again with a new sample.   
  
Because the variety of the devices, it is not intended to cover all  
devices, but common ones to keep all the process working.

**References:**  
  
[https://github.com/idanr1986/cuckoo-droid](https://github.com/idanr1986/cuckoo-droid)  
  
[https://github.com/honeynet/droidbot](https://github.com/honeynet/droidbot)  
  
[https://www.frida.re/docs/android/](https://www.frida.re/docs/android/)  
  
[http://repo.xposed.info/module/de.robv.android.xposed.installer](http://repo.xposed.info/module/de.robv.android.xposed.installer)  

* * *

# Capstone/Unicorn/Keystone Projects

## #22 - Capstone Disassembler

Mentor Nguyen Anh QuynhBackup Mentor tbdSkills required

- C (strong)
- Linux (good)

Project type Improve existing toolDescription Capstone disassembler is a multi-arch, multi-platform disassembler framework, which is widely used in the security community & beyond (see [https://www.capstone-engine.org](https://www.capstone-engine.org/)).  
The main core of Capstone is forked from LLVM disassemblers ([https://www.llvm.org](https://www.llvm.org/)), and we need to sync with LLVM frequently to keep updated. This project is to help to maintain the existing code (fixing bugs, adding some small missing features), and update Capstone, so it supports the latest instructions added to LLVM recently.  

## #23 - Unicorn Emulator

Mentor Nguyen Anh QuynhBackup Mentor tbdSkills required

- C (strong)
- Linux (good)

Project type Improve existing toolDescription Unicorn emulator is a multi-arch, multi-platform emulator framework, which is widely used in the security community & beyond (see[https://www.unicorn-engine.org/](https://www.unicorn-engine.org/)).  
The main core of Unicorn is forked from QEMU emulator ([https://www.qemu.org](https://www.qemu.org/)), and we need to sync with QEMU frequently to keep updated. This project is to help to maintain the existing code (fixing bugs, adding some small missing features), and update Unicorn, so it supports the latest instructions added to QEMU recently.  

## #24 - Keystone Assembler

Mentor Nguyen Anh QuynhBackup Mentor tbdSkills required

- C (strong)
- Linux (good)

Project type Improve existing toolDescription Keystone assembler is a multi-arch, multi-platform assembler framework, which is widely used in the security community & beyond (see[https://www.keystone-engine.org/](https://www.keystone-engine.org/)).  
The main core of Keystone is forked from LLVM disassemblers ([https://www.llvm.org](https://www.llvm.org/)), and we need to sync with LLVM frequently to keep updated. This project is to help to maintain the existing code (fixing bugs, adding some small missing features), and update Keystone, so it supports the latest instructions added to LLVM recently.  

* * *

# Independent Projects

## #14 - LibVMI extensions: Bareflank Hypervisor support

Mentor Tamas LengyelBackup Mentor Dr. Rian QuinnSkills required C, C++, PythonProject type Improve existing toolProject goal Add support for the Bareflank research hypervisor to LibVMIDescription

LibVMI is a C library with Python bindings that makes it easy to monitor the low-level details of a running virtual machine by viewing its memory, trapping on hardware events, and accessing the vCPU registers. The Bareflank Hypervisor is an open source, lightweight hypervisor, that provides the scaffolding needed to rapidly prototype new hypervisors. Adding support to LibVMI to interact with Bareflank will provide the ability for malware researchers to rapidly prototype and test virtualization based ideas against even the most elusive malwares.

Further Resources

- [http://libvmi.com](http://libvmi.com/)
- [https://github.com/Bareflank/hypervisor](https://github.com/Bareflank/hypervisor)

## #15 - CONPOT: Protocols Wave #2

Mentor Daniel HaslingerBackup Mentor Johnny VestergaardSkills required Python; A deeper understanding of how protocols workProject type Improve existing toolProject goal Extend Conpot protocol stacks, intercommunication and internal featuresDescription

The last GSoC for Conpot turned out to be great: We fixed crucial flaws in our BACnet and MODBUS implementation and added ENIP (EtherNet/Industrial Protocol). This time, we’re trying to extend the industrial honeypot with common protocols (FTP, telnet, ..), a virtual (“journaled/versioned”) file system and a new internal interface that let’s protocols interact more deeply with each other.

Wave 2 of Conpot Protocols aims to make the industrial honeypot more versatile and - leveraging new core enhancements like a virtual file system, collects new data such as uploaded malware in order to enable further research on automated attacks against critical infrastructure.

\[0\] [https://github.com/mushorg/conpot](https://github.com/mushorg/conpot)  
  
\[1\] [http://conpot.org/](http://conpot.org/)

## #16 - Cuckoo Sandbox: Longterm Analysis Improvements

Mentor Ricardo van ZutphenBackup Mentor Jurriaan BremerSkills required Python 2 (strong), Linux (good), Common network protocols (basic)Project type Improve existing toolProject goal Improving the Longterm Analysis functionality in Cuckoo SandboxDescription

Cuckoo Sandbox Longterm Analysis (Cuckoo LTA) was ported from legacy to the latest version of Cuckoo Sandbox a few months ago.  
The aim of longterm support is to be able to monitor specific malware samples/families over a longer period of time. E.g: running a sample for five days from 09:00 to 17:00 to simulate an office environment.

To increase the usefulness of LTA, additional features should be added and challenges need to be solved. During this project, one or more new features will be worked on. Of course, we would also love suggestions on new features using the data collected (network, API calls, etc) by Cuckoo LTA.

During a normal Cuckoo analysis, a large amount of data can be collected in a matter of minutes. Because longterm analyses can run for multiple days, this can result in impractical amounts of data. To solve this, less data should/will be collected longterm analyses. The modules that process and report the collected  
data should still be able to use this data to generate realtime and useful reports.  
At the time of writing this, Cuckoo LTA is being worked on, meaning it is likely more challenges and features to build will arise.

Tasks for this project would among others things be: designing/writing new (OO) classes, optimizing database schemas, thinking about how specific types of data can best be stored, testing the implementation (unit testing).

More Details: [https://cuckoosandbox.org](https://cuckoosandbox.org/), [https://github.com/cuckoosandbox/cuckoo](https://github.com/cuckoosandbox/cuckoo)

## #17 - Thug: Python 3 Port and PyV8 Replacement

Mentor Angelo Dell’AeraBackup Mentor (to be done)Skills required Python 2 and 3, Thug internals, JavaScript (Google V8 engine)Project type Improve existing toolProject goal Thug long-term improvementsDescription

The number of client-side attacks has grown significantly in the past few years shifting focus on poorly protected vulnerable clients. Just as the most known honeypot technologies enable research into server-side attacks, honeyclients allow the study of client-side attacks.

A complement to honeypots, a honeyclient is a tool designed to mimic the behavior of a user-driven network client application, such as a web browser, and be exploited by an attacker's content.

Thug is a Python low-interaction honeyclient aimed at mimicking the behavior of a web browser in order to detect and emulate malicious contents.

The project aims at

1. porting Thug to Python 3
2. replacing PyV8, the currently used V8 Python wrapper which is no longer maintained by its author, with a new one i.e. v8py.

**References:**  
  
[https://github.com/buffer/thug](https://github.com/buffer/thug)  
  
[https://github.com/flier/pyv8](https://github.com/flier/pyv8)  
  
[https://github.com/tbodt/v8py](https://github.com/tbodt/v8py)

## #18 - SNARE/TANNER

Mentor (to be done)Backup Mentor Evgeniia TokarchukSkills required Python 3Project type Improve existing toolProject goal Spend summer improving TANNER/SNAREDescription

The project contains work both on SNARE \[1\] and TANNER \[2\] sides.  
Since a lot of work has been done during last two GSoC on TANNER side, in this year we suggest focusing on the SNARE side.

- Migrate to latest aiohttp version. We are using deprecated low-level server on the SNARE side. In order to use latest aiohttp version, we need to rewrite SNARE server using the new web server.
- Improve SNARE architecture. Right now all the code is located in a single file, which make it hard to read and understand the code. Also it is hard to maintain such a code.
- Add logging system on the SNARE side. If the SNARE is running with default TANNER, SNARE user can not get any information. It can be improved by using separate logging system for SNARE.
- Write tests/documentation for the SNARE.
- Improve storing and analyzing sessions in TANNER. The current analyzing process makes simple suggestions about the peer status (bot/attacker/user). But we can extract more from the collected data.

**References:**  
  
[https://github.com/mushorg/snare](https://github.com/mushorg/snare)  
  
[https://github.com/mushorg/tanner](https://github.com/mushorg/tanner)

## #20 - D2 Environment Builder

Mentor David DittrichBackup Mentor TBDSkills required Linux (Debian, Ubuntu) system administration (strong), Ansible (familiar), Python (strong), Bash (strong)Project type Improve existing toolProject goal Add new security-related or data analytic open source  
components to an existing automated deployment environment.Description

A Department of Homeland Security sponsored project at the  
University of Washington \[1\] produced a set of open source Ansible  
playbooks and software \[2\] usable for constructing a small-scale  
distributed system composed of multiple Linux virtual machines  
(including development of a software system “Tupelo” that re-implements  
a previous Honeynet Project tool “Manuka”). This proposed project will  
extend a fork known as “D2” \[3\] that supports deploying systems on  
Digital Ocean supporting the following features: Semi-automated  
provisioning and deployment of Digital Ocean droplets and DNS records  
using Hashicorp “terraform"; Support for SSH host key management  
allowing StrictHostKeyChecking to be left enabled, while avoiding manual  
host key validation or insertion/deletion: A Trident trust group  
management and communication portal behind an NGINX reverse proxy  
secured by TLS; A Jenkins build server behind an NGINX reverse proxy  
secured by TLS, with Jenkins CLI secured with SSH; Support for  
Letsencrypt SSL/TLS certificate generation, backup & restoration,  
renewal-hooks for deploying certificates to non-privileged services, and  
scheduled certificate renewal maintenance; Support for SPF, DKIM, and  
DMARC in Postfix SMTP email; Centralized rsyslog logging secured by TLS;  
AMQP (RabbitMQ) message bus for remote procedure call, log distribution,  
and simple text chat, all secured by TLS. Potential new features include  
supporting other cloud providers (Google Compute Engine, Amazon Web  
Services, Azure, etc.), playbooks for installing threat intelligence  
tools (Collective Intelligence Framework, MISP), playbooks for  
installing open source log monitoring tools (Mozilla Defense Platform),  
playbooks for installing host forensic tools (Google Rapid Response,  
Tupelo).

**References:**  
  
\[1\] [https://staff.washington.edu/dittrich/home/dims.html](https://staff.washington.edu/dittrich/home/dims.html)  
  
\[2\] [https://github.com/uw-dims?type=source](https://github.com/uw-dims?type=source)  
  
\[3\] [https://davedittrich.readthedocs.io/projects/ansible-dims-playbooks/en/latest/](https://davedittrich.readthedocs.io/projects/ansible-dims-playbooks/en/latest/)

## #21 - Infection Monkey

![infection monkey logo](images/Infection-Monkey-Logo-1-300x288.png)

The Infection Monkey is an open source Breach and Attack Simulation (BAS) tool that assesses the resiliency of networks to post-breach attacks and lateral movement. Using the Infection Monkey, organizations can consistently check their network security by simulating a repeatable attacker.

To see more, visit [https://www.github.com/guardicore/monkey](https://www.github.com/guardicore/monkey).Mentor Daniel GoldbergBackup Mentor Ofri ZivSkills required Python, basic familiarity with web securityProject type Improve existing toolProject goal Add a set of logical vulnerabilities exploitersDescription

The Infection Monkey relies on a mix of password brute force attacks and some potentially wormable vulnerabilities. We’d like to extend this capability to cover recent logical long lived vulnerabilities such as the Oracle weblogic and Struts2 Java framework vulnerabilities, so the Monkey can test more systems. A key requirement is the stability of the network services, so any attack cannot risk disabling the target service.

Adding exploiters consists of adding a scanning module and exploitation module, to recognise and attack the target.

**Tickets:**  
  
[https://github.com/guardicore/monkey/issues/105](https://github.com/guardicore/monkey/issues/105)  
  
[https://github.com/guardicore/monkey/issues/106](https://github.com/guardicore/monkey/issues/106)  

- [Twitter](https://twitter.com/share?url=https%3A%2F%2Fwww.honeynet.org%2Fnode%2F1368&text=Google%20Summer%20of%20Code%202018%20Project%20Ideas)
- [Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.honeynet.org%2Fgsoc2018%2Fideas&t=Google+Summer+of+Code+2018+Project+Ideas)
- [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.honeynet.org%2Fgsoc2018%2Fideas&title=Google+Summer+of+Code+2018+Project+Ideas&summary=%0D%0A++.screenshot+%7B%0D%0A++++++max-width%3A+90%25%3B%0D%0A++++++margin%3A+0.5em+auto%3B%0D%0A++++++display%3A+block%3B%0D%0A++++++object-fit%3A+fill%3B%0D%0A++%7D%0D%0A++dl+%7B%0D%0A++++++margin-left%3A+0%3B%0D%0A++%7D%0D%0A++dd%2C+dt+%7B%0D%0A++++++display%3A+inline%3B%0D%0A++%7D%0D%0A++dd%3Aafter+%7B%0D%0A++++++display%3A+block%3B%0D%0A++++++content%3A+%22%22%3B%0D%0A++%7D%0D%0A++dt+%7B%0D%0A++++++font-weight%3A+bold%3B%0D%0A++%7D%0D%0A++dd+%7B%0D%0A++++++margin-left%3A+0.3em+%21important%3B%0D%0A++%7D%0D%0A++hr+%7B%0D%0A++++margin%3A+1em%3B%0D%0A++%7D%0D%0A++%0D%0A%0D%0A++%0D%0A%0D&source=The+Honeynet+Project)
