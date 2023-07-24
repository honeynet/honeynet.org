---
title: "Cuckoo Sandbox - Automated Malware Analysis"
date: "2011-02-05"
---

 

* * *

## ![](images/cuckoo-1-300x108.png)

## What is Cuckoo?

* * *

Cuckoo Sandbox is the **leading open source automated malware analysis system**.You can throw any suspicious file at it and in a matter of minutes Cuckoo will provide a detailed report outlining the behavior of the file when executed inside a realistic but isolated environment.

Malware is the swiss-army knife of cybercriminals and any other adversary to your corporation or organization.

In these evolving times, detecting and removing malware artifacts is not enough: it's vitally important to understand how they operate in order to understand the context, the motivations, and the goals of a breach.

Cuckoo Sandbox is free software that automated the task of analyzing any malicious file under **Windows**, **OS X**,**Linux**, and **Android**.

 

_Cuckoobox was originally developed as part of GSoc 2010 by Claudio Guarnieri and has been greatly enhanced in subsequent GSocs and Cuckoo development team. Current development of Cuckoo is available from [http://www.cuckoosandbox.org](http://www.cuckoosandbox.org)._

 

## What can it do?

* * *

Cuckoo Sandbox is an advanced, extremely modular, and 100% open source automated malware analysis system with infinite application opportunities. By default it is able to:

- Analyze many different malicious files (executables, office documents, pdf files, emails, etc) as well as malicious websites under Windows, Linux, Mac OS X, and Android virtualized environments.
- Trace API calls and general behavior of the file and distill this into high level information and signatures comprehensible by anyone.
- Dump and analyze network traffic, even when encrypted with SSL/TLS. With native network routing support to drop all traffic or route it through InetSIM, a network interface, or a VPN.
- Perform advanced memory analysis of the infected virtualized system through Volatility as well as on a process memory granularity using YARA.

Due to Cuckoo's open source nature and extensive modular design one may customize any aspect of the analysis environment, analysis results processing, and reporting stage. Cuckoo provides you all the requirements to easily integrate the sandbox into your existing framework and backend in the way you want, with the format you want, and all of that without licensing requirements.

Cuckoo is available from [http://www.cuckoosandbox.org](http://www.cuckoosandbox.org).
