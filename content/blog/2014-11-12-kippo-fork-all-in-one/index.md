---
title: "Kippo fork - all in one"
date: "2014-11-12"
tags: 
  - "kippo"
---

Hello,  
  
last week I published kippo fork [https://gitlab.labs.nic.cz/honeynet/kippo](https://gitlab.labs.nic.cz/honeynet/kippo)  
which contains commits from [https://github.com/micheloosterhof/kippo-mo](https://github.com/micheloosterhof/kippo-mo)  
(Michel Oosterhof brought awesome SFTP, and exec support)  
and original kippo [https://github.com/desaster/kippo](https://github.com/desaster/kippo)  
(I am very pleased is now on github. was on google code before).  
  
On top of that are my changes:  
\- use shasum to store binaries from wget and SFTP (less disk space is used)  
\- store records about SFTP downloads in db  
\- log client IP and port in textlog  
\- log only info about downloads in textlog  
\- config file supports hpfeeds settings (more info in README)  
\- terminal doesn't reset when user logs out (no clear screen in ttylog)  
\- accept port other than 80 in wget (difference from original kippo)  
  
There are other changes from Michel Oosterhof  
in [https://github.com/micheloosterhof/kippo](https://github.com/micheloosterhof/kippo)  
which I want to add to fork sometime later.  
  
have a nice day,  
  
Katarina Durechova  
CZ.NIC (member of Czech Chapter)
