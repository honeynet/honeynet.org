---
title: "Detecting Conficker"
authors: ["Tillmann Werner"]
date: "2009-03-30"
tags: 
  - "conficker"
  - "detection"
  - "downadup"
  - "scanner"
  - "signature"
---

As you know, bad things are going to happen on April 1st: people will be sending out emails to their friends, telling silly jokes and putting MTAs under a higher load. Besides that (but not quite that bad), Conficker will activate its domain name generation routine to contact command-and-control servers. We have been researching this piece of malware recently, with a focus on how to detect Conficker-infected machines. Felix and I had a discussion with Dan Kaminsky about the possibilities to actively detect Conficker and wrote a scanner for this task. Our proof-of-concept code is publicly available and [can be downloaded from here](http://iv.cs.uni-bonn.de/wg/cs/applications/containing-conficker/). The output looks like this:

  

  
`  
./scs.py 127.43.16.76  
Could not send SMB request to 127.43.16.76:445/tcp.  
./scs.py 127.99.100.2  
127.99.100.2 seems to be infected by Conficker.  
./scs.py 127.36.15.80  
127.36.15.80 seems to be clean.  
`

  

A windows python to exe build of the same tool is [available here](http://www.doxpara.com/scs.zip). Further, the nature of Conficker's server service shellcode can be exploited to detect infection attempts. Here are our snort rules we created based on signatures generated with [nebula](http://nebula.carnivore.it " nebula – An Intrusion Signature Generator") that match the static shellcode:

  

  
`  
alert tcp any any -> $HOME_NET 445 (msg: "conficker.a shellcode"; content: "|e8 ff ff ff ff c1|^|8d|N|10 80|1|c4|Af|81|9EPu|f5 ae c6 9d a0|O|85 ea|O|84 c8|O|84 d8|O|c4|O|9c cc|IrX|c4 c4 c4|,|ed c4 c4 c4 94|&`  
`  
alert tcp any any -> $HOME_NET 445 (msg: "conficker.b shellcode"; content: "|e8 ff ff ff ff c2|_|8d|O|10 80|1|c4|Af|81|9MSu|f5|8|ae c6 9d a0|O|85 ea|O|84 c8|O|84 d8|O|c4|O|9c cc|Ise|c4 c4 c4|,|ed c4 c4 c4 94|&`

  

This shellcode string can even be used with [ngrep](http://ngrep.sourceforge.net/ "ngrep - network grep") as a lightweight Conficker IDS:

  

  
`  
$ sudo ngrep -qd eth0 -W single -s 900 -X  
0xe8ffffffffc25f8d4f108031c4416681394d5375f538aec69da04f85ea4f84c84f84d84fc44f9ccc497365c4c4c42cedc4c4c494263c4f38923bd3574702c32cdcc4c4c4f71696964f08a203c5bcea953bb3c096969592963bf33b24699592514f8ff84f88cfbcc70ff73249d077c795e44fd6c717cbc404cb7b040504c3f6c68644fec4b131ff01b0c282ffb5dcb61f4f95e0c717cb73d0b64f85d8c7074fc054c7079a9d07a4664eb2e244680cb1b6a8a9abaac45de7991dacb0b0b4feebeb  
'tcp port 445 and dst net 127.0.208.0/24'  
`

  

If ngrep detects a matching packet, it prints a line like the following:

  

  
`  
88.29.81.25:2238 -> 127.94.208.64:445 [AP] .....SMB%................................................T...T...&..@...\.P.I.P.E.\..............................?..............H.H.D.H.H...1.......1...\.axvmrXmJJVGxhtnmhAVmIJrjFTQDJCvfRwqgxalfTYTObcmhRrDhctYQGlndNZRQxfcAQjRpALmMsUElrvXiQuauTRwyHarfCGDQ......_.O..1.Af.9MSu.8....O..O..O..O.O..Ise...,.....&`

  

Both the scanner and the detection methods can be used to contain Conficker's impact, and are being [integrated into various popular scanning tools](http://www.doxpara.com/?p=1285 "DoxPara") right now with the help of the [Conficker Working Group](http://www.confickerworkinggroup.org/wiki/). We'll be providing much more information about detecting, mitigating and  containing Conficker in a new "Know Your Enemey" white paper soon, so call back here for more information.

  

  

Tillmann
