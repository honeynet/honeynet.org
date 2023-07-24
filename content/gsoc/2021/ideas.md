---
title: "Google Summer of Code 2021 Project Ideas"
date: "2021-01-27"
---

### Getting Started

This page contains a list of potential project ideas that we are keen to develop during GSoC 2021. If you would like to apply as a GSoC student, please follow these two steps to get started:

1. Read through this page and identify the project ideas you find interesting. Play around with our tools!
2. Join us on Slack and talk to your potential mentors at [https://gsoc-slack.honeynet.org/](https://gsoc-slack.honeynet.org/)

If there are any questions, please don’t hesitate and get in touch! 🙂

### GSoC and The Honeynet Project

During the previous years of GSoC, the Honeynet Project's students have created a wide range of very successful open source security projects, many of which have gone on to become the industry standard open source tools in their respective fields.

We are also always interested in hearing any ideas for additional relevant computer security and honeynet-related R&D projects (although remember that to qualify for receiving GSoC funding from Google your project deliverables need to fit in to [GSoC's 3-month project timescales](//developers.google.com/open-source/gsoc/faq)!). If you have a suitable and interesting project, we will always try and find the right resources to mentor it and support you.

Please note - even if you aren't an [eligible GSoC student](//developers.google.com/open-source/gsoc/faq), we are also always looking for general volunteers who are enthusiastic and interested in getting involved in honeynet R&D.

Each sponsored GSoC 2021 project will have one or more mentors available to provide a guaranteed contact point to students, plus one or more technical advisors to help applicants with the technical direction and delivery of the project (often the original author of a tool or its current maintainer, and usually someone recognised as an international expert in their particular field). Our Google Summer of Code organisational administrators will also be available to all sponsored GSoC students for general advice and logistical support. We'll also provide hosting for project infrastructure, if required.

For all questions about the Honeynet Project, the GSoC program or our projects, please contact us on **[gsoc-slack.honeynet.org](//gsoc-slack.honeynet.org/) (preferred)** or email us at [project@honeynet.org](mailto:project@honeynet.org).

* * *

# GSoC 2021 Project Ideas Overview

- [#1 - Hack on Mitmproxy!](//www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#hack-on-mitmproxy)
- [#2 - Fuzzing Xen with Xen](//www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#fuzzingxen)
- [#3 - Quark Engine: The Storyteller of Android Malware](//www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#quark)
- [#4 - IntelOwl Plugin Framework](//www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#intelowl-plugin)
- [#5 - IntelOwl improvements](//www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#intelowl-improve)
- [#6 - Implement DdiMon for Windows and Linux using Bareflank](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#bareflank)
- [#7 - HosTaGe: the mobile all around honeypot](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#hostage)
- [#8 - RIOTPOT: an OT and IoT honeypot](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#riotpot)
- [#9 - PcapMonkey improvments](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#pcapmonkey)
- [#10 - Implement a log browser in DRAKVUF Sandbox web interface](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#drakvuf1)
- [#11 - Add a summary of malware behavior to DRAKVUF Sandbox](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#drakvuf2)
- [#12 - Add graph representing malware execution to DRAKVUF Sandbox](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#drakvuf3)
- [#13 - SNARE Improvements](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#snare)
- [#14 - Implement Linux support in DRAKVUF Sandbox](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#drakvuf4)
- [#15 - Implement the Xen ABI for Virtual Machine Introspection (VMI) in MicroV](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#microv)
- [#16 - Adding Python Bindings to IntroVirt](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#introvirt)
- [#17 - Integrate a PLC CPU Emulator into Conpot](https://www.honeynet.org/gsoc/gsoc-2021/google-summer-of-code-2021-project-ideas#conpot)

* * *

## #1 - Hack on Mitmproxy!

**Mentor:** Maximilian Hils

**URL:** [https://mitmproxy.org](https://mitmproxy.org)

**Project type**: Improving an existing tool

mitmproxy is your swiss-army knife for debugging, testing, privacy measurements, and penetration testing. It can be used to intercept, inspect, modify and replay web traffic such as HTTP/1, HTTP/2, WebSockets, or any other SSL/TLS-protected protocols. You can prettify and decode a variety of message types ranging from HTML to Protobuf, intercept specific messages on-the-fly, modify them before they reach their destination, and replay them to a client or server later on.

mitmproxy is a large project with a huge number of interesting areas to explore, down from low-level protocol work up to UX improvements. If you are motivated and know what you’re interested in, why not get in touch with us and map out a custom GSoC project? Below are some ideas with a rough project size estimations – an enterprising student should be able to complete one large or 3 or more small projects during the GSoC period.

Potential Tasks: [https://github.com/mitmproxy/mitmproxy/issues/4404](https://github.com/mitmproxy/mitmproxy/issues/4404)

* * *

## #2 - Fuzzing Xen with Xen

**Mentor:** Tamas K Lengyel, Andrew Cooper

**URL:** [http://xenbits.xenproject.org/docs/xtf/](http://xenbits.xenproject.org/docs/xtf/)

**Project type**: Improving an existing tool

The latest version of Xen provides the ability to perform high-performance fuzzing using VM forks. So far this fuzzer has only been used to target Operating Systems and user-space processes. Xen's unique architecture allows Xen to boot inside a Xen VM without requiring nested virtualization, thus allowing us to fuzz Xen with Xen. The project will focus on creating the test harnesses for the fuzzer to exercise various Xen hypercalls through the Xen Test Framework (XTF) and upstreaming these test harnesses into XTF itself. The project will further explore potential Xen-internal channels to fuzz.

Further info: [https://github.com/intel/kernel-fuzzer-for-xen-project](http://xenbits.xenproject.org/docs/xtf/)

* * *

## #3 - Quark Engine: The Storyteller of Android Malware

**Mentor:** JunWei Song

**URL:** [https://github.com/quark-engine/quark-engine](https://github.com/quark-engine/quark-engine)

**Project type**: Improving an existing tool

Quark is one of the most popular analysis engines for hunting threat intelligence inside the APK files. Since it is rule-based, you can use the ones built-in or customize as needed. With ideas decoded from criminal law, Quark has its unique angles for malware analysis. We developed a Dalvik bytecode loader that has tainted analysis inside but also defeats the obfuscation techniques used against reverse engineering. And surprisingly, the loader matches perfectly the design of our malware scoring system.

Features/Progress in recent versions of Quark:

1\. Public Reports: AhMyth RAT and Roaming Mantis. And we give out all detection rules used in the reports

2\. Call Graphs for behavior detected

3\. Behavior Classification

4\. New Strategy for Generating Rules

5\. Open-Sourced all codes for rule generation

6\. Python Binding APIs: Made Quark easy to be integrated.

7\. Integrated to Intel Owl, BlackArch Linux, Pithus/Bazaar and APKLAB

In recent versions of Quark, we put huge efforts into making it more useful and practical. We have public reports that analyze classic samples like AhMyth RAT and Roaming Mantis. And we gave out all detection rules used in these reports! In those reports, we show how users can use new features of Quark to quickly realize how the malware works. For example, malware analysts now can use Quark to generate call graphs of each behavior detected. And we also provide a feature that can automatically classify the detected behaviors in APK so as to boost up the storytelling of malware. Moreover, to make Quark a more practical tool to use, we developed a new strategy for generating detection rules.

The new strategy improves the effectiveness of the rules and efficiency of the generating process. Even better, we open-sourced all codes for everyone. With the usefulness of Quark, we now have developed python binding APIs for integration with other open-source projects. Now you can use Quark in projects like Intel Owl, BlackArch Linux, Pithus/Bazaar, and APKLab. We’re happy to enrich the analysis chain of open source intelligence.

Below are some ideas we think are valuable and are open:

1\. Resilience: Improve test coverage, documentation and CI, etc.

2\. Practicality: Develop more comprehensive call graphs for boosting up the storytelling of the malware.

3\. Performance: Propose a plan for detecting bottlenecks of the performance and improve them.

4\. Enrich the analysis chain of open source intelligence: Integrate with/to upstream open source projects like APKiD and downstream projects like Intel Owl and APKLab.

* * *

## #4 - Intel Owl Plugin Framework

**Mentors:** Matteo Lodi - Eshaan Bansal

**URL:** [https://github.com/intelowlproject/IntelOwl/](https://github.com/intelowlproject/IntelOwl)

**Project type**: Improving an existing tool

**Skills required**: Web development, Docker, Django, Django Rest Framework

One of the strongest limits of this project is the lack of built-in integrations with other widespread open source CTI-related platforms, like MISP or OpenCTI. We would like to add a plugin framework that can be leveraged to easily connect IntelOwl with other external tools.

This issue at [https://github.com/intelowlproject/IntelOwl/issues/249](https://github.com/intelowlproject/IntelOwl/issues/249) could be a starting point.

This project would require knowledge of how MISP and OpenCTI work to properly integrate them with the platform.

* * *

## #5 - IntelOwl Improvements

**Mentors:** Matteo Lodi - Eshaan Bansal

**URL:** [https://github.com/intelowlproject/IntelOwl/](https://github.com/intelowlproject/IntelOwl)

**Project type**: Improving an existing tool

**Skills required**: Web development, Docker, Django, Django Rest Framework, Angular 9+.

This slot is open for people who aims to:

\* propose innovative and valuable additions to the project and realize them. We want to hear your ideas!

\* work on improving test coverage, documentation, website, CI and overall stability and resilience of the project

\* work on already existing issues spanning all 5 repositories: IntelOwl (Django), Intelowl-ng (Angular), pyintelowl (click CLI, python), go-intelowl (CLI, go), intelowlproject.github.io (official website)

* * *

## #6 - Implement DdiMon for Windows and Linux using Bareflank

**Mentors:** Rian Quinn

**URL:** [https://bareflank.github.io/hypervisor](https://bareflank.github.io/hypervisor)

**Project type**: Create a new tool

DdiMon is an introspection engine capable of hooking PatchGuard in Windows using shadow EPT style hooks. Specifically, DdiMon hooks the execution of specific kernel level function calls, while using EPT to prevent the guest from seeing or being able to modify these hooks.

This project will port this capability to the Bareflank hypervisor to create an example for educational purposes. Like DdiMon, the results of this project will provide the user with the ability to hook and monitor PatchGuard for Windows. In addition, this project will extend this capability to the Linux operating system. Specifically, the student will identify key kernel level functions within Linux to hook and monitor, similar to the Windows variant, demonstrating the ability to monitor the execution of the Linux operating system without detection.

Finally the results of this project will be well simplified, tested, documented and upstreamed to the Bareflank hypervisor project as examples that others can use in the future.

* * *

## #7 - HosTaGe: the mobile all around honeypot

**Mentors:** Emmanouil Vasilomanolakis

**URL:** [https://github.com/aau-network-security/HosTaGe](https://github.com/aau-network-security/HosTaGe)

**Project type**: Improving an existing tool

Hostage is a low interaction mobile honeypot for Android devices. The idea is to have a fast, on-the-go honeypot that emulates most modern protocols. Hostage is already mature and this project will be focusing on its improvements (e.g. IoT protocol support, visualizations, security features, etc.). The project is open source and available on Google Playstore. The project is about improving HosTaGe, a mobile, all-around, low interaction, honeypot. The student will choose between the different improvement options based on their preferences. Options include new protocol support (especially in the IoT area), improvements of old protocols, GUI improvements, honeypot stealthiness, etc.

* * *

## #8 - RIOTPOT: an OT and IoT honeypot

**Mentors:** Emmanouil Vasilomanolakis

**URL:** [https://github.com/aau-network-security/riotpot](https://github.com/aau-network-security/riotpot)

**Project type**: Improving an existing tool

RIOTPOT is a modern open-source medium interaction OT/IoT honeypot written in Go. This goal of this project is to enhance RIOTPOT’s capabilities by adding new protocol emulation support in the form of device profiles. In addition, the project can explore how the honeypot is handling fingerprinting (e.g., via Nmap) and how it can trick such systems and hide its honeypot nature. The student can decide to follow one or more of the following options:

• OT device profile creation (e.g., devices using DNP3, Fieldbus, Profibus)

• IoT device profile creation (e.g., devices using AMQP, CoAP, M2M)

• OT-based dynamic response system

• Attack signature export

• Anti-fingerprinting response generation

* * *

## #9 - PcapMonkey improvments

**Mentors:** Federico Foschini, Pietro Delsante

**URL:** [https://github.com/certego/PcapMonkey](https://github.com/certego/PcapMonkey)

**Project type**: Improving an existing tool

Pcapmonkey is a project that will provide an easy way to analyze pcap using the latest version of Suricata and Zeek. It can also save Suricata and Zeek logs in Elasticsearch using the new Elasticsearch Common Schema or the original field names.

Pcapmonkey uses default docker container for most images and aims to be easy and straightforward to use. Help is needed in creating dashboards, visualization, integrating windows event logs and adding features that let analysist work faster and smarter.

* * *

## #10 - Implement a log browser in DRAKVUF Sandbox web interface

**Mentors:** Michal Leszczynski

**URL:** [](https://github.com/certego/PcapMonkey)[https://github.com/CERT-Polska/drakvuf-sandbox/](https://github.com/CERT-Polska/drakvuf-sandbox/)

**Project type**: Improving an existing tool

**Skills required**: JavaScript, Python

DRAKVUF Sandbox is an open source automated black-box malware analysis system using virtual machine introspection (VMI) with DRAKVUF ([https://drakvuf.com/](https://drakvuf.com/)) engine under the hood.

Most of the analysis results generated by DRAKVUF Sandbox are available as plain JSON files, which can be significant in size. The goal of this project is to implement an interactive log browser that would allow analysts to easily browse and search the results. The log browser should also automatically collapse sequences of similar log lines to reduce excessive output that is generated when certain APIs are called in a loop for example.

The project includes creating a design of the search user interface for individual analyses, proposal of heuristics for collapsing similar log lines and implementing the feature in Drakvuf Sandbox.

* * *

## #11 - Add a summary of malware behavior to DRAKVUF Sandbox

**Mentors:** Michal Leszczynski

**URL:** [https://github.com/CERT-Polska/drakvuf-sandbox/](https://github.com/CERT-Polska/drakvuf-sandbox/)

**Project type**: Improving an existing tool

**Skills required**: JavaScript, Python, basics of malware analysis

DRAKVUF Sandbox is an open source automated black-box malware analysis system using virtual machine introspection (VMI) with DRAKVUF (https://drakvuf.com/) engine under the hood.

As DRAKVUF Sandbox monitors behavior of malware samples it collects a lot of detailed data, like APIs, syscalls, network traffic, etc., however it lacks a summary of most important characteristics of the analyzed sample, for example if any anti-analysis tricks are used, files are downloaded, code injected into another process, persistence methods and more.

The goal of this project is to add overview of the most important behaviors of the malware to the results view based on the information already present in the logs collected by the sandbox, so an analyst can quickly see main properties of the sample.

Other existing sandboxing solutions can serve as an inspiration for the design of the feature. Examples: [https://cuckoo.cert.ee/analysis/2045661/summary](https://cuckoo.cert.ee/analysis/2045661/summary) [https://www.vmray.com/analyses/guloader-delivering-azorult/report/overview.html](https://www.vmray.com/analyses/guloader-delivering-azorult/report/overview.html) [https://www.joesandbox.com/analysis/347016/0/html](https://www.joesandbox.com/analysis/347016/0/html )

The scope of this project includes design of the interface that will be used to present the overview, selection of heuristics to extract interesting features from logs (possibly by embedding the CAPA tool: https://github.com/fireeye/capa) and implementation of the new view in DRAKVUF Sandbox.

* * *

## #12 - Add graph representing malware execution to DRAKVUF Sandbox

**Mentors:** Michal Leszczynski

**URL:** [https://github.com/CERT-Polska/drakvuf-sandbox/](https://github.com/CERT-Polska/drakvuf-sandbox/)

**Project type**: Improving an existing tool

**Skills required**: JavaScript, basics of malware analysis

DRAKVUF Sandbox is an open source automated black-box malware analysis system using virtual machine introspection (VMI) with DRAKVUF (https://drakvuf.com/) engine under the hood.

As DRAKVUF Sandbox monitors behavior of malware samples it collects a lot of detailed data, like APIs and syscalls that were used. Currently the data is available as a big log file, which makes it difficult to get a high-level understanding of the malware activities.

The goal of this project is to present an analyst with a graph that would illustrate all important activities of the sample, for example process creation or code injection based on the logs available.

Graph visualisations offered by existing solutions can serve as an inspiration for designing the feature. Examples: [https://www.joesandbox.com/analysis/347016/0/html#behaviorGraph](https://www.joesandbox.com/analysis/347016/0/html#behaviorGraph) [https://www.vmray.com/analyses/303ad8c115d9/report/behavior\_grouped.html](https://www.vmray.com/analyses/303ad8c115d9/report/behavior_grouped.html) [https://procdot.com](https://procdot.com)/

The scope of the project includes proposing a design of the visualization for a limited set of activities (at least process creation, termination, code injection), evaluation of open source JavaScript visualization libraries for graph layout and rendering (D3.js, Dagre, ELK, etc.) and implementing the feature in DRAKVUF Sandbox.

* * *

## #13 - SNARE improvements

**Mentors:** Evgenia Tokarchuk

**URL:** [https://github.com/mushorg/snare](https://github.com/mushorg/snare)

**Project type**: Improving an existing tool

**Skills required**: Python, basics of malware analysis

SNARE is a web application honeypot sensor attracting maliciousness from the Internet, aiming to focus on attack surface generation. SNARE generates events that are then evaluated by TANNER ([github.com/mushorg/tanner](http://github.com/mushorg/tanner)) and returns the attack emulated results to the end-user.

The main focus for the upcoming GSoC 2021 will be:

\- Improve cloning system: current cloning system has limited functionality and unable to work with many websites. So the purpose of this task is to explore the existing tools and either integrate external libraries or improve the existing modules.

\- Architectural changes: currently, SNARE works with the aiohttp v.3.4.4, which is obsolete and disagrees with the TANNER setup. The server functionality has to be re-designed and re-written using the updated packages.

We are open to discuss other task ideas in the scope of the SNARE project.

* * *

## #14 - Implement Linux support in DRAKVUF Sandbox

**Mentors:** Adam Kliś, Michal Leszczynski

**URL:** [https://github.com/CERT-Polska/drakvuf-sandbox/](https://github.com/CERT-Polska/drakvuf-sandbox/)

**Project type**: Improving an existing tool

**Skills required**: Python (programming), C++ (reading existing code), JavaScript (minimally)

DRAKVUF Sandbox is an open source automated black-box malware analysis system using virtual machine introspection (VMI) with DRAKVUF ([https://drakvuf.com/](https://drakvuf.com/)) engine under the hood. Currently, the DRAKVUF Sandbox project offers an easy installation process that allows to setup a Windows 7/10 Virtual Machine snapshot that could be further used for automated malware analysis.

Although DRAKVUF engine supports analysis of both Windows and Linux guest VMs, the Sandbox project doesn’t have any support for Linux yet. The goal of the project is to design and implement a simple installation process for Linux guests, which would work in a similar manner as Windows guest installation process do.

* * *

## #15 - Implement the Xen ABI for Virtual Machine Introspection (VMI) in MicroV

**Mentors:** Christopher Pelloux

**URL:** [https://github.com/Bareflank/MicroV/tree/mono](https://github.com/Bareflank/MicroV/tree/mono)

**Project type**: Improving an existing tool

**Skills required**: C++, VM introspection, and general hypervisor knowledge

MicroV (renamed from Boxy) is a type 1 hypervisor that supports late launch by demoting the host OS, early launch with EFI, Windows and Linux host OS, and Linux guest VMs.

This year, a newly open sourced version of MicroV implements a subset of the Xen ABI that adds a compatibility layer for Xen and support PCI passthrough. This allows Xen service VMs (i.e. Linux VMs with the Xen drivers and services) to run on top of MicroV and gain new features otherwise not supported by Xen, namely late launch and Windows host OS support.

By implementing the Xen ABI for introspection in MicroV, existing VMI projects built for Xen, e.g. LibVMI, IntroVirt, DRAKVUF, etc. will be able to run on top of MicroV directly and not require to be modified.

The student will need to identify parts of the Xen ABI relevant for VMI and  
implement them in MicroV. e.g. Xen hypercalls for memory access, vCPU events, altp2m, etc.

A LibVMI service VM with the Xen drivers will be created by the student to run the existing LibVMI examples for Xen. This will help support, test and verify the development of the Xen ABI in MicroV throughout the project.

* * *

## #16 - Adding Python Bindings to IntroVirt

**Mentors:** Rian Quinn

**URL:** [https://github.com/IntroVirt/IntroVirt](https://github.com/IntroVirt/IntroVirt)

**Project type**: Improving an existing tool

**Skills required**: C++, VM introspection, and general hypervisor knowledge

IntroVirt is the VMI new kid on the block that has recently been released into the wild. We have almost a decade of time into the framework and looking to get some fresh eyes and new ideas. Specifically we would like to extend the C++ based framework into other scripting languages via SWIG. Python 3 is a high priority as target language. Historically language bindings fell out of maintenance due to a lack of testing, so ideally some quick automated tests are written to alert the team and ensure the language bindings remain functional.

Once the IntroVirt Python bindings are implemented, we would like reference tools developed in any of the following areas (choose your own adventure style):

• Replicate existing introvirt C++-based reference tools in Python

• Develop a method to capture VM network traffic and tag it with host-based contextual data obtained through introvirt observations (e.g. - packet X came from pid Y, etc. etc.). Ideally this capture is viewable in Wireshark or equivalent (might require custom dissector).

• Expose a pluggable interface that allows activity or objects within VM to be accessed via introvirt and scanned or analyzed by a third-party tool (e.g. Clamav or Yara scans files via introvirt interfaces - either out-of-band or in real-time)

* * *

## #17 - Integrate a PLC CPU Emulator into Conpot

**Mentors:** Lukas Rist

**URL:** [https://github.com/mushorg/conpot](https://github.com/mushorg/conpot)

**Project type**: Improving an existing tool

**Skills required**: Python, programming PLCs (AWL, STL), network programming

Add support for a AWL/STL/PLC simulator. Goals is to run AWL/STL programs in Conpot and allow communication with the PLC emulator. Description: Conpot supports the protocols a common PLC is providing but not the functionality of a PLC. This means besides some randomized values and linear incrementing values like uptime the data in the honeypot is static. In order to appear more realistic and handle input values properly, we would like to support a PLC simulator. A good candidate is Awlsim (https://github.com/mbuesch/awlsim): Awlsim is a free Step 7 compatible AWL/STL Soft-PLC written in Python. Awlsim provides an interface for virtual hardware connection modules. This interface could be used to connect Awlsim to Conpot. Maybe we could add an I/O interface to it in order to retrieve and even inject data to a running simulation.
