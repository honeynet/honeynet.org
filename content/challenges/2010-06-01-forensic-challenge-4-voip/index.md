---
title: "Forensic Challenge 4 - VoIP"
date: "2010-06-01"
---

**Challenge 4 - VoIP -** (provided by Ben Reardon from the Australian and Sjur Eivind Usken from Norwegian Chapter) takes you into the world of voice communications on the Internet. VoIP with SIP is becoming the de-facto standard for voice communication on the Internet. As this technology becomes more common, malicious parties have more opportunities and stronger motives to take control of these systems to conduct nefarious activities. This Challenge is designed to examine and explore some of attributes of the SIP and RTP protocols. Enjoy the challenge.  

**Skill Level: Intermediate**  

**The Challenge:**  
  
**Section 1**

This attached logfile "logs\_v3.txt" was generated from an unadvertised, passive honeypot located on the internet such that any traffic destined to it must be nefarious. The honeypot was scanned by parties unkonwn, with a range tools and this activity is represented in the logs\_v3.txt file.

Notes on logs\_v3.txt  

- The IP address of the honeypot has been changed to "honey.pot.IP.removed". In terms of geolocation, pick your favourite city.
- The MD5 hash in the authorization digest is replaced with "MD5\_hash\_removedXXXXXXXXXXXXXXXX"
- Some octets of external IP addresses have been replaced with an "X"
- Several trailing digits of phone numbers have been replaced with an "X"
- Assume the the timestamps in the logfiles are UTC

1. What protocol is being used? Is it TCP or UDP? (1 point)
2. Could this log be the result a simple nmap scan being run against the honeynet? Explain  
    (1 point)
3. a) Name the scanning tools that may have been used to by the attacker (1 points).  
    b) What was the tool suite author's intended use of this tool suite ? Who was it designed  
    to be used by? (1 point)  
    c) One of these tools was only used against a small subset of extensions. Which were  
    these extensions and why were only they targeted with this tool ? (2 points)
4. a) How many extensions were scanned? Are they all numbered extensions, or named as  
    well?. List them (2 points)  
    b) Categorize these extensions into the following groups, and explain to method you  
    used:  
    \- Those that exist on the honeypot, AND require authentication (2 points)  
    \- Those that exist on the honeypot, and do NOT require authentication (2 points)  
    \- Those that do not exist on the honeypot (2 points)
5. Was a real SIP client used at any point ? If it was, what time was it used, and why ? (1  
    point)
6. List the following, include geo-location information.  
    \- Source IP addresses involved (1 point)  
    \- The real world phone numbers that were attempted to be dialled (2 points)
7. Draw a simple static or animated timeline of events, describing when and where certain  
    phases occurred from, and what the purpose of each phase was (5 points).
8. Assuming this were a real incident, write 2 paragraphs of an Executive summary of this  
    incident. Assume the reader does not have IT Security or VOIP experience.  
    a) First Paragraph: Write, in the minimum detail necessary a description the nature and  
    timings, and possible motives of the attack phases. (3 points)  
    b) Second Paragraph: What actions would you recommend should occur following this  
    particular incident, include any priority/urgency. Also describe any good practices that  
    should be employed to mitigate future attacks. (3 points)

**Section 2**

The attached packet capture "Forensic\_challenge\_4.pcap" was created by honeynet members for this forensic challenge in order to give participants an opportunity to employ network analysis skills in the VOIP context. Analyse this pcap and answer the following questions:

1. Which 4 protocols are involved in the PCAP (VOIP protocols and otherwise) ? Give a brief explanation as to their purpose. (4 points)
2. a) Which codec does the RTP stream use? (1 point)  
    b) How long is the sampling time (in milliseconds)? (1 point)
3. How did the attacker gain access to the server? List ways this could have been  
    prevented. (2 points)
4. What information was gained by the attacker ? (2 points)
5. The PCAP includes a (not so) hidden bonus! \[hint1: You can't read it in the pcap, hint2:  
    It's a city with an active honeynet chapter\]  
    a) Describe it, and explain how you found it. (10 points)  
    b) If VOIP packets between the two calling parties traverse an untrusted network (eg the  
    wireless/internet) and a similar PCAP was captured by a malicious party, would you think  
    this a security problem? why? (3 points)  
    c) Wireshark has an option "Use RTP timestamp". What is the function of this option? (2  
    points)
6. What technologies or protocols can be used to protect confidentiality of RTP traffic as it  
    traverses untrusted networks. ( 3 points)

**Section 3**  

1. What is "RTP injection" and describe how it functions. What conditions are required to  
    allow this? (2 points)
2. Explain how a SIP password digest could be intercepted or stolen. Is this a security  
    issue? why or why not. (2 points)
3. Is DDoS a threat to VOIP systems? Are there any general functional requirements of  
    telephony systems that would be impaired by a DDoS? (2 points)

  
This work by Ben Reardon and Sjur Eivind Usken is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.

**The Winners:**  

1. Franck Guenichot (France) - Franck's submission - Sha1: d1f59ebb514b9e3b559d3461782d9d60e754a1f9
2. Fabio Panigatti (Italy) - Fabio's submission - Sha1: c0a29a4110d08ed73c5f3fd8b31589a8b57f1e4b
3. Shaun Zinck (USA)- Shaun's submission - Sha1: b362c9fd94f4dd79d056322635b997640323e48d

| Attachment | Size |
| --- | --- |
| logs\_v3.txt | 1.92 MB |
| Forensic\_challenge\_4.pcap | 1.13 MB |
| \[your email\]\_Forensic Challenge 2010 - Challenge 4 - Submission Template.doc | 97.5 KB |
| \[your email\]\_Forensic Challenge 2010 - Challenge 4 - Submission Template.odt | 26.4 KB |
| franck\_guenichot\_Forensic\_Challenge\_2010\_-\_Challenge\_4\_-\_Submission.pdf | 2.11 MB |
| fabio\_panigatti\_Forensic\_Challenge\_2010\_-\_Challenge\_4\_-\_Submission.pdf | 146.59 KB |
| shaun\_zinck\_Forensic\_Challenge\_2010\_-\_Challenge\_4\_-\_Submission.pdf | 550.25 KB |
