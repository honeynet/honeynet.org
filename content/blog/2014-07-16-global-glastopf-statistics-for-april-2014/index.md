---
title: "Global Glastopf statistics for April 2014"
date: "2014-07-16"
tags: 
  - "glastopf-d23"
  - "logs-d11"
  - "report"
  - "statistics-d53"
---

**During the month of April the following information was obtained from Glastopf installations worldwide**  
  
**Number of alert for the period:** 1325919  
  
**Filenames (RFI) - 10 most common during the period:**  
  
  
  
  
  
  
  
  
  
  
  
  
  

<table><tbody><tr><td><strong>Hash:</strong></td><td>Hits:</td></tr><tr><td>F8a4da2e35b840891335d90cb48a6660</td><td 6256<="" td=""></td></tr><tr><td>b8cbfe520d4c2d8961de557ae7211cd2</td><td>1072</td></tr><tr><td>3cc11c8fa7e3e36f0164bdcae9de78ec</td><td>998</td></tr><tr><td>7de0bcb903eaba7881c6d03a8c7769a8</td><td>682</td></tr><tr><td>9e866b8855c08a93f23afce1b9a79756</td><td>460</td></tr><tr><td>67b873f7541b039c049414dfe3fd7993</td><td>352</td></tr><tr><td>9f67913d2c77545a4187053ad18230e4</td><td>187</td></tr><tr><td>fbef119cf310d6b0b40af7e486416f82</td><td>186</td></tr><tr><td>ab4d03072cc0532afc83d13854ed7e4f</td><td>173</td></tr><tr><td>afdc0866a82a6bb23bc4d4fb329672b6</td><td>172</td></tr></tbody></table>

  
  
  
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
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

<table><tbody><tr><td><strong>Resource:</strong></td><td>Count (requests):</td></tr><tr><td>/xmlrpc.php</td><td>35500</td></tr><tr><td>/stats/awstats.pl?framename=mainright&amp;output=refererpages<br></td><td>7694</td></tr><tr><td>/stats/awstats.pl</td><td>5862</td></tr><tr><td>/wp-login.php</td><td>5146</td></tr><tr><td>/wp-login.php?action=register</td><td>4255</td></tr><tr><td>/phpMyAdmin-2.5.5/index.php</td><td>2353</td></tr><tr><td>/phpMyAdmin-2.5.5-pl1/index.php</td><td>2297</td></tr><tr><td>/administrator/index.php</td><td>1933</td></tr><tr><td>/api/v1/notice/ios/?type=pro</td><td>1450</td></tr><tr><td>/phpMyAdmin-2.7.0-beta1/scripts/setup.php</td><td>896</td></tr><tr><td>/server-status/</td><td>852</td></tr><tr><td>/phpTest/zologize/axa.php</td><td>758</td></tr><tr><td>/files.pl</td><td>750</td></tr><tr><td>/sqlmanager/setup.php</td><td>730</td></tr><tr><td>/sprawdza.php</td><td>694</td></tr><tr><td>/azenv.php</td><td>615</td></tr><tr><td>/plugins/content/plugin_googlemap2_proxy.php<br></td><td>552</td></tr></tbody></table>

  
  
**And a few other request that are "interesting" to highlight**  
  
  
  
  
  
  
  

<table><tbody><tr><td><strong>Resource:</strong></td><td>Count:</td><td>Reference:<strong></strong></td></tr><tr><td>/zabbix/httpmon.php</td><td>464</td><td>https://www.corelan.be/index.php/2013/10/04/zabbix-sql-injectionrce-cve-2013-5743/</td></tr><tr><td>/%22GRC.DAT/%22</td><td>397</td><td>http://www.symantec.com/business/support/index?page=content&amp;id=TECH101234 (?)</td></tr><tr><td>/HNAP1/</td><td>343</td><td>https://isc.sans.edu/diary/Linksys+Worm+%22TheMoon%22+Summary %3A+What+we+know+so+far/17633</td></tr><tr><td>/cgi-bin/nph-test-cgi</td><td>170</td><td>party like it's 1996 (still included in some scanners ..)</td></tr></tbody></table>

  
  
  
  
This was a small excerpt from the collected data. I hope this encouraged you to continue to have hpfeeds enabled (or to enable it, if you have turned it off) on your honeypot/honeypots as the data gives a very valuable insight into current threats globally.  
  
  
**System reference:**  
  
“Glastopf is a Honeypot which emulates thousands of vulnerabilities to gather data from attacks targeting web applications. The principle behind it is very simple: Reply the correct response to the attacker exploiting the web application.”  
  
For more information please visit:  
http://www.glastopf.org/index.php or https://github.com/glastopf/glastopf  
  
All data was collected using hpfriends, for more information please visit: http://hpfriends.honeycloud.net/
