---
title: "Capture-HPC"
date: "2008-08-14"
---

**Capture** is a high interaction [client honeypot](https://projects.honeynet.org/capture-hpc/wiki/client_honeypot) (also called [honeyclient](https://projects.honeynet.org/capture-hpc/wiki/honeyclient)). A client honeypot or [honeyclient](https://projects.honeynet.org/capture-hpc/wiki/honeyclient) is a security technology that allows one to find malicious servers on a network. Capture identifies malicious servers by interacting with potentially malicious servers using a dedicated virtual machine and observing its system state changes. If an system state change is detected, since no other activity occurs on the dedicated client machine, the server Capture interacted with is classified as malicious.

High level overview of Capture:

- Capture Server/Capture? Client architecture allows one to control numerous Capture clients on the localhost as well as remote hosts.
- Capture's monitors are able to observe the file system, registry, process of a system on a kernel level.
- Architecture allows Capture to drive various http aware client application. This includes a variety of browsers, but also various office applications and media players.
- Centralized logs keep track of which links have not been visited and which have, server classifications and state changes incurred by visiting malicious servers.
- Capture is able to automatically collect malware that might have been placed on a compromised client system as well as generated network traffic.
- Capture is flexible to run on a variety of virtual machine technology. The default installation runs on VMware Server 1.x; instructions to run Capture on VMware's hypervisor ESX and ESXi can be found here [ESX](https://projects.honeynet.org/capture-hpc/wiki/ESX) (thanks to Lasse Borup for those instructions). Emre Bastuz has posted instructions on how to compile Capture to work with VMware Server 2.x on his blog at  [http://www.emre.de/wiki/Capture-HPC](http://www.emre.de/wiki/Capture-HPC). Capture is flexible to be extended to function on additional virtual machine technology or even bare metal installations (Chiraag Aval is currently working on changing Capture to run on bare-metal hardware.)

We have set up a public mailing list for discuss issues around installation & operation, request support, voice feature requests, share your findings, etc. You can subscribe to it via  [https://public.honeynet.org/mailman/listinfo/capture-hpc](https://public.honeynet.org/mailman/listinfo/capture-hpc)

 

## About Capture Client Honeypot / Honeyclient

* * *

Capture is a high interaction client honeypot (or honeyclient) developed at Victoria University of Wellington by Ramon Steenson and Christian Seifert. Only a few high interaction client honeypot clients are available today. Capture differs from existing client honeypots in various ways. First, it is designed to be fast. State changes are being detected using an event based model allowing to react to state changes as they occur. Second, Capture is designed to be scalable. A central Capture server is able to control numerous clients across a network. Third, Capture is suppose to be a framework that allows to utilize different clients. The current version of Capture various HTTP aware clients, such as Firefox, Opera, Internet Explorer, Adobe Acrobat Reader, MS Office Applications, Open Office Applications and various media players.

 

## **Functionality**

* * *

In this section, we describe the existing functionality of Capture at a high level. Following, we provide a glimps into the future and describe our plans to extend Capture . Capture allows to find malicious servers on a network. Capture is split into two functional areas: a Capture Server and Capture Client. The primary purpose of the Capture Server is to control numerous Capture clients to interact with web servers. It allows to start and stop clients, instruct clients to interact with a web server retrieving a specified URI, and aggregating the classifications of the Capture clients regards the web server they have interacted with. The server provides this functionality in a scripting fashion. The Capture clients actually perform the work. They accept the commands of the server to start and stop themselves and to visit a web server. As a Capture client interacts with a web server, it monitors its state for changes on the file system, registry, and processes that are running. Since some events occur during normal operation (e.g. writing files to the web browser cache), exclusion lists allow to ignore certain type of events. If changes are detected that are not part of the exclusion list, the client makes a malicious classification of the web server and sends this information to the Capture server. Since the state of the Capture client has been changed, the Capture client resets its state to a clean state before it retrieves new instructions from the Capture server. In case no state changes are detected, the Capture client retrieves new instructions from the Capture server without resetting its state. Capture allows to automatically collect network dumps and downloaded files (ie malware) when a malicious server is encountered.

 

## **Technical Description**

* * *

The Capture server is a simple TCPIP server that manages several capture clients and the VMware servers that host the guest OS that run the Capture clients. The Capture server takes each URL it receives and distributes them to the available clients in a round robin fashion. The server listens for client that connect to the server upon startup on a specified TCP port. The Capture server is written in Java and controls the VMware servers using the VMware C API that it wraps using jni. The communication protocol between the Capture Server and Capture Client is XML based and described in [Capture Communication Protocol.pdf](https://projects.honeynet.org/capture-hpc/attachment/wiki/AboutCapture/Capture%20Communication%20Protocol.pdf).

The Capture client in turn consists of two components, a set of kernel drivers and a user space process. The kernel drivers operate in kernel space and use event-based detection mechanisms for monitoring the system's state changes. The user space process, which accepts visitation requests from the Capture server, drives the client to interact with the server and communicates the state changes back to the server via a simple TCPIP connection. The user space process captures the state changes from the kernel drivers and filters the events based on the exclusion lists. Each component is written in unmanaged C code.

 

## **Kernel Drivers**

* * *

The Capture client uses kernel drivers to monitor the system by using the existing kernel callback mechanism of the kernel that notifies registered drivers when a certain event happens. These callbacks invoke functions inside of a kernel driver and pass the actual event information so that it can either be modified or, in Capture's case, monitored. The following callback functions are registered by Capture:

- CmRegistryCallback
- PsSetCreateProcessNotifyRoutine
- FilterLoad, FltRegisterFilter

When events are received inside the Capture kernel drivers, they are queued waiting to be sent to the user space component of the tool. This is accomplished by passing a user allocated buffer from user space into kernel space where the kernel drivers then copy information into that buffer, so the application can process it in user space. User Space Process

The user space process is an application that resides in user space. It is the entry point of the Capture application. It is responsible to load the drivers, process the events received by the drivers and output the events to the report.

As mentioned above, the user space application, once it has loaded the drivers, creates a buffer and passes it from user space to the kernel drivers. Passing of the buffer occurs via the Win32 API and the IO Manager. The kernel drivers copy the event data into the buffer, so the user level application can process the events. Each event is serialized and compared against the entries in the exclusion list. The exclusion lists are built using regular expressions, which means event exclusions can be grouped into one line. This functionality is provided by the Boost::regex library. For each monitor, an exclusion list is parsed and internally mapped between event types and allowed regular expressions are created. If a received event is included in the list, the event is dropped; otherwise, it is output to the final report that Capture BAT generates.

 

## **Academic References**

* * *

Below, you will find several papers that have utilized Capture-HPC in one form or the other:

1\. M. Egele, P. Wurzinger, C. Kruegel, and E. Kirda, "Defending Browsers against Drive-by Downloads: Mitigating Heap-spraying Code Injection Attacks," Secure Systems Lab, 2009, p. Available from  [http://www.iseclab.org/papers/driveby.pdf](http://www.iseclab.org/papers/driveby.pdf); accessed on 15 May 2009.

2\. C. Seifert, V. Delwadia, P. Komisarczuk, D. Stirling, and I. Welch, "Measurement Study on Malicious Web Servers in the .nz Domain," in 14th Australasian Conference on Information Security and Privacy (ACISP), Brisbane, 2009.

3\. C. Seifert, P. Komisarczuk, and I. Welch, "Application of divide-and-conquer algorithm paradigm to improve the detection speed of high interaction client honeypots," in 23rd Annual ACM Symposium on Applied Computing Ceara, Brazil, 2008.

4\. C. Seifert, P. Komisarczuk, and I. Welch, "Identification of Malicious Web Pages with Static Heuristics," in Austalasian Telecommunication Networks and Applications Conference, Adelaide, 2008.

5\. C. Seifert, I. Welch, P. Komisarczuk, C. Aval, and B. Endicott-Popovsky, "Identification of Malicious Web Pages Through Analysis of Underlying DNS and Web Server Relationships," in 3rd IEEE Conference on Local Computer Networks, Montreal, 2008.

6\. C. Seifert, R. Steenson, T. Holz, Y. Bing, and M. A. Davis, "Know Your Enemy: Malicious Web Servers," The Honeynet Project, 2007, p. Available from  [https://www.honeynet.org/papers/mws/](https://www.honeynet.org/papers/mws/); accessed on 25 September 2007.

7\. M. Xie, Z. Wu, and H. Wang, "HoneyIM: Fast Detection and Suppression of Instant Messaging Malware in Enterprise-Like Networks," in Computer Security Applications Conference, Miami Beach, 2007, pp. 64-73.

When citing Capture-HPC, please use the following bibtex:

@misc{

> Author = {Seifert, Christian and Steenson, Ramon},

> Title = {Capture - Honeypot Client (Capture-HPC)},

> Publisher = {Victoria University of Wellington, NZ},

> Pages = {Available from [https://projects.honeynet.org/capture-hpc](https://projects.honeynet.org/capture-hpc); accessed on 22 September 2008},

> Year = [{2006}](https://projects.honeynet.org/capture-hpc/report/2006)

}

 

 

## Capture FAQ

* * *

**Where can I get additional help?**

There is troubleshooting guide located on the Capture release page, which contains solutions to common problems encountered.

In addition, we have set up a public mailing list for discuss issues around installation & operation, request support, voice feature requests, share your findings, etc. You can subscribe to it via  [https://public.honeynet.org/mailman/listinfo/capture-hpc](https://public.honeynet.org/mailman/listinfo/capture-hpc)

**Is there any additional documentation provided with Capture?**

Yes, Readme files that come with the Capture distribution contain a wealth of information on how to install, configure and run Capture.

**What clients are currently supported with Capture?**

Any http protocol clients that allow to specify a URL on the command line (e.g. iexplore  [https://www.honeynet.org](https://www.honeynet.org/)) are supported by Capture-HPC. This includes Opera, Internet Explorer, Firefox and various Office Application.

**Where can I find additional exl other than the default provided with the distribution?**

Check the mailing list for additional exclusion lists. If you don't find any there and end up creating one, please share it on the mailing list for others to benefit from it.

**What other implementations of client honeypots exist?**

Besides Capture there are a few other high interaction client honeypots:

- [MITRE's HoneyClient](http://www.honeyclient.org/trac)
- [WebExploitFinder](http://www.xnos.org/security/overview.html)

But there are several low interaction client honeypots:

- [MonkeySpider](http://monkeyspider.sourceforge.net/about.html)
- [HoneyC](https://projects.honeynet.org/honeyc)
- [PhoneyC](http://svn.mwcollect.org/log/phoneyc)
- [SpyBye](http://spybye.org/)

There are several other, like the spycrawler from the UW and Honeymonkey from MSFT, but those are not publicly available.

**What's up with the client honeypot and honeyclient term?**

[Honeyclient](https://projects.honeynet.org/capture-hpc/wiki/honeyclient) and [client honeypot](https://projects.honeynet.org/capture-hpc/wiki/client_honeypot) are synonyms. They are generic terms that describe the concept. However, there is a subtlety here, as "honeyclient" is actually a homograph that could also refer to the first open source client honeypot implementation:  [MITRE's HoneyClient](http://www.honeyclient.org/trac).

**What other resources are out there to learn about and keep up to date about client-side attacks?**

There are several excellent blogs from security researchers and corporations. A few we read regularly are listed below:

- [WebSense Blog](https://securitylabs.websense.com/content/blogs.aspx)
- [Dancho Danchev's Blog](https://ddanchev.blogspot.com/)
- [Google's Online Security Blog](https://googleonlinesecurity.blogspot.com/)
- [Stopbadware.org Blog](http://blogs.stopbadware.org/)
- ... and many more ...

**Under what license is Capture-HPC written and distributed?**

The GNU General Public License, v2.

**We would like to thank the following individuals for their support, feedback, and discussions on the Capture-HPC tool:**

Bing Yuan, David Stirling, David Watson, Devinder Singh, Ian Welch, Jamie Riden, Lance Spitzner, Michael A Davis, Mike Johnson, Ralph Logan, Peter Komisarzcuk, Steve Mumford, Thorsten Holz, Xeno Kovah, Lasse Borup, Josh Smith, Armin Garcia

 

* * *

## Latest Release

**_NOTE: This version contains precompiled binaries (for Fedora linux and Windows) for VMWare Server 1.0.7. You can download additional versions from [RevertBinaries](https://projects.honeynet.org/capture-hpc/wiki/RevertBinaries). Alternatively, you can also compile the binaries yourself. Please refer to the compile readme file that comes with the capture server._**

[capture-client-2.5.1-389.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.5.1-389.zip)

md5: 4606de44b893e91ef134761f2a686e12

The source can be obtained through the following command: svn co  [https://projects.honeynet.org/svn/capture-hpc/capture-hpc/tags/2.5/capture-client](https://projects.honeynet.org/svn/capture-hpc/capture-hpc/tags/2.5/capture-client). (You need to register on this site to obtain credentials)

[capture-server-2.5.1-389-withLinuxRevert.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.5.1-389-withLinuxRevert.zip)

md5: a363d57be21033b7c65e6af89deb3733

The source can be obtained through the following command: svn co  [https://projects.honeynet.org/svn/capture-hpc/capture-hpc/tags/2.5/capture-server](https://projects.honeynet.org/svn/capture-hpc/capture-hpc/tags/2.5/capture-server). (You need to register on this site to obtain credentials)

[TroubleshootingGuide](https://projects.honeynet.org/capture-hpc/wiki/TroubleshootingGuide)

## Beta Release

**_NOTE: This version contains precompiled binaries (for Windows) for VMWare Server 1.0.9. You can download additional versions from [RevertBinaries](https://projects.honeynet.org/capture-hpc/wiki/RevertBinaries). Alternatively, you can also compile the binaries yourself. Please refer to the compile readme file that comes with the capture server._**

[CaptureClient-Setup-3.0.0.exe](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/CaptureClient-Setup-3.0.0.exe)

md5: e1db92a7b4f93c6d53956ca39b85e931

The source can be obtained through the following command: svn co  [https://projects.honeynet.org/svn/capture-hpc/capture-hpc/tags/3.0.0/capture-client](https://projects.honeynet.org/svn/capture-hpc/capture-hpc/tags/3.0.0/capture-client). (You need to register on this site to obtain credentials)

[CaptureServer-Release-3.0.0.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/CaptureServer-Release-3.0.0.zip)

md5: d0f79100b2907b1fbdb7105b21140cc3

The source can be obtained through the following command: svn co  [https://projects.honeynet.org/svn/capture-hpc/capture-hpc/branches/3.0.1/capture-server](https://projects.honeynet.org/svn/capture-hpc/capture-hpc/branches/3.0.1/capture-server) (You need to register on this site to obtain credentials)

[CaptureServer-PcapPostprocessor-Release-3.0.0.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/CaptureServer-PcapPostprocessor-Release-3.0.0.zip)

md5: e7239da70ea510a2a3d11ae48ac37df0

The source can be obtained through the following command: svn co  [https://projects.honeynet.org/svn/capture-hpc/capture-hpc/branches/3.0.1/capture-server-postprocessors](https://projects.honeynet.org/svn/capture-hpc/capture-hpc/branches/3.0.1/capture-server-postprocessors) (You need to register on this site to obtain credentials)

**Release Notes 3.0.0 Beta - 441**

- added connection monitor that can alert on connection/listening events on the network. This could be used to identify attacks that merely reside in memory.
- added support for a backend mysql or postgress database
- added post processor plugin architecture. Postprocessors allow to perform actions on classified URLs.
- added a post processor that analyzes the network data of a classified URL. It extracts DNS information, HTTP requests and determines whether any domain name is part of a fast flux network. Note that this post processor only works with a group size of 1. Otherwise the network of the entire group is analyzed.

**Release Notes 2.5.1 - 389**

- fixed bug 741 (389)

**Release Notes 2.5.1 - 384**

- added missing \\n for each line in http log file (384)
- fixed issue that didnt capture network dumps properly (384)
- fixed bug that didnt handle circumstance when revert gets stuck. this leads to infinite ping/pongs. (383)

**Release Notes 2.5.1 - Gold**

- added preprocessor plugin architecture. Preprocessor plugins allow to handle the input urls before they are passed onto capture. For instance, this could be used to create a crawler or filtering plugin.
- added processor ids for state changes (this value is only set if the client plug-in supports this). This allows the client plug-in to determine what URL the attack originates even if multiple URLs are visited at once.
- Added internetexplorerbulk plug-in that takes advantage of the processor id functionality. Allows to run multiple URLs without the need to revisit the URLs. A mapping of the state changes to the process id will determine which URL was malicious.
- modified client plug-in to communicate the algorithm it is able to support (Divide-and-conquer, bulk, sequential)
- upgraded vmware server to 1.0.6, java 6 update 7, NSIS 2.38, boost 1.35.0, visual studio 2008 (requires new VC++ Redist Libraries!)
- removed timeout factor and added absolute timeout/delay config values (see documentation for description of each option)
- modified tailing of input file; if no more URLs after a specific timeout are detected, the capture server can configured to terminate or keep tailing the input file for new URLs.
- implemented staggering revert of virtual machines. If server is configured with multiple VMs, they are not all reverted at the same time.
- changed threading structure to be more stable (leads to less client inactivity errors)
- changed IE plugin to close all IE windows (fixes pop ups hanging around)
- optimized handling of zipping of files - leads to speedup if network capture is not enabled
- fixed bug 718,729,709

_Known Issues_

- 737 capture client crashes when installing a program (lots of events).
- 736 When IE instance locks up, close method fails leading to a VM stalled error. (but those failures are now retried once)
- 735 When Capture-Client crashes, it will lead to a client inactivity errors. (but those failures are now retried once)
- 734 Terminate process is not recorded
- 615 Registry monitoring can't handle a key named
- 690 Capture is not able to detect file renames
- 676 Empty password on the user of the guest vm in the config.xml causes the capture server to crash (Windows only).
- 706 Capture seems to ignore the VM server port.
- 719 Closing a browser during visitation does not cause this event to be reported back to the server
- 721 filedownloader writes to const file name preventing dac algorithm to be applied for applications that make use of this feature

**Release Notes 2.1.0**

- Implemented divide & conquer algorithm that allows to visit URLs faster (685)
- Added Safari plugin (693) (Note that the safari plug in does not support the divide & conquer algorithm.)
- Network traffic collection can now be configured to occur on malicious as well as benign URLs. Previously, only network traffic on malicious URLs was pushed to the server. (707)
- Added stats log to for tuning capture and troubleshooting issues.
- Adjusted error handling. Now errors are only logged in the error.log file. The operator needs to decide on how to handle these errors.
- Redirect client output to log file for debugging purposes.
- Added option -r to server parameters that can instruct the server to exit upon encountering an error (turn on by setting "-r true"). For debugging purposes.
- A malicious classification is now reported even if the client machine crashes (e.g. drive by download causes blue screen).
- Logs that capture state changes are now only created if state changes are detected.
- The process,malicious,safe and eror log format now includes a new column that is related to the divide & conquer functionality . It shows the group ID number.
- Because of the new features, the config file format has changed.

> > \*\* the client-path attribute now points to a bat file

> > \*\* global options changed and some were added

- removed jni usage for revert and replaced with a stand alone C prg for stability reasons
- fixed bug 696, 655, 657, 613, 689, 711

**Release Notes 2.01**

- fixed bug 699, 666, 673
- increased some timeouts on the server that trigger upon the client connecting to the server. Should allow to use more client instances with one server.
- compiled vix libs are compatible with vmware server 1.0.4

**Release Notes 2.0**

- support for any client application that is http protocol aware (for example, Microsoft Excel)
- ability to automatically collect downloaded malware
- ability to automatically collect network traffic on the client
- ability to push exclusion lists from the Capture Server to the Capture Client
- improved control of Internet Explorer: obtain html error codes; specify visitation delay AFTER page has been retrieved; retry visitation of URLs in case of time outs or network errors
- support for plug-in architecture, that allows to create fine grained control of clients (for example, as provided for Internet Explorer), but also allows for integration of client applications that require complex interactions to retrieve content from the web (e.g. Safari is such an application. It doesn’t allow retrieval of web content by passing the URL as a parameter)
- enhancement to file monitor to monitor file deletions
- communication between Capture Client and Server has been converted to XML. This allows one to easily write custom Capture Servers that utilize the existing Capture Client.
- added installer/uninstaller for the Capture Client
- improved reporting
- improved stability
- improved performance
- numerous bug fixes

**Release Notes 1.1**

- enhancements in stability & speed
- java implementation of server component
- multi-browser support
- fix in exclusion list minus notation
- compatibility with Microsoft Vista

**Release Notes 1.0**

- addition of registry monitor
- reimplementation of monitors as kernel drivers utilizing kernel callbacks

Capture is written and distributed under the GNU General Public License.

### Attachments

- [capture-client-2.0.0-5601.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.0.0-5601.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-client-2.0.0-5601.zip "Download") (458.8 KB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-01-19T23%3A15%3A18Z&precision=second "2008-01-19T23:15:18Z in Timeline") ago.
- [capture-client-2.0.0-5601-src.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.0.0-5601-src.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-client-2.0.0-5601-src.zip "Download") (430.5 KB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-02-14T21%3A24%3A20Z&precision=second "2008-02-14T21:24:20Z in Timeline") ago.
- [capture-server-2.0.0-5601.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.0.0-5601.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.0.0-5601.zip "Download") (1.3 MB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-02-14T21%3A25%3A16Z&precision=second "2008-02-14T21:25:16Z in Timeline") ago.
- [capture-server-2.0.0-5601-src.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.0.0-5601-src.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.0.0-5601-src.zip "Download") (194.8 KB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-02-14T21%3A25%3A52Z&precision=second "2008-02-14T21:25:52Z in Timeline") ago.
- [capture-client-2.0.1-261.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.0.1-261.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-client-2.0.1-261.zip "Download") (459.5 KB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-02-21T00%3A20%3A31Z&precision=second "2008-02-21T00:20:31Z in Timeline") ago.
- [capture-client-2.0.1-261-src.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.0.1-261-src.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-client-2.0.1-261-src.zip "Download") (0.9 MB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-02-21T00%3A21%3A33Z&precision=second "2008-02-21T00:21:33Z in Timeline") ago.
- [capture-server-2.0.1-261.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.0.1-261.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.0.1-261.zip "Download") (1.3 MB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-02-21T00%3A22%3A17Z&precision=second "2008-02-21T00:22:17Z in Timeline") ago.
- [capture-server-2.0.1-261-src.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.0.1-261-src.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.0.1-261-src.zip "Download") (194.7 KB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-02-21T00%3A22%3A35Z&precision=second "2008-02-21T00:22:35Z in Timeline") ago.
- [capture-client-2.1.0-300.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.1.0-300.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-client-2.1.0-300.zip "Download") (465.4 KB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-03-26T18%3A25%3A00Z&precision=second "2008-03-26T18:25:00Z in Timeline") ago.
- [capture-client-2.1.0-300-src.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.1.0-300-src.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-client-2.1.0-300-src.zip "Download") (441.3 KB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-03-26T18%3A25%3A37Z&precision=second "2008-03-26T18:25:37Z in Timeline") ago.
- [capture-server-2.1.0-300.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.1.0-300.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.1.0-300.zip "Download") (1.2 MB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-03-26T18%3A26%3A28Z&precision=second "2008-03-26T18:26:28Z in Timeline") ago.
- [capture-server-2.1.0-300-src.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.1.0-300-src.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.1.0-300-src.zip "Download") (202.4 KB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-03-26T18%3A27%3A07Z&precision=second "2008-03-26T18:27:07Z in Timeline") ago.
- [capture-client-2.5.0-381.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.5.0-381.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-client-2.5.0-381.zip "Download") (1.9 MB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-08-28T14%3A55%3A39Z&precision=second "2008-08-28T14:55:39Z in Timeline") ago.
- [capture-server-2.5.0-381.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.5.0-381.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.5.0-381.zip "Download") (1.5 MB) - added by _cseifert_ [10 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-08-28T14%3A57%3A08Z&precision=second "2008-08-28T14:57:08Z in Timeline") ago.
- [capture-client-2.5.1-383.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.5.1-383.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-client-2.5.1-383.zip "Download") (1.9 MB) - added by _cseifert_ [9 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-08-29T15%3A46%3A49Z&precision=second "2008-08-29T15:46:49Z in Timeline") ago.
- [capture-server-2.5.1-383.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.5.1-383.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.5.1-383.zip "Download") (1.5 MB) - added by _cseifert_ [9 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-08-29T15%3A50%3A50Z&precision=second "2008-08-29T15:50:50Z in Timeline") ago.
- [capture-server-2.5.1-384.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.5.1-384.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.5.1-384.zip "Download") (1.5 MB) - added by _cseifert_ [9 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-09-03T18%3A37%3A52Z&precision=second "2008-09-03T18:37:52Z in Timeline") ago.
- [capture-client-2.5.1-384.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.5.1-384.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-client-2.5.1-384.zip "Download") (1.9 MB) - added by _cseifert_ [9 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-09-03T18%3A39%3A40Z&precision=second "2008-09-03T18:39:40Z in Timeline") ago.
- [capture-client-2.5.1-389.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-client-2.5.1-389.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-client-2.5.1-389.zip "Download") (1.9 MB) - added by _cseifert_ [9 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-10-07T14%3A30%3A51Z&precision=second "2008-10-07T14:30:51Z in Timeline") ago.
- [capture-server-2.5.1-389.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.5.1-389.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.5.1-389.zip "Download") (1.4 MB) - added by _cseifert_ [9 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-10-07T14%3A31%3A36Z&precision=second "2008-10-07T14:31:36Z in Timeline") ago.
- [capture-server-2.5.1-389-withLinuxRevert.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/capture-server-2.5.1-389-withLinuxRevert.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/capture-server-2.5.1-389-withLinuxRevert.zip "Download") (281.2 KB) - added by _cseifert_ [9 years](https://projects.honeynet.org/capture-hpc/timeline?from=2008-10-18T19%3A20%3A19Z&precision=second "2008-10-18T19:20:19Z in Timeline") ago.
- [CaptureServer-PcapPostprocessor-Release-3.0.0.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/CaptureServer-PcapPostprocessor-Release-3.0.0.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/CaptureServer-PcapPostprocessor-Release-3.0.0.zip "Download") (426.4 KB) - added by _cseifert_ [8 years](https://projects.honeynet.org/capture-hpc/timeline?from=2009-11-01T19%3A49%3A49Z&precision=second "2009-11-01T19:49:49Z in Timeline") ago. e7239da70ea510a2a3d11ae48ac37df0 captureserver-pcappostprocessor-release-3.0.0.zip
- [CaptureServer-Release-3.0.0.zip](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/CaptureServer-Release-3.0.0.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/CaptureServer-Release-3.0.0.zip "Download") (2.8 MB) - added by _cseifert_ [8 years](https://projects.honeynet.org/capture-hpc/timeline?from=2009-11-01T19%3A52%3A18Z&precision=second "2009-11-01T19:52:18Z in Timeline") ago. d0f79100b2907b1fbdb7105b21140cc3 captureserver-release-3.0.0.zip
- [CaptureClient-Setup-3.0.0.exe](https://projects.honeynet.org/capture-hpc/attachment/wiki/Releases/CaptureClient-Setup-3.0.0.exe "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/capture-hpc/raw-attachment/wiki/Releases/CaptureClient-Setup-3.0.0.exe "Download") (1.9 MB) - added by _cseifert_ [8 years](https://projects.honeynet.org/capture-hpc/timeline?from=2009-11-01T19%3A55%3A07Z&precision=second "2009-11-01T19:55:07Z in Timeline") ago. e1db92a7b4f93c6d53956ca39b85e931 captureclient-setup-3.0.0.exe
