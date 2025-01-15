---
title: "Low Interaction Honeypots Revisited"
authors: ["David Watson"]
date: "2015-08-06"
categories: 
  - "honeypot"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

**TL;DR:** Low interaction honeypots are designed to emulate vulnerable services and potentially detect attacks without exposing full operating system functionality. Although they have evolved in many ways over the past 15 years, understanding their limitations and sometimes inherent design weaknesses is important when you consider deploying them. Understanding the history of attempted honeypot detection and evasion allows system defenders to improve their continued use of honeypots and hopefully helps makes all of our networks safer.

**A trip down memory lane…**

When the Honeynet Project first formed in 1999 and began researching attacks against computer networks, very little was known about our enemies, their motives, or the tools and techniques they used. During the early years of honeynet research we developed a range of honeypot tools to help us collect and analyse data occurring from attacks against real systems deployed in the wild. Although commonplace now, at the time, this was a pretty novel activity and regularly featured in presentations such as at [BlackHat 2002](https://www.youtube.com/watch?v=xXMkkd79YlM) and [BlackHat 2003](http://www.blackhat.com/presentations/bh-usa-03/bh-us-03-honeynet-project/bh-us-03-honeynet.pdf).

One of the initial challenges we faced was balancing the trade-offs between the high quality data that could potentially be obtained through increasingly complex instrumentation of real computer systems, versus the risk of potential damage and liability that could possibly be caused by attackers abusing compromised honeypot systems. This has always been a major concern for honeypot operators, and remains so today.

A potential solution to this problem was the development of emulated honeypots, which attempted to mimic various networked services without actually exposing a full operating system to the attacker. These “low interaction” emulated honeypots could be designed to respond in at least a basic way to potentially malicious network inputs, allowing attacks to be logged while much reducing the associated risk, effort, deployment and management complexity required.

Low interaction honeypots started out as relatively simple network emulation tools such as [honeyd](http://www.honeyd.org/background.php) (2003), which when deployed waited for inbound network connections and offered only limited service emulation. But over time, these tools evolved into more capable solutions - such as [Nepenthes](http://nepenthes.carnivore.it) for collecting Windows network spreading malware, and eventually [Dionaea](http://dionaea.carnivore.it). Special purpose low interaction honeypots were also created, such as [Glastopf](http://glastopf.org) for web attacks and [Conpot](http://conpot.org) for SCADA/ICS systems, or [Thug](https://buffer.github.io/thug/) as a low interaction client honeypot designed to actively crawl and evaluate potentially malicious web sites.

Although full operating system (“high interaction”) honeypots would always provide the highest quality data, and were still essential for observing skilled human attackers, low interaction honeypots definitely turned out to be useful in some deployment scenarios: being particularly well suited for easy, low cost roll outs on a large scale; for minimizing management effort and reducing the potential attack surface, operating risk and liability; detecting mass network scanning or compromised internal hosts; tracking network based malware propagation (worms); studying internet wide threats at the macro level or providing real time alerting for highly automated attacks with little initial human input (brute force, scanners, etc). An old [Blackhat Federal 2003 presentation](http://www.blackhat.com/presentations/bh-federal-03/bh-fed-03-spitzner.pdf) still gives a pretty good overview of the key differences between low and high interaction honeypots and their associated issues. Although technologies and attackers have changed, the concepts remain the same.

Since this research was breaking new ground and the tools were all open source, our developers regularly faced efforts to fingerprint, detect, attack or circumvent our honeynet tools. We always expected this to come from the black hat community, but sometimes we were also surprised (and challenged) by research published by academic or whitehat security researchers too. Over the years there have been many regular cycles in the arms race occurring between system attackers and defenders. For example:

· Honeypot detection and exploitation were regular features of Phrack magazine during 2003 (for example [p62-0x07.txt](http://repo.hackerzvoice.net/depot_ouah/p62-0x07.txt) and [p63-0x09.txt](http://www.ouah.org/p63-0x09.txt)), with attackers looking for ways to detect or defeat honeypots.

· [BlackHat 2004 - NoSEBrEak - Defeating Honeynets](http://www.blackhat.com/presentations/bh-usa-04/bh-us-04-holz/bh-us-04-holz-up.pdf) featured enthusiastic German students showing how to potentially detect and defeat the Sebek rootkit component of our then current generation high interaction honeypot. The authors then went on to join the Honeynet Project, [helped improve honeynet technologies](https://www3.honeynet.org/wp-content/uploads/attachments/DefeatingHPs-IAW05.pdf) (with the help of French colleagues) and eventually authored one of the [leading books](http://www.amazon.com/Virtual-Honeypots-Tracking-Intrusion-Detection/dp/0321336321) on honeypots for system defenders. Sebek was improved in the next generation release ([2005](https://www.dfn-cert.de/dokumente/workshop/2005/dfncert-ws2005-f1.pdf)), to hopefully limit the impact of those published approaches.

By the mid 2000s, our members were [regularly presenting](http://www.ists.dartmouth.edu/library/97.pdf) about balancing the risks of detection and compromise versus the early warning and intelligence gathering capabilities that could be obtained by deploying honeypots. We also regularly published articles on Security Focus (now owned by Symantec) highlighting the potential detection challenges facing honeypot operators:

[http://www.symantec.com/connect/articles/problems-and-challenges-honeypots  
](http://www.symantec.com/connect/articles/problems-and-challenges-honeypots)[http://www.symantec.com/connect/articles/defeating-honeypots-system-issues-part-1  
](http://www.symantec.com/connect/articles/defeating-honeypots-system-issues-part-1)[http://www.symantec.com/connect/articles/defeating-honeypots-system-issues-part-2  
  
](http://www.symantec.com/connect/articles/defeating-honeypots-system-issues-part-2)

As honeypots continued to evolve, the back and forth between honeypot attackers and developers continued. Other examples include:

· Books released with [chapters covering fingerprinting](http://books.gigatux.nl/mirror/honeypot/final/ch09lev1sec1.html) of low interaction honeypots such as honeyd.

· The popular network scanning tool [Nmap](http://www.nmap.org) (developed by a Honeynet Project member) gaining the ability to [fingerprint Dionaea](http://blog.prowling.nu/2012/04/detecting-dionaea-honeypot-using-nmap.html) honeypots, and the community providing [advice](http://www.cyberbrian.net/2014/09/dionaea-honeypot-obfuscation/) on [avoiding service detection](http://www.securityartwork.es/2014/06/05/avoiding-dionaea-service-identification/) or Dionaea fingerprinting changes being made to the source code.

· [Kippo SSH honeypot fingerprinting](https://isc.sans.edu/forums/diary/Kippo+Users+Beware+Another+fingerprinting+trick/18119/) tricks and [attacks](http://www.rafayhackingarticles.net/2013/06/using-honeypots-to-your-advantage.html), along with [detection and patching battles](http://morris.guru/detecting-kippo-ssh-honeypots/).

· Penetration testing companies [blogging](https://www.pentestpartners.com/blog/need-to-avoid-a-honeypot-heres-how/) about how to avoid honeypots during engagements.

· Security researchers wearing hats of various colours setting up sites to [publicly expose](http://voices.washingtonpost.com/securityfix/2009/10/former_anti-virus_researcher_t.html) the IP addresses of known honeypots/sandboxes.

· [Search engines](https://honeyscore.shodan.io) that allow anyone to easily search for deployed honeypots that they have detected by scanning the entire internet for known fingerprints.

With [BlackHat 2015](https://www.blackhat.com/us-15/) happening this week, the topic of honeypots is once again on the agenda. So this seemed like an appropriate time to recap what this regular cycle means for honeypot operators worldwide.

Although our website provides much more detail, our advice regarding low interaction honeypots continues to be:

1. When considering deploying honeypots, start by reading the [books published](http://www.amazon.com/Know-Your-Enemy-Learning-Security/dp/0321166469/ref=sr_1_3?s=books&ie=UTF8&qid=1438812056&sr=1-3&keywords=know+your+enemy) on the topic. They will help understand the potential pros and cons of low/high interaction honeypots, and offer advice about technologies, best practices and managing the risk.
2. If you are deploying low interaction honeypots, understand that service emulation is still relatively simple and these tools are primarily designed to detect highly automated basic attacks. It is likely that there will always be ways to fingerprint low interaction honeypots.
3. Advanced attackers are unlikely to be distracted by unsophisticated low interaction honeypot systems for long. Observing sophisticated, targeted attackers will require tuned high interaction honeypot approaches, although low interaction honeypots may still detect initial probe activity.
4. Review the default low interaction honeypot configurations and consider changing them in production, to reduce the risk of detection.
5. Run the latest production code branches and follow discussions on announcement lists to be informed about potential honeypot problems. Although relatively low risk, low interaction honeypots are still not fire and forget solutions since they will regularly be targeted by attackers.
6. If you become aware of means to fingerprint, detect or exploit current honeypots, please provide bug reports to the developers to enable the issues to be addressed.
7. Assume that there are determined adversaries out there who are willing to study source code and slowly probe your environment to identify and potentially bypass your defenses.
8. Accept that the cycle of detect, attack, patch, improve is actually beneficial in the long term, as it “battle tests” and strengthens the tools available to system defenders (along with providing occasional moments of discomfort too!).
9. Always depend on “defence in depth” and multiple detection methodologies, not just honeypots.

The Honeynet Project has existed for over 15 years as a community that [supports honeypot users/developers](https://www.honeynet.org/gsoc) and [educates the public](http://stavanger2015.honeynet.org) about their benefits and use. All of our software is open source supported by volunteers, so patches, improvements, feature requests, user feedback and [funding donations](https://www.honeynet.org/about) are always welcome. We are always happy to work on co-ordinating responsible disclosure of detection techniques or vulnerabilities in popular honeypot technologies, and will always credit your organization with the discoveries and improvements if you request it.

If you are interested in the topic of honeypots and honeynets, please get in touch - either via email (project @ honeynet.org) or on Twitter [@ProjectHoneynet](https://twitter.com/projecthoneynet). We look forwards to hearing from you.
