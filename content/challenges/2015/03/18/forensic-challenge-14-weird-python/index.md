---
title: "Forensic Challenge 14 - Weird Python"
date: "2015-03-18"
---

Your boss John went to a BYOD conference lately. Yeah, he's that kind of security guy... After some mumble about targeted attacks happening during the event, your team finally got their hands on a PCAP with his traffic. Your colleague Pete Galloway investigated the incident. Yesterday, he casually mentioned that he found some weird Python bytecode, but couldn't make much sense out of "random" payloads yet. Today, Pete didn't come to work. Five minutes ago, he sent a company-wide mail with a total of four words: “Fuck you, I quit.“. What has happened!?

<!--more-->

**Skill Level: Both entry- and intermediate-level tasks**


### Files

[conference.pcapng](https://github.com/honeynet/forensic_challenges/raw/master/zip_files/challenges/fc14.zip) [(mirror)](https://www.dropbox.com/s/3a8z129uk8c1sec/conference.pcapng?dl=1)

### Write-Up

You can view a crowd-sourced write-up compiled from the submissions we received [here](https://github.com/honeynet/forensic_challenges/blob/master/zip_files/submissions/fc14.pdf). If you are interested in using the challenge for educational purposes, let us know and we are happy to remove this part temporarily.

### Questions

For each question, please explain your methodology (How did you get the answer? Which tools did you use?). Submissions will be primarily rated by accuracy and quality.

1. BYOD seems to be a very interesting topic. What did your boss do during the conference?
2. What method did the attacker use to infect your boss? Which systems (i.e. IP addresses) are involved?
3. Based on the PCAP, which files were exfiltrated? List the filenames.
4. Can you sketch an overview of the general actions performed by the malware?
5. Do you think this is a targeted or an automated attack? Why?
6. The malware seems to be written in Python. Is this "normal" Python? What's different?
7. What does main.pyc do? (Bonus: Can you provide a decompiled version?)
8. How is the final payload protected? How is it decrypted by the dropper? (Bonus: Can you provide a decompiled version?)
9. Why did Pete leave the company?
10. Your boss mentioned he's going to the Honeynet Workshop in Stavanger, but you're not allowed to join him. Why so?
11. Bonus: There are five superheroes hidden in the challenge. Which of them did you find?
12. Optional (not rated, feel free to submit separately): Please provide some feedback on the challenge! What did you like/dislike?

* * *

This work by Thomas Chopitea and Maximilian Hils is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.
