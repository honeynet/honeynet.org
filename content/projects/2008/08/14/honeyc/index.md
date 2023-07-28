---
title: "HoneyC"
---

HoneyC is a low interaction client honeypot framework that allows to find malicious servers on a network. Instead of using a fully functional operating system and client to perform this task, HoneyC uses emulated clients that are able to solicit as much of a response from a server that is necessary for analysis of malicious content. Developed by Christian Seifert of the New Zealand Chapter.

 

## Overview

* * *

HoneyC is a low interaction client honeypot / honeyclient that allows to identify malicious servers on the web. Instead of using a fully functional operating system and client to perform this task (which is done by high interaction client honeypots, such as Honeymonkey or Honeyclient), HoneyC uses emulated clients that are able to solicit as much of a response from a server that is necessary for analysis of malicious content. HoneyC is expandable in a variety of ways: it can use different visitor clients, search schemes, and analysis algorithms.

For more information on the internals of HoneyC refer to section About HoneyC.

The initial HoneyC (version 1.0.x) concentrates on searching for malicious web servers based on Snort signatures. The initial version does not contain any malware signatures yet, but it is planned that those will appear shortly in the next version.

 

## About HoneyC

* * *

HoneyC is a low interaction client honeypot developed at Victoria University of Welligton by Christian Seifert. Before we describe HoneyC in detail, let us provide some background information around honeypots and client honeypots.

Honeypots, in general, are dedicated devices whose value lies in being probed, attacked, and compromised. Traditionally honeypots are server components that passively wait to be attacked. These honeypots allow to capture active attacks, such as worms. Client honeypots turn around this situation. Instead of passively awaiting to be attacked, client honeypots actively crawl the web to search for servers that exploit the client as part of the server response.

The idea of client honeypots was first articulated by Lance Spitzner in June 2004. A few client honeypots have been created since then, namely Honeymonkey (Microsoft), HoneyClient (available at www.honeyclient.org/trac), and of course Capture. These implementations crawl the web with a real browser (Internet Explorer) and perform analysis for exploit based on the state of the OS (such as monitoring changes to the file system, configuration, and process list) Since these implementations make use of real systems, they are classified as high interaction client honeypots. With HoneyC, we provide an implementation of a low interaction client honeypot. Such an low interaction implementation makes use of emulated clients (e.g. wget to emulate Internet Explorer) and analysis engine that might make use of an algorithm other than OS state inspection (e.g. signature matching).

[![](images/hcfigure1.png)](https://projects.honeynet.org/honeyc/attachment/wiki/AboutHoneyC/hcfigure1.png)

Figure 1 - HoneyC Component Diagram

HoneyC consists of three components as shown in Figure 1: Visitor, Queuer, and Analysis Engine. The Visitor is the component responsible to interact with the server. The Visitor usually makes a request to the server, consumes and processes the response. The Queuer is the component responsible to create a queue of servers for the Visitor to interact with. The Queuer can employ several algorithms to create the queue of servers (for example crawling, search engine integration). The Analysis Engine is the component responsible to evaluate whether security policy have been violated after the Visitor interacted with the server. Each of these components allows using pluggable modules to suit specific needs. This is achieved by loosely coupling the components via command redirection operator (pipes) and passing a serialized representation of the request and response objects via those pipes. This makes components implementation independent and interchangeable. For example, one could create a Queuer component that generates request objects via integration with a particular search engine API written in Ruby or one could also implement a Queuer component that crawls a network in C.

[![](images/hcfigure2.png)](https://projects.honeynet.org/honeyc/attachment/wiki/AboutHoneyC/hcfigure2.png)

Figure 2 - HoneyC System Use Cases

Figure 2 shows some of the system use cases that HoneyC fulfills. It has to fill a queue of servers for the visitor to interact with. After the interaction has taken place, the analysis engine has to determine whether the visit solicited an exploit from the server.

[![](images/hcfigure3.png)](https://projects.honeynet.org/honeyc/attachment/wiki/AboutHoneyC/hcfigure3.png)

Figure3 - End-User Use Cases

Figure 3 shows how an end user interacts with HoneyC.

From the basic start and force stop function (HoneyC stops automatically after the queue can not be filled anymore), the user should be able to configure HoneyC in the matter described above.

The user should be able to change and adjust the Visitor, Queuer, and Analysis Engine to meet the specific needs of the crawl. After a crawl has been completed, the user should be able to view a report that lists servers visited and which servers solicited a malicious response

 

## HoneyC FAQ

* * *

**Under what license is HoneyC written and distributed?**

The GNU General Public License.

**How do client honeypots differ from traditional honeypots?**

Traditional honeypots passively wait to be probed, attacked, and compromised. These honeypots allow to capture active attacks, such as worms. Client honeypots turn around this situation. Instead of passively awaiting to be attacked, client honeypots actively crawl the web to search for servers that exploit the client as part of the server response.

**What other open-source client honeypots exist?**

Honeyclient at :  [http://www.honeyclient.org/trac](http://www.honeyclient.org/trac) and Capture at :  [https://projects.honeynet.org/capture-hpc](https://projects.honeynet.org/capture-hpc)

**How does HoneyC differ from HoneyClient or Capture?**

HoneyClient and Capture crawl the web with a real browser (Internet Explorer) and performs the analysis for exploit based on the state of the OS. As such, they are classified as a high interaction client honeypot. HoneyC, on the other hand, uses emulated clients (e.g. wget to emulate Internet Explorer) and uses an analysis engine that might make use of an algorithm other than OS state inspection (e.g. signature matching). As such, HoneyC is classified as a low interaction client honeypot.

**What is the Visitor component?**

The Visitor is the component responsible to interact with the server. The visitor usually makes a request to the server, consumes and processes the response. With version 1.0.0, HoneyC contains a web browser visitor component that allows to visits web servers.

**What is the Queuer component?**

The Queuer is the component responsible to create a queue of servers for the visitor to interact with. The queuer can employ several algorithm to create the queue of servers, such as crawling, scanning, utilizing search engines, etc. With version 1.0.0, HoneyC contains a Yahoo search queuer that creates a list of servers by querying the Yahoo Search API. A simple list queuer was added in version 1.1.2, that allows to statically set a list of server request to be put into the queue.

**What is the Analysis Engine?**

The Analysis Engine is the component responsible to evaluate whether security policy have been violated after the Visitor interacted with the server. This can be done by inspecting the state of the environment, analyze the response based on signatures or heuristics, etc. With version 1.0.0, HoneyC contains a simple analysis engine that generates snort fast alerts based on snort signature matching against web server responses.

**When was the HoneyC project incepted?**

July 2006

 

## Releases

* * *

[HoneyC-1.3.0.zip](https://projects.honeynet.org/honeyc/attachment/wiki/Releases/HoneyC-1.3.0.zip)

md5: 0a97f23c9b12239a6f3b25fe747f4f23

**Release Notes 1.3.0**

- implemented flow\_bit evaluation (feature 1629168)
- performance optimizations
- added functionality to snort rules permutator (additional encoding schemes, ability to replace substrings in regex and dealing with nocase content fields)

HoneyC is written and distributed under the  [GNU General Public License](https://www.gnu.org/licenses/gpl.html).

### Attachments

- [HoneyC-1.3.0.zip](https://projects.honeynet.org/honeyc/attachment/wiki/Releases/HoneyC-1.3.0.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/honeyc/raw-attachment/wiki/Releases/HoneyC-1.3.0.zip "Download") (295.9 KB) - added by _cseifert_ [10 years](https://projects.honeynet.org/honeyc/timeline?from=2008-01-19T23%3A52%3A14Z&precision=second "2008-01-19T23:52:14Z in Timeline") ago.
