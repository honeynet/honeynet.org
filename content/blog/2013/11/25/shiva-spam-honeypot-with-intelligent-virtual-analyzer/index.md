---
title: "SHIVA (Spam Honeypot with Intelligent Virtual Analyzer)"
authors: ["Angelo Dellaera"]
date: "2013-11-25"
categories: 
  - "honeypot"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

**SHIVA (Spam Honeypot with Intelligent Virtual Analyzer) is an open-source, high interaction spam honeypot developed in Python2.7 and is released under [GNU GPL v3](http://opensource.org/licenses/GPL-3.0).**


SHIVA provides the capability of collecting and analyzing all spam thrown at it. Analysis of data captured can be used to get information on phishing attacks, scamming campaigns, malware campaigns, spam botnets, spammers identity etc. Following are the features which describes the functionality of SHIVA:  

- **Intelligence:** A lot of research has been done to develop SHIVA and to counter the techniques used by spammers. There are lots of counter techniques and workarounds that SHIVA uses to pose itself as an authentic open relay SMTP host. These techniques have been researched and deduced from spam analyzed by SHIVA and from the spammers themselves.

- **Open Source:** SHIVA is open source and therefore available to extend the capabilities. For example, one could develop module to send the captured attachments to Cuckoo or captured links to Thug for further analysis.

- **Extraction of Information from Spam:** Every spam mail received passes through the mail parser. SHIVA's mail parser is written to extract all the information that is important. Mail parser extracts source IP, spam's various parts like – ‘to’, ‘from’, ‘header’, ‘subject’, ‘body’, ‘URLs’, ‘attachments’, etc. This information could be saved in database (if user has opted for setting up database locally) and/or published to hpfeeds channels.

- **Identification of Unique Spam:** SHIVA uses [fuzzy hashing](http://ssdeep.sourceforge.net/) technique to distinguish between new and already analyzed spam. This makes it possible to analyze millions of spam and still keeping the database size in check.

- **Controlled Relay:** SHIVA provides the ability to control the relay part completely. User can enable/disable and set the number of spam to be relayed, in the configuration file.

- **Supports Authentication:** SHIVA provides more control over the SMTP receiver by adding SMTP authentication feature to it. This way, a user can restrict the access to his SMTP server by setting up credentials.

- **Hpfeeds sharing:** SHIVA makes sharing the analyzed data easy by adding [hpfeeds/hpfriends](http://hpfriends.honeycloud.net/#/home) support.

To understand more about architecture, SHIVA is divided into two parts - Receiver and Analyzer. In short, the receiver part acts as an open relay SMTP server, collects all spam thrown at it and dumps them into a local directory. The analyzer, then, picks up spam and proceeds with analysis and extraction of useful information.

![](images/SHIVA_Honeynet_Blog_11252013_html_9ca672a1.png)

SHIVA, other than being used as traditional open but controlled relay honeypot, can be used for other purposes too. Listed below are some of the possible usage scenarios:

- **Collecting Emails**: SHIVA can be used as an SMTP server that'll dump all the emails that it receives, into a local directory. If only receiver part is started, SHIVA acts as an SMTP server, and all mails are dumped into queue directory.

- **Analyzing Stored Spam**: SHIVA can also be used to analyze spam that might have been collected from various sources. All that needs to be done is to transfer all spam into queue folder and start the analyzer part.

- **Hpfeeds Sharing**: SHIVA can be easily configured for sharing data via hpfeeds. There's a dedicated section in configuration file that deals with all steps needed to set up hpfeeds sharing.

- **Distributed Environment -** With a little trouble, SHIVA can be used to setup up a distributed network of multiple sensors with one centralized node. In this setup, there will be multiple sensors collecting unique spam and sending them to the master node. This master node will further analyze those spams and save data. Client nodes can share spam via hpfeeds, in form of raw spam files.

- **Extensibility -** Due to the simple design of SHIVA, small modules could be easily written to send collected attachments and URLs received in a spam to other honeypot like Cuckoo sandbox and Thug for further analysis.

Installing SHIVA has been made pretty straightforward and simple. It is as easy as running a single bash script; given user have required permissions and prerequisites installed. Detailed documentation is available at [github](https://github.com/shiva-spampot/shiva/blob/master/docs/User%20Manual.pdf) repository of SHIVA.

We expect following packages to be installed on system before user starts installation procedure.

- Debian based OS (Preferably Ubuntu or Mint Linux)
- Python2.7
- exim4-daemon-light
- g++
- python-virtualenv
- python-dev
- libmysqlclient-dev
- mysql-client (optional, only if user wants to save spam data in database)
- mysql-server (optional, only if user wants to set up MySQL database on same machine)
- phpmyadmin (optional, only if user wants to monitor databases, the GUI way)

Following are the recommended hardware specifications:


- Processor – 2 cores, one for receiver and one for analyzer
- OS - Debian-based. Tested on Ubuntu 12.04/13.04 and Mint Linux 15
- RAM - 2 Gb or more
- Hard disk - 10 Gb or more.

SHIVA can be easily installed by executing the bash installer script available with package. Installation, depending on internet speed, takes around 5-15 minutes to install required packages. Detailed documentation is available at  
[github](https://github.com/shiva-spampot/shiva/blob/master/docs/User%20Manual.pdf) repository of SHIVA.

Steps to configure SHIVA have been attempted to keep straight and easy. Everything that needs to be configured is in "shiva/shiva.conf" file. Detailed documentation is available on [github](https://github.com/shiva-spampot/shiva/blob/master/docs/User%20Manual.pdf) repository of SHIVA.

For running SHIVA, open two terminals, one for receiver and another one for analyzer. Activate respective virtual environments and start SHIVA instances. Detailed documentation is available on [github](https://github.com/shiva-spampot/shiva/blob/master/docs/User%20Manual.pdf) repository of SHIVA.

The project is in infant stage, contribution from community would be highly appreciated. If you find a bug, report it to us. If you have a patch or you have added some cool feature, clone our github repository, send us a pull request. We'll be more than happy to merge your patches.

Please note that while submitting patches make sure patch follows [PEP 8 -- Style Guide for Python Code](http://www.python.org/dev/peps/pep-0008/).

SHIVA source code is available at [https://github.com/shiva-spampot/shiva](https://github.com/shiva-spampot/shiva).

Following are the authors/developers of SHIVA please feel free to reach out in case of any queries or suggestions.  

- **[Sumit Sharma](http://www.linkedin.com/pub/sumit-sharma/12/949/a43)** <sumit.iips@gmail.com> [@SumitSharma](https://twitter.com/b0ndGarage)

- **[Rahul Binjve](http://in.linkedin.com/pub/rahul-binjve/75/460/36/)** <rahulbinjve@gmail.com> [@RahulBinjve](https://twitter.com/RahulBinjve)
