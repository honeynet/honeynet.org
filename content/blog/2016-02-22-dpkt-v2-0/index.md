---
title: "dpkt v2.0"
date: "2016-02-22"
categories: 
  - "gsoc"
tags: 
  - "dpkt"
  - "gsoc-d20"
  - "python-d32"
---

### What is dpkt?

  

[dpkt](https://github.com/kbandla/dpkt/) is a Python library that helps with "_fast, simple packet creation/parsing, with definitions for the basic TCP/IP protocols_". It supports a lot of protocols (currently about 63) and has been increasingly used in a lot of network security projects. It is 44x faster than `Scapy2`, and 5x faster than `Impacket3`. With `Scapy` no longer in development, `dpkt` is the only network creation/parsing library for Python that is active.

  

### GSoC 2015 : dpkt v2.0

  

For the Google Summer of Code 2015, one of the projects at The Honeynet Project was improving the dpkt library. Hao Sun, a student of Peking University, China worked on this project for 3 months. At the end of these 3 months, we were able to have a branch of dpkt which worked on Python 2.7 and later!

  

### Which aspects need to be improved for dpkt?

  

Firstly the project needed more test cases, to expand the test coverage. Secondly it also needed to update the code to offer Python 3 support. Lastly some pending bugs or issues had to be solved, and the documentation needed to be improved.

  

### Hao's accomplishments during GSoC

  

  
- Made the dpkt [Python 3 compatible](https://github.com/kbandla/dpkt/tree/migrate_py3). The trick is that we need to keep support for Python 2 as well. There are many potential code updates to achieve this goal. Also this is the major job I've done during last summer. See technical details in the next section of this blog.
  
- Fixed bugs in the project issue queue
  
- Added some test cases to improve test coverage and also added a few documentations
  

  

### Approaches to migrate dpkt to Python 3

  

There were many changes that had to be made to make dpkt compatiable with Python3. A detailed technical discussion is available at Hao's [wiki](https://github.com/sunhao2014/dpkt/wiki/Migrate-Dpkt-to-Python-3-(Sub-project-of-GSoC-2015-Honeynet-Project))). Hao's detailed weekly logs over the 3 months of GSoC are available [here](https://github.com/sunhao2014/dpkt/wiki/dpkt-2.0)

  

### Future work

  

The migration related modifications are in a standalone branch has hasn't been merged to the master branch yet, after a thorough test, we will finish the merging and do the final release very soon. At the time of writing this blog,there are still 60 open issues on the dashboard, we are currently working on fixing them - one at a time. dpkt is a very cool library and it would be more popular if we can further improve its documentation and demos - something which we are still working on.  
This blog post was posted on behalf of Hao Sun.
