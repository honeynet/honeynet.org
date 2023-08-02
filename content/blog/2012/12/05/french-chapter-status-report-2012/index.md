---
title: "French Chapter Status Report 2012"
authors: ["Guillaume Arcas"]
date: "2012-12-05"
categories: 
  - "android"
  - "chapters"
tags: 
  - "chapter"
  - "report"
---

ORGANIZATION

Active members: - Sébastien Tricaud - Guillaume Arcas - Anthony Desnos - Franck Guénichot - François-René Hamelin - Christophe Grenier

DEPLOYMENTS We have following technologies deployed:

\- Kippo on honeycloud. Goal of this deployment is to provide a centralized instance of Kippo & share findings, logs, collected data. - HoneyProxy on honeycloud. - Honeeebox

RESEARCH AND DEVELOPMENT

\* New tools => HoneyProxy as part of GSoC 2012. => FAUP (formerly furl) => OpenNormalizer => PhotoRec/TestDisk => A.R.E. / AndroGuard

Enhanced tools: => minor HPfeeds patches. => TestDisk & PhotoRec: Too many improvements to list them (More than 150 commits) => minor (not-yet-committed) modifications for Kippo: make kippo randomly accept/reject login/passwords & work without prepopulated password database.

PROJECTS

\=> Centralized Kippo Honeypot This project's goal is to provide members with a standard Kippo server and allow them to redirect incoming SSH scan to this server instead of dropping them.

FINDINGS

\=> Analysis of country wide DNS Traffic => Analysis of HTTP usage by malware

PAPERS AND PRESENTATIONS

\=> S. Tricaud - Hack.lu 2011 - How Visualization makes it possible => S. Tricaud - HES - Capture me if you can => S. Tricaud / CIRCL LU - CanSecWest 2012 - Scrutinizing a country using passive DNS and PicViz => Honeynet Worksho, Network Training, Visualization Training => S. Tricaud, FIRST Malte 2012 => A. Desnos, Android: Static Analysis Using Similarity Distance (HICSS) => A. Desnos,Android : from reversing to decompilation (Blackhat Abu Dhabi) => A. Desnos,Analyzing Android Applications (Computer Security Congress - Mexico City) => A. Desnos,Android Malwares: is it a dream ? (EICAR)

GOALS

\=> GSoC mentoring => Workshop => Enhancing tools

\=> Focus on analysis: OSINT, dedicated tools including Timeline Builder. => "HoneyCIF" based on HPFeeds. As described here\[http://threatthoughts.com/2012/05/07/introduction-to-the-collective-intelligence-framework/\], "CIF allows you to run queries against many data sources at once. If you have other private data sources available, particularly via XML (RSS), JSON, or in a file (e.g. CSV), you can incorporate those, as well as additional OSINT sources."

MISC ACTIVITIES

\=> A.R.E. / AndroGuard funded by Rapid7 => Franck Guénichot co-authored Forensic Challenge #9 (Mobile malware) => ongoing discussion with french botnets.fr community on collaboration on specific areas => new website, twitter account

MENTORING

\=> HoneyProxy - G. Arcas - GSoC 2012 => Automated Attack Community Graph Construction #1 & #2 - F.Guénichot (Backup mentor) - GSoC 2012
