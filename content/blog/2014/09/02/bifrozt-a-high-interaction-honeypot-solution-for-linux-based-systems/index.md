---
title: "Bifrozt - A high interaction honeypot solution for Linux based systems."
date: "2014-09-02"
categories: 
  - "honeypot"
tags: 
  - "bifrozt-d66"
  - "high-interaction-honeypot"
  - "linux-d95"
---

A few days ago I was contacted by our CPRO, Leon van der Eijk, and asked to write a blog post about my own project called Bifrozt; something which I was more than happy to do. :) This post will explain what Bifrozt is, how this got started, the overall status of the project and what will happen further down the road.

**What is Bifrozt?** Generally speaking, Bifrozt is a NAT device with a DHCP server that is usually deployed with one NIC connected directly to the Internet and one NIC connected to the internal network. What differentiates Bifrozt from other standard NAT devices is its ability to work as a transparent SSHv2 proxy between an attacker and your honeypot. If you deployed a SSH server on Bifrozt's internal network it would log all the interaction to a TTY file in plain text that could be viewed later and capture a copy of any files that were downloaded. You would not have to install any additional software, compile any kernel modules or use a specific version or type of operating system on the internal SSH server for this to work. It will limit outbound traffic to a set number of ports and will start to drop outbound packets on these ports when certain limits are exceeded.

![](images/drupal_image_1192.png)

**How it started.** Bifrozt is not something I can take full credit for, it depends on a awesome python project by Thomas Nicholson which I discovered in February 2014. Thomas had coded a SSH proxy called [HonSSH](https://code.google.com/p/honssh/) and had taken inspiration and utilized code from the medium interaction [Kippo](https://code.google.com/p/kippo/) honeypot. After I discovered HonSSH I decided to build an ISO file, that would allow me to install a pre-configured NAT device with HonSSH, on either a hardware or virtualized machine. I thought this would be a suitable project that I could occupy myself with during a 2 week holiday. Six months later and the project is still very much alive.

**Current status.** Me and Thomas have been co-operating over the last five months to align our projects as much possible. Developing Bifrozt is much like building a car. Thomas is developing the engine (HonSSH) and making sure it's running smoothly, whilst I am developing the strong and solid frame (firewall, data extraction from log files, data control, system configuration etc etc) around it.

Bifrozt has been in a proof of concept stage (Alpha) for the last six months. The current version, 0.0.8, has a relative humble feature list, but this is about to change.

Bifrozt 0.0.8 -------------- - Intercept downloaded files - Logs all SSH communications to plain text file and TTY logs - Enforces data control - Facilitates data capture - Provides high level integrity of the captured data - Hardware installation - Virtual installation - Honeyd is pre-installed - Easy data extraction from logs - Disrupts outbound SYN flood attacks from the honeypot - Disrupts outbound UDP flood attacks from the honeypot - Compatible with amd64 architecture

After after a few weeks of summer vacation I've started planning and testing the next release of Bifrozt.

Bifrozt 0.0.9 -------------- - Compatible with x86 architecture - IDS (Snort or Suricata) - Viewing alerts and statistics trough a browser - Complete overhaul of the Python code - Multiple installation options to better suit the hardware resources and needs of the end user - Expand the current toolbox - Change base system from Ubuntu to Debian (not made any final decision about this yet) - Tool to generate DROP rules based on country of origin - Update and add more functions to bifrozt\_stats (log data extraction)

**Roadmap for the future.** No one knows what is going to happen down the road but, at the present time neither me or Thomas plan on abandoning our projects any time soon. We have both decided to create a road map for the future and he has allowed me to share them here, together with mine.

Bifrozt roadmap. ------------------- Short term goals (Alpha stage): System: - Off line installation - Desktop environment (install option) - Optimizing IDS - Expand/improve web stats (optimize current, add HonSSH, create a dedicated start page) - HP feeds data sharing - Optimize firewall and data control

Tools: - Simple static malware analysis (add VirusTotal upload function) - System re-configuration tool(s) (DHCP, SSH, firewall etc etc) - Develop new tools or adjust current to complement additional data captured by HonSSH

Long term goals (Beta stage and beyond): - Provide a NAT device that provides reliant data capture of the most commonly used protocols - Quickly display data about the attacks, malware, outbound communication in a easy understandable format - To the extent of my abilities, make suer the project continues to be based on open source and freely available to anyone.

HonSSH roadmap. --------------------- Short term: - Bring HonSSH out of proof-of-concept code into a more logical production format - Implement a bot to owner correlation technique using random passwords - Bug bashing

Longer term: - Output data to ElasticSearch - Allow HTTP tunneling (currently disabled), parse HTTP outputs etc. - Parse X11 sessions - not sure if this will be worth it or not. - More consideration on data analysis (might be a separate project)

HonSSH's current aim: - Parse, interpret and log all communications that travel through an SSH tunnel. Currently supports Terminal, Exec (and SCP) and SFTP traffic.

HonSSH's current challenges: - Parsing the terminal - knowing what is a command, and what is program input e.g. nano etc.

HonSSH's current questions: - Should HonSSH act on commands? e.g. When a wget command is detected, should it pull down the file (active), or should we use/develop another tool for passive packet capture/MITM of HTTP and IRC

**LINKS: [Bifrozt](http://sourceforge.net/projects/bifrozt/) [HonSSH](https://code.google.com/p/honssh/)**
