---
title: "A new infosec era? Or a new infosec error?"
authors: ["David Dittrich"]
date: "2013-03-11"
tags: 
  - "botnet"
  - "ethics"
  - "takedown"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

On March 4, 2013, a contest was held at the Nullcon conference in Goa, India, to see who could take over a botnet. The Times of India reported that [the prize money was provided by an Indian government official](http://timesofindia.indiatimes.com/city/goa/Will-support-cyber-security-initiatives-CM/articleshow/18899132.cms) and was [awarded to the Garage4Hackers](https://www.facebook.com/photo.php?v=574303972588033&set=vb.138904662794635&type=2&theater) team. The co-founder of the Nullcon conference, Antriksh Shah, said "At Nullcon Goa 2013, for the first time in the world the government has come forward and announced a bounty prize of Rs 35,000 to whoever provides critical information on the command and control servers of a malware recently found in one of the government installations in India," and then tweeted, "Dawn of new infosec era. Govt of India announced (and actually paid) first ever bounty (Rs. 35 k) at nullcon to take down a c&c." When asked whether this was a live botnet, or a simulated botnet held within a safe and isolated virtual network where no harm could result, [Nullcon](https://twitter.com/nullcon) tweeted, "it was a live campaign up since a couple of yrs and the malware was found in a gov. Infra."  
  
  
People may argue that a botnet that is active for over a year is a problem that needs to be dealt with. They may criticize law enforcement for not taking care of the problem. They may also argue that India is an autonomous country whose government can, as Shah put it, "\[show\] the first signs of government-community partnership in fighting cyber crimes in \[India\]."  
  
But I fail to see how this action can be [justified on any ethical grounds](http://ssrn.com/abstract=790585), on legal grounds, or conform with any international legal norms that I am aware of. A contest is the least controlled, riskiest, noisiest, and most irresponsible way to deal with a criminal botnet I can imagine. And [I have looked at a few botnet takedowns](http://staff.washington.edu/dittrich/talks/dcc2013_dittrich_botnets.pdf).  
  
I would really love to see some skilled reporters ask the Indian government official who put up the prize money and conference organizers to answer a few questions about this little stunt, and I hope everyone who applauded this action and congratulated the team on its victory thinks about them as well. We need to have ways to counter botnets, but this is _not_ the way to go about it. If this really is the dawning of a new era, is it one that we all (as internet users whose computers are often used for criminal acts such as the one represented by this botnet) want to see as a new norm, a new everyday occurrence where random attendees at a conference blast away as they see fit, not giving any apparent thought to the harm they may cause to innocent third parties? That's not the internet I want to see develop.  
  

  
- What justification is there for doing such an uncontrolled experiment on a live botnet, which is also an active crime scene? Can the conference organizer or government official involved articulate _any_ ethical or legal justification? (Hint: "We wanted to" is _not_ an ethical justification.)  
      
    
- What qualified someone to enter the contest? What training was required, what skill level, what tools/tactics/procedures were they allowed to use? Or was it just a free-for-all?  
      
    
- What were the objectives of the contest, and how were those objectives supposed to have any benefit on law enforcement activity or any kind of justice under Indian law or international law? Did contestants take careful notes of what they did so law enforcement can actually investigate without just finding a pile of randomly damaged evidence? How does this takeover help law enforcement in any way, or was any though given to that at all?  
      
    
- What constraints where placed on the contestants as to methods they could use to take control? Could they delete files, disable network interfaces, reconfigure the bots so they can't be controlled anymore? What happened if they crashed the system or permanently damaged it in the process? Was _anything_ out-of-scope?  
      
    
- What limits were there on what the contestants were allowed to do once they took control? Where they allowed to shut it down, try to follow the bad guys, or were they supposed to just hand over control to the government? What _did happen_ with the command and control server after the winning team took control of it?  
      
    
- Who would be responsible if those who controlled the botnet fought back and took down the network being used by the conference with a DDoS attack? Or what if they flattened every computer, wiping the hard drive completely clean, once they knew it was under attack? (Since I assume there were multiple teams, there is no stealth or surprise at all, in fact just the opposite. This would be about as obvious and noisy from the botnet controller's perspective as it could get.)  
      
    
- Who would be responsible if the contestants accidentally destroyed the contents of computers used for command and control, or any other infected hosts being controlled? Are all the computers involved in India? If not, what international legal ramifications would there be in the Indian government supported private citizens who in turn lost control or made a mistake and harmed computers in another country? Was anything known about the botnet except the command and control server's IP address?  
      
    
- What kind of a public/private partnership do they expect to develop if this is the debut of the new model? Do they intend to do this at every conference, or develop some closed market for paying citizen hacker groups to take down botnets that pop up?  
      
    
- How would the Indian government interpret a different conference in another country holding a similar contest to see if command and control servers in India could be taken over, without reporting to the Indian government first, and then used in any way the group who took them over saw fit? What if critical Indian government computers, or hospital computers, or systems used for transportation, where damaged in the process?  
      
    

  
  
These are just a few of the questions that deserve to be asked and answered before the next conference organizer in India or any other country decides to up the ante, make a bigger splash, generate even more headlines, and further increase the level of risks being taken without ethical justifications, legal justifications, or any reasonable care and caution against harming innocent third parties. This isn't a game, though more and more it seems the cheering conference crowds and twitter followers think it is and want to see more of it.
