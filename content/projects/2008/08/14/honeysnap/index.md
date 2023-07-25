---
title: "Honeysnap"
date: "2008-08-14"
---

Honeysnap is a tool used for extracting and analyzing data from pcap files, including IRC communications. Developed and maintained by Arthur Clune of the UK Chapter.

 

## About

* * *

Honeysnap is designed to be a command-line tool for parsing single or multiple pcap data files and producing a 'first-cut' analysis report that identifies significant events within the processed data. This presents security analysts with a pre-prepared menu of high value network activity, aimed at focusing manual forensic analysis and saving significant incident investigation time. Once you have identified data that interests you, you can then employ other tools for more in depth analysis, such as the Walleye user interface to the Honeywall. Honeysnap is also suitable for manual operation or automation via cron.

Please provide any feedback or suggestions to the  [Honeysnap public maillist](https://public.honeynet.org/mailman/listinfo/honeysnap). Bugs should be submitted as [Trac Tickets](https://projects.honeynet.org/honeysnap/newticket), after registering a user account.

Examples of functionality include:

- Packet and connection overview.
- Flow extraction of ASCII based communications.
- Protocol decode of the more common Internet communication protocols.
- Binary file transfer extraction.
- Flow summary of inbound and outbound connections.
- Keystroke extraction of ver2 and ver 3 Sebek data.
- Identification and analysis of IRC traffic, including keyword matching.

 

## Documentation

* * *

Each distribution of Honeysnap comes with documentation on how to install, configure, and use Honeysnap. In addition, we highly recommend you join the  [Honeysnap public maillist](https://public.honeynet.org/mailman/listinfo/honeysnap).

See the bottom of the page for the USAGE and INSTALL documents. The latest versions will always be in svn.

 

## Functionality / Updates

* * *

Version 1.0.6 now decodes the following protocols.

- DNS
- FTP
- HTTP
- IRC
- Socks
- Sebek

In addtion, the new 1.0.6 version includes

- Socks proxy traffic stats
- User definable filters for the counts
- Improved DNS output
- Fixed bug in file extraction
- A big speed increase in gzip decoding
- Print querying IP for DNS decodes
- Auto-spotting of IRC traffic on any port
- SOCKS decoding
- Fix to the truncation of extracted files
- Includes magicpy in the distribution to solve the problems caused by the original website going away.

 

## Distribution

* * *

Either download the .tar.gz file below (for Unix-like systems) or the .zip file (for windows) or checkout from svn.

To checkout the svn repository,

$ svn checkout  [https://projects.honeynet.org/svn/honeysnap/trunk](https://projects.honeynet.org/svn/honeysnap/trunk) honeysnap

For CentOS 5/Fedora or Honeywall 1.3 or later, rpms are provided. You need to install all four.

### Attachments

- [USAGE](https://projects.honeynet.org/honeysnap/attachment/wiki/WikiStart/USAGE "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/honeysnap/raw-attachment/wiki/WikiStart/USAGE "Download") (7.4 KB) - added by _arthur_ [10 years](https://projects.honeynet.org/honeysnap/timeline?from=2008-01-11T15%3A12%3A49Z&precision=second "2008-01-11T15:12:49Z in Timeline") ago. USAGE for Honeysnap, with examples
- [pypcap-1.1.tar.gz](https://projects.honeynet.org/honeysnap/attachment/wiki/WikiStart/pypcap-1.1.tar.gz "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/honeysnap/raw-attachment/wiki/WikiStart/pypcap-1.1.tar.gz "Download") (22.7 KB) - added by _arthur_ [10 years](https://projects.honeynet.org/honeysnap/timeline?from=2008-01-11T15%3A17%3A14Z&precision=second "2008-01-11T15:17:14Z in Timeline") ago. Dug Song's pypcap, with minor alterations to the installer
- [dpkt-1.6-1.noarch.rpm](https://projects.honeynet.org/honeysnap/attachment/wiki/WikiStart/dpkt-1.6-1.noarch.rpm "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/honeysnap/raw-attachment/wiki/WikiStart/dpkt-1.6-1.noarch.rpm "Download") (142.5 KB) - added by _arthur_ [10 years](https://projects.honeynet.org/honeysnap/timeline?from=2008-01-18T15%3A59%3A13Z&precision=second "2008-01-18T15:59:13Z in Timeline") ago. dpkt rpm for CentOS 5
- [pcap-1.1-1.i386.rpm](https://projects.honeynet.org/honeysnap/attachment/wiki/WikiStart/pcap-1.1-1.i386.rpm "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/honeysnap/raw-attachment/wiki/WikiStart/pcap-1.1-1.i386.rpm "Download") (42.8 KB) - added by _arthur_ [10 years](https://projects.honeynet.org/honeysnap/timeline?from=2008-01-18T15%3A59%3A46Z&precision=second "2008-01-18T15:59:46Z in Timeline") ago. CentOS 5 rpm for pypcap
- [python-irclib-0.4.6-1.noarch.rpm](https://projects.honeynet.org/honeysnap/attachment/wiki/WikiStart/python-irclib-0.4.6-1.noarch.rpm "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/honeysnap/raw-attachment/wiki/WikiStart/python-irclib-0.4.6-1.noarch.rpm "Download") (38.0 KB) - added by _arthur_ [10 years](https://projects.honeynet.org/honeysnap/timeline?from=2008-01-18T16%3A00%3A12Z&precision=second "2008-01-18T16:00:12Z in Timeline") ago. CentOS 5 rpm for python-irclib
- [INSTALL](https://projects.honeynet.org/honeysnap/attachment/wiki/WikiStart/INSTALL "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/honeysnap/raw-attachment/wiki/WikiStart/INSTALL "Download") (4.8 KB) - added by _arthur_ [8 years](https://projects.honeynet.org/honeysnap/timeline?from=2010-02-22T15%3A35%3A51Z&precision=second "2010-02-22T15:35:51Z in Timeline") ago. INSTALL file for honeysnap
- [honeysnap-1.0.7.tar.gz](https://projects.honeynet.org/honeysnap/attachment/wiki/WikiStart/honeysnap-1.0.7.tar.gz "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/honeysnap/raw-attachment/wiki/WikiStart/honeysnap-1.0.7.tar.gz "Download") (65.8 KB) - added by _arthur_ [8 years](https://projects.honeynet.org/honeysnap/timeline?from=2010-04-17T18%3A43%3A00Z&precision=second "2010-04-17T18:43:00Z in Timeline") ago. Honeysnap 1.0.7 .tar.gz files (Unix/Linux?/OS X)
- [honeysnap-1.0.7.zip](https://projects.honeynet.org/honeysnap/attachment/wiki/WikiStart/honeysnap-1.0.7.zip "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/honeysnap/raw-attachment/wiki/WikiStart/honeysnap-1.0.7.zip "Download") (90.7 KB) - added by _arthur_ [8 years](https://projects.honeynet.org/honeysnap/timeline?from=2010-04-17T18%3A44%3A09Z&precision=second "2010-04-17T18:44:09Z in Timeline") ago. Honeysnap 1.0.7, Zip format (Windows)
- [honeysnap-1.0.7-1.noarch.rpm](https://projects.honeynet.org/honeysnap/attachment/wiki/WikiStart/honeysnap-1.0.7-1.noarch.rpm "View attachment") [![Download](images/download.png)](https://projects.honeynet.org/honeysnap/raw-attachment/wiki/WikiStart/honeysnap-1.0.7-1.noarch.rpm "Download") (163.6 KB) - added by _arthur_ [8 years](https://projects.honeynet.org/honeysnap/timeline?from=2010-04-17T18%3A47%3A52Z&precision=second "2010-04-17T18:47:52Z in Timeline") ago. Honeysnap 1.0.7 RPM (RHEL/CentOS 5)
