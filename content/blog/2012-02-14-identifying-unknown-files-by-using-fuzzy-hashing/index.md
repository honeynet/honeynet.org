---
title: "Identifying unknown files by using fuzzy hashing"
date: "2012-02-14"
tags: 
  - "fuzzy-hashing"
---

Identifying unknown files by using fuzzy hashing  
  
Over the last couple of years I have captured about 2 gigabytes of malware using the Dionaea honeypot. Analysing and identifying those files can mostly be done by sites as Virustotal, Anubis or CWsandbox. By modifying the ihandler section in the dionaea.conf this can be done fully automated.  
Every now and then even these excellent analysis sites come up with nothing. No result or whatsoever. This could be because its a brand new sample of malware which simply isn't recognised yet or it is a morphed sample of a known and existing one.  
  
There still is a method to determine what kind of malware the file represent. This method is called fuzzy hashing. The technique finds its origin in spam filtering (spamsum)  
From the README file:  
  
“spamsum is a tool for generating and testing signatures on files. The signature is designed to be particularly suitable for producing a result that can be used to compare two emails and see if they are 'similar'. This can provide the core of a SPAM detection system.  
  
The algorithms in spamsum are in two parts. The first part generates a signature which is encoded as a string of ascii characters less than 72 characters long. The second part takes a new signature and a database of existing signatures (actually just a text file with one  
signature per line) and finds the existing signature that best matches the new signature. A match result in the range of 0 to 100 is generated, where 100 is a perfect match and 0 is a complete mismatch.”  
  
A similar tool based on spamsum is SsDeep maintained by Jesse Kornblum (if you google for it, a link to a sourceforge page shows up. This site is down on the time of writing this text but there are ubuntu packages available in the ubuntu package-tree. So a apt-get install ssdeep should do the trick ).  
  
So this can be done for unrecognized malware as well. By generating a hash from the alleged malware, we can compare it against the 2 gigabyte collection already caught and identified malware.  
  
By using ./ssdeep -lr 11a1f1acc4ed824dc1e332ce8c2fd50e > testhash  
  
you generate a file that looks like this:  
ssdeep,1.0--blocksize:hash:hash,filename  
3072:GiSkUYBQgZ+z1vezLPVr7Qe4lAtWhazqiatiPiHpOKeXmPFYZK/z:Gi3BBZ+5v0LtQx+tQauieHAXCFycz,"11a1f1acc4ed824dc1e332ce8c2fd50e"  
  
So if we do: ./ssdeep -lrm testhash .  
  
snip  
./3a74bc105edfe54445d1fca28cc4f542 matches testhash:11a1f1acc4ed824dc1e332ce8c2fd50e (99)  
./556b6807d33ebfe2ec95f3598e168f62 matches testhash:11a1f1acc4ed824dc1e332ce8c2fd50e (85)  
./daf46feccab82f6c86daae4f366bfbe1 matches testhash:11a1f1acc4ed824dc1e332ce8c2fd50e (75)  
./3bcd999965892aea89be5606f6811bfa matches testhash:11a1f1acc4ed824dc1e332ce8c2fd50e (69)  
./33a91a9ed61fe8f59190f4d73791bf06 matches testhash:11a1f1acc4ed824dc1e332ce8c2fd50e (82)  
./525fc4565d588c11a5b56aaf4f3c7a12 matches testhash:11a1f1acc4ed824dc1e332ce8c2fd50e (99)  
./fead84c5df2e585749a8da2ce583c926 matches testhash:11a1f1acc4ed824dc1e332ce8c2fd50e (99)  
/snip  
  
So for example, if we take out the last result “fead84c5df2e585749a8da2ce583c926” and run a clamscan against it, we come up with the following result:  
  
fead84c5df2e585749a8da2ce583c926: Worm.Kido-175 FOUND  
  
Where daf46feccab82f6c86daae4f366bfbe1 seems to match with Worm.Kido-268 FOUND. Another variant from the same malware family.  
  
We we can safely assume that the file is for 99 percent the same as “11a1f1acc4ed824dc1e332ce8c2fd50e” and is a variant of Kido-175  
Probably the same malware has been identified under different names. So, to be sure we have identified it correctly, we can also match it to other 99% matches in the list, e.g. "3a74bc105edfe54445d1fca28cc4f542".  
  
To sum up: All matches seem to indicate that this particular piece of malware is \_some\_ variant of Kido. Possibly a new incarnation. Even if we can't pinpoint which type it is exactly, we still can make some educated guesses as to the family and its dangers. Knowing what a certain malware tends to do (e.g. it tries to find a C&C server for further instructions) we can assess the potential threat this piece of malware poses. If all connections to C&C servers are blocked (because all known C&C are filtered and the usual IRC traffic blocked) an infection with this type of malware doesn't immediately mean a widespread breakout or data-leakage.  
  
So, even if the md5 checksums don't match, fuzzy hashing can come in handy to identify unknown and suspicious files.  
  
Thanks Dennis Lemckert (@dlemckert) for helping me out on some grammar issues :)
