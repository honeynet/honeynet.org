---
title: "Speaking Waledac"
authors: ["Felix Leder"]
date: "2009-01-27"
categories: 
  - "encryption"
tags: 
  - "botnet-protocols"
  - "encrypted-traffic"
  - "encryption"
  - "waledac"
---

While it seems to be impossible to say whether waledac is the successor of storm or not, what we _can_ do is take a look at the traffic encryption. They guys over at Shadowserver have already [blogged some details](http://www.shadowserver.org/wiki/pmwiki.php?n=Calendar.20081231) about this. We at the [Giraffe Chapter](/chapters/giraffe) investigated waledac's communication protocol further. Here are our results.

Waledac uses regular HTTP request to transmit command requests and to retrieve responses. It uses HTTP fast-flux proxies to hide the true origin of the command&control (C&C) server. Due to the fact that the regular Windows HTTP API (`WinINet`) is used, the traffic is hard to differentiate from regular HTTP traffic. Furthermore, it even allows Waledac to use proxy servers after the user has generally authenticated. The requests use POST and encrypted + encoded payload data:

```POST /fkuxmdptyjga.png HTTP/1.1 Referer: Mozilla Accept: */* Content-Type: application/x-www-form-urlencoded User-Agent: Mozilla Host: 93.152.147.192 Content-Length: 957 Cache-Control: no-cache```

```
a=_wAAArey4UgPCbKuN9ZgHBkYoPdoaWn0dw51xJClwDdO5bC6BkzuPHFhlrcJrwRxAf2xSZODFj7s97WqzKpkm2PS9P558QkFULZdu0evXky8d3anbYpDYn7fn5FvxIIeHejPsiJAYDv2EyekM2-JBgvnxSlMIr-4oQHiD6v9Tny8TxrtINu8MQ9tBXVSuxEiflMi2r-_8LqAdWpufsG0drou6eBXaUzT32z3oBjUbi1O47EqyWqNqw6cxijxC1jAcRhSFGrd-88wVqLutt6mSGZlRzAxB-2KspmEE0RyjfrEdNNhHNwWoZbLGosUFpiwC1hPBW8k2w1rqlVb08jZCMxtqu4cK5OWV-8sWZ4D0MSfM1uzLy-F4CnOUj0x61sMHEiIk2E7ZyLvDb-MNm4LeTKgNSPKO9QHo_29JsdIaH7D0ePXvCeAyAePYMfK-dN2KC3rruFNwd_VnYLGfrZ-5RTQk3UfDYIaPk1f9fDsojTyE1ffPl-rD3PpxdsnzA2BNyviWL9zaLYqqJKxq-WsmUyWKXQwRZx5tzTUVSfCSryQ5dWD67mMLDdoaRqQoeOF9cgiJ9zmO4kDkx39GwGN_MuhWhPkeFa1ExqlhkHh9ahc5cDW63mk73KCe2hdqwANdWtgqLujUsaB0BcifLENVJYxUCYnBXsAUAw5iitAbigZwBegODMXtXYln8VDpc3qX8nilIk0DUvZZLDnAPNbePQFKOMak2AV33BbLlk2C3NfwEqUotDpE-7SRIh1JPPAC4Ig04sW2hYDDQXG-PmIrs2W9rXey4pupbbTpSC2ZMJZlhfaSoqpkkzTYlMZG6dvMgm_4kI98YqLOC1XR5nVQrF944NklMDC7yZn5QFgjkeFaUMLOOmeOvXJ9nAPI5RYkZFheybkiKDc3IoMmjoa4h0nOHsod3-gTIWcZgp7Zhcxwc8DFg&b=AAAAAA
```

Waledac relies on up-to-date encryption technologies, like e.g., [RSA](http://en.wikipedia.org/wiki/RSA). We reverse engineered important parts of the traffic encryption engine inside the executable and extracted the important encoding and decoding parts. This enables us to read Waledac traffic. [Thanks to Greg Sinclair](http://www.nnl-labs.com/cblog/index.php?/archives/7-Waledacs-Communcation-Protocol.html), a design fault has been found that allows a fast crypto attack and offline decoding. We have developed a traffic decoder that has been used to gather information about the C&C protocol underneath.

### 1st Stage: Waledac handshake

The first request is of type `0xff` and is used to exchange encryption keys between the infected node and the botnet master.  The traffic is nicely formatted using XML. Each request and response start with "`lm`" and a command enclosed in "`t`"-tags.  The "`v`"-tag holds the protocol version, which varies among different generations of waledac binaries. The "`i`"-tag uniquely identifies the infected node and stays the same after reboots. Here is the decoding of the message from above:

```Type: 0xff Length: 695 getkey27_3d08552f660a522ca300201b4c740e62_0```

```
-----BEGIN CERTIFICATE----- MIIBvjCCASegAwIBAgIBADANBgkqhkiG9w0BAQQFADAlMQswCQYDVQQGEwJVSzEW MBQGA1UEAxMNT3BlblNTTCBHcm91cDAeFw0wOTAxMjcxOTUyMTJaFw0xMDAxMjcx OTUyMTJaMCUxCzAJBgNVBAYTAlVLMRYwFAYDVQQDEw1PcGVuU1NMIEdyb3VwMIGf MA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4Y00pilCs8lelq1WKagV00LKFPaQI l0oeVOb3oqStzbMrjz+QDCn8dULGGLCErUcndInZ2vNx/dXZLEjJIvpPjKPsBitY Tp5STzK4Z5E2fYfP3Usoei6dFv3uynrfP38jn6z08mharGyx/07AISD0TIkpcTMC gYAzJsYk+rNmOwIDAQABMA0GCSqGSIb3DQEBBAUAA4GBALHhri4p4umHYLIOqAwi +T7WKdp4M7zhtj8Gozt/LjQCCw2DlDL0SHDRwSdN2L5MiCMPFzYWGiSRrzftB4dI INOVF8W4eP18urV7yBDA17Apew8npsOt4g7rR+5GZfppH2CXsWH78HaSiOZ0ca0h vzaFmxy8dze7Q/B5+CwIUVBg -----END CERTIFICATE-----
```

As we can see, for the handshake, the `getkey` command is issued. The payload contains an X.509 certificate that holds a self-signed version of the node's public key. It is always generated on the fly even though containing a validity of one year. Details about the certificate can be found [here](/node/325 "Waledac is wishing merry christmas").

The response looks very similar. Version and command tags are duplicated. Instead of the certificate, a base64 encoded session key is exchanged that is encrypted using the RSA key contained in the request's certificate. This session key is then used for all subsequent C&C traffic.

`Type: 0xff Length: 264 27getkey`

`ccyRiwhtHQyryTh4oDjuvZzUUojo1bmxEo6I8S7XnsonuVndEswma6Syd0/b48uaZdDl8r4F/9m5xBxJYrtyvjmkMUrhtfXQw9PnoP9ESREUmFxnq5YpXaHdgm6OnaLU0BooXbBUyJ9jhum+g0ABhICDyxh7qU2eBkXMwRoiZvY=`

### 2nd Stage: Staying up to date

After a successfull handshake, waledac zombies issue a `notify` request containing an entity to contact, like e.g., "`mirabella_site`". Information about the host's clock is also included, possibly for time synchronization:

`Type: 0x2 Length: 229 notify27_2efd78765123abbadc0ded00deadbeef_0`

`mirabella_site`

Tue Jan 27 20:52:12 2009

Tue Jan 27 20:53:43 2009

Tue Jan 27 20:53:44 2009

79172453

The next reponse contains a lot of information: The node's external ip-address and hostname together with a special DNS IP and SMTP address. Both are not related to the node's IP address, but probably related to the fast-flux and spamming engine. In this case the DNS IP address belongs to an open DNS server in the US, the SMTP IP address points to an SMTP server at [Google](http://www.google.com/search?&q=giraffe+honeynet+project):

`Type: 0x2 Length: 337 27notify`

`bonn-007.pool.t-online.de`

93.137.206.86

216.195.100.100

209.85.201.114

3600

35

2000

`` `<pn="short_logs">true` ``

\]\]>

`</pn="short_logs">`

Very interesting are the "`dos`"-tags (denial of service?), and the commands attribute. The "`p`"-tag, in this case, contains an "`update`" command that results in the download of a picture of the Governor of California shown below. Besides the real image data, it carries additional data piggybacked that is to be executed on the node. This additional data is actually a Windows PE file, ecnrypted with a static key. We have observed several such updates, all with varying executables.

![](images/drupal_image_347.png)

### And the story continues...

We are not done with our investigations, yet. And there are still a lot of open question. We will keep you up to date here. Other interesting commands, like the following, are likely to come:

`Type: 0x3 Length: 109 taskreq27_2efd78765123abbadc0ded00deadbeef_0`

Stay tuned!
