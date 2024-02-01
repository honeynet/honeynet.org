---
title: "Improving the RioTPot hybrid interaction honeypot"
date: "2024-02-01"
project_url: "https://github.com/honeynet/riotpot"
hours: "small, medium, and large projects are possible."
mentor: "Emmanouil Vasilomanolakis"
project_type: "Improving an existing tool"
---

RIoTPot is a hybrid interaction honeypot, primarily focused on the emulation IoT and OT protocols, although, it is also capable of emulating other services. In essence, RIoTPot acts as a proxy service for other honeypots included in the system. Therefore, you can run any honeypot and other services alongside RIoTPot. In addition, there is an UI web-application that you can use to manage your routing. Moreover, RIoTPot comes with multiple low-interaction services ready to use. Since these services are written as plugins, they are only supported on Linux; however, you can start RIoTPot without them. The following table contains the list of services included in RIoTPot by default, their internal port, and proxy port.

The project aims at providing RioTPot with the ability to run in a light mode that requires minimum user interaction and minimize existing external library utilization. Furthermore, we will improve the support for existing profiles and protocols.