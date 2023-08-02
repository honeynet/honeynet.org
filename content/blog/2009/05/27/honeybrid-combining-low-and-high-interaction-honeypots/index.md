---
title: "Honeybrid: combining low and high interaction honeypots"
authors: ["Robin Berthier"]
date: "2009-05-27"
categories: 
  - "analysis"
  - "gsoc"
  - "honeypot"
tags: 
  - "gsoc-d20"
  - "honeybrid-gsoc-introduction"
---

The goal of this post is to introduce [myself](http://www.enre.umd.edu/~robinb/) and my [project](/gsoc/project6): my name is Robin Berthier and I just got my PhD from the [University of Maryland.](http://www.umd.edu) I'll be working this summer on improving [Honeybrid](http://honeybrid.sf.net), a hybrid honeypot architecture. I've been working with honeypot technologies for the past 4 years, and Honeybrid represents a central part of my dissertation. 

  

Honeypots are usually divided into two categories according to the level of interaction they provide to attackers. First, we have low interaction honeypots that emulates network services and collect the beginning of attack processes. And then we have high interaction honeypots that are identical to production machines and collect detailed information about attacks. These two types of honeypot offer complementary advantages and limitations. The goal of honeybrid is to combine the best of both world. As such, Honeybrid is a hybrid honeypot solution.

  

The key for this solution to work is to correctly filter incoming attacks. This task is achieved by something called the decision engine. This engine integrates different attack filtering criteria to allow Honeybrid to collect a large variety of attacks while keeping a high scalability. Attacks which are filtered out are handled by a low interaction front-end. Attacks which are filtered in are transparently redirected to a back-end of high interaction honeypots for further analysis.

  

The following diagram gives an overview of how Honeybrid interacts with the low and high interaction honeypots:

  

![Honeybrid Architecture](images/honeybridoverallarchite.jpg)

  

This filtering/redirection mechanism works pretty well and a prototype of Honeybrid has already been implemented and tested. My objective for this summer is to build a robust application out of it. My first task for this week is to get rid of a memory leak and a data corruption problem. Honeybrid is implemented in C and uses multiple threads, which means it's going really fast, but access to data structures is often difficult to debug. I will use [valgrind](http://valgrind.org/) to hunt down incorrectly freed variables, and I will study if it would not be better to switch from a threaded environment to an [event-based](http://monkey.org/~provos/libevent/ "libevent") environment.

  

  

* * *

  

If you are looking for more information about hybrid honeypots, I would suggest the following publications:

  

  
- [A hybrid honeypot architecture for scalable network monitoring](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.84.7009&rep=rep1&type=pdf "A hybrid honeypot architecture for scalable network monitoring"), by Bailey et Al. (2004)
  
- [GQ: Realizing a System to Catch Worms in a Quarter Million Places](http://research.microsoft.com/en-us/um/people/wdcui/papers/gq-techreport.pdf), by Cui et Al. (2006)
  
- [SGNET: A Worldwide Deployable Framework to Support the Analysis of Malware Threat Models](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=4555995), by Leita and Dacier (2008)
