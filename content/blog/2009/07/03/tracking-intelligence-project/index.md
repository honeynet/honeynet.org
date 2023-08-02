---
title: "Tracking Intelligence Project"
authors: ["Angelo Dellaera"]
date: "2009-07-03"
---

What is TIP? TIP stands for Tracking Intelligence Project. In my most beautiful dreams, TIP should be an information gathering  
framework whose purpose is to autonomously collect Internet threat  
trends. It's entirely written in Python using Twisted and bound to the Django framework in order to abstract the underlying database and to easily build a web interface to the data.

  

TIP is made up of a few modules which are totally independent one from the other but with each one feeding the other ones. Its design is based on a core module which acts as a kind of scheduler which schedules what we can call "first level modules" at a precise time in future or in response to a particular event.  
  
The first module I developed is about collecting information from sources of various kind such as projects which maintain domains/network addresses blacklists and then weighting these sources with some kind of metrics. I coded the core of this module and added just few sources to it. This module acts as a scheduler for submodules, one for each blacklist. When the submodule has done its work it notifies the upper scheduler and exits. When all the submodule are done the upper scheduler notifies the core which reschedules the update.

  

Another module I developed is about collecting information from spamtraps. Currently this module is being splitted into two submodules. The first submodule is scheduled right after the blacklist module and its target are spamtrap repositories such as the one at [untroubled.org](http://untroubled.org/spam/) which are generally updated daily. The second submodule is currently under development and its approach is quite different from the first one. Its targets are spamtraps located on mailservers which I administer. Few of these mailservers generate huge amounts of spam mails and this leads to great performance troubles if you try to download them by POP3/IMAP and then parse. A different approach was thought for situations like these. In fact, I developed a small agent which has to be run on the mailserver host. This agent loops listing the spam files in the maildir and parsing them without any network-based data transfer. When it has done, it saves the interesting data in a serialized form on the filesystem (through the Python cPickle module) and assigns to this data a version number. This allows a remote agent to ask the last version and download just the missing versions. This submodule was developed using Twisted Perspective Broker directly serializing on the wire saved data and currently defines a basic authentication mechanism too. While developing this submodule I was thinking that it could be nice to use it for sharing data between researchers coming from multiple spamtraps. Suggestions are welcome here.

  

Another module I developed is related to Fast-Flux tracking but few days ago I started thinking about the scalability limits of this module and realized its design was really awful. The approach was based on the idea of assigning a monitoring thread to each fluxy domain. This approach is well suited if the number of threads is quite small but not for what I was just realizing. First of all, when the number of threads starts growing the performance starts decreasing due to the Python Global Interpreter Lock which limits concurrency of a single interpreter process with multiple threads (and there are no improvements in running the process on a multiprocessor system). Moreover, it's really hard to guarantee each thread enough stack space for running not raising segmentation faults. For these reasons I decided to rewrite the module from scratch and currently I'm testing it. The new design is really simple, effective and scalable and I have to thank Jose Nazario, [Marcello Barnaba](http://sindro.me/) and Orlando Bassotto for the really interesting talks we had about this matter. Just one process and no monitoring threads. The code is written is such a way not to have blocking calls thus realizing a really asynchronous module. But when a domain starts being monitored there's the need to access to backend database thus requiring blocking calls. When this happens, the blocking calls are delegated to the Twisted thread pool with a cloned copy of the collected data in order not to compromise code scalability with not necessary locks. Moreover the module is now turning to be a Twisted Application of its own and the first tests done using the Twisted Epoll Reactor are absolutely encouraging.

  

Last but not the least TIP will be released as a GPL code as soon as it will meet the quality requirements I would like to reach so stay tuned!
