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
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

**During the month of May the following information was obtained from Glastopf installations worldwide**  
  
**Number of alert for the period:** 1859863  
  
**Filenames (RFI) - 10 most popular during the period:**  
  
  
  
  
  
  
  
  
  
  
  
  
  

<table><tbody><tr><td>Hash:</td><td>Hits:</td></tr><tr><td>48101bbdd897877cc62b8704a293a436</td><td>2425</td></tr><tr><td>4997ed27142837860014e946eed96124</td><td>2050</td></tr><tr><td>d070c4cccf556b9da81da1e2de3cba54</td><td>644</td></tr><tr><td>3cc11c8fa7e3e36f0164bdcae9de78ec</td><td>330</td></tr><tr><td>ab4d03072cc0532afc83d13854ed7e4f</td><td>286</td></tr><tr><td>8f8adad762a39ba298b9ee8b7555acf3</td><td>261</td></tr><tr><td>474c4daeff3d82ae49d7c96acb8c0d84</td><td>208</td></tr><tr><td>e5f9687d94bf23f395799dec3fcafc3f</td><td>199</td></tr><tr><td>873f84fe2b641c2934203c7f6621b7fb</td><td>167</td></tr><tr><td>7de0bcb903eaba7881c6d03a8c7769a8</td><td>124</td></tr></tbody></table>

  
  
  
  
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
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

<table><tbody><tr><td>Resource:</td><td>Count:</td></tr><tr><td>/wp-content/plugins/yd-recent-posts-widget/timthumb/timthumb.php?src&amp;sa&amp;sa</td><td>44348</td></tr><tr><td>/xmlrpc.php</td><td>37918</td></tr><tr><td>/awstats/awstats.pl</td><td>10917</td></tr><tr><td>/awstats/awstats.pl?framename=mainright&amp;output=refererpages</td><td>9319</td></tr><tr><td>/PMA/index.php</td><td>7444</td></tr><tr><td>/wp-login.php</td><td>5609</td></tr><tr><td>/pma2005/index.php</td><td>5224</td></tr><tr><td>/phpMyAdmin-2.6.3/index.php</td><td>5182</td></tr><tr><td>/phpMyAdmin-2.2.3/index.php</td><td>5017</td></tr><tr><td>/phpMyAdmin-2.5.7/setup.php</td><td>4883</td></tr><tr><td>/phpMyAdmin/</td><td>4541</td></tr><tr><td>/phpMyAdmin-2.6.4-rc1/index.php</td><td>4442</td></tr><tr><td>/bb_lib/index2.php</td><td>4435</td></tr><tr><td>/administrator/index.php</td><td>4171</td></tr></tbody></table>

  
  
And ..  
  
  
  
  

<table><tbody><tr><td>Resource:</td><td>Count:</td><td>Reference:</td></tr><tr><td>/cgi-bin/rtpd.cgi</td><td>252</td><td>http://www.coresecurity.com/advisories/d-link-ip-cameras-multiple-vulnerabilities</td></tr></tbody></table>

  
  
This was a small excerpt from the collected data. I hope this encouraged you to continue to have hpfeeds enabled (or to enable it, if you have turned it off) on your honeypot/honeypots as the data gives a very valuable insight into current threats globally.  
  
  
**System reference:**  
  
“Glastopf is a Honeypot which emulates thousands of vulnerabilities to gather data from attacks targeting web applications. The principle behind it is very simple: Reply the correct response to the attacker exploiting the web application.”  
  
For more information please visit:  
http://www.glastopf.org/index.php or https://github.com/glastopf/glastopf  
  
All data was collected using hpfriends, for more information please visit: http://hpfriends.honeycloud.net/
