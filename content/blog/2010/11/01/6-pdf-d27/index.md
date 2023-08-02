---
title: "取证分析挑战 6 - 分析恶意编码 PDF 档案"
authors: ["Roland Cheung"]
date: "2010-11-01"
categories: 
  - "challenge"
tags: 
  - "challenge"
  - "forensic-challenges"
  - "malware"
  - "pdf-d64"
  - "simplified-chinese"
---

  

**取证分析挑战 6：分析恶意编码 PDF 档案 -** (由来自马来西亚分支的Mahmud Ab Rahman和Ahmad Azizan Idris提供) 利用含恶意编码 PDF档案进行的典型攻击。  
  
  
  
  
  
请在2010年11月30日星期二之前在 [https://www.honeynet.org/challenge2010/](https://www.honeynet.org/challenge2010/) 透过我们的表格 (请使用 [MS word解答范本](/files/[your%20email]_Forensic%20Challenge%202010%20-%20Challenge%206%20-%20Submission%20Template - Simplified Chinese.doc) 或 [Open Office解答范本](/files/[your%20email]_Forensic%20Challenge%202010%20-%20Challenge%206%20-%20Submission%20Template - Simplified Chinese.odt)) 提交您的挑战解答。结果约在12月的第三个星期公布。)  
  
  
  
  
  
难度等级：中级  
  
  
  
  
欢迎透过下列链接访问:[英文版内容](https://www.honeynet.org/challenges/2010_6_malicious_pdf)  
  
  
  
  

**挑战内容：**  
  
  
  
  

PDF 格式是在线文件交换的业界标准 (de facto standard)。由于它的普及性，因此亦吸引了罪犯利用它来向信任的使用者传播恶意程序。在很多攻击工具中已经包含了建立恶意编码 PDF档案的功能来散播恶意程序。如果使用者对开启 PDF 档案缺乏警觉性，恶意编码 PDF档案会是一个颇成功的攻击手段。  
  
  
在网络封包记录 lala.pcap 内藏有关于一个典型的恶意编码 PDF档案。这个封包记录了一个使用者开启了一个已被入侵的网页，然后被重新转向去下载一个恶意编码 PDF档案。当浏览器内的PDF插件开启PDF时，没有安装修补程序的Adobe Acrobat Reader会被攻击，结果在使用者的计算机上无声无色地下载并安装恶意程序。

  

  
2. 在这次事故中包含了多少个 URL 路径？请列出找到的URL 路径。(1分)
  
4. 在PCAP档案内，你能找到什么程序代码？请解释这些程序代码做了什么。 (2分)
  
6. 在PCAP档案内，你能找到什么档案吗？若找到任何档案，请利用zip密码保护(密码：infected)的压缩档案方式，将档案命名为：\[your email\]\_Forensic Challenge 2010 – Challenge 6 – Extracted Files.zip并提交到[https://www.honeynet.org/challenge2010/](https://www.honeynet.org/challenge2010/)。
  
8. 在PDF档案内包含多少个对象？(1分)
  
10. 请利用PDF 字典及对象参考详细解释PDF档案的流程结构。(1分)
  
12. 有多少个过滤机制应用在对象串流，它们是什么？请解释你如何将串流解压。
  
14. 哪个对象串流可能藏有恶意编码内容？请列出该对象及解释所使用的隐匿技术 (obfuscation technique(s))。(3分)
  
16. 在PDF档案内包含了什么攻击？哪一个攻击能成功执行并触发漏洞？请在答案上提供一些相应的解释。 (4分)
  
18. 在PDF档案内包含了什么负载 (payloads)？如果有，请列出及解释它们做了什么，那些负载(payload)会被执行？(2分)
  
20. 对于PDF 格式结构的理解，请解释在开启 PDF 档案时，我们能如何启动其它攻击 (2分)
  

  

奖励分：

  
  

  
2. 请提供PDF 文件内PDF对象连结的 dot graph (1分)
  
4. 请提供一个在 PDF档案内提取JavaScript程序代码并进行分析的自动方案。请拿出你的创意！(描述你的方案，然后将源始码和执行档利用zip压缩档案方式命名为：\[your email\]\_Forensic Challenge 2010 – Challenge 6 –Bonus2.zip并提交到[https://www.honeynet.org/challenge2010/](https://www.honeynet.org/challenge2010/ "https://www.honeynet.org/challenge2010/")。 (1分)
  

  

**下载：**  
  
  
[lala.pcap](/files/lala.pcap) Sha1: 77183f064996b18276fd44dfcc3048bbb8216da2  
  
  
[\[your email\]\_Forensic Challenge 2010 - Challenge 6 - Submission Template - Simplified Chinese.doc](/files/[your%20email]_Forensic%20Challenge%202010%20-%20Challenge%206%20-%20Submission%20Template%20-%20Traditional%20Chinese.doc) Sha1: 5ECBE476A7012BD51285B604C3958F21E251BF90  
  
  
[\[your email\]\_Forensic Challenge 2010 - Challenge 6 - Submission Template - Simplified Chinese.odt](/files/[your%20email]_Forensic%20Challenge%202010%20-%20Challenge%206%20-%20Submission%20Template%20-%20Traditional%20Chinese.odt) Sha1: E17D187A7656A2154D69DB55F71AA0E198747B4F
