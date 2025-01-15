---
title: "鑑識分析挑戰 6：分析惡意編碼 PDF 檔案"
authors: ["Roland Cheung"]
date: "2010-11-01"
categories: 
  - "challenge"
tags: 
  - "challenge"
  - "forensic-challenges"
  - "hong-kong"
  - "malware"
  - "pdf"
  - "traditional-chinese"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

**鑑識分析挑戰 6：分析惡意編碼 PDF 檔案 -** (由來自馬來西亞團隊的Mahmud Ab Rahman和Ahmad Azizan Idris提供) 利用含惡意編碼 PDF檔案進行的典型攻擊。  

請在2010年11月30日星期二之前在 [https://www.honeynet.org/challenge2010/](https://www.honeynet.org/challenge2010/) 透過我們的表格 (請使用 [MS word解答範本](/files/[your%20email]_Forensic%20Challenge%202010%20-%20Challenge%206%20-%20Submission%20Template - Traditional Chinese.doc) 或 [Open Office解答範本](/files/[your%20email]_Forensic%20Challenge%202010%20-%20Challenge%206%20-%20Submission%20Template - Traditional Chinese.odt)) 提交您的挑戰解答。結果約在12月的第三個星期公佈。)  

難度等級：中級  

歡迎透過下列鏈結訪問:[英文版內容](https://www.honeynet.org/challenges/2010_6_malicious_pdf)  

**挑戰內容：**  

PDF 格式是在線文件交換的業界標準 (de facto standard)。由於它的普及性，因此亦吸引了罪犯利用它來向信任的使用者傳播惡意程式。在很多攻擊工具中已經包含了建立惡意編碼 PDF檔案的功能來散播惡意程式。如果使用者對開啟 PDF 檔案缺乏警覺性，惡意編碼 PDF檔案會是一個頗成功的攻擊手段。  

在網路封包記錄 lala.pcap 內藏有關於一個典型的惡意編碼 PDF檔案。這個封包記錄了一個使用者開啟了一個已被入侵的網頁，然後被重新轉向去下載一個惡意編碼 PDF檔案。當瀏覽器內的PDF插件開啟PDF時，沒有安裝修補程式的Adobe Acrobat Reader會被攻擊，結果在使用者的電腦上無聲無色地下載並安裝惡意程式。

1. 在這次事故中包含了多少個 URL 路徑？請列出找到的URL 路徑。(1分)
2. 在PCAP檔案內，你能找到什麼程式碼？請解釋這些程式碼做了什麼。 (2分)
3. 在PCAP檔案內，你能找到什麼檔案嗎？若找到任何檔案，請利用zip密碼保護(密碼：infected)的壓縮檔案方式，將檔案命名為：\[your email\]\_Forensic Challenge 2010 – Challenge 6 – Extracted Files.zip並提交到[https://www.honeynet.org/challenge2010/](https://www.honeynet.org/challenge2010/)。
4. 在PDF檔案內包含多少個物件？(1分)
5.  請利用PDF 字典及物件參考詳細解釋PDF檔案的流程結構。(1分)
6.  有多少個過濾機制應用在物件串流，它們是什麼？請解釋你如何將串流解壓。
7.  哪個物件串流可能藏有惡意編碼內容？請列出該物件及解釋所使用的隱匿技術 (obfuscation technique(s))。(3分)
8.  在PDF檔案內包含了什麼攻擊？哪一個攻擊能成功執行並觸發漏洞？請在答案上提供一些相應的解釋。 (4分)
9.  在PDF檔案內包含了什麼負載 (payloads)？如果有，請列出及解釋它們做了什麼，那些負載(payload)會被執行？(2分)
10. 對於PDF 格式結構的理解，請解釋在開啟 PDF 檔案時，我們能如何啟動其他攻擊 (2分)

獎勵分：

1. 請提供PDF 文件內PDF物件連結的 dot graph (1分)
2. 請提供一個在 PDF檔案內提取JavaScript程式碼並進行分析的自動方案。請拿出你的創意！(描述你的方案，然後將源始碼和執行檔利用zip壓縮檔案方式命名為：\[your email\]\_Forensic Challenge 2010 – Challenge 6 –Bonus2.zip並提交到[https://www.honeynet.org/challenge2010/](https://www.honeynet.org/challenge2010/ "https://www.honeynet.org/challenge2010/")。 (1分)

**下載：**  

[lala.pcap](/files/lala.pcap) Sha1: 77183f064996b18276fd44dfcc3048bbb8216da2  

[\[your email\]\_Forensic Challenge 2010 - Challenge 6 - Submission Template - Traditional Chinese.doc](/files/[your%20email]_Forensic%20Challenge%202010%20-%20Challenge%206%20-%20Submission%20Template%20-%20Traditional%20Chinese.doc) Sha1: F6EA583DA1687874D184C632F75C4249A644ECFA  

[\[your email\]\_Forensic Challenge 2010 - Challenge 6 - Submission Template - Traditional Chinese.odt](/files/[your%20email]_Forensic%20Challenge%202010%20-%20Challenge%206%20-%20Submission%20Template%20-%20Traditional%20Chinese.odt) Sha1: 2039799E7F304D029EC0F7276A328C23ADE1619F
