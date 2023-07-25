---
title: "The Spamhattan Project"
date: "2016-01-11"
---

_Let’s develop a nextgen spamtrap and create intel feeds for .NL_

  

  

A rising amount of criminals are spreading cryptoware in order to ‘make money’. Cryptoware is ransomware that secretly encrypts files, like documents and pictures, of innocent users. The criminals make money by selling the decryption key. Most of the cryptoware is spread via email. Virus-scanners and anti-spam solutions have a hard time in defending against those threats and often there are no Indicators of Compromise (IoC) that help detecting infected devices in an early phase.

  

  

**How to defend against this new threat?** It’s key to catch new versions and incarnations of cryptoware in an early phase. Most often the cryptoware is spread via email so it was decided to focus on attracting lots of emails by creating a next generation spamtrap honeypot. Why create something new? Many people have reported about running a spamtrap! Why is nobody sharing tools?

  

We decided to create the spamtrap honeypot based on these elements:

  

  
- Should be Open-Source
  
- Be able to receive and analyze spam messages in high volume
  
- Act as a regular mailserver, NOT an open-relay (like Shiva)
  
- Act as a honeypot: never send out any mail (bounces, ndr, etc)
  

  

**What will The Spamhattan Project deliver?** By deploying the spamtrap in strategic economic sectors in The Netherlands insight in spam targeted at Dutch citizens will be gained. Also information about the actors behind the spamruns can be gathered. Key organizations, like ISPs, major banks and NCSC-NL will be warned in an early phase when new cryptoware campains are detected.

  

  

**Will this spamtrap be of use to other countries as well?** In our current spamtrap deployment we’ve only attached .NL domains to our spamtrap. By deploying the spamtrap yourself and feeding the right spam-sources you will be able to create your own Intel feed. Information and tips&tricks in order to get the **right** spam feed will be provide in future blog postings and presensations.

  

  

A first proof-of-concept of the spamtrap honeypot has been created and is crunching the first spam messages. Based on the results a next version is currently being developed. In the end we would like to release the source-code under an open-source license. Keep an eye on this blog and the **HoneyNED** website! ([https://www.honeyned.nl/](https://www.honeyned.nl/))

  

  

_Jop (email myname@honeyNED.nl)_
