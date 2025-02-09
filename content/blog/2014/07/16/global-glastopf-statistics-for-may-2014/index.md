---
title: "Global Glastopf statistics for May 2014"
authors: ["Mikael Keri"]
date: "2014-07-16"
tags: 
  - "glastopf"
  - "logs"
  - "reports"
  - "statistic"
---

**During the month of May the following information was obtained from Glastopf installations worldwide**  

**Number of alert for the period:** 1859863  

**Filenames (RFI) - 10 most popular during the period:**  

**Hashes - 10 most popular during the period:**

| Hash                                | Hits |
|-------------------------------------|------|
| 48101bbdd897877cc62b8704a293a436    | 2425 |
| 4997ed27142837860014e946eed96124    | 2050 |
| d070c4cccf556b9da81da1e2de3cba54    | 644  |
| 3cc11c8fa7e3e36f0164bdcae9de78ec    | 330  |
| ab4d03072cc0532afc83d13854ed7e4f    | 286  |
| 8f8adad762a39ba298b9ee8b7555acf3    | 261  |
| 474c4daeff3d82ae49d7c96acb8c0d84    | 208  |
| e5f9687d94bf23f395799dec3fcafc3f    | 199  |
| 873f84fe2b641c2934203c7f6621b7fb    | 167  |
| 7de0bcb903eaba7881c6d03a8c7769a8    | 124  |

**Ping back**  

pingback.ping, which is a legit WordPress feature misused to DoS victims using legit WordPress sites.  

URL describing the issue: http://blog.sucuri.net/2014/03/more-than-162000-wordpress-sites-used-for-distributed-denial-of-service-attack.html  

**Method:**  

`  
pingback.pinghttp://victim.comwww.anywordpresssite.com/postchosen'  
`  

**Extent:**  

During may we collected 37705 pingback.ping request targeting various sites. This month it were sites that was facilitating DDoS attacks that was in focus, most likely from competition.  

**Top pick from list of requested resources**  

**Top pick from list of requested resources**

| Resource                                                                 | Count  |
|--------------------------------------------------------------------------|--------|
| /wp-content/plugins/yd-recent-posts-widget/timthumb/timthumb.php?src&sa&sa | 44348  |
| /xmlrpc.php                                                              | 37918  |
| /awstats/awstats.pl                                                      | 10917  |
| /awstats/awstats.pl?framename=mainright&output=refererpages              | 9319   |
| /PMA/index.php                                                           | 7444   |
| /wp-login.php                                                            | 5609   |
| /pma2005/index.php                                                       | 5224   |
| /phpMyAdmin-2.6.3/index.php                                              | 5182   |
| /phpMyAdmin-2.2.3/index.php                                              | 5017   |
| /phpMyAdmin-2.5.7/setup.php                                              | 4883   |
| /phpMyAdmin/                                                             | 4541   |
| /phpMyAdmin-2.6.4-rc1/index.php                                          | 4442   |
| /bb_lib/index2.php                                                       | 4435   |
| /administrator/index.php                                                 | 4171   |

And ..  

| Resource            | Count | Reference                                                                 |
|---------------------|-------|--------------------------------------------------------------------------|
| /cgi-bin/rtpd.cgi   | 252   | [D-Link IP Cameras Multiple Vulnerabilities](http://www.coresecurity.com/advisories/d-link-ip-cameras-multiple-vulnerabilities) |

This was a small excerpt from the collected data. I hope this encouraged you to continue to have hpfeeds enabled (or to enable it, if you have turned it off) on your honeypot/honeypots as the data gives a very valuable insight into current threats globally.  

**System reference:**  

“Glastopf is a Honeypot which emulates thousands of vulnerabilities to gather data from attacks targeting web applications. The principle behind it is very simple: Reply the correct response to the attacker exploiting the web application.”  

For more information please visit:  
http://www.glastopf.org/index.php or https://github.com/glastopf/glastopf  

All data was collected using hpfriends, for more information please visit: http://hpfriends.honeycloud.net/
