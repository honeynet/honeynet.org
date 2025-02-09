---
title: "Global Glastopf statistics for June 2014"
authors: ["Mikael Keri"]
date: "2014-08-08"
tags: 
  - "glastopf"
  - "logs"
  - "reports"
  - "statistics"
---

**During the month of June the following information was obtained from Glastopf installations worldwide**

**Geographical spread**

![](images/drupal_image_1181.png)

**10 most popular injected files during the period**

Short introduction to RFI:

“Remote File Inclusion (RFI) is a type of vulnerability most often found on websites. It allows an attacker to include a remote file, usually through a script on the web server. The vulnerability occurs due to the use of user-supplied input without proper validation. This can lead to something as minimal as outputting the contents of the file or more serious events such as: Code execution on the web server .. “ source: Wikipedia

| **Hash**                               | **Hits** | **VirusTotal detection ratio** |
|----------------------------------------|----------|---------------------------------|
| 30a7bb30303f7da9ad102edc313dc80e       | 929      | 0 / 52                          |
| ab4d03072cc0532afc83d13854ed7e4f       | 577      | 22 / 49                         |
| 474c4daeff3d82ae49d7c96acb8c0d84       | 514      | 21 / 53                         |
| 9f67913d2c77545a4187053ad18230e4       | 496      | 7 / 52                          |
| 369aab6f3a40d0259e6b036b68c27d25       | 411      | 7 / 54                          |
| 10b5c4f77bbd80a3886e591dc3426198       | 267      | N / A                           |
| 6427bb17f4922b82c0147099429cfef9       | 203      | 3 / 53                          |
| be52cd4e8a8f6e42418c87d3468bba20       | 191      | 9 / 51                          |
| f922514cec9b9dc9c74b99ce9e39d3bc       | 164      | 15 / 53                         |
| 46f5757064a2a0a081d6fd099f2916b5       | 159      | 18 / 46                         |

Note: VirusTotal scan was performed on the 20:th of July 2014. N/A means that the injected binary was no longer present at it's original location and no sample could be acquired

**Top pick from list of requested resources**

Glastopf is a web application Honeypot which emulates vulnerabilities and lures the attacker that the requested service/application is vulnerable to gather data from attacks targeting web applications.

| **Resource**                                                                 | **Count** |
|------------------------------------------------------------------------------|-----------|
| admin                                                                        | 467194    |
| administrator/index.php                                                      | 73285     |
| changes.html                                                                 | 13193     |
| wp-login.php                                                                 | 11248     |
| awstats/awstats.pl                                                           | 9961      |
| robots.txt                                                                   | 8620      |
| xmlrpc.php                                                                   | 8175      |
| index.php?app=core&module=global§ion=login&do=process                        | 7339      |
| phpMyAdmin-2.5.5/index.php                                                   | 3738      |
| phpMyAdmin-2.5.5-pl1/index.php                                               | 3712      |
| awstats/awstats.pl?framename=mainright&output=refererpages                   | 3538      |

**Other requests that are interesting to highlight**

| **Resource**                  | **Reference**                                                                 | **CVE**         |
|-------------------------------|-------------------------------------------------------------------------------|-----------------|
| plugin_googlemap2_proxy.php   | [http://securityvulns.ru/docs29645.html](http://securityvulns.ru/docs29645.html) | CVE-2013-4764   |
| HNAP1/                        | [http://tools.cisco.com/security/center/viewAlert.x?alertId=32899](http://tools.cisco.com/security/center/viewAlert.x?alertId=32899) | CVE-2013-5122   |
| rom-0                         | [http://www.exploit-db.com/exploits/33803/](http://www.exploit-db.com/exploits/33803/) | CVE-2014-4019   |
| cgi-bin/rtpd.cgi              | [http://www.coresecurity.com/advisories/d-link-ip-cameras-multiple-vulnerabilities](http://www.coresecurity.com/advisories/d-link-ip-cameras-multiple-vulnerabilities) | CVE-2013-1599   |

**And a few findings that we found extra interesting**

**TimThumb Remote Code Execution: webshot**

**About**

TimThumb is a small php script for cropping, zooming and resizing web images (jpg, png, gif).

**Exploitation**

`http:///wp-content/themes//path/to/timthumb.php?webshot=1&src=http:// $()`

Please see the URL below for more information about this vulnerability **URL** http://cxsecurity.com/issue/WLB-2014060134

**Example of collected requests** `http:///wp-content/themes/eGallery/HTTP/wp-content/themes/eGallery/timthumb.php?webshot=1&src=http:///$(ls)`

http:///wp-content/themes/eGallery/HTTP/wp-content/themes/eGallery/timthumb.php?webshot=1&src=http:///$(touch$IFS/tmp/a.txt)

`http:///wp-content/themes/eGallery/HTTP/wp-content/themes/eGallery/timthumb.php?webshot=1&src=http:// /$(cat$IFS/etc/passwd)`

**WordPress Pingback.ping DDoS attempts**

**About**

pingback.ping, is a legit WordPress feature misused to DoS victims using legit WordPress sites.

Please see the URL below for more information about this vulnerability **URL** http://blog.sucuri.net/2014/03/more-than-162000-wordpress-sites-used-for-distributed- denial-of-service-attack.html

**Exploitation**

`pingback.pinghttp://victim.com www.anywordpresssite.com/postchosenparam>'`

**Victims per category**

In an attempt to visualise the type of targets for these attacks we took the help of the public available resource: sitereview.bluecoat.com to categorise the targeted sites

![](images/drupal_image_1182.png)

Many of the sites categorised as not yet rated by the webfilter vendor, ended up being sites offering DDoS services, many of them protected by legit DDoS protection services.

**WordPress wp.getUsersBlogs brute force attempts**

**Comment** We were able to quickly detect wp.getUserBlogs attempts when they "started", now a month later there are several blog post describing the issue.

The first occurrences detected was on the 29:th of June, targeting only a limited amount of Honeypots and originated from two European countries.

**About** "This attack is being made possible because many calls in the WordPress XMLRPC implementation required a username and password. It these attacks, we are seeing wp.getUsersBlogs being used (and very few times wp.getComments), but it could be other calls as well. If you provide a user and a password to them, it will reply back if the combination is correct or not:" sucuri.net

Please see the URL below for more information about this vulnerability **URL** http://blog.sucuri.net/2014/07/new-brute-force-attacks-exploiting-xmlrpc-in-wordpress.html

**Exploitation** `wp.getUsersBlogs admin112233`

**Passwords**

The list is quite long, so here is a small sample

| **Password** | **Password** | **Password** |
|--------------|--------------|--------------|
| password     | melody       | master       |
| gogogo       | "name of the domain" | admin |
| 12345678     | trustno1     | test         |
| secret       | reset123     | qwerty123    |
| pass         | [redacted]   | audrey       |
| admin123     | 1qaz2wsx     | 123          |
| 12345        | 123456       | 123456789    |
| 1111         | zaq12wsx     | yellow       |
| wisdom       | winter       | windows      |

**Summary**

This was a small excerpt from the collected data. I hope this encouraged you to continue to have hpfeeds enabled (or to enable it, if you have turned it off) on your honeypot/honeypots as the data gives a very valuable insight into current threats globally.

**System reference:**

“Glastopf is a Honeypot which emulates thousands of vulnerabilities to gather data from attacks targeting web applications. The principle behind it is very simple: Reply the correct response to the attacker exploiting the web application.”

For more information please visit: **URL** http://www.glastopf.org/index.php or https://github.com/glastopf/glastopf

All data was collected using hpfriends, for more information please visit **URL** http://hpfriends.honeycloud.net/
