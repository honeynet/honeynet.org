---
title: "The new version of dorothy2 is out!"
authors: ["Marco Riccardi"]
date: "2014-10-27"
tags: 
  - "dorothy"
  - "forensics"
  - "sandbox"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

Howdy all,  
The Italian Chapter is proud to release the latest version of [dorothy2](https://github.com/m4rco-/dorothy2) (our ruby-based malware analysis framework) :).  
The new features introduced by this versions are severals. A lot of work has been done on the core system, by making the whole system even more [modular](http://www.honeynet.it/wp-content/uploads/dorothy2-structure.pdf) and customisable. A dummy webgui written in Sinatra has been also introduced, in order to let the analyst able to browse within the results. Binaries can now also be directly uploaded from the web.  
A particular attention has been dedicated on the network part: on the sample's resume page the analyst will now able to download the pcap of every single network flow in order to manually analyse it whenever needed.  
This version also introduces the use of the "analysis profiles" which give the researcher the possibility to run analyses on a set of binaries by using different environments (OS versions, sandbox timeout, number of screens, etc). As it is known, some malwares might run only in specific environment and this feature could guarantee the successful execution of those. A CSIRT might also use this feature to test suspicious malwares only against an environment that reflects the one of its customers. Sources can also be configured to be automatically analysed by certain profiles (e.g. use Profile\_Windows\_30sc for all the binaries retrieved by Kippo\_source).  
Lastly, Dorothy is now able to fetch binaries also from a mailbox (also if an email is forwarded "As Attachment"). This could be useful for everyone who wants to setup an analysis email sinkhole, and redirects all the incoming SPAM there.  
  
The [readme](https://github.com/m4rco-/dorothy2/blob/master/README.md) gives a good overview of the new modular structure. A detailed wiki will be soon available in order to document all the goodies of this tool.  
  
Don't hesitate in contacting [us](mailto:dorothy2@googlegroups.com) for sharing your feedbacks or to ask for support!  
  
To try it, just type:  
gem install dorothy2  
  
Hope you'll enjoy it,  
m4rco-
