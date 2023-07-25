---
title: "Forensic Challenge 7 - Analysis of a Compromised Server"
date: "2011-03-02"
---

**Challenge 7 - Forensic Analysis of a Compromised Server** - (provided by Guillaume Arcas from the French Honeynet Project Chapter, Hugo Gonzales from the Mexican Honeynet Project Chapter, Julia Cheng from the Taiwan Honeynet Project Chapter)  
  
Pls submit your solution using the submission template below by March 30th 2011

Results will be announced around the third week of April. For any questions and inquiries, please contact forensicchallenge2010@honeynet.org.  
  
Skill Level: Beginner

**The Challenge:**  
A Linux server was possibly compromised and a forensic analysis is required in order to unterstand what really happened. Hard disk dumps and memory snapshots of the machine are provided in order to solve the challenge.

1. What service and what account triggered the alert? (1pt)
2. What kind of system runs on targeted server? (OS, CPU, etc) (1pt)
3. What processes were running on targeted server? (2pts)
4. What are attackers IP and target IP addresses? (2pts)
5. What service was attacked? (1pt)
6. What attacks were launched against targeted server? (2pts)
7. What flaws or vulnerabilities did he exploit? (2pts)
8. Were the attacks successful? Did some fail? (2pts)
9. What did the attacker obtain with attacks? (2pts)
10. Did the attacker download files? Which ones? Give a quick analysis of  
    those files. (3pts)
11. What can you say about the attacker? (Motivation, skills, etc) (2pts)
12. Do you think these attacks were automated? Why? (1pt)
13. What could have prevented the attacks? (2pts)

**Download:**  
victoria-v8.kcore.img.zip  
victoria-v8.memdump.img.zip  
victoria-v8.sda1.img.zip  
  
victoria-v8.kcore.img: memory dump done by dd'ing /proc/kcore  
victoria-v8.memdump.img: memory dump done with memdump\[1\]  
  
\[1\]http://www.porcupine.org/forensics/tct.html  
MD5:  
victoria-v8.kcore.img.zip = 3b74b32279422e93f93927b80f18df2c  
victoria-v8.memdump.img.zip = 7d271455ad65e55678a530aaed696040  
victoria-v8.sda1.img.zip = cba614f59020ce8910346cc43056692f  
  
SHA1:  
victoria-v8.kcore.img.zip = e971ccfd4853d4b7459eb6862e4b747074f23a7  
victoria-v8.memdump.img.zip = eae53cb9fb1e98f9f9ba334edfe8a4b3e7ca9104  
victoria-v8.sda1.img.zip = cddc70ca67db4f3cfca4d48c755c43bb286738c3  
  
Share:

This work by Guillaume Arcas, Hugo Gonzales and Julia Cheng is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.

**The Winners:**

1\. Dev Anand (Submission SHA-1: 8150e907a114d862a4c25387f2ea42371569781c)  
2\. Fernando Quintero & Camilo Zapata (Submission SHA-1: f122f9a93b8ec2c708a447cb74ba214569d8716f)  
3\. (3 submissions)  
    Matt Erasmus (Submission SHA-1: a49543b0022416b946e89134839d916ea25d94c9)  
    Joseph Kahlich (Submission SHA-1: fc2d1898edc542bd1f2b7f82b962d361503b3e8b)  
    Kevin Mau (Submission SHA-1: 0eef1421350edcd5b3266006d07df19aa342c431)

| Attachment | Size |
| --- | --- |
| \[your email\]\_Forensic Challenge 2010 - Challenge 7 - Submission Template.doc | 49.5 KB |
| \[your email\]\_Forensic Challenge 2010 - Challenge 7 - Submission Template.odt | 18.89 KB |
| Devanand\_Forensic Challenge 2010 - Challenge 7 - Submission.pdf | 351.74 KB |
| Fernando Quintero\_Forensic Challenge 2010 - Challenge 7 - (2011-03-30).odt | 128.32 KB |
| Matt Erasmus\_Forensic Challenge 2010 - Challenge 7 - Submission.doc | 76 KB |
| Joseph Kahlich\_Forensic Challenge 2010 - Challenge 7 - Submission.doc | 88 KB |
| Kevin Mau\_Forensic Challenge 2010 - Challenge 7 - Submission.doc | 83.5 KB |
