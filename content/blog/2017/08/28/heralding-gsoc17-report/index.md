---
title: "Heralding GSoC17 Report"
date: "2017-08-28"
categories: 
  - "gsoc"
tags: 
  - "gsoc-d20"
  - "gsoc2017"
  - "heralding-d24"
---

The summer is coming to the end as well as my GSoC17 happy days. So, now it’s time to sum up the results and say goodbye to the GSoC until the next year.

  
  

## My impressions about working on the Heralding project

  

Working on the Heralding project was awesome experience for me. I feel I did something helpful, fun and challenging at the same time. I hadn’t wanted anything else before the summer!

  

## What work was done?

  

  

  
- Heralding was ported from Python 2 to Python 3.
  
- Heralding was ported from gevent to asyncio.
  
- IMAP capability was implemented.
  
- Various bugfixes and code cleanups.
  
- Fixing [issue #17](https://github.com/johnnykv/heralding/issues/17) and [issue #22](https://github.com/johnnykv/heralding/issues/22)
  

  

  

## What code got merged?

  

Almost all the code, I wrote during the summer, was merged and can be found here:  
[https://github.com/johnnykv/heralding/commits/master/?author=kajojify](https://github.com/johnnykv/heralding/commits/master/?author=kajojify)

  

## What’s left to do?

  

My summer plan is 100% complete, so according to it, nothing is left to do.  
  
But there is much work beyond the plan:  

  
- Finish implementing VNC capability.
  
- Investigate speed difference between gevent and asyncio versions.
  
- Adapt Heralding to work with all popular bruteforcers.
  
- Continue to work on implementations of other protocols.
  

  

  

## The current state of the project

  

New [“logging” branch](https://github.com/johnnykv/heralding/tree/logging) was created. We are developing the protocols, where we can log the username, but not the password. All future PRs will be merged to “logging” branch.  

  

## Challenges

  

Honestly, when I started working on Heralding, I didn’t think I would have any difficult challenges during the summer. I was wrong:  

  
- When Heralding was Python 2 based, it used telnetsrvlib module for telnet protocol. The thing was, this module didn’t have Python 3 version and there weren’t any suitable analogues. So, when I started porting Heralding to Python 3, I had to port telnetsrvlib as well. It wasn’t easy for me.
  
- Porting gevent to asyncio was pretty challenging. The most difficult things were to save Heralding structure after porting and reduce the number of third-party modules.
  
- Since I often used popular bruteforcers (Hydra, Medusa, Ncrack) to test changes I did, I always had problems with them. Sometimes, after one more change in the Heralding, Medusa stopped working, but Hydra continued. I had to read their source code in order to figure out the problem and it wasn't a single case.
  

  

  

## Learnings

  

  

  
- Improved my programming skills.
  
- Improved problem solving skills.
  
- Deepened the knowledge of many network protocols and their authentication mechanisms.
  
- Knew the details of difference between Python 2 and Python 3.
  
- Learnt a lot about gevent, asyncio and asynchronous programming in general.
  
- Got acquainted with Hydra, Medusa and Ncrack bruteforcers, using them for legal purposes.
  
- Improved English and communicating skills.
  

  

  

## Special thanks

  

I want to thank my mentor, [Johnny Vestergaard](https://www.linkedin.com/in/johnnykv), for responsible approach, professionalism, patience and many-many other cool things, which I faced during the summer.  
  
I want to thank The Honeynet Project administrators for true taking care of students.  
  
I want to thank Google for a great possibility to dive into the world of open source.  
  

  

##### [Samoilenko Roman](https://www.linkedin.com/in/roman-samoilenko-ab041114a)
