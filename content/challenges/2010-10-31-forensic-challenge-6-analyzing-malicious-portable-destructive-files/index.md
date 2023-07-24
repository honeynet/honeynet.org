---
title: "Forensic Challenge 6 - Analyzing Malicious Portable Destructive Files"
date: "2010-10-31"
---

**Challenge 6 - Analyzing Malicious Portable Destructive Files -** (provided by Mahmud Ab Rahman and Ahmad Azizan Idris from the Malaysia Honeynet Project Chapter) presents a typical attack using a malicious pdf file.  
  
Submission deadline has passed. Results have been posted below. For any questions and inquiries, please contact forensicchallenge2010@honeynet.org.  
  
**Skill Level: Intermediate**  
  
**The Challenge:**  

PDF format is the de-facto standard in exchanging documents online. Such popularity, however, has also attracted cyber criminals in spreading malware to unsuspecting users. The ability to generate malicious pdf files to distribute malware is functionality that has been built into many exploit kits. As users are less cautious opening PDF files, the malicious PDF file has become quite a successful attack vector.  
The network traffic captured in lala.pcap contains network traffic related to a typical malicious PDF file attack, in which a unsuspecting user opens a compromised web page, which redirects the user's web browser to a URL of a malicious PDF file. As the PDF plug-in of the browser opens the PDF, the unpatched version of Adobe Acrobat Reader is exploited and, as a result, downloads and silently installs malware on the user's machine.

1. How many URL path(s) are involved in this incident? Please list down the URL path(s) found. (1pt)
2. What code can you find inside the PCAP file? Explain what the code does. (2pts)
3. What file(s) can you find within the PCAP file? If any files are found, please zip compress into password protected file (password infected) with file name: \[your email\]\_Forensic Challenge 2010 – Challenge 6 – Extracted Files.zip and submit (3pts)
4. How many object(s) are contained inside the PDF file? (1pt)
5. Using PDF dictionary and object referencing, explain in detail the flow structure of a PDF file. (1pt)
6. How many filtering schemes are used for the object streams and what are they? Explain how you can decompress the stream. (1pt)
7. Which object streams might contain malicious content? List the object and explain the obfuscation technique(s) used. (3pts)
8. What exploit(s) are contained inside the PDF file? Which one that actually runs and triggers the vulnerability(ies)? Please provide some explanation for your answer. (4pts)
9. Are there any payloads inside the PDF file? If any, list them all and explain what they do. Which payload will be executed? (2pts)
10. With the understanding of the PDF format structure, please explain how we can enable other exploits to run when the PDF file is opened. (2pts)

Bonus:

1. Please provide the dot graph of the PDF object’s connectivity inside the PDF file. (1pt)
2. Please provide an automated solution to extract and analyze JavaScript code within the PDF file. Be creative! (describe your solution below, but submit any source code and executable in a compressed zip file with file name \[your email\]\_Forensic Challenge 2010 – Challenge 6 – Bonus2.zip via our submission form [https://www.honeynet.org/challenge2010/](https://web.archive.org/web/20180729053915/https://www.honeynet.org/challenge2010/).) (1pt)

This work by Mahmud Ab Rahman and Ahmad Azizan Idris is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License

**The Winners:**

1. Vos (Russia) - [Vos's submission (perfect score!)](https://web.archive.org/web/20180729053915/https://www.honeynet.org/files/vos_Forensic_Challenge_2010_-_Challenge_6_-_Submission.pdf) - Sha1: 0eaf2a4f7559c6420e7d5fb1f8bdf2b4521e670f
2. Cordut Marinescu (Romania) - [Cordut's submission](https://web.archive.org/web/20180729053915/https://www.honeynet.org/files/codrut_Forensic_Challenge_2010_-_Challenge_6_-_Submission.pdf) - Sha1: 9ee2e4f3fd7fbd74fc7904a7cc43a889769a557a
3. Mike Mai Tu (Canada)- [Mike's submission](https://web.archive.org/web/20180729053915/https://www.honeynet.org/files/mike_Forensic_Challenge_2010_-_Challenge_6_-_Submission.pdf) - Sha1: c84e401b426f7a4c62f199b68aa05059528c3370

| Attachment | Size |
| --- | --- |
| lala.pcap | 40.67 KB |
| \[your email\]\_Forensic Challenge 2010 - Challenge 6 - Submission Template.doc | 72.5 KB |
| \[your email\]\_Forensic Challenge 2010 - Challenge 6 - Submission Template.odt | 21.75 KB |
| vos\_Forensic\_Challenge\_2010\_-\_Challenge\_6\_-\_Submission.pdf | 840.58 KB |
| mike\_Forensic\_Challenge\_2010\_-\_Challenge\_6\_-\_Submission.pdf | 564.53 KB |
| codrut\_Forensic\_Challenge\_2010\_-\_Challenge\_6\_-\_Submission.pdf | 291.07 KB |
