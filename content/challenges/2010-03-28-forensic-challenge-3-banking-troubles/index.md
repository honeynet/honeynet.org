---
title: "Challenge 3 of the Forensic Challenge 2010 - Banking Troubles"
date: "2010-03-28"
coverImage: "facebook.gif"
---

**Challenge 3 - Banking Troubles -** (provided by Josh Smith and Matt Cote from The Rochester Institute of Technology Chapter, Angelo Dell'Aera from the Italian Chapter and Nicolas Collery from the Singapore Chapter) is to investigate a memory image of an infected virtual machine.  

The challenge has been completed on May 12th 2010. 
Skill Level: Difficult  

**The Challenge:**  

Company X has contacted you to perform forensics work on a recent incident that occurred. One of their employees had received an email from a fellow co-worker that pointed to a PDF file. Upon opening, the employee did not seem to notice anything, however recently they have had unusual activity in their bank account. Company X was able to obtain a memory image of the employee’s virtual machine upon suspected infection. Company X wishes you to analyze the virtual memory and report on any suspected activities found. Questions can be found below to help in the formal report for the investigation.

1. List the processes that were running on the victim’s machine. Which process was most likely responsible for the initial exploit? (2pts)
2. List the sockets that were open on the victim’s machine during infection. Are there any suspicious processes that have sockets open? (4pts)
3. List any suspicious URLs that may be in the suspected process’s memory. (2pts)
4. Are there any other processes that contain URLs that may point to banking troubles? If so, what are these processes and what are the URLs? (4pts)
5.  Were there any files that were able to be extracted from the initial process? How were these files extracted? (6pts)
6.  If there was a file extracted from the initial process, what techniques did it use to perform the exploit? (8pts)
7.  List suspicious files that were loaded by any processes on the victim’s machine. From this information, what was a possible payload of the initial exploit be that would be affecting the victim’s bank account? (2pts) 
8.  If any suspicious files can be extracted from an injected process, do any anti-virus products pick up the suspicious executable? What is the general result from anti-virus products? (6pts)
9.  Are there any related registry entries associated with the payload? (4pts)
10. What technique was used in the initial exploit to inject code in to the other processes? (6pts)  

**Download:**  

[hn\_forensics.tgz](/challenge2010/downloads/hn_forensics.tgz) Sha1: 8178921fd065ad2de9c6738fe062d2b37402c04a  

**Sample Solution:**  
  
[Forensic\_Challenge\_3\_-\_Banking\_Troubles\_Solution.pdf](https://www3.honeynet.org/wp-content/uploads/attachments/Forensic_Challenge_3_-_Banking_Troubles_Solution.pdf) - Sha1: 986752a9aa4b832951dfa6319cb5e16256a9b3c9  

This work by Josh Smith, Matt Cote, Angelo Dell'Aera and Nicolas Collery is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.  
  
**The Winners:**  

1. Mario Pascucci (Italy) - [Mario's submission](https://www3.honeynet.org/wp-content/uploads/attachments/Mario_Pascucci_Forensic_Challenge_2010_-_Challenge_3_-_Submission.pdf) - Sha1: ad6e08bd0bff8a65e5ea8865e63addf9d6324212
  
2. Tyler Hudak (USA) - [Tyler's submission](/files/Tyler_Hudak_Forensic_Challenge_2010_-_Challenge_3_-_Submission.odt) - Sha1: 226e15990dac263402670d5976c8b63f241864c7
  
3. Carl Pulley (UK)- [Carl's submission](https://www3.honeynet.org/wp-content/uploads/attachments/Carl_Pulley_Forensic_Challenge_2010_-_Challenge_3_-_Submission.pdf) - Sha1: 2d20203403cf33bd565dbf81a54dbe414a17a597
