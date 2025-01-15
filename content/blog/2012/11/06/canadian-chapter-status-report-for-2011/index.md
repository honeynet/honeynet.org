---
title: "Canadian Chapter Status Report For 2011"
authors: ["Natalia Stakhanova"]
date: "2012-11-06"
categories: 
  - "chapters"
tags: 
  - "chapter"
  - "report"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

ORGANIZATION Last year our chapter membership has gone through several changes: some members moved to new places and new positions and are no longer a part of the honeynet chapter, while others (Natalia Stakhanova) came back.

Our current members include Ali Ghorbani, Natalia Stakhanova, Hadi Shiravi (Unversity of New Brunswick) and Sami Guirguis (Toronto).

DEPLOYMENTS

We currently have deployed a cluster of server honeypots and SGNET sensor. Both are primarily used for capturing botnet network traffic.

RESEARCH AND DEVELOPMENT

1\. List any new tools, projects or ideas you are currently researching or developing.

Malware Classification: This is ongoing area of research for us. Accurate malware classification is still (and probably will be for quite a while) an important issue for anti-malware industry. Existing research on malware classification does not fully leverage malware network activity for detection. Thus we primarily focus on network behavior of malware samples aiming to build an automated online detection tool for recognition and characterization of malicious network traffic.

P2P Botnet Detection: This year we were able to focus on online detection of P2P bots. Our preliminary funding showed that it is possible to effectively detect botnets during a Command-and-Control (C&C) phase right before an attack launch based on analysis of network behavior only. We are currently working on more scalability issues and targeting more thorough testing.

2\. Explain what kind of help or tools or collaboration you are interested in.

FINDINGS

Earlier this year we were able to successfully reverse engineer one of ZeroAccess botnet samples found in the wild. Tweaking some of its code allowed us to monitor its communication and capture IP addresses of the compromised computers across the world. These findings have received some media attention in Canada (105.3FM: http://www.foxrocks.ca/TheBottomLine/story.aspx?ID=1773849 , Telegraph-Journal Fredericton). The results of the project were shared with the Department of Public Safety Canada.

PAPERS AND PRESENTATIONS

Are you working on or did you publish any papers or presentations, such as KYE or academic papers? If yes, please provide a description and link (if possible)

W. Lu, G. Rammidi and A. A. Ghorbani. Clustering Botnet Communication Traffic Based on N-gram Feature Selection, Computer Communications, Elsevier, 34(3): 502-514, 2011.

J. Rrushi, E. Mokhtari, and A. A. Ghorbani, Estimating Botnet Virulence within Mathematical Models of Botnet Propagation Dynamics, Journal of Computers & Security, Elsevier, 30(8): 791-802, 2011

D Zhao, I. Traoré, A. A. Ghorbani, B. Sayed, S. Saad, W. Lu, Peer to Peer Botnet Detection Based on Flow Intervals, 27th IFIP TC 11 Information Security and Privacy Conference SEC 2012: pp. 87-102, June 4-6 2012, Heraklion, Crete.

N. Stakhanova, M. Couture, and A. Ghorbani, Exploring network-based malware classification,Malicious and Unwanted Software (MALWARE), 2011 6th International Conference on , vol., no., pp.14-20, 18-19 Oct. 2011

J. Rrushi, E. Mokhtari, and A. A. Ghorbani, A statistical approach to botnet virulence estimation, In Proc. of the 6th ACM Symposium on Information, Computer and Communications Security (ASIACCS ’11), pp. 508-512, 2011.

GOALS

We have ambitious goals for the next year. We would like to continue our research on malware detection and develop a set of new techniques for fast and accurate detection malware on a network.

We would also like to continue our work on offering security workshop sessions to community.

MISC ACTIVITIES We were involved in several summer camps this year, giving workshops and presentations for kids focusing mostly on Internet security.

MENTORING

Natalia Stakhanova was mentoring a GSoC 2012 project: “Automated Attack Community Graph Construction” (https://honeynet.org/gsoc/slot2). The student has successfully finished the project.
