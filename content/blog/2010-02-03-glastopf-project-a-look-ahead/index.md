---
title: "Glastopf Project: A Look Ahead"
date: "2010-02-03"
---

**Glastopf:**  
On January the 22nd I met [Sven](http://www.disenchant.ch/blog/about). Sven is a bachelor student at the [Bern university of applied sciences](http://www.bfh.ch/) and will write his thesis about Glastopf. During his work he will rewrite the current Glastopf unstable version, but when he will be finished the new version will have at least the same features like the previous version. The goals are: A much better modular structure, this means there is one core which directs every request to the modules. They store the data, emulating the vulnerability and compose the response which the core gives back to the attacker. There will be a much better classification of incoming attacks and the rules used for this will be totally detached from the source code to distribute them easily between different sensors. I will post some details as soon as we started the work. This also means that we will freeze the current unstable version to put all effort into the new version.  
  
**PHP Sandbox:**  
I’m working on a connection between Glastopf and a PHP sandbox to classify the collected samples. Furthermore there is the possibility to reply common requests to a Glastopf sensor with the same perfectly emulated reply from the sandbox. The collected bots have a great potential to help us to do some research on web server botnets. I cobbled a script together which extracts the command and control information from the PHP sandbox output and stores the data into a sqlite database which is getting used by a simple IRC bot to gather information about the web server botnets. As soon as I get some time I'll write a bit about my findings.  
  
**Project:**  
We are looking forward to intense our cooperations with interested universities and corporations. Especially with [1and1](http://1und1.de/) and the Bern university of applied sciences. We are also officially integrating some people who are already working within the project.  
  
**Mailing list:**  
To move Glastopfs support away from the IRC data nirvana, we got a mailing list from the Honeynet Project. You can subscribe on the web interface: [Mailman](https://public.honeynet.org/mailman/listinfo/glastopf), and browse the yet glorious archive right here: [Pipermail](http://public.honeynet.org/pipermail/glastopf/). I’m looking forward to see some good discussions ;)  
  
**Meeting:**  
At the end of March we are planning a meeting for interested peoples in Karlsruhe, Germany. The goal is to further the discussions, exchange knowledge, get to know each other and, of course, drink some beer :) . There also will be some short talks on how we continue with the project and some of us will talk about how they use Glastopf. More information and, in the near future, the schedule, can be found on our wiki: [GlasCon-3-2010](http://dev.glastopf.org/wiki/glastopf/GlasCon).
