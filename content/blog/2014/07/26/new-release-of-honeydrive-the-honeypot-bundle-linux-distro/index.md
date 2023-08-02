---
title: "New release of HoneyDrive; the honeypot bundle Linux distro"
authors: ["Ioannis Koniaris"]
date: "2014-07-26"
categories: 
  - "honeypot"
tags: 
  - "honeydrive"
---

It is my great pleasure to announce that HoneyDrive 3 is here, codenamed Royal Jelly!  
  
For those in need of a more official description or for people that haven’t heard of HoneyDrive before, here is one:  
  
_HoneyDrive is the premier honeypot Linux distro. It is a virtual appliance (OVA) with Xubuntu Desktop 12.04.4 LTS edition installed. It contains over 10 pre-installed and pre-configured honeypot software packages such as Kippo SSH honeypot, Dionaea and Amun malware honeypots, Honeyd low-interaction honeypot, Glastopf web honeypot and Wordpot, Conpot SCADA/ICS honeypot, Thug and PhoneyC honeyclients and more. Additionally it includes many useful pre-configured scripts and utilities to analyze, visualize and process the data it can capture, such as Kippo-Graph, Honeyd-Viz, DionaeaFR, an ELK stack and much more. Lastly, almost 90 well-known malware analysis, forensics and network monitoring related tools are also present in the distribution._  
  
**DOWNLOAD:**  
Download HoneyDrive 3 from SourceForge.net: [http://sourceforge.net/projects/honeydrive/](http://sourceforge.net/projects/honeydrive/)  
Make sure to examine the README.txt file for information about the installed software.  
  
**What you need to know (PLEASE READ):**  

  
2. HoneyDrive 3 has been created entirely from scratch. It is based on Xubuntu Desktop 12.04.4 LTS edition and it is distributed as a standalone OVA file that can be easily imported as a virtual machine using virtualization software such as VirtualBox and VMware.  
    
3. All the honeypot programs from the previous version of HoneyDrive are included, while they have also been upgraded to their latest versions and converted almost entirely to cloned git repos for easier maintenance and updating. This latter fact on its own could be considered reason enough to release the new version.  
    
4. Many new honeypot programs have been installed that really make HoneyDrive 3 “complete” in terms of honeypot technology, plus around 50(!) new security related tools in the fields of malware analysis, forensics and network monitoring.  
    
5. The main honeypot software packages and BruteForce Lab’s projects reside in /honeydrive. The rest of the programs reside in /opt. The location of all software can be found inside the README.txt file on the desktop.  
    
6. HoneyDrive 3 doesn’t make itself as known to the outside world as the previous version. There are no descriptive messages and apart from Kippo-Graph and Honeyd-Viz every other piece of software is not accessible from the outside (unless if you configure them otherwise, or even lock down Kippo-Graph and Honeyd-Viz as well).  
    

  
A note on versioning: previous versions of HoneyDrive started with a zero (0.1 and 0.2) which seemed confusing to some. I didn’t like it either and in the end I decided to “renumber” those as versions 1 and 2, essentially making this new version HoneyDrive 3, .i.e the third official release.  
  
**CHANGELOG:**  

  
- Upgraded ALL existing honeypot software to the corresponding latest versions.  
    
- Converted ALL existing honeypot software to cloned git repos for easier maintenance.  
    
- Removed distinguishable HoneyDrive artifacts and secured access to web tools.  
    
- Added Kippo-Malware and Kippo2ElasticSearch.  
    
- Added Conpot SCADA/ICS honeypot.  
    
- Added PhoneyC honeyclient.  
    
- Added maltrieve malware downloader.  
    
- Added the ELK stack (ElasticSearch, Logstash, Kibana).  
    
- Added the following security tools: dnstop, MINI DNS Server, dnschef, The Sleuth Kit + Autopsy, TekCollect, hashMonitor, corkscrew, cryptcat, socat, hexdiff, pdfid, disitool, exiftool, Radare2, chaosreader, netexpect, tcpslice, mitmproxy, mitmdump, Yara, Recon-ng, SET (Social-Engineer Toolkit), MASTIFF + MASTIFF2HTML, Viper, Minibis, Nebula, Burp Suite, xxxswf, extract\_swf, Java Decompiler (JD-GUI), JSDetox, extractscripts, AnalyzePDF, peepdf, officeparser, DensityScout, YaraGenerator, IOCExtractor, sysdig, Bytehist, PackerID, RATDecoders, androwarn, passivedns, BPF Tools, SpiderFoot, hashdata, LORG.  
    
- Added the following extra software: 7zip, Sagasu.  
    
- Added the following Firefox add-ons: Disconnect, Undo Closed Tabs Button, PassiveRecon.  
    
- Removed the following software: Kojoney, mwcrawler, Vidalia, ircd-hybrid, DNS Query Tool, DNSpenTest, VLC, Parcellite, Open Penetration Testing Bookmarks Collection (Firefox).  
      
    For comments, suggestions, fixes, please use the HoneyDrive page: [http://bruteforce.gr/honeydrive](http://bruteforce.gr/honeydrive).
