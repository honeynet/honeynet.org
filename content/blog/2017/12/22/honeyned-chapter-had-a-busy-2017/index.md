---
title: "HoneyNED chapter had a busy 2017"
authors: ["Rogier Spoor"]
date: "2017-12-22"
categories: 
  - "chapters"
tags: 
  - "chapter"
  - "honeyned"
  - "report"
coverImage: "preview.png"
---

**This is a contribute by HoneyNED chapter from the Netherlands about all their 2017 activities.**

As the end of the year has come, we from HoneyNED, the Dutch Honeynet chapter, want to share what has happened during the year. We have worked on several projects in the honey space and a few members represented our chapter at the annual Honeynet workshop hosted in Australia. In this post, we will discuss what honeypots have been deployed, what projects are in the pipeline and what will be the focus in 2018. But let’s start by thanking the Honeynet community for all knowledge sharing, collaboration and code-sharing.

Honeypots

Since a while we have  multiple Cowrie SSH honeypots deployed, this year we were able to obtain a non-profit license from Splunk for 10GB a day which was an incredible acquisition as we were able to start collecting and analysing all the logs in one central solution. Together with a grant from Amazon on their EC2 platform,  we’re able to easily deploy multiple honeypots.

As we now have a good basis for collecting the data, we created a docker compose file which automated the installation and configuration of Cowrie honeypots and logging to Splunk so we could expand more quickly in the future.

 

![](https://lh4.googleusercontent.com/oNpUujCbOIuQBHbJTTeaLLGjHvNKJqv4vL1mx0w4_wFBUtVwuZc9NQBbwyc4Etqv8UiF07UlFNV0YY9alnfCYTMlK7_TSAvV37SJF-vWdwDJGs9lNa9RBepWsszvyvatH-h5igLM)

Image 1: Honeypot activity of the last 3 months. Every color is a different honeypot

 

Sometimes some of them stopped unexpectedly as the data shows. Currently we restart the  honeypots manually, the idea is to make this automatic soon. We are being informed that a sensor is down via an alert sent from Splunk to our Slack channel, as seen in image 2.

 

![](https://lh6.googleusercontent.com/Wx28FNQAvvEfcB8qMRnfARAz4XWEaryHVnrklLJ0tLu5np7kLsA4QL1vhC33ANndi0mDamGrmGkSe1NrN_bkn4wHDCS34SoznsDtvkZl-hFuxesaA_GRrHCeuUOmR7tO-b5oUYXG)

Image 2: Slack alert from Splunk

With the help of the Tango Intelligence app some interesting statistics are available.

![](https://lh4.googleusercontent.com/5zDmlNz-UMlAYyqJWhRiHVUzmoOwmgewBgO6KMSrS_jWnpOzlezRlna6-AHNKwJl0sKPVjvMlmem_XpZH20JUqX8uABeHeiDjaCN6QynFI4k7NOQBccKLbjZuHJZpNkJtoy88ss6)

Image 3: High level overview of the last 30 days

![](https://lh5.googleusercontent.com/Z6aAt2c0CJThc6I1IdHv7s1_75ktqz2bQJXohZrzIzsYQezadrPFqpOacQKF5HXGcykVfv9kYeZ5IucrfEhcostWU7j-WGL3IZMpTM3ECFXRFx16nykQIaZuDJWi7vJNVK5tbl3A)

Image 4: Top 10 users and passwords from October till the 19th of December

![](https://lh5.googleusercontent.com/Ep3p_xN1wplWkgBalo7ihI0fSDbpV0o_hh6lSDcHGEOZdc_IoBbHpMPj_H994CZ-mcc3n9abLNaLpqOfRVmH7WWe7stx58vjSqpXsY6qQxMB4MLLPQUL80pldww76WfRzZHK69pN)

Image 5: Scanning location overview of the last 30 days

Lastly, we are grouping together scans by hashing the commands and listing the different countries, IP’s and via lookup which ISP the scanning IP belongs to.

 

![](https://lh4.googleusercontent.com/K7EQEXy90T1Y72hxxLfSZC6hK2s-kYiQ7CpIdFmDDCIQ2yCqean3CJNTDzt4Pragem5DoY_r0Mud54iItZLrMdN-bTJ2zojBR90LZxfvdCzAFghERn2zj45wCsDBr-uUmqZy8cbS)

Image 6: Scan correlations

 

Other projects

Next to our honeypots  some different projects are running within the chapter. A small subset:

- URL shortening honeypot
- Setting up MISP has been completed to share information with a broader community
- Temporary mail service
- Phish Catcher
- Pastebin Scraping
- Collect more data :)

Workshop

We had a blast!! Three members from our chapter got the opportunity to attend the annual workshop, this year held in Canberra. Ben Whitham did a very good job in organizing the whole thing and he really deserves all the credits for that. For us it was a very fruitful meeting, met old friends and made some new ones. We hope we can work together on some projects the upcoming year. We really hope the data sharing breakout session will lead to some concrete plans and implementation of a collaborative data sharing platform. Our offer to develop a Gollum to MISP plugin still stands!

Roadmap

For 2018, we want to keep working on promoting Honeynet and our chapter, sharing intelligence with peers and the community and continue to deploy honeypots and work on projects together.

Have a great and safe 2018!

The HoneyNED Chapter
