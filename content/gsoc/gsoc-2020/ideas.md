---
title: "Google Summer of Code 2020 Project Ideas"
date: "2020-02-20"
url: "/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas"
---

### Getting Started

This page contains a list of potential project ideas that we are keen to develop during GSoC 2020. If you would like to apply as a GSoC student, please follow these two steps to get started:

1. Read through this page and identify the project ideas you find interesting. Play around with our tools!
2. Join us on Slack and talk to your potential mentors

If there are any questions, please don’t hesistate and get in touch! 🙂

### GSoC and The Honeynet Project

During the previous years of GSoC, the Honeynet Project's students have created a wide range of very successful open source security projects, many of which have gone on to become the industry standard open source tools in their respective fields. Examples for these include:

- [Cuckoo Sandbox](//www.cuckoosandbox.org/) (2010+)
- [Mitmproxy](//mitmproxy.org/) (2012+)
- [Thug Client Honeypot](//buffer.github.io/thug/) (2012+)
- [DroidBox Android Sandbox](//github.com/pjlantz/droidbox) (2011+)
- [ConPot ICS/SCADA Honeypot](//conpot.org/) (2013+)
- [Glastopf Web Application Honeypot](//glastopf.org/) (2009+)
- [Dionaea](//dionaea.carnivore.it/) (2009+)
- [Holmes Processing](//www.holmesprocessing.com/) (2017+)

We are also always interested in hearing any ideas for additional relevant computer security and honeynet-related R&D projects (although remember that to qualify for receiving GSoC funding from Google your project deliverables need to fit in to [GSoC's 3-month project timescales](//developers.google.com/open-source/gsoc/faq)!). If you have a suitable and interesting project, we will always try and find the right resources to mentor it and support you.

Please note - even if you aren't an [eligible GSoC student](//developers.google.com/open-source/gsoc/faq), we are also always looking for general volunteers who are enthusiastic and interested in getting involved in honeynet R&D.

Each sponsored GSoC 2020 project will have one or more mentors available to provide a guaranteed contact point to students, plus one or more technical advisors to help applicants with the technical direction and delivery of the project (often the original author of a tool or its current maintainer, and usually someone recognised as an international expert in their particular field). Our Google Summer of Code organisational administrators will also be available to all sponsored GSoC students for general advice and logistical support. We'll also provide hosting for project infrastructure, if required.

For all questions about the Honeynet Project, the GSoC program or our projects, please contact us on **[gsoc-slack.honeynet.org](//gsoc-slack.honeynet.org/) (preferred)** or email us at [project@honeynet.org](mailto:project@honeynet.org).

* * *

# GSoC 2020 Project Ideas Overview

- [#1 Hack on Mitmproxy!](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#hack-on-mitmproxy)
- [#2 Unikraft VMI](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#unikraft-vmi)
- [#3 SNARE/TANNER](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#snare-tanner)
- [#4 HosTaGe: a mobile honeypot](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#hostage)
- [#5 Intel Owl improvements](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#intel-owl-improvements)
- [#6 Analytical Malware Classification](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#analytical-malware-classification)
- [#7 tenjint: Implement Plugins for the Automated Analysis or Detection of Malicious Code](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#tenjint-plugins)
- [#8 tenjint: Behavioral Profile](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#tenjint-profile)
- [#9 tenjint: Orchestration Framework](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#tenjint-framework)
- [#10 QUICk: a go library for analysing QUIC traffic](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#quick)
- [#11 Heralding: Protocol refinements](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#heralding)
- [#12 PAL Support for AMD/LibVMI](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#libvmi)
- [#13 Stealthy Kernel Debugging using Boxy/LibVMI](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#libvmi2)
- [#14 Expanding Clang-Tidy to include AUTOSAR compliance](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#clang-tidy)
- [#15 Infection Monkey](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#monkey)
- [#16 libmicrovmi - full bindings to Xen and KVM](//www.honeynet.org/gsoc/gsoc-2020/google-summer-of-code-2020-project-ideas#libmicrovmi)

* * *

## #1 - Hack on Mitmproxy!

**Mentor:** Maximilian Hils

**Backup Mentor:**  
Aldo Cortesi

**Skills required:**  
Knowledge of HTTP, Python, and optionally JavaScript

**Project type:**  
Improving an existing tool

**TLDR:  
**Want to ship your code to thousands of users? Hack on mitmproxy!

**Description:**  
mitmproxy is your swiss-army knife for debugging, testing, privacy measurements, and penetration testing. It can be used to intercept, inspect, modify and replay web traffic such as HTTP/1, HTTP/2, WebSockets, or any other SSL/TLS-protected protocols. You can prettify and decode a variety of message types ranging from HTML to Protobuf, intercept specific messages on-the-fly, modify them before they reach their destination, and replay them to a client or server later on.  
  
mitmproxy is a large project with a huge number of interesting areas to explore, down from low-level protocol work up to UX improvements. If you are motivated and know what you're interested in, why not get in touch with us and map out a custom GSoC project? Below are some ideas with a rough project size estimations - an enterprising student should be able to complete one large or 3 or more small projects during the GSoC period.

- Sans-IO Proxy Core: A major feature on mitmproxy’s roadmap is the replacement of our proxy core with an implementation that separates I/O and protocol logic (“sans I/O”). We've [proposed this previously as a GSoC project](//www.honeynet.org/gsoc/gsoc-2018/gsoc-2018-ideas/#mitmproxy-sansio), but have made significant progress since then. If you are interested in low-level protocol work, this is your chance to have a direct and definite impact.  
    
- Many mitmproxy users want to use mitmproxy to just see all traffic of their current device without configuring individual applications, but that requires a complicated iptables configuration or undocumented scripts on Windows. You can make tremendous improvements to mitmproxy onboarding experience here! \[[#1261](//github.com/mitmproxy/mitmproxy/issues/1261)\]  
    
- Extend mitmproxy's console UI to support WebSockets and raw TCP mode. These protocols are well-supported and mature in the core, but we haven't found the time to expose them to users in the UI**.**  
    
- Map Remote Editor: Other proxies have a feature which maps one URL to another, e.g. one can map //example.com/foo.js to a local file that is served to the client instead. It is easy to write a mitmproxy script that does this, but we want this to be a built-in feature! Fun fact: This task was initially proposed by a GSoC student in \[[#1454](//github.com/mitmproxy/mitmproxy/issues/1454)\]!

We encourage you to also think beyond what is listed above - what would **you** do to improve mitmproxy? Please see \[[#3805](//github.com/mitmproxy/mitmproxy/issues/3805)\] for some more details and get in touch with us on Slack to get started. :)

* * *

## #2 - Unikraft VMI

**Mentor:** Tamas K Lengyel

**Backup Mentor:**  
Sergej Proskurin

**Skills required:**  
C

**Project type:**  
Improving an existing tool

**TLDR:  
**Harden VM introspection applications by building them as a Unikernel with the Unikraft build system

**Description:**  
VM introspection applications often interact with VMs that have been compromised one-way or another. Usually the reason of moving the application out of the VM and using introspection is to make tampering harder. However, since the introspection application still needs to access information in the compromised VM, it is possible that a bug would lead to a VM escape through the introspection application itself.  
  
To avoid this, it is possible to run VM introspection applications in their own VMs. A previous year's GSoC explored running LibVMI in a MiniOS-based VM ([//tinyvmi.github.io](//tinyvmi.github.io)). Compiling and setting up MiniOS however is an unpleasant experience. In recent years the Unikraft project ([//xenproject.org/developers/teams/unikraft](//xenproject.org/developers/teams/unikraft)) has been solving this problem by creating an excellent build systems for Unikernel applications.  

This GSoC project would explore taking LibVMI and building a Unikernel application with it using Unikraft. The goal would be to create an extremely hardened VM application that would still be easy to build and port to new hypervisors.

* * *

## #3 - SNARE/TANNER

**Mentor:** Evgeniia Tokarchuk

**Backup Mentor:**  
Lukas Rist

**Skills required:**  
Python3

**Project type:**  
Improving an existing tool

**TLDR:  
**SNARE/TANNER: Make our web application honeypot attract new sorts of maliciousness

**Description:**  
SNARE \[1\] is a web application honeypot sensor attracting all sort of maliciousness from the Internet. TANNER \[2\] is remote data analysis, and classification service, to evaluate HTTP requests and composing the response then served by SNARE events. SNARE and TANNER have been in development since GSoC 2016 and this year we would like to bring more awesome features to the project. The main focus will be on the SNARE side, especially on the page cloning. On the TANNER side currently, we are encountering problems with scalability, so some engineering work towards moving to PostgreSQL/MongoDB instead of Redis should be done.  
  
\[1\] [//github.com/mushorg/snare](//github.com/mushorg/snare)  
\[2\] [//github.com/mushorg/tanner](//github.com/mushorg/tanner)

* * *

## #4 - HosTaGe: a mobile honeypot

**Mentor:** Emmanouil Vasilomanolakis

**Backup Mentor:**  
Shreyas Srinivasa

**Skills required:**  
basic network security knowledge, protocol understanding, Java, honeypot understanding

**Project type:**  
Improving an existing tool

**TLDR:  
**HosTaGe is a low interaction mobile honeypot for Android devices. The idea is to have a fast, on-the-go honeypot that emulates most modern protocols. Hostage is already mature and this project will be focusing on its improvements (e.g. IoT protocol support, visualizations, security features, etc.). The project is open source and will be re-launched as part of the Google playstore as well as part of the Honeynet Project arsenal.

**Description:**  
The project is about improving HosTaGe, a mobile, all-around, low interaction, honeypot. The student will choose between the different improvement options based on their preferences. Options include new protocol support (especially in the IoT area), improvements of old protocols, GUI improvements, honeypot stealthiness, etc. Upon deciding the direction that the student prefers we will create user stories for the software development process. Nevertheless, with regard to the specifics of the software development methodology, we are open. The project will be supervised closely by the mentors (Aalborg University, Copenhagen, Denmark).

* * *

## #5 - Intel Owl improvements

**Mentor:** Matteo Lodi

**Backup Mentor:**  
Pietro Delsante

**Skills required:**  
Web development, Python, Docker

**Project type:**  
Improving an existing tool

**TLDR:  
**Intel Owl is a project which aims to ease, scale out and speed up the generation of cyber threat intelligence data. It can analyze observables or files thanks to more than 40 analyzers that can be queried with a single API request. We are looking for people who would like to add new analyzers, new connectors and a new interface.

**Description:**  
Intel Owl is a project which aims to ease, scale out and speed up the generation of cyber threat intelligence data. It can analyze observables or files thanks to more than 40 analyzers that can be queried with a single API request. We are looking for people who would like to add new analyzers, new connectors and a new interface. In particular, we would like to integrate most of the available open source tools that can be used to analyze an observable or a file. Some of them (Cuckoo, Yara, Oletools, Stringsifter,...) are already integrated. New integrations could be Thug, Drakvuf, ClamAV, PEframe, Shodan, Box-js, Manet, Malpedia, etc. Also, we would like to add new connectors for open source threat intelligence platforms like MISP or OpenCTI to allow their users to enrich their data with Intel Owl more easily. Ultimately, we would like to improve the actual basic interface to allow the users to better interact with the platform.

* * *

## #6 - Analytical malware classification

**Mentor:** Ricardo van Zutphen

**Backup Mentor:**  
Jurriaan Bremer

**Skills required:**  
Python, Malware Analysis, Cuckoo Sandbox

**Project type:**  
Improving an existing tool

**TLDR:  
**Helping users to more easily interpret analysis results by searching and developing a malware classification feature

**Description:**  
Cuckoo Sandbox is currently undergoing a complete redesign from the ground up. This means we have the unique opportunity to introduce new features. As a part of this redesign, we want to include features that make it easier for users to understand what how a sample behaved during an analysis and how it might impact them. Malware can exist in multiple forms and display a wide array of behaviors that can be categorized into a labeled type of category; ransomware, spyware, etc. The goal of this project is to make a proof of concept module that uses an analytical approach to classify behavior into one or more categories. This means researching what categories can be properly defined and measured, the malware/behavior of each category, the best approaches to measure this, and implementing a proof of concept module that takes in Cuckoo behavior logs and outputs a ‘score’ for each category. If there is spare time, it can be used to try to improve the categorization using machine learning.

* * *

## #7 - tenjint: Implement Plugins for the Automated Analysis or Detection of Malicious Code

**Mentor:** Jonas Pfoh

**Backup Mentor:**  
Sebastian Vogl

**Skills required:**  
Python, Virtualization, Forensics, Binary Analysis

**Project type:**  
Umbrella Project / Improving an existing tool

**TLDR:  
**Develop novel analysis plugins on a multi-architecture VMI platform.

**Description:**  
tenjint is a VMI-based system analysis framework for x86 and ARM written in Python and we plan on maintaining a repository of plugins. We welcome any submissions for plugins that implement interesting detection or analysis techniques. This might include (but is not limited to) novel ROP detection, shellcode detection, auto-unpacking code sections, extracting control flow, etc.

* * *

## #8 - tenjint: Behavioral Profile

**Mentor:** Sebastian Vogl

**Backup Mentor:**  
Jonas Pfoh

**Skills required:**  
Python, Virtualization, Forensics, Binary Analysis

**Project type:**  
Umbrella Project / Improving an existing tool

**TLDR:  
**Extract the behavioral profile of an application using a multi-architecture VMI platform.

**Description:**  
tenjint is a VMI-based system analysis framework for x86 and ARM. The framework can be easily extended with Python plugins. To detect exploits more reliably, we would like to create a plugin that is capable of extracting a behavioral profile of an application. This behavioral profile should describe the capabilities of a program according to its intended use. Exploits will often deviate from this norm by forcing an application to perform actions it would never conduct under normal circumstances.

* * *

## #9 - tenjint: Orchestration Framework

**Mentor:** Jonas Pfoh

**Backup Mentor:**  
Sebastian Vogl

**Skills required:**  
Python, Web development, Linux

**Project type:**  
Umbrella Project / Improving an existing tool

**TLDR:  
**Develop a web API and orchestration framework for binary analysis sandboxes.

**Description:**  
tenjint is a VMI-based system analysis framework for x86 and ARM. We are looking for someone to develop a web API for the submission of samples to a tenjint-based sandbox and the retrieval of reports. This would include the implementation of the API as well as the required orchestration of VMs behind the scenes.

* * *

## #10 - QUICk: a go library for analysing QUIC traffic

**Mentor:** Adel Karimishiraz

**Backup Mentor:**  
TBA

**Skills required:**  
Golang, a good understanding of network protocols, being familiar with QUIC protocol

**Project type:**  
Improving an existing tool

**TLDR:  
**QUICk is an initial go library based on gopacket for analysing QUIC protocol’s ClientHello messages. Your task would be to add support for other gQUIC / IETF QUIC versions and message types.

**Description:**  
QUIC is a UDP-based multiplexed and secure transport protocol. HTTP/3 uses QUIC as its transport protocol, instead of using TCP! There are actually two different protocols: (1) Google QUIC or gQUIC, the original protocol designed by Google, and (2) IETF QUIC which is an effort by the Internet Engineering Task Force to standardise the protocol. Chrome browsers have gQUIC enabled by default, and Google has been using this protocol to deliver traffic for their products such as Google Search, Gmail, and YouTube. This protocol is still not widely supported by network security and monitoring tools, and this makes QUIC an interesting communication protocol for attackers. One example is Merlin, an open-source post-exploitation tool, which is added support for QUIC as a Command and Control (C2) protocol. QUICk is an initial go library based on gopacket for analysing QUIC ClientHello messages. Your task would be to add support for other gQUIC / IETF QUIC versions and message types.

* * *

## #11 - Heralding - protocol refinements

**Mentor:** Johnny Vestergaard

**Backup Mentor:**  
TBA

**Skills required:**  
Python, medium to high

**Project type:**  
Improving an existing tool

**TLDR:  
**Investigate each protocol and find interesting facts that we can log in order to improve fingerprinting.

**Description:**  
Currently Heralding supports 14 protocol. At the moment we only log username and password for each login attempt. In order to do better fingerprinting for the application that tries to connect, we want to collect additional data for each login attempt. Some examples of this could be ciphers asked, terminal settings, user agents, etc.

* * *

## #12 - PAL Support for AMD/LibVMI

**Mentor:** Rian Quinn

**Backup Mentor:**  
Tamas K. Lengyel

**Skills required:**  
Basic knowledge of Python, C and C++

**Project type:**  
Improving an existing tool

**TLDR:  
**Add AMD and LibVMI support for PAL. PAL provides comprehensive C/C++ header-only intrincis support (raw access to CPU registers) for ARM and Intel and the goal of this effort is to add AMD support, and integer PAL into the LibVMI project.

**Description:**  
This project will add AMD to PAL as well as integrate PAL into the LibVMI project. When performing VM introspection and working with hypervisors, kernels, embedded systems, etc..., you often times need to directly interface with hardware. CPUs like those provided by Intel, AMD and ARM not only provide general purpose registers which are used to execute code, they also provide registers that store the CPU's configuration, capabilities, and current execution environment. There are hundreds of these special purpose registers and often times, these special purpose registers are broken into bit fields that must be individually programmed. If you want to determine, for example, if your Intel CPU supports the Time Stamp Counter, you must load EAX with 1, run CPUID, and then bit-mask EDX to get the value of bit 4, which can tell your code if the Time Stamp Counter is supported. With hundreds of special purpose registers, each with several bit fields, the total number of fields that a programmer must work with is huge (and that is just for one CPU) and prone to error.

The PAL project started from a DARPA funded effort to use the ARM's CPU specification to automatically generate APIs in C and C++ that a programmer can use to interface with the CPU (commonly referred to as intrinsics, although PAL extends the traditional definition to also include APIs for each individual bit field). These APIs are header-only, and designed to be used in low-level programming, malware research, reverse engineering, introspection, kernel/hypervisor development, etc... The project was such a success, it has since, manually added support for Intel.

This project will extend PAL to add support for AMD processors. AMD's recent success over Intel in performance and price will almost certainly lead to greater adoption of the architecture across all use cases, including malware analysis, reverse engineering and introspection. Adding AMD support to PAL will ensure researchers and engineers alike have easy access to the CPU's special purpose registers as they work to add support for AMD. In addition, this project will also integrate PAL into LibVMI. LibVMI provides APIs for performing VM introspection, which is commonly used for malware analysis and reverse engineering. VM introspection APIs like LibVMI provide access to a virtual CPU's state including special purpose registers. Integrating PAL into LibVMI will ensure users of LibVMI have easy to use APIs for working with virtual CPUs registers making LibVMI more approachable to new and existing users.

* * *

## #13 - Stealthy Kernel Debugging using Boxy/LibVMI

**Mentor:** Rian Quinn

**Backup Mentor:**  
Tamas K. Lengyel

**Skills required:**  
Knowledge of LibVMI, VM introspection, and general hypervisor knowledge

**Project type:**  
Improving an existing tool

**TLDR:  
**This project will implement a stealthy kernel debugger using the Boxy hypervisor and LibVMI

**Description:**  
This project will implement a stealthy kernel debugger using the Boxy hypervisor and LibVMI.

LiveKB ([//docs.microsoft.com/en-us/sysinternals/downloads/livekd](//docs.microsoft.com/en-us/sysinternals/downloads/livekd)) provides a Windows kernel debuggerlocally live on a running system, similar to using GDB with the Linux Kernel. The problem with these kernel debuggers is their use is visible to the operating system and any software running including malware.

This effort will research and implement a prototype kernel debugger using the Boxy Hypervisor and LibVMI. The Boxy Hypervisor provides the ability to run small Linux VMs, isolated from the host operating system as "service VMs" (i.e., services that run in a VM and not directly in the operating system). Unlike existing hypervisors, Boxy VMX rootkits the host operating system, lifting the operating system into a lightweight virtual machine, providing these services VMs with the ability to introspect the host operating system in real-time. Previous GSoC projects have added Boxy support to LibVMI. This project will leverage this previous work and extend it to provide stealthy, kernel level debugging facilities. The successful completion of this project will provide better tools for malware analysis, reverse engineering, introspection and even general kernel-level software development.

* * *

## #14 - Expanding Clang-Tidy to include AUTOSAR compliance

**Mentor:** Rian Quinn

**Backup Mentor:**  
Tamas K. Lengyel

**Skills required:**  
Previous experience with C++, basic knowledge of LLVM, Clang and Clang-Tidy

**Project type:**  
Improving an existing tool

**TLDR:  
**This project will extend Clang-Tidy to include AUTOSAR compliance to ensure malware analysis and introspection tools written in C++ can be used on critical systems

**Description:**  
This project will extend Clang-Tidy to include AUTOSAR compliance to ensure malware analysis and introspection tools written in C++ can be used on critical systems.

There is a growing trend of malware analysis tools being used on deployed systems to get live, real-time data on malware including how it propagates. Extending these capabilities to critical systems applications such as automotive, healthcare, power, etc... is problematic for open source software, however, as the tools needed to ensure compliance for use on critical systems is expensive and proprietary. The best option currently available to open source is SonarCloud, which sadly does not include AUTOSAR with only limited support for MISRA.

To address this issue, this project will extend the Clang Tidy static analysis tool to include limited support for AUTOSAR. Currently, Clang Tidy has support for CERT C++, High Integrity C++ and the C++ Core Guidelines, all of which were used to develop the AUTOSAR specifications, providing a starting point for this project. In addition, there have been some open source attempts to start this work (at least with MISRA [//github.com/rettichschnidi/clang-tidy-misra](//github.com/rettichschnidi/clang-tidy-misra)) that could also be leveraged. Although it is unlikely full AUTOSAR compliance is possible on a single GSoC project, getting the ball rolling will pave the way for future projects to complete full support.The successful completion of this effort will dramatically change the compliance landscape, finally providing an open source alternative to expensive, closed-source compliance tools. With support for AUTOSAR compliance, open source, malware analysis projects (any any other open source projects) written in C++ will have a viable means to ensure support for critical system environments, expanding their applicability to new operating environments that have traditionally been forgotten.

* * *

## #15 - Infection Monkey

**Mentor:** Shay Nehmad

**Backup Mentor:**  
Daniel Goldberg

**Skills required:**  
Python, Networks

**Project type:**  
Umbrella Project: Improving an existing tool

**TLDR:  
**Breach and Attack simulation tool

**Description:**  
The Infection Monkey helps answer the question "What if attackers breach my network?" by simulating a post-breach attacker. The Monkey does this by simulating all the steps of a network attack; from reconnaissance and lateral movement and all the way to data exfiltration to a simulated command and control server.

A good metaphor might be to think about the Infection Monkey as a tool that you control, armed with the tools of a 16-year-old script kiddie and the persistence of a 60-year-old chess grand-master. Infection Monkey is useful for people from all over the security industry – Penetration Testers, Network Engineers, Exploit Developers, and other Security professionals.

After running the Monkey, all the findings are presented in reports – similar to what one might get from Pen Testers. The reports include specific actions that the blue team can perform to implement better security measures – for example, after breaching a machine using ElasticGroovy, the Monkey will report "The attack was made possible because the Elastic Search server was not patched against CVE-2015-1427. Update your Elastic Search server to version 1.4.3 or higher". Then you can implement the suggestion and run the exact same attack again to make sure you did it right. Other reports map the Monkey's actions in the network to the MITRE ATT&CK and Zero Trust frameworks in order to communicate the Monkey's results in popular Security lingo.

The Infection Monkey is an Open Source GPLv3 licensed tool, mostly developed by Guardicore developers. The Monkey has >3K stars on GitHub and an active user community within the Security industry.

In this year's GSoC (our third time!) we want to focus on EXPANDING the Monkey's stealth and attack capabilities:

- Avoid Antiviruses: Upgrade Mimikatz to a version that avoids malware detection techniques (perhaps by migrating to pykatz) and then using the capabilities of the upgraded version for new domain attacks.
- Add attack capabilites: Adding new reliable (high stability) exploits to the Monkey. Come with an idea for a vuln (maybe something off exploitdb or MetaSploit).
- Add detection capabilities: Intergrating AtomicRedTeam as a post-breach action for the Monkey.

* * *

## #16 - libmicrovmi - full bindings to Xen and KVM

**Mentor:** Dorian Eikenberg

**Backup Mentor:**  
Mathieu Tarral

**Skills required:**  
Rust language, CFFI bindings, bindgen

**Project type:**  
Umbrella Project: Improving an existing tool

**TLDR:  
**libmicrovmi is a VMI abstraction layer implementation in Rust

**Description:**  
libmicrovmi aims to be a unified VMI interface across multiple hypervisors and emulators. It remains simple (no semantic translation, no page table walking) and composable making it a new basic block in the VMI ecosystem, on which any VMI app previously targeting a single hypervisor or emulator can rebase.

In this year's GSoC we want to improve the (currently only partial) bindings to some of our supported hypervisors:

- create full bindings to Xen and KVM
- complete the definition of the libmicrovmi API (mostly event management)
- take care of compatibility issues and breaking API changes between different versions of Xen
- write a series of tests to validate that the newly created bindings are working as intended

* * *

* * *
