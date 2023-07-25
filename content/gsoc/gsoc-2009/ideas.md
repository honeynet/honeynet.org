---
title: "Google Summer of Code 2009 Project Ideas"
date: "2009-08-28"
url: "/gsoc/gsoc-2009/google-summer-of-code-2009-project-ideas"
---


_Please note that GSoC 2009 has now successfully completed. This content is being retained for reference only._

# **Project Ideas**

Below is an overview of a number of current projects ideas that we are keen to develop during 2009. We are also always interested in hearing any ideas for additional relevant honeynet-related R&D projects (although remember to qualify for receiving GSoC funding it needs to fit in to Google's 3-month project timescales!). If you have a suitable project and we have the right resources to mentor it, we'd also be happy to support you.

Each sponsored project will have one or more mentors available to provide a guaranteed contact point plus one or more technical advisors to help applicants with the technical direction and delivery of the project (often the original author of the tool or its current maintainer, and usually someone recognised as an international expert in their particular field). Our Google Summer of Code administrator Lance Spitzner will also be available to all sponsored GSoC students for general advice and logistical support.   For all questions about the Honeynet Project, the GSoC program or our projects, please contact us at project@honeynet.org.  To learn more about the Google Summer of Code event, see the [GSoC Website.](https://socghop.appspot.com/)

##   

# **Project 1 - Improving our low interaction client honeypot (PHoneyC)**

Attacks against Internet users are increasingly delivered through web browsers via client side exploits. Browser scripts have become a major client-side exploit delivery mechanism, with drive-by download attacks using obfuscated Javascript becoming the dominant form. Client honeypots have been developed to access potentially malicious web content and attempt to determine whether the content returned is malicious or not. Low-interaction client honeypots have the advantages of higher-performance, greater scalability and lower resource consumption than high-interaction client honeypot, and are used in many Internet initiatives such as the Google Safe-Browsing Project. However, to achieve higher detection rates, low-interaction client honeypots must develop effective deobfuscation mechanisms to deal with obfuscated Javscript.

Honeynet Project members have been working on a low interaction, emulated client honeypot called PHoneyC ([http://code.google.com/p/phoneyc/](https://code.google.com/p/phoneyc/)) that attempts to detect malicious content in the wild in a number of ways. It is designed to be faster and more scalable than traditional high interaction client honeypots (you can find the latest draft of Jose's LEET 09 paper [here](https://code.google.com/p/phoneyc/source/browse/phoneyc/trunk/doc/papers/leet09/phoneyc.pdf) for background reading). In addition, members have been working on a stand-alone proof of concept called Pyprofjsploit ([http://code.mwcollect.org/projects/show/pyprofjsploit](http://code.mwcollect.org/projects/show/pyprofjsploit)) to detect malicious shellcode within javascript byte code using the LibEmu generic x86 emulator for shellcode detection ([http://libemu.carnivore.it](http://libemu.carnivore.it/)), which is now basically complete.

The initial goal of this project is to integrate the Pyprofjsploit proof of concept into phoneyc and then complete a number of missing PHoneyC features and improvements before formally releasing it publicly. Depending on the number of volunteers available, there are some additional features that we would like to also pursue:

### Deobfuscation Mechanisms by combining DOM Simulation and Javascript Engine

Currently PhoneyC uses Mozilla’s SpiderMonkey as the Javascript engine to interpret the obfuscated Javascript which is commonly used by the client-side exploits. However, this approach lacks a carefully designed and coded DOM simulation module. Without a complete simulated DOM, the Javascript engine fails to interpret a majority of in-the-wild Javascript and cannot detect the malicious exploits delivery by them. To improve the detection capability of PHoneyC, the first idea is to develop more reliable and effective deobfuscation mechanisms by combining DOM simulation and the Javascript engine.

### Client-side vulnerability analysis, signature generation and detection

Analyze the detailed internals of new client-side vulnerabilities, generate predicate signatures that reflect the essentials of these vulnerabilities for detection, and improve current honeyclient simulation and exploit detection mechanisms.

### Client-side exploit analysis to support collection of downloads

Develop a client-side exploit analysis mechanism, to extract the URLs of downloaded malware from malicious exploit Javascript, and then automatically collect any malware samples as well as the detected client-side exploits. We feel that this project is important to the community because many people will benefit from faster, more reliable ways of automatically detecting malicious websites. The project also provides some interesting technical challenges and has scope for successful applicants to extend this approach with their own ideas.

**Skills required:  
**  
C programming, Python programming, good understanding of Javascript and the DOM model

**Mentors:** Georg Wicherski (DE) and Jose Nazario (US)

##   

# **Project 2 - Improving the effectiveness of low interaction honeypots (Nepenthes/HoneyTrap/LibEmu)**

Honeynet Project members have developed a number of solutions for emulating vulnerable computer systems and automatically collecting attacks against them. Honeypots such as Nepenthes and HoneyTrap have proven to be successful at capturing known attacks, but have generally proved difficult to extend and add signatures to for newly discovered vulnerabilities. They have also struggled to reliably detect and capture previously unknown, zero day exploits. Shellcode emulation in LibEmu has helped, but integration with existing honeypots has been demanding.

We are currently working on a new low-interaction server honeypot which builds on the lessons learned to date. This will include detection of unknown attacks via LibEmu and better updatability and scalability. The goal of this project is to advance this next generation low interaction server honeypot to the working prototype stage. We believe that this project is important because existing low interaction honeypots are used by a wide range of researchers and organisations to study internet attacks, so increasing attack detection rates will potentially benefit many people with interests in this area.

**Skills required:  
**  
C programming, Python programming, understanding Windows x86 shellcode.  
Previous experience with Nepenthes, HoneyTrap and LibEmu would be very useful

**Mentor:** Paul Baecher (DE)

**Technical Advisors:** Georg Wicherski (DE)

##   

# **Project 3 - Improving our high interaction client honeypots (Capture-HPC and CaptureBAT)**

Capture-HPC is one of our most actively developed public projects. Capture-HPC provides a method of driving a real high interaction windows system running within a virtual machine to potentially malicious websites, obtained from sources such as spam or DNS typosquatting. State changes to the VM are monitored and malicious activity is detected by measuring unexpected changes. It is regularly used in surveys of malicious websites and has been extended to support a number of Internet enabled applications and file formats. CaptureBAT is the original behavioural analysis tool that Capture-HPC is based on, using Windows API hooking to monitor state.

The goal of this project would be to continue the current planned development of Capture-HPC and CaptureBAT, in the areas of improving data logging and operational management, adding network API hooking, improving stateful operations (pause, failover, etc) and moving result data storage from flat file to a suitable database solution. We also seek input for the future development roadmap of Capture-HPC v3, for which we currently plan to add:

- GenericExclusionLists - Define a generic exclusion list that can contain an arbitary amount of access regular expressions per object
- ErrorHandling - Define a specification for error messages on the client and how the server should react to them
- KernelEventMap - A generic kernel based event map that can dynamically handle different event structures
- BootStrapClient - A base client that connects to the server and downloads the full client, plugins etc
- WindowMonitor - Monitor windows creation and deletion on a system
- WindowAI - Framework for detecting new windows are opened and how to deal with them
- PythonVisitationPlugin - A visitation plugin where people can write there own python scripts that deal with the visitation process
- XenoRegistryIntegration - Integrate registry work from Xeno
- FileMonitorEvents - Expand the already existing feature to bring it more in line with filemon

We believe that continuing to improve Capture-HPC will encourage more automated analysis of malicious websites, helping to detect new generations of client focused attacks and further improve web browser security for Internet users.

**Skills required:**

C programming, Java programming, familiarity with Windows and Internet Explorer internals

**Mentor:** Peter Komisarczuk (NZ) and Ian Welch (NZ)

##   

# **Project 4 - Developing a solution for managing client honeypots (New)**

Honeynet Project members have developed a number of leading open source client honeypot solutions for analysing potentially malicious web sites. However, these tools are generally stand alone in nature and do not provide a number of features necessary for large scale, long running analysis excercises such as crawling the top N web sites from Google in a particular category each each day and reporting activity trends. The current tool construction also does not encourage centralised submission of suspect URLs and web based reporting.

The goal of this project would be to implement a web based management layer for registering existing instances of client honeypots, submitting URLs for analysis, scheduling analysis runs, persisting results data, summarising trends and presenting the results to to multiple users. Prototype user stories, designs, etc are available, as is access to client honeypot data, but we would welcome additional input on the best means of managing client honeypot workflow and presenting this information through a web interface.

**Skills required:  
**  
Web development skills in appropriate technologies

**Mentor:**  Peter Komisarczuk (NZ), Ian Welch (NZ) and David Watson (UK)

# **Project 5 - Improvements to high interaction honeypot data capture systems (Sebek and Virtual Machine Introspection)**

Sebek is the de-facto open source honeypot monitoring tool and was developed and released by The Honeynet Project. Sebek is a kernel module that is installed on high-interaction honeypots for the purpose of collecting I/O activity. Sebek allows administrators to collect attackers' activities, such as keystrokes and API calls on the system. However, currently Sebek has a number of problems, which include: operational instability, lack of invisibility, potential for detection by correlation with network activities and lack of regular maintenance and development on some platforms. Collectively this means that today Sebek does not satisfy all the requirements for stealthy and stable high interaction honeypot monitoring, especially for the win32 high-interaction honeypots.

### Ideas List

While you can submit a proposal for whatever cool idea you would like to improve our current high interaction data collection capabilities, here are a few suggestions that would be extremely helpful to the Sebek project and its users. Basically, they fall into two categories: improvement of the current kernel rootkit based approach and development of a new virtualization based approach. These suggested ideas are in no particular order.

### Sebek Win32 Version - Improve Stability, Stealth, and Data Correlation

Sebek currently lacks regular maintenance. The Sebek development team has been relatively inactive after the release of Honeywall GenIII version in 2006, only really patching bugs rather than developing new features. For the Win32 client on recent OS releases, the situation is even worse - it is unstable, which badly limits its practical deployment and usage. We would like some developers with experience of kernel driver development and testing to help us with a concerted drive this Summer to find any remaining lurking bugs and fix them. We also hope developers could make Sebek Win32 client support modern Windows OS better, such as XP and Vista, which should be an interesting technical challenge.

Sebek's stealth could definitely be improved. It can currently be detected, subverted and disabled by a determined attacker. Tan Chew Keong has presented several techniques to detect the existence of Sebek Win32 client. We need some experienced kernel driver developers to help us improve the stealth of Sebek client by replacing the old fashioned rootkit mechanism with one of the more powerful techniques that have evolved in the last few years. We have a number of candidate ideas and prototypes, so we hope to be able to improve the difficulty of detecting or subverting the Sebek client in the future.

Another current weakness with Sebek is the easy correlation of system activities with the network activities. It is currently hard to determine the relationship between monitored system calls and network connections, especially for keystrokes, where the parent process that receives data from the network is not necessarily the child process that actually uses the data. Developers are needed for improving the data capture mechanism and improving the identification of the network source of captured keystrokes.

### Sebek Linux 2.6 Kernel Version - Improve Stability, Stealth, and Data Correlation

The same goals as per the Win32 version above, but for the Linux 2.6 kernel family.

### Virtualization Based Honeypot Monitoring

A virtualization based approach to high interaction data collection potentially provides us with better invisibility (it is almost impossible to determine whether you are monitored by a hyperviser or not), better isolation (it is much harder to compromise a hyperviser than compromising Sebek running with a VM) and better introspection (it is extremely difficult to fool or bypass the monitoring if this occurs external to the processes running in a VM). We need talented, creative developers to develop hooking mechanisms for Virtual Machine Monitors as the infrastructure of high interaction data capture. There is no requirement for VMM, developers will decide this based on their experience, but we would like the hooking to be as stealthy as possible. Again, we have a number of internal prototypes and possible VMM solutions include QEMU, Xen, KVM and VirtualBox, but we are open to suggestions.

Although virtualization based solutions to high interaction data capture have many advantages, the data captured at the virtualization layer is low level and lacks the usual semantic information available within a traditional OS rootkit. We need capable developers to help us develop the code to reconstruct OS level information (e.g. process information, file system information) from the raw data (e.g. memory values, disk values) captured by the virtualization-based Sebek, so this project offers plenty of technical challenge. We think that this project is important as it will help to improve high interaction data capture capabilities, potentially decrease the chance of honeypot detection in areas such as sandboxing and malware analysis and will also provide positive input into the hyperviser and kernel development community.

**Skills required:  
**  
C programming, kernel driver programming, familiarity with Windows or Linux internals, virtualisation.

**Mentors:** Brian Hay (US, Win32/VMI), Rob McMillen (US, Linux), Eugene Teo (SG, Linux), Georg Wicherski (DE, VMI)

##   

# **Project 6 - Automatic generation of IDS signatures from honeynet data (Nebula)**

In May 2008, the Honeynet Project released a new tool called nebula. The program implements a new concept for automatic intrusion signature generation based on data from honeynets and honeypots. Automatic IDS signature engineering becomes more important as attack trends change very fast nowadays, making it impossible to keep up  
with manually written rules. Generating signatures from attack traces is one of the most interesting data analysis tasks. While signature generation is a hot scientific topic, the outcomes of a project can be an immediate contribution to practical network security if the tools are used to detect and block intrusion attempts.

Nebula implements a general signature generation framework based on efficient automatic classification for identifying unique classes per attack type. In a second step, information common to all members of a cluster are extracted. Finally, a signature is composed of these. The approach allows to correlate data without any further knowledge about the input which is a general requirement for signatures that match previously unknown attacks.

With the first nebula release it was shown that generated signatures can be used in the snort IDS to detect or block other intrusion attempts. While the current nebula version can already be set up in a distributed sensor setup, it must still be seen as a proof-of-concept. Past development aimed at implementing the core algorithms in a stable  
and efficient way. For the time being integration into production setups had low priority. A submission plugin is currently only available for honeytrap , but tests with argos netlogs, malware binaries showed that in principle the method works with other input as well.

Plans are to mprove nebula such that it better supports data analysis as a central collector in a distributed, heterogeneous sensor setup. The concrete goals are:

To develop a public web-based signature archive, o to further develop the nebula daemon, in particular:  
\- improve the attack processing system with respect to speed,  
\- implement additional metrics for automated attack classification,  
\- add a white-listing feature that allows to exclude certainpatterns from the  
\- generation process for false-positive prevention,

To develop a nebula client C library for easy nebula integration in other applications,

To develop extensions to other honeypot sensors (primarily nepenthes) such that they can contribute attack data to a signature generator,

To create a honeywall addon (as snort preprocessor for inline usage) for central passive data collection and nebula attack submission.

**Skills required:  
**  
C programming, good knowledge of network traffic protocols and IDS signatures

**Mentor:** Felix Leder (DE)

##   

# **Project 7 - Developing a user interface for analysing collected low interaction honeypot data (New)**

Honeynet Project members have developed a number of leading open source low interaction honeypot solutions that are used to automatically record data about network based malware attacks, such as [Nepenthes](http://nepenthes.carnivore.it/) and [HoneyTrap](https://sourceforge.net/projects/honeytrap/). We have a number of active [international sensor deployments](http://www.ukhoneynet.org/2007/12/03/global-dis) to collect malware globally and are in the process of [rolling out](http://www.ukhoneynet.org/2008/04/02/global-distributed-honeynet-gdh-phase-two-starting/) a larger low interaction sensor network during 2009. However, currently there is no publicly available web based reporting interface available for users of low interaction sensor systems.

The goal of this project would be to implement a web based user interface and management reporting tool to allow analysts to easily explore large amounts of malware data. Typical tasks will be to search for high level trends (growth of a particular malware strain over time, attacks from a certain location on a particular day, etc). End users will be the operators of malware collection sensors or interested analysts within the secuirty community.

As input, the system will take [reasonably simple CSV type](http://www.ukhoneynet.org/sample_submissions.txt) data from low interaction malware sensors (such as timestamp, source IP, attack type, attacker IP address, MD5sum, etc in the form of an HTTP POST). This data is then automatically enriched by submitting the malware binary samples to [multiple](http://anubis.iseclab.org/) [sandbox](http://www.cwsandbox.org/) and [antivirus](https://www.virustotal.com/) engines for analysis (both public and private). The output from this post processing analysis is usally returned  as XML or text after a short period, by HTTP or email. We also perform [IP geo-location](https://en.wikipedia.org/wiki/Geolocation) and [ASN resolution](http://asn.cymru.com/) against IP address to provide more information about sources, including latitude and longitutude for spatial mapping. 

This data will be persisted in a database, procesed and then presented via a new web interface to multiple distributed analyst users. This interesting project and malware data set provides many potential data analysis, information presentation and information security data visualisation options for interested GSoC students. We have a number of prototype reporting interface examples available internally, or you are free to develop a new system from scratch. [Background](https://www.amazon.com/Know-Your-Enemy-Learning-Security/dp/0321166469/ref=pd_bbs_3?ie=UTF8&s=books&qid=1237469266&sr=8-3) [reading](https://www.amazon.com/Virtual-Honeypots-Tracking-Intrusion-Detection/dp/0321336321/ref=pd_bbs_sr_1?ie=UTF8&s=books&qid=1237469266&sr=8-1) and [design](https://www.amazon.com/Applied-Security-Visualization-Raffael-Marty/dp/0321510100/ref=sr_1_1?ie=UTF8&qid=1237469355&sr=8-1) [inspiration](http://www.secviz.org/) might be found by looking at how leading [network](http://atlas.arbor.net/) [security](http://www.threatexpert.com/) and [antivirus](https://tms.symantec.com/Default.aspx) [vendors](http://www.f-secure.com/weblog/archives/00001467.html) or [opensource](https://www.shadowserver.org/wiki/pmwiki.php?n=Stats.Statistics) [groups](http://www.mwcollect.org/) current present similar information, or by applying skills you bring to the project from your personal experiences and specialisms. Successful students will also be lucky enough to have access to a number of the leading subject matter experts in this field as technical advisors.

We believe that this project is important to the community as it will help researchers to more easily understand the types of attacks routinely occuring on the Internet today.

**Skills required:  
**  
Probably Python and Javacript programming plus some database experience, although any suitable previous web development and user interface development experience would be good. We are happy to support whatever development toolkit you are most capable in, and follow a development approach of releasing small updates often, for maximum user feedback.

**Mentor:** David Watson (UK)

##   

# **Project 8 - Improving Honeynet data visualisation (DAVIX / PicViz / AfterGlow)**

To process and analyze the vast amount of HoneyPot data, we have a set of visualization tools. Among them PicViz ([http://www.wallinfire.net/picviz](http://www.wallinfire.net/picviz)), which is a parallel coordinates plotter, AfterGlow ([http://afterglow.sf.net](http://afterglow.sf.net/)) a tool that builds link graphs, and the Data Analysis and Visualization Linux (DAVIX) ([http://davix.secviz.org](http://davix.secviz.org/)), which is a live CD containing a large number of visualization tools.

Each of these three tools or projects are in need of specific additions and improvements:

- DAVIX: In order for people to visualize their data with the various visualization tools on DAVIX, their data needs to be translated from the original format into whatever format the visualization tools require. We will build a general purpose parser framework that allows for easy definition of parsers through a user interface. In addition, we will be building a number of these parsers to out-of the box support various data sources and output data formats.
- PicViz: Extend PicViz to improve presentation of honeynet sourced data, particularly with regard to incident timelines.
- AfterGlow: The command-line driven tool needs a user interface. We will add a simple interface that exposes all run-time parameters for AfterGlow and GraphViz, as well as the graph configurations. A second project is to build an output interface for AfterGlow that renders link graphs and lets the user interact with the graphs.

**Skills required:  
**

PicViz: Python programming  
  
AfterGlow: Flash, Web, (or Tcl/TK), Perl  
  
DAVIX: UNIX/Linux, python/perl, parsers/regular expressions, HTML/Web applications

**Mentors:**  Sebastien Tricaud (FR), Raffael Marty (US) and Kara Nance (US)

#   

# **How to become a Google Summer of Code student with the Honeynet Project.**

If you are interested in getting started, please:

1. Read our publicly available information
2. Consider joining the various public mailing lists and creating yourself a self-service account on our public projects server, so you get a feel for typical project activity
3. Consider setting up a web page about your ideas, with your account names (email, IRC nick, etc) so that we can recognize you
4. Contact our Google Summer of Code 2009 contact (Lance Spitzner) and express your interest
5. We will not be doing formal interviews, but you will be asked to join up to an internal mailing list and an IRC channel so we can discuss project ideas with you. Once there, we will introduce you to our people and their areas of expertise, and put you in touch with the correct mentor and advisors for each project proposal. Please feel free to ask any questions you might have about us or the project.
6. Complete our GSOC 2009 questionnaire. Please provide as much information as possible about your idea, including examples of any previous relevant work and suitable project milestones. If you have previously worked on Honeynet Project R&D or submitted patches to our public projects, please highlight this. The more information you provide to us, the easier it is for us to decide if your proposal is what we are looking for.
7. [Submit your application](https://socghop.appspot.com/document/show/program/google/gsoc2009/faqs#student_apply) to Google by their deadline of Friday, 3 April 2009, 19:00:00 UTC time.

#   

# More information about the Honeynet Project

You can find more information about the Honeynet Project at our [About Us section](https://www.honeynet.org/about), including links to our international chapters and their members.  You can also subscribe to [our blog](https://www.honeynet.org/blog)  to learn more about our recent R&D activities.

- [Twitter](https://twitter.com/share?url=https%3A%2F%2Fwww.honeynet.org%2Fnode%2F378&text=Google%20Summer%20of%20Code%202009%20Project%20Ideas)
- [Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.honeynet.org%2Fgsoc2009%2Fideas&t=Google+Summer+of+Code+2009+Project+Ideas)
- [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.honeynet.org%2Fgsoc2009%2Fideas&title=Google+Summer+of+Code+2009+Project+Ideas&summary=Please+note+that+GSoC+2011+has+now+successfully+completed.+This+content+is+being+retained+for+reference+only.%0D%0A%0D%0AProject+Ideas%0D%0A&source=The+Honeynet+Project)
