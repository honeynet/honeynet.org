---
title: "Google Hack Honeypot"
---

Google Hack Honeypot is the reaction to a new type of malicious web traffic: search engine hackers. It is designed to provide reconnaissance against attackers that use search engines as a hacking tool. Developed by Ryan McGeehan & Brian Engert of the Chicago Chapter.

Home page: [http://ghh.sourceforge.net/](http://ghh.sourceforge.net/)

 

## **What is GHH?**

* * *

Google Hack Honeypot is the reaction to a new type of malicious web traffic: search engine hackers. GHH is a “Google Hack” honeypot. It is designed to provide reconaissance against attackers that use search engines as a hacking tool against your resources. GHH implements honeypot theory to provide additional security to your web presence.

Google has developed a powerful tool. The search engine that Google has implemented allows for searching on an immense amount of information. The Google index has swelled past 8 billion pages \[February 2005\] and continues to grow daily. Mirroring the growth of the Google index, the spread of web-based applications such as message boards and remote administrative tools has resulted in an increase in the number of misconfigured and vulnerable web apps available on the Internet.

These insecure tools, when combined with the power of a search engine and index which Google provides, results in a convenient attack vector for malicious users. GHH is a tool to combat this threat.

GHH is powered by the [Google](http://google.com/) search engine index and the Google Hacking Database (GHDB) maintained by the [johnny.ihackstuff.com](http://johnny.ihackstuff.com/) community.

 

## **Honeynet Research with GHH**

* * *

You can view research done with GHH in the Honeynet Project's "Know Your Enemy" [paper on web application honeypots.](https://www.honeynet.org/papers/webapp)

**GHDB Honeypots Available:**

GHDB Signature #365 **Emulated** (intitle:"PHP Shell \*" "Enable stderr" filetype:php) GHDB Signature #833 (filetype:php HAXPLORER "Server Files Browser") GHDB Signature #733 ("Enter ip" inurl:"php-ping.php") GHDB Signature #365 (intitle:"PHP Shell \*" "Enable stderr" filetype:php) GHDB Signature #935 (inurl:"install/install.php") GHDB Signature #361 ("Powered by PHPFM" filetype:php -username) GHDB Signature #161 (inurl:phpSysInfo/ "created by phpsysinfo") GHDB Signature #1013 ("SquirrelMail version 1.4.4" inurl:src ext:php) GHDB Signature #162 (allinurl: admin mdb) GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" )) GHDB Signature #937 (filetype:blt "buddylist") GHDB Signature #734 ("File Upload Manager v1.3" "rename to") GHDB Signature #58 (inurl:passlist.txt) GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt GHDB Signature #769 (inurl:webutil.pl)

GHDB Signatures are maintained by the [johnny.ihackstuff.com](http://johnny.ihackstuff.com/) community.

 

## News

* * *

**February 23, 2007-** We have released a "Know Your Enemy" paper with the [Honeynet Project](https://www.honeynet.org/). You can view it [here](https://honeynet.org/papers/webapp/). We have also released an updated set of tools to go with the paper release, which includes remote logging for honeynets over XML-RPC and SSL, malware collection, and improved logging of browser headers. (Available on the SourceForge download page)

**November 1, 2005 -** Bugfix made to the php-ping honeypot. We have also begun heavy development into a GHH honeynet.

**October 23, 2005 -** We've made some bugfixes to the Haxplorer honeypot. Thanks for those who sent in suggestions.

**August 1, 2005 -** It's 3:30 in the morning, and GHH v1.1 has been released. New features include file spoofing, MySQL (honeynet) support, and 7 new prebuilt honeypots. Send any comments or questions to soda\_popinsky@users.sourceforge.net (email now working, apparently the last 6 months it hasn't. Feel free to resend any questions.)

**June 20, 2005** - GHH v1.1 is being developed and is looking to release on the first of August. Send any comments or questions to soda\_popinsky@users.sourceforge.net

**Febuary 17, 2005** - The site has been updated and tweaked. The release appears to have gone well. Planning and design sessions for the next major release of GHH will be taking place shortly. Anyone interested in getting involved should shoot us an email: gsmith3231@users.sourceforge.net

**Febuary 13, 2005** - First GHH Release, 7 honeypots and template available on [Sourceforge Project Page](http://sourceforge.net/projects/ghh).
