---
title: "Project Honeynet “Log Mysteries” Challenge Lessons"
authors: ["Anton Chuvakin"]
date: "2010-11-10"
tags: 
  - "challenge"
  - "lessons-learned"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

We just finished grading the [results](https://honeynet.org/challenges/2010_5_log_mysteries) of [Project Honeynet “Log Mysteries” Challenge #5](https://honeynet.org/node/581) and there are some useful lessons for BOTH future challenge respondents and to log analysts and incident investigators everywhere.

  
  

If you look at the challenge at high level, things seem straightforward: a bunch of log data (not that much data, mind you – only  [1.14MB compressed](https://www3.honeynet.org/wp-content/uploads/attachments/sanitized_log.zip)) from a Linux system. You can squeak by even if you use manual analysis and simple scripting. Fancier tools would have worked too, of course. The questions lead you to believe that compromise might have occurred.

  
  

Overall, people did get to some of the truth, but there were a few lapses which are worth highlighting.

  
  

First, justifying that a login activity pattern is malicious was required. Yes, a very long (hundreds) string of login failures followed by success, all from the same IP address in China, smells very fishy,  but shorter login sequences theoretically can be legit. Few people chose to justify it – in all their excitement after finding a compromise. Jumping to conclusions is one of the biggest risks during the incident investigations, especially if things can go to court.

  
  

Second, just because you found reliable compromise indication does not mean there isn’t more – of the same OR completely different type. You got the login  brute forcing via SSH, now check for web app hacking, will ya? More successful attacks in the same log? Anything of the same sort in other logs? Anything completely different but just as ominous? Finding one means little – cast a wide net again and again, even after you find reliable signs of system compromise. A good approach is to pretend that you found nothing and then try harder!

  
  

Third, post-compromise activity investigation is often as important as incident detection. Yeah, we got 0wned by “parties unknown.” And? What did the parties do after they got root? Did they drop an IRC bot to chat with their buddies or did they clean your crown jewels? Did they impact other systems and possibly other business processes? Maybe they DoS’d NSA from your box and that whirring noise you are hearing is a mean-looking SWAT team heli-dropping on your data center roof….? ![Smile](images/-wlEmoticon-smile2.png)

  
  

Finally, everybody chose to ... not succeed at my trick question about timing: “How certain are you of the timing?” Everybody was in the range from “certain” to “fairly sure.” Guys, you are given a bunch of logs by somebody possibly untrusted (me, in this case). How on Earth can you be sure about timestamps in the logs reflecting reality? Did you set up that NTP server? Did you check it before the incident? Did you maintain chain of custody of logs after they were captured? But WHY!? Of course, you cannot be sure at all about the _absolute time_ and you can make a reasonably good bet that _relative to themselves log timestamps_ are consistent. A good bet, BTW, is not the same as being certain. An opposing side lawyer will tear you  a new one in a second if you show up with that “certainty” in a court of law…

  
  

There was also an open-ended question about attacker motivations. Why did we ask it – think about it! So that you can learn a more social part of investigative trade. What can you hypothesize and prove? What can you learn by comparing this case with other cases you might have seen or even read about? Is this hot APT stuff? Or is this a lone monkey-boy who can barely type?

  
  

Regarding commercial [SIEM](http://chuvakin.blogspot.com/search/label/SIEM) correlation tools: IMHO many should have picked this bruteforcing by using basic correlation rules (if count\[login\_failure\]>100 _followed by_ login\_success _where_ src IP = same across all failures and success, then alert). Check your tool and make sure you have rules like this (or [hire somebody](http://www.securitywarriorconsulting.com) to build you a useful correlation ruleset ![Smile](images/-wlEmoticon-smile2.png)), even OSSEC can be used for this! Your exposed DMZ servers might be owned already ![Smile](images/-wlEmoticon-smile2.png) 

  
  

More challenges [are coming!](https://www.honeynet.org/challenges)

  
  

Possibly related posts:

  
  

  

  
- 
    
    ###### [Incident Log Review Checklist](http://chuvakin.blogspot.com/2010/03/simple-log-review-checklist-released.html)
    
      
    
  
  
- 
    
    ###### [Fun Project Honeynet Log Challenge: Log Mysteries](http://chuvakin.blogspot.com/2010/09/fun-project-honeynet-log-challenge-log.html)
    
      
    
  
  
- 
    
    ###### [Public Log Sharing Site: logs for research](http://log-sharing.dreamhosters.com)
    
      
    
  
  
- 
    
    ###### [Presentation on logs for incident response](http://chuvakin.blogspot.com/2009/10/another-old-presentation-first-2006.html)
    
      
    
  

  

  
  

[![Enhanced by Zemanta](https://img.zemanta.com/zemified_e.png?x-id=8ade0cee-482c-4d3d-a0c7-d12f827a32a5)](http://www.zemanta.com/ "Enhanced by Zemanta")

  
  
  
Updated by [Anton Chuvakin](http://www.chuvakin.org)
