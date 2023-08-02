---
title: "GSoC 2017: First Month Progress"
authors: ["Maximilian Hils"]
date: "2017-06-30"
categories: 
  - "android"
  - "gsoc"
tags: 
  - "gsoc-d20"
  - "gsoc2017"
coverImage: "gsoc.png"
---

![GSoC Logo](images/GSoC-logo-horizontal-800.png)

At the end of February we were very happy to [announce](https://twitter.com/ProjectHoneynet/status/836618999572152325) that The Honeynet Project had once again been selected to be a mentoring organization for Google Summer of Code (GSoC) 2017. Since then, there has a been a flurry of activity: We received more than 50 project proposals during the application phase, selected 14 fantastic students, set them up to work with us during the community bonding period, and now completed the first month of actual work! Now that the first tangible results are tickling in, it’s time to take a closer look at our students and see what they have achieved so far.

For this blog post, we asked one half of our mentors to share their students’ progress. I’m more than happy to say that all mentors are very pleased with their students, and we’re all excited to see how the summer will progress!

**Nikolaos Filippakis ([go-dpi](https://github.com/mushorg/go-dpi), mentored by Lukas Rist and Hugo Gascon)**: Niko is very self motivated, produces very high quality code and we are well ahead of schedule and have plenty of time now to focus on fun and challenging tasks. He started a project from scratch and did exceptionally good ground work, making sure we have good test coverage and continuous integration in place. I’m looking forward to get some in-the-wild experience with this project soon.

**Ziyue Yang ([Android sandbox detection and countermeasures](https://github.com/yzygitzh/ReDroid), mentored by Yuanchun Li)**: We have investigated many techniques that Android malware uses to evade test environment, and we have been working on detecting such malware through static analysis and dynamic analysis. The preliminary result has shown that the technique is able to detect some simple and common sandbox-evading behaviors. In next months we will explore more cases and try to integrate our techniques to real test environments.

**Ujjwal Verma ([Mitmproxy](https://github.com/mitmproxy/mitmproxy), mentored by Thomas Kriechbaumer)**: In this month, we bumped the coverage of 12 files in total to 100%, increasing the overall code coverage. The custom TLS client hello parser was replaced with a custom Kaitai Struct parser. We also added a content view for x-icon(.ico) files as they are quite common in mitmproxy. A PR for HTTP request & WebSocket message streaming is almost done as well but we've hit a roadblock on that one, hopefully it will be merged soon.

**Ravinder Nehra ([SNARE/TANNER](https://github.com/mushorg/tanner), mentored by Evgeniia Tokarchuk and Lukas Rist)**: In this month, Ravinder has improved the base architecture of all tanner emulators, implemented a new cmd injection emulator with docker, improved the existing LFI emulator, and added cookie support for attacks. I’m really happy with the great work so far!

**Matthew Shao ([Mitmproxy](https://github.com/mitmproxy/mitmproxy), mentored by Maximilian Hils and Clemens Brunner)**: In the last month, Matthew has raised the test coverage for mitmproxy’s web ui from a sad 0% to a fantastic 83%! In total, this increased mitmproxy’s entire line coverage from 82% to 87% and gives us much more confidence to implement new features without breaking things. We have also started implementing a new REST API for options and will build a user interface for this in the next cycle. :-)

**Yuru Shao ([Conpot](https://github.com/mushorg/conpot), mentored by Daniel Haslinger and Johnny Vestergaard)**: Conpot is a project that can be improved in a lot of ways, but as it comes with a whole little ecosystem of protocol stacks, you need to keep track of the bigger picture to do this right. Yuru spent the first month on fixing stuff that makes conpot easier to maintain and install, he also showed that he is flexible and able to work autonomously. The next weeks will be dedicated to the implementation of a new protocol stack that will make conpot an even more versatile industrial control honeypot.

**Bilal Arif ([Glutton](https://github.com/mushorg/glutton), mentored by Lukas Rist)**: Bilal continued where we left off before GSoC and keeps fixing issues and adding new features. I’m much more comfortable now promoting Glutton with the needed increase in stability. The work on the new features is coming along well and we are good on track in regards to our goals. Glutton is shaping into the generic honeypot we envisioned and is already a valuable tool in discovering new attack patterns.

**Roman Samoilenko ([Heralding](https://github.com/johnnykv/heralding), mentored by Johnny Vestergaard and Daniel Haslinger)**: Roman is doing good and is way ahead of schedule. In the first couple of weeks he implemented the imap protocol and converted the project to Python 3. In the coming weeks he will start converting from gevent to asyncio.
