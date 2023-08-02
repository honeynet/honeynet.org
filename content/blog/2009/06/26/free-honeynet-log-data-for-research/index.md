---
title: "Free Honeynet Log Data for Research"
authors: ["Anton Chuvakin"]
date: "2009-06-26"
tags: 
  - "data"
  - "honeynet"
  - "honeypot"
  - "linux"
  - "logging"
  - "logs"
  - "research"
  - "security"
---

  

  

  

**UPDATE**: the log data is posted [here](http://log-sharing.dreamhosters.com/).  A notification group about new log sharing is [here](/groups.google.com/group/log-sharing).

  

  

This [WASL 2009 workshop](http://www.systemloganalysis.com/) reminded me that I always used to bitch that some academic researchers use antediluvian data sets for their research ([Lincoln labs 1998 set](http://www.ll.mit.edu/mission/communications/ist/corpora/ideval/data/index.html) used in 2008 “security research”  makes me want to just curse and kick people in the balls, then laugh, then cry, then cry more…).

  

However, why are they doing it? Don’t they realize that testing their “innovative intrusion detection” or “neural network-based log analysis” on such prehistoric data will not render it relevant to today’s threats? And will only ensure ensuing hilarity :-)

  

Well, maybe the explanation is simpler: there is no public, real-world source of logs that allows comparison between different security research efforts.

  

Correction! There wasn’t. **And now [there is](http://log-sharing.dreamhosters.com/)!**

  

I hereby promise to make my collection of real-world logs (mostly collected from the honeypots run in 2004-2006) public (**UPDATE**: logs available [here](http://log-sharing.dreamhosters.com/)).  Here is the description of the collection:

  

  

  

**Size**: 100MB compressed; about 1GB uncompressed (more is available upon request)

  

  

**Date collected:** 2006

  

  

**Type:** Linux logs _/var/log/messages, /var/log/secure_, process accounting records_/var/log/pacct_, other Linux logs,  Apache web server logs _/var/log/httpd/access\_log, /var/log/httpd/error-log, /var/log/httpd/referer-log_ and _/var/log/httpd/audit\_log_, Sendmail _/var/log/mailog,_ Squid _/var/log/squid/access\_log, /var/log/squid/store\_log, /var/log/squid/cache\_log, etc._ Firewall and Snort NIDS logs are also available.

  

  

**License:**  public; use for whatever you want. Acknowledging the source is nice;[Beerware](http://en.wikipedia.org/wiki/Otherware) license is even better.

  

  

**Sanitization:** No additional sanitization is required before use for research.

  

  

  

So, for now, if your research requires real-world logs with normal operation data, suspicious data, anomalous data and attack data – drop me an email or get them [here](http://log-sharing.dreamhosters.com/).

  

**Possibly related posts:**

  

  
- 
    
    ##### [Workshop on the Analysis of System Logs (WASL) 2009 CFP](http://chuvakin.blogspot.com/2009/06/workshop-on-analysis-of-system-logs.html)
