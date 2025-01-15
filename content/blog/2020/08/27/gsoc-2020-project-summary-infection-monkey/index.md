---
title: "GSOC 2020 PROJECT SUMMARY: INFECTION MONKEY"
authors: ["Abhinav Saxena"]
date: "2020-08-27"
tags: 
  - "gsoc"
  - "gsoc2020"
  - "infection-monkey"
coverImage: "infection_monkey_2020.png"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

_Shreya Malviya wrote this post as a project summary of her GSoC2020 experience._

**_Team_**:  
Mentors: Shay Nehmad, Daniel Goldberg  
Student: Shreya Malviya

![](https://lh3.googleusercontent.com/OhuLMDvEhFl-tjQMs-4H09vVPyxpnKY2mwhie32DNRGV6230Mkw-YgifvoMYSBQjYiSY9U6Kck6G_nIhcCgYliRvvrj-aGkSPVO-p_02E3nl4DFWvlH87gn8fuzpPZlCJKzfoAV1)

## Introduction

### What is Infection Monkey?

[Infection Monkey](https://www.guardicore.com/infectionmonkey/) is an open-source security tool for testing a data center’s resiliency to perimeter breaches and internal server infection. The Monkey uses various methods to self-propagate across on-premises/cloud-based data centers and finds their weaknesses, whose results it then reports to a centralized Monkey Island Command and Control server.

In simpler words, Infection Monkey allows you to simulate breach and attack scenarios in your environment to help you assess the damage that you may endure in a real attack and verify that your security solutions work as expected.

Let’s talk about phishing attacks, for example. Almost everyone is prone to phishing attacks, and if successful, they can prove to be extremely costly. Using Infection Monkey, you can easily simulate a successful attack on your network, starting from the point where malware is executing, by running the Monkey with your desired configuration. You can then evaluate the results of your simulated attack using a detailed report found on the Monkey Island, comprising the Monkey’s findings, essential things the simulation discovered, and more.

### What did you do for the project, briefly? (TL;DR)

I enhanced the detection capabilities of the Monkey by improving the MITRE ATT&CK coverage. This includes the addition of several new post-breach actions. These PBAs are mapped to the [MITRE ATT&CK knowledge base](https://attack.mitre.org/) in Monkey, in order to provide the user with a detailed visualisation of the utilized actions/techniques and their recommended mitigations, all of which can be found in the ATT&CK report on the Monkey Island. This ATT&CK report is also more explanatory now, owing to the modifications that I made. In addition, I ended up working on other general improvements of the tool, such as boosting the Monkey’s performance by making post-breach actions run in parallel with network scanning.

## Delving Into What Happened

### New MITRE ATT&CK techniques

The MITRE ATT&CK knowledge base is a comprehensive matrix of tactics and techniques based on real-world observations, which is widely used as a basis for network security assessments, used to classify attacks, assess an organization’s risk, and prioritize holes in defenses based on their risks.

Infection Monkey provides a way to configure the ATT&CK techniques that you want to test easily, and offers more insight about how those techniques were used and how you can further protect yourself. 

As part of my GSoC project, I added twelve new techniques (with many more on the way!):

- [T1136](https://attack.mitre.org/techniques/T1136) — “Create Account” attack technique ([#579](https://github.com/guardicore/monkey/issues/579))
- [T1158](https://attack.mitre.org/techniques/T1158) — "Hidden Files and Directories" attack technique ([#672](https://github.com/guardicore/monkey/issues/672))
- [T1156](https://attack.mitre.org/techniques/T1156) — "_.bash\_profile_ and _.bashrc_" attack technique ([#682](https://github.com/guardicore/monkey/issues/682))
- [T1168](https://attack.mitre.org/techniques/T1168) — "Local Job Scheduling" attack technique ([#683](https://github.com/guardicore/monkey/issues/683))
- [T1053](https://attack.mitre.org/techniques/T1053) — "Scheduled Task" attack technique ([#685](https://github.com/guardicore/monkey/issues/685))
- [T1504](https://attack.mitre.org/techniques/T1504) — "PowerShell Profile" attack technique ([#686](https://github.com/guardicore/monkey/issues/686))
- [T1154](https://attack.mitre.org/techniques/T1154) — "Trap" attack technique ([#697](https://github.com/guardicore/monkey/issues/697))
- [T1166](https://attack.mitre.org/techniques/T1166) — “_setuid_ and _setgid_” attack technique ([#702](https://github.com/guardicore/monkey/issues/702))
- [T1216](https://attack.mitre.org/techniques/T1216) — "Signed Script Proxy Execution" technique ([#703](https://github.com/guardicore/monkey/issues/703))
- [T1087](https://attack.mitre.org/techniques/T1087) — "Account Discovery" technique ([#705](https://github.com/guardicore/monkey/issues/705))
- [T1146](https://attack.mitre.org/techniques/T1146) — "Clear Command History" attack technique ([#794](https://github.com/guardicore/monkey/issues/794))
- [T1099](https://attack.mitre.org/techniques/T1099) — “Timestomping” attack technique ([#795](https://github.com/guardicore/monkey/issues/795))

Take, for example, the "[Hidden Files and Directories](https://attack.mitre.org/techniques/T1158)" attack technique. Hidden files exist on operating systems to prevent normal users from accidentally changing special system files. However, adversaries can use this concept to hide malicious files anywhere on the system. The MITRE ATT&CK framework lists over 20 examples of real-life cases where this property has been exploited for defense evasion.

![](https://lh3.googleusercontent.com/nDDB6TrFOEsE2qHeDtrqs2W3lHLgNVEI4Dqaq1zSvhz0I8fqGieY7VSYkP2m8TPosykwJ6lcc8sBS3i8fHlHvEFqWYASBMG44ClNMd02Bxt_2401KAdG0Boi1OR4dt6p_f-6r1WK)

_“Hidden Files and Directories” technique in the MITRE ATT&CK database_

The Monkey attempts to create and destroy a hidden file or directory on your system. Ideally, your antivirus software or security solution should incorporate the investigation of hidden files, notify you of unrecognized hidden files on the system, or simply block the creation of an unauthorized hidden file or directory. However, if the Monkey tells you that it was able to carry out the technique successfully, it is probably time for you to take a second look or upgrade to a better security service.

![](https://lh3.googleusercontent.com/F9oOp1VKZkpIC2V_WxIlxSZPW0zP1SzEFQsbUMPfcenFeF5x2TaQzSYRHo7l0MRI5UfRcOba4Im2K82l0KPiIF3zeYrQGTrRF201ehjYN9bdmuBvAJwnsSRKofdv1ZnbKf6JXl6k)

![](https://lh6.googleusercontent.com/iJjNnSAQwOVncV_n5ud_HLqhG5H9rBu7KFAWXJS5_hK63dvv0U0Gz61RrMvPQUUBdRH2GiTtCEgqrSGA-j7wpoIKzp9N2y81_nKKoT6sOqxACpb-wwTaDNvGpdn8WKLsxfr63e5D)

_ATT&CK report on the Monkey Island server — the ATT&CK matrix followed by details of the selected technique (Hidden Files and Directories)_

The MITRE ATT&CK matrix covers many more similar techniques. With the addition of the aforementioned 12, Infection Monkey now includes a total of 36 ATT&CK techniques out 272!

### Improved reporting

Once the Monkey finishes its execution, the report is generated on the Monkey Island server, consisting of 3 sections — the Security report, the Zero Trust report, and the ATT&CK report. The [ATT&CK report](https://www.guardicore.com/infectionmonkey/docs/usage/reports/mitre/) is a detailed account of the results of the ATT&CK techniques that Monkey configures.

While working on the addition of new techniques, we decided on making the ATT&CK report more actionable by revamping it to better cover known-unknowns. 

- ATT&CK report modifications ([#717](https://github.com/guardicore/monkey/pull/717))

For instance, if the Monkey does not run the “[_setuid_ and _setgid_](https://attack.mitre.org/techniques/T1166)” attack technique in a given simulation, the ATT&CK report will mention the reason — whether no Linux machines were found or whether it was disabled in the configuration for the simulation. This can help you better understand and answer questions such as why an attacker would scan your network but leave out some part of the network.

![](https://lh5.googleusercontent.com/Lj6KXMZiWj0Z8ugRZGwBzqX2b8zNc6tQz1DexcnKNk86kn-DA1AcpSgXBB9axbQ6FQL5qDUCmjn9hqmbRuIsDMM5NpaMNc-yMX09jf4CADlZEymKVgiXD9BHse50VqyXvgBKHrzD)

_ATT&CK report on the Monkey Island server — the ATT&CK matrix followed by details of the selected technique (Setuid and Setgid)_

### General improvements

Besides these, I worked on some general improvements —  
→ Bug fixes

- Fix rendering bug in security report generation due to PBA section ([#762](https://github.com/guardicore/monkey/pull/762))
- Link ATT&CK techniques of the same PBA in the config ([#761](https://github.com/guardicore/monkey/pull/761))
- Windows' "modify shell startup files" PBA fix ([#757](https://github.com/guardicore/monkey/pull/757))
- Preserves ATT&CK config order on clicking 'Reset to defaults' ([#753](https://github.com/guardicore/monkey/pull/753))
- Make setuid/setgid and trap PBAs not crash on windows ([#732](https://github.com/guardicore/monkey/pull/732))
- Remove \`None\` values from the list of networks to scan ([#550](https://github.com/guardicore/monkey/pull/550))

→ Performance improvements

- Run post-breach phase in a separate thread ([#758](https://github.com/guardicore/monkey/pull/758))
- Telemetry modifications for "modify shell startup files" PBA ([#731](https://github.com/guardicore/monkey/pull/731))

  
→ Miscellaneous (feature improvements, documentation updates, refactoring)

- Update MITRE images in documentation ([#783](https://github.com/guardicore/monkey/pull/783))
- ATT&CK report message modifications ([#717](https://github.com/guardicore/monkey/pull/717))
- Use mongo search for T1136's report data ([#693](https://github.com/guardicore/monkey/pull/693))
- Autoscroll to the last line in the telemetry console ([#565](https://github.com/guardicore/monkey/pull/565))

## The Community Aspect

Since my very first interaction, the development team of Infection Monkey has been SUPER encouraging! The last few months have been an amazing experience for me, and I am extremely appreciative of all that I have learnt.  
  
Besides guiding me about the technical aspects of the project, my mentors have helped me acquire and practice soft skills as well, such as prioritising tasks and managing time accordingly, and taking charge and kicking off discussions revolving around future plans for the Monkey.  

![](https://lh3.googleusercontent.com/YlZoBrWyTfebpKHKf0lYF7Vr_2cVDRpC6E9M81BAK47bLXhb_P0ASo53aJxRJS1D2g7E4z8m6DZSEwsjz8qqzpQx-9txzxv9pHgRnwvdM2MupRQpkIhpMZp7-rpK7gt9CuVSLalq)  
_Slack discussion about the addition of a feature to Monkey_

  
All of these have tremendously helped me grow as a developer in its entirety, and I can say with confidence that this has definitely been the most fruitful summer of my life! :)

If you would like to get involved, feel free to join our Slack workspace: [https://infectionmonkey.slack.com/join/shared\_invite/enQtNDU5MjAxMjg1MjU1LWM0NjVmNWE2ZTMzYzAxOWJiYmMxMzU0NWU3NmUxYjcyNjk0YWY2MDkwODk4NGMyNDU4NzA4MDljOWNmZWViNDU#/](https://infectionmonkey.slack.com/join/shared_invite/enQtNDU5MjAxMjg1MjU1LWM0NjVmNWE2ZTMzYzAxOWJiYmMxMzU0NWU3NmUxYjcyNjk0YWY2MDkwODk4NGMyNDU4NzA4MDljOWNmZWViNDU#/)!

# Learning Outcomes

- Acquired a firmer grasp over developing and debugging in Python
- Practised unit testing in Python
- Implemented multithreading in Python
- Learned JavaScript and basic frontend development using ReactJS
- Dived deeper into the features of Linux and Windows operating systems and shell scripting
- Was introduced to NoSQL databases — worked with MongoDB
- Brushed up on clean coding constructs
- Exercised time management and task prioritisation
