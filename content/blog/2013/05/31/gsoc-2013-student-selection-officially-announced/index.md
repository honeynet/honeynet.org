---
title: "GSoC 2013 Student Selection Officially Announced"
authors: ["David Watson"]
date: "2013-05-31"
categories: 
  - "gsoc"
tags: 
  - "gsoc-d20"
  - "gsoc2013"
coverImage: "gsoc2013_accepted_stats_1.png"
---

After a pretty hectic few weeks of student application review, setting and scoring coding challenges, and assessing proposals, mentoring organizations participating in [GSoC 2013](http://www.google-melange.com/gsoc/homepage/google/gsoc2013) had to confirm their student slot allocations and final short list of preferred candidates by [Friday May 24th at 19:00 UTC](https://google-melange.appspot.com/gsoc/events/google/gsoc2013). This is always one of the most difficult periods for us, with many tough decisions required trying to balance the best mix of students/projects/mentors into a limited number of student slots. It is always less that we would ideally like, making it impossible to keep everyone happy, and often pretty challenging. This year was no different, with a lot of late nights and last minute debate.  
  
De-duplication between orgs passed easily this time, since almost all of our top students only applyied to us. The weekend gave tired mentors and org admins the chance to sleep while Google finalized and confirmed student selections.  
  
On [Monday May 27th at 19:00 UTC](https://google-melange.appspot.com/gsoc/events/google/gsoc2013), Google [officially announced](http://google-opensource.blogspot.co.uk/2013/05/students-announced-for-google-summer-of.html) the list of 1194 lucky [students accepted](http://www.google-melange.com/gsoc/projects/list/google/gsoc2013) to participate in [GSoC 2013](http://www.google-melange.com/gsoc/homepage/google/gsoc2013). Cue much rejoicing or unhappiness for thousands of students worldwide.  
  
As repeating GSoC mentoring organisation, The Honeynet Project were very happy to once again be allocated 15 student slots by Google. Our congratulations to those students who were accepted, and our commiserations to those who we unfortunately could not accept this year.  
  
The names of our officially accepted GSoC 2013 students can be found on the official Melange site (filter the results by Organization = "The Honeynet Project"):  
  
[http://www.google-melange.com/gsoc/projects/list/google/gsoc2013](http://www.google-melange.com/gsoc/projects/list/google/gsoc2013<br>)  
  
This year we feel we have a pretty strong line up, with a students and mentors from many different countries around the world working on a mix of new greenfield projects and also improvements to existing tools.  
  
Completely new projects include Cornelius Aschermann (DE) and Felix Glaser (DE) working on the backend/frontend of a new platform independent binary debugger and Guo Li (CN) working on a Standard Variable and Type Inference Library for use in reverse engineering of malicious code (all projects suggested by the students themselves).  
  
Although we could not work on everything we wanted to given the number of student slots available, improvement to existing tools include at the client honeypot level: Ruoyu Wang (CN) working on enhancing ROP detection features in our [Malicious Code Execution Detection Prevention (MCEDP)](https://github.com/shjalayeri/MCEDP) High Interaction Client Honeypot (now renamed pwnypot) and Tobias Jarmuzek (DE) integrating MCEDP/pwnypot with [Cuckoo Sandbox](http://www.cuckoosandbox.org) to improve management and detection (itself a previous GSoC project). We hope this should result in some powerful new honeypot capabilities. We also have Akshit Agarwal (IN) working on adding Distributed Task Queing to our existing [Thug honeyclient](https://github.com/buffer/thug), aiming at increasing distributed URL analysis scalability.  
  
On the networking front, Gürcan GERÇEK (TR) and Hao Ma (CN) will be working to extend our existing [Ovizart](https://github.com/oguzy/ovizart) network analyzer and add powerful new capabilities, while Joshua Bonsink (NL) will be exteding our existing [IMALSE: Integrated Malware Simulator and Emulator](http://people.bu.edu/wangjing/open-source/imalse/html/index.html) tool from GSoC 2012 to include better traffic generation and improved an GUI. Jianjun Chen (CN) will be working on expanding our existing [IPv6 (6Guard)](https://www.honeynet.org/node/944) honeypot, to ensure that the latest IPv6 attack techniques such as extension headers combinations, fragmentation techniques or RA-Guard bypass tricks are correctly handled.  
  
Visualization remains a focus area too, with Tanya Guza (UA) working to improve our hosted [Afterglow Cloud](http://afterglow.secviz.org/) data vizualization using D3.js, while Vincent Wei-Chen Kao (TW) will be improving [HpfeedsHoneyGraph](https://www.honeynet.org/node/957) for further visualizing malicious activities with D3.js graph generation, new graphs and timeline capabilites.  
  
Meanwhile we will also continue to explore new types of honeypots, with Aniket Panse (IN) working on tracking credential theft and abuse through the upcoming [Beeswarm](https://github.com/honeynet/beeswarm) honeytoken system. Rahul Binjve (IN) will be extending and improving the deployability of our [SHIVA – Spam Honeypot with Intelligent Virtual Analyzer](https://github.com/honeynet/shiva) project, and last but definitely not least, Maximillian Hils is returning to GSoC again to continue his previously excellent GSoC 2012 work on [HoneyProxy](http://honeyproxy.org/) for HTTPS MITM application analysis.  
  
We wish all of our selected students (and mentors) the best of luck with their projects this summer. You can keep track the progress of each of our accepted GSoC 2013 projects via our [student slots page](gsoc/slots).  
  
Although we know that many students who applied unfortunately were not accepted, please don't take this as a personal failing. With more than 5 students applying per available student slot available and less slots than project ideas or mentors, even before students suggested 10+ of their own project topics, we had to make a number of very difficult decisions and couldn't support every good student application or project topic.  
  
Following on from my [recent](https://www.honeynet.org/node/1046) and [previous](https://www.honeynet.org/node/840) posts about GSoC statistics, for comparison:  
  
In 2012, 180 of 406 mentoring orgs were accepted. 4258 students submitted 6685 proposals, of which 1212 were accepted. The Honeynet Project received 82 student applications, which was 1.23% of the total student applications submitted, and was offered 15 funded student project slots by Google.  
  
In 2013, 177 of 417 mentoring orgs were accepted. 4144 students submitted 5999 proposals, of which 1192 were accepted. The Honeynet Project again received 82 student applications, which was 1.37% of the total student applications submitted, and again was offered 15 funded student project slots by Google.  
  
It is nice to see that our gentle upwards trend in percentage of overall student applications received has continued (and even better, many of our selected students only applyied to us). Reducing the number of possible applications seems to have slightly reduced the number of student applications, but not hugely, and did not really seem to impact the quality or level of spam proposals we received this year.  
  
Compared to [last year](https://www.honeynet.org/node/858), we had more a more balanced mix of early and late student applications being selected:  
  
![](images/gsoc2013_accepted_stats_1.png)  
  
Although still very international, with a number of Chinese and German students being selected, our overall geographic converage of students and mentors is slightly less wide:  
  
![](images/gsoc2013_accepted_stats_2.png)  
  
The [next GSoC 2013 milestone](http://www.google-melange.com/gsoc/events/google/gsoc2013) is [June 17th](https://google-melange.appspot.com/gsoc/events/google/gsoc2013), when student coding officially begins. Until then, GSoC is in the [Community Bonding Period](http://googlesummerofcode.blogspot.co.uk/2007/04/so-what-is-this-community-bonding-all.html), and students and mentors should be making initial contact, discussing the detail of their project, agreeing how they will work and communicate together, building personal relationships and becoming familiar with our tools, processes and community. For the org admins, we will be busy setting up credentials, getting access to supporting project resources, establishing and verifying communication channels, and ensuring adequate discussing and planning for each GSoC 2013 project.  
  
Students - please remember - only code written between the official GSoC coding period of June 17th to September 23rd counts for project assessments. However, you can do preparation, planning, prototyping, testing, research, etc before then, so please try and make as constructive use as possible of the community bonding period as you can.  
  
Thanks to everyone involved for all their hard work and enthusiasm, and your interest in The Honeynet Project and Google Summer of Code 2013. We really appreciate your motivation and energy, and hopefully the last few weeks will prove to be the starting steps to some great new projects and some future Honeynet Project members (whether officially accepted for GSoC 2013 or not). Fingers crossed we'll get the chance to meet at least some of you face to face next spring at our next annual workshop, when you'll hopefully be demoing your new tools.  
  
It is definitely going to be another busy summer, but we would not have it any other way. Happy coding! :-)
