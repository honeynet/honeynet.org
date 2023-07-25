---
title: "Forensic Challenge 12 – Hiding in Plain Sight"
date: "2012-10-16"
---

**Forensic Challenge 12 – “Hiding in Plain Sight"**

(provided by the Alaska Chapter under the leadership of Lucas McDaniel)


**Skill Level: Intermediate** 

**Background** You belong to a company specializing in hosting web applications through KVM-based Virtual Machines. Over the weekend, one VM went down, and the site administrators fear this might be the result of malicious activity. They extracted a few logs from the environment in hopes that you might be able to determine what happened. This challenge is a combination of several entry- to intermediate-level tasks of increasing difficulty focusing on authentication, information hiding, and cryptography. Participants will benefit from entry-level knowledge in these fields, as well as knowledge of general linux operations, kernel modules, a scripting language, and reverse engineering. Not everything may be as it seems. Innocuous files may turn out to be malicious so take precaution when dealing with any files from this challenge. 

**Main Questions** 1. How did the attacker gain access to the system? 2. How many failed attempts were there? 3. What credentials (username and password) were used to gain access? Refer to shadow.log and sudoers.log. 4. How was the malware installed on the system? Provide all relevant files. 5. Where did the malware keep local files? 6. What is missing from ps.log? 7. What files were used to remove this information from ps.log, and how do they work? 8. What was the malware sending and receiving? Provide all files and data streams when appropriate. 9. Who was the malware connecting to, and what was their purpose? 10. Why are these files important? 11. Provide all private keys used. 12. Provide all secrete messages. 13. What was the purpose of the final payload, and how did it achieve this goal? 14. Was the attack successful, and if so then why did the VM to go down? 15. What other logs or files could verify this attack? 

**Bonus Questions** 16. What other credentials are susceptible to attack? 17. Why would the hiding method used not work on many other systems? 18. How else could the malware have been hidden? 19. List the problem(s) with the encryption used, and how they should be fixed. 20. (Broken) What was the super-secret message(s)? This work by the Honeynet Project Alaska Chapter under the leadership of Lucas McDaniel is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.

 **The Winners**
1. Shaun Zinck (1345961479\_shaun-zinck-hnp-2012-12.zip) 
2. Vadim Kotov & Alberto Boschetti (1347160881\_answer.odt) 
3. José Valentín Gutiérrez Boquete (1347218667\_fc12.zip)

| Attachment | Size |
| --- | --- |
| 2012-HP\_Challenge-12.zip | 7.65 MB |
| 1345961479\_shaun-zinck-hnp-2012-12.zip | 14.87 MB |
| 1347160881\_answer.odt | 53.1 KB |
| 1347218667\_fc12.zip | 8.29 MB |
| hp\_malware.c.zip - Malware source code (not included in the original challenge and released just for reference purposes) | 6.24 KB |
