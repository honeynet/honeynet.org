---
title: "Global Glastopf statistics for April 2014"
authors: ["Mikael Keri"]
date: "2014-07-16"
tags: 
  - "glastopf"
  - "logs"
  - "report"
  - "statistics"
---

**During the month of April the following information was obtained from Glastopf installations worldwide**  

**Number of alert for the period:** 1325919  

**Filenames (RFI) - 10 most common during the period:**  

**Hashes - 10 most common during the period:**

| Hash                                | Hits |
|-------------------------------------|------|
| F8a4da2e35b840891335d90cb48a6660    | 6256 |
| b8cbfe520d4c2d8961de557ae7211cd2    | 1072 |
| 3cc11c8fa7e3e36f0164bdcae9de78ec    | 998  |
| 7de0bcb903eaba7881c6d03a8c7769a8    | 682  |
| 9e866b8855c08a93f23afce1b9a79756    | 460  |
| 67b873f7541b039c049414dfe3fd7993    | 352  |
| 9f67913d2c77545a4187053ad18230e4    | 187  |
| fbef119cf310d6b0b40af7e486416f82    | 186  |
| ab4d03072cc0532afc83d13854ed7e4f    | 173  |
| afdc0866a82a6bb23bc4d4fb329672b6    | 172  |

**Specifically newsworthy event:** Ping back”

pingback.ping, which is a legit WordPress feature is misused to DoS victims using legit WordPress sites.  

URL describing the issue: http://blog.sucuri.net/2014/03/more-than-162000-wordpress-sites-used-for-distributed- denial-of-service-attack.html  

**Method:**  
`
pingback.pinghttp://victim.com  
www.anywordpresssite.com/postchosenparam>'  
`

**Extent:**

We started monitoring this event, late into the month. But even so, the top 10 victim sites was hit with a total of 13441 requests.  

**Summary:**  

The targets that we detected was a blend of a legit businesses/services but also a mix of underground forums, hacking and carding sites. Some of the sites targeted were also protected by DDoS mitigation services.  

**Top pick from list of requested resources:**  

**Top pick from list of requested resources:**

| Resource | Count (requests) |
|----------|------------------|
| /xmlrpc.php | 35500 |
| /stats/awstats.pl?framename=mainright&output=refererpages | 7694 |
| /stats/awstats.pl | 5862 |
| /wp-login.php | 5146 |
| /wp-login.php?action=register | 4255 |
| /phpMyAdmin-2.5.5/index.php | 2353 |
| /phpMyAdmin-2.5.5-pl1/index.php | 2297 |
| /administrator/index.php | 1933 |
| /api/v1/notice/ios/?type=pro | 1450 |
| /phpMyAdmin-2.7.0-beta1/scripts/setup.php | 896 |
| /server-status/ | 852 |
| /phpTest/zologize/axa.php | 758 |
| /files.pl | 750 |
| /sqlmanager/setup.php | 730 |
| /sprawdza.php | 694 |
| /azenv.php | 615 |
| /plugins/content/plugin_googlemap2_proxy.php | 552 |

**And a few other request that are "interesting" to highlight**  

**Resource:** | **Count:** | **Reference:**
--- | --- | ---
/zabbix/httpmon.php | 464 | [Zabbix SQL Injection/RCE CVE-2013-5743](https://www.corelan.be/index.php/2013/10/04/zabbix-sql-injectionrce-cve-2013-5743/)
`/"GRC.DAT/"` | 397 | [Symantec Support](http://www.symantec.com/business/support/index?page=content&id=TECH101234) (?)
/HNAP1/ | 343 | [Linksys Worm "TheMoon" Summary](https://isc.sans.edu/diary/Linksys+Worm+%22TheMoon%22+Summary%3A+What+we+know+so+far/17633)
/cgi-bin/nph-test-cgi | 170 | party like it's 1996 (still included in some scanners ..)

This was a small excerpt from the collected data. I hope this encouraged you to continue to have hpfeeds enabled (or to enable it, if you have turned it off) on your honeypot/honeypots as the data gives a very valuable insight into current threats globally.  

**System reference:**  

“Glastopf is a Honeypot which emulates thousands of vulnerabilities to gather data from attacks targeting web applications. The principle behind it is very simple: Reply the correct response to the attacker exploiting the web application.”  

For more information please visit:  
http://www.glastopf.org/index.php or https://github.com/glastopf/glastopf  

All data was collected using hpfriends, for more information please visit: http://hpfriends.honeycloud.net/
