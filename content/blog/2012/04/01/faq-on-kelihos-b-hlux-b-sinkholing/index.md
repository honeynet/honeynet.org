---
title: "FAQ on Kelihos.B/Hlux.B sinkholing"
date: "2012-04-01"
tags: 
  - "code-of-conduct"
  - "ethics"
  - "kelihos-d89"
  - "kelihos-b-hlux-b"
---

On March 31, 2012, the Honeynet Project published a draft [Code of Conduct](https://honeynet.org/codeofconduct) and a statement about [Ethics in Computer Security Research: Kelihos.B/Hlux.B botnet takedown](https://honeynet.org/node/834).

  
  

The initial draft of the Code of Conduct was drawn from concepts described in the [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](http://www.cyber.st.dhs.gov/wp-content/uploads/2011/12/MenloPrinciplesCORE-20110915-r560.pdf) that was published in the United States [Federal Register on December 28, 2011](http://www.federalregister.gov/articles/2011/12/28/2011-33231/submission-for-review-and-comment-the-menlo-report-ethical-principles-guiding-information-and) for public comment. The Code of Conduct was refined through discussion within the Legal and Ethics Committee and volunteer Honeynet Project members to help make it workable within the structure of the Honeynet Project membership for evaluating the ethics of future research activities.

  
  

The following FAQ reflects how the [Menlo Report](http://www.computer.org/csdl/mags/sp/2012/02/msp2012020071-abs.html) principles and proposed Honeynet Project Code of Conduct can be used to analyze and explain an action like the Kelihos/Hlux sinkholing operation.

  
  
  

  
**Question:** Who are all the stakeholders involved in the Kelihos.B/Hlux.B botnet?  
  
**Answer:** The set of stakeholders can be divided up into three categories based on: (1) their ability to directly affect the botnet operation (for good or bad), (2) their involvement in delivery of services affected by the botnet (for good or bad), and (3) the end-users and individuals in society who are generally impacted by the botnet operation (for good or bad).

  
  
Those (key) stakeholders who have an directly affecting role:  

  
- The Honeynet Project in general, and those researchers in specific who have been reverse engineering this malware.  
    
- The organizations involved in the sinkholing (Kaspersky, CrowdStrike, Dell SecureWorks)  
    
- The individual or group who is operating the botnet.  
    
- Law enforcement who may be investigating crime and who learn how to investigate crime through reading our research publications.  
    

  
  
Those (secondary) stakeholders who are involved as intermediaries:  

  
- The owners/providers of hosts being used for the top-level C&C infrastructure.  
    
- The owners/providers of network services that are receiving spam emails.  
    
- Malware distribution ("pay per install" or dropper) services used to spread the bot.  
    

  
  
Those (primary) stakeholders/end-users who are affected:  

  
- People whose computers are infected with the malware and anyone using or relying upon those computers.  
    
- Those individuals who recieve spam emails and/or are defrauded by spam selling fake drugs, etc.  
    
- Any persons who benefit from computer crime activity (e.g., spammers, people purchasing/using stolen credit cards or Bitcoin wallets for financial fraud, etc.)  
    
- The general public, who reads our research papers and blog posts.  
    

  

  
  

  
**Question:** What harms are occurring now to these stakeholders?  
  
**Answer:** Computer owners are being targeted for installation of Kelihos.B/Hlux.B. This botnet is then used to send large amounts of spam, to steal credentials, and steal Bitcoin wallets. Also victimized are those who receive spam. Botnets of this type can also easily be modified to perform distributed denial of service (DDoS) attacks, which can cripple legitimate web services for extended periods of time.

  
  

  
**Question:** What is the goal of this sinkhole operation and what benefit to society will be achieved by the intended actions?  
  
**Answer:** The objective of this action is to remove from the attacker's control all computers currently infected with the Kelihos.B/Hlux.B malware by poisoning the peer lists and routing tables in the lower layers of command and control. This will prevent the botnet operator from doing any more harm with this set of infected computers.  
  
By sinkholing the infected hosts, we will be able to collect additional data that will help, determine the response rate of attackers in countering takedown actions, as well as the decay rate of infected hosts due to remediation efforts. This information will allow a better understanding of generalized aspects of botnets (e.g., the size of botnets), as well as the effectiveness of various mitigation techniques used in concert with sinkholing operations in botnet takedowns. It also prevents further theft of login credentials that put servers used by owners of infected computers for exploit kit installation (e.g., [Blackhole](http://blog.imperva.com/2011/12/deconstructing-the-black-hole-exploit-kit.html), phishing pages, etc.)

  
  

  
**Question:** What will the security community and/or the general public learn from this action?  
  
**Answer:** Data collected by the sinkhole will be studied by various researchers. We are hoping to determine things like the effects of IP address dynamism and NAT on the accuracy of counting infected hosts, attacker counter-actions to botnet takedown, the rate of decay of infected hosts after being taken out of attacker control, and the comparative effectiveness of various host cleanup mechanisms on the time it takes for all infected hosts to be cleaned up.

  
  

  
**Question:** What other benefits are there to stakeholders?  
  
**Answer:** The researchers involved will obtain data that can be analyzed and shared with other researchers leading to greater understanding of the effectiveness of botnet sinkholing operations. Involved organizations increase their visibility while they and other key stakeholders, such as law enforcement, can benefit from insights gained from the data being collected. These benefits are added to the other benefits described here and balanced against the risks that are present. There is currently no security community consensus on how best to transparently make this balance, nor how to accurately quantify benefits across stakeholders, which is the [responsibility of the security community to address](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5669246).

  
  

  
**Question:** What risks are there to the owners of infected computers?  
  
**Answer:** There is very little risk to those whose computers are being sinkholed, as their computers are simply being diverted from control by the attacker running the botnet to a neutral sinkhole. This actually reduces harm to them. No changes are being made to the infected hosts, so their is no increased risk from being sinkholed. Tests were performed to establish that the peer-list poisoning would not disrupt the infected hosts, so there is no anticipated harm to infected computers.

  
  

  
**Question:** How does this risk compare with other previous botnets that were sinkholed?  
  
**Answer:** Earlier generations of this botnet family have been subjected to sinkhole operations on two previous occasions: Waledac was taken down in [February 2010](http://online.wsj.com/article/SB10001424052748704240004575086523786147014.html), and its successor Kelihos/Hlux was taken down in [September 2011](http://blogs.technet.com/b/microsoft_blog/archive/2011/09/27/microsoft-neutralizes-kelihos-botnet-names-defendant-in-case.aspx). This is the second time Kelihos/Hlux will have been sinkholed. In neither of the two previous takedown/sinkhole operations was there reported harm to infected computers that were directed to and held by the sinkhole.

  
  

  
**Question:** What has this attacker (or others) done in the past when a takedown was attempted?  
  
**Answer:** After the Waledac sinkholing operation, the attackers abandoned the top layer C&C infrastructure and re-wrote their malware as Kelihos/Hlux. When Kelihos/Hlux was [sinkholed](http://www.securelist.com/en/blog?weblogid=208193137), the attackers again abandoned the top later C&C servers, and reconstituted a new botnet (Kelihos.B/Hlux.B) with slight modification, this time via a "pay per install" distribution mechanism, in a matter of months.

  
  

  
**Question:** What do we believe the attacker will do in response?  
  
**Answer:** We anticipate they will likely do the same as last time and try to reconstitute the botnet with little or no major modification.

  
  

  
**Question:** What where the risks that were considered in planning for the sinkholing and how are they mitigated?  
  
**Answer:** An isolated network was used to separate the sinkhole from other production networks, and it was deployed on on a high-bandwidth network segment. Mechanisms were employed to prevent the botnet operator from re-acquiring control of the bots, even if the sinkhole is attacked. Poisoning was done from multiple countries in order to ensure detection and counteracting of the poisoning would be unlikely.

  
  

  
**Question:** How will owners of infected computers be notified?  
  
**Answer:** They will be contacted by a response team who is assisting the sinkhole operators and provided with lists of infected IP addresses on their networks.

  
  

  
**Question:** How will infected computers be cleaned up?  
  
**Answer:** Owners of the infected hosts are responsible for cleaning up their own computers. Information provided to the response team will assist in identifying these owners to facilitate this process.

  
  

  
**Question:** How long will the sinkhole be operated?  
  
**Answer:** The sinkhole will be maintained for an indeterminate time period, as long as it takes before the botnet is considered effectively non-existent.

  
  

Feel free to ask other questions that were not cover here and we will consider how to integrate them. This is intended to be a learning experience in ethical analysis as much as an basic explanation of facts.
