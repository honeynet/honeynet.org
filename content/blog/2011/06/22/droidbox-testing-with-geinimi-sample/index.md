---
title: "DroidBox: testing with Geinimi sample"
authors: ["Patrik Lantz"]
date: "2011-06-22"
categories: 
  - "android"
  - "encryption"
  - "gsoc"
tags: 
  - "android"
  - "droidbox"
  - "dynamic-analysis"
  - "gsoc"
  - "sandbox"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

One of the very first Android malwares, [Geinimi](http://www.symantec.com/security_response/writeup.jsp?docid=2011-010111-5403-99&tabid=2) has been analyzed in the application sandbox [DroidBox](https://www.honeynet.org/gsoc/slot5) that is currently being developed. The project is part of GSoC 2011 in collaboration with Honeynet and as a master thesis. The Geinimi application uses DES encryption, and it's possible to [uncrypt](http://code.google.com/p/androguard/source/browse/demos/geinimi_analysis.py) statically the content, see picture below.

![](images/drupal_image_693.png)

But it's very easy to do that because the key is not well hidden, so an approach by using dynamic analysis will be more interesting with complex samples. This first real-world sample analysis was carried out to specifically test the crypto API logging.

The malware attempts to contact one of the following command & control servers:

- www.widifu.com:8080
- www.udaore.com:8080
- www.frijd.com:8080
- www.islpast.com:8080
- www.piajesj.com:8080
- www.qoewsl.com:8080
- www.weolir.com:8080
- www.uisoa.com:8080
- www.riusdu.com:8080
- www.aiucr.com:8080
- 117.135.134.185:8080

to receive instructions and to send sensitive information stored on the phone. However, the Strings containing these servers are encrypted, DroidBox outputs the following logs on decryption performed by the application:

```
W/dalvikvm( 369): TaintLog: Encyption: KEY = { 1, 2, 3, 4, 5, 6, 7, 8 } with algorithm: DES W/dalvikvm( 369): TaintLog: Decrypted data[cmd] with DES W/dalvikvm( 369): TaintLog: Decrypted data[www.widifu.com:8080] with DES W/dalvikvm( 369): TaintLog: Decrypted data[www.udaore.com:8080] with DES W/dalvikvm( 369): TaintLog: Decrypted data[www.frijd.com:8080] with DES W/dalvikvm( 369): TaintLog: Decrypted data[www.islpast.com:8080] with DES W/dalvikvm( 369): TaintLog: Decrypted data[www.piajesj.com:8080] with DES W/dalvikvm( 369): TaintLog: Decrypted data[www.qoewsl.com:8080] with DES W/dalvikvm( 369): TaintLog: Decrypted data[www.weolir.com:8080] with DES W/dalvikvm( 369): TaintLog: Decrypted data[www.uisoa.com:8080] with DES W/dalvikvm( 369): TaintLog: Decrypted data[www.riusdu.com:8080] with DES W/dalvikvm( 369): TaintLog: Decrypted data[www.aiucr.com:8080] with DES W/dalvikvm( 369): TaintLog: Decrypted data[117.135.134.185:8080] with DES
```

The encryption key is retrieved as a byte buffer. We can also see that each of the servers mentioned are decrypted by the PID 369 (Geinimi app). Furthermore, the app makes an initial contact with a control server to negotiate the communication link:

`W/dalvikvm( 369): TaintLog: OSNetworkSystem.sendStream(localhost:5432) sending data=[hi,are you online?]`

W/dalvikvm( 369): TaintLog: OSNetworkSystem.receiveStream(). Response=\[hi,are you online??????????....\] from null:0 ID: 30

W/dalvikvm( 369): TaintLog: OSNetworkSystem.sendStream(unknown:0) sending data=\[yes,I'm online!\]

```
W/dalvikvm( 369): TaintLog: OSNetworkSystem.receiveStream(). Response=[yes,I'm online!???...] from localhost:5432 ID: 30` to then perform new decryptions of data from the communication protocol: `W/dalvikvm( 369): TaintLog: Decrypted data[IMEI] with DES W/dalvikvm( 369): TaintLog: Decrypted data[IMSI] with DES W/dalvikvm( 369): TaintLog: Decrypted data[CPID] with DES W/dalvikvm( 369): TaintLog: Decrypted data[_value@] with DES W/dalvikvm( 369): TaintLog: Decrypted data[PTID] with DES W/dalvikvm( 369): TaintLog: Decrypted data[_value@] with DES W/dalvikvm( 369): TaintLog: Decrypted data[SALESID] with DES W/dalvikvm( 369): TaintLog: Decrypted data[_value@] with DES W/dalvikvm( 369): TaintLog: Decrypted data[DID] with DES W/dalvikvm( 369): TaintLog: Decrypted data[_value@] with DES W/dalvikvm( 369): TaintLog: Decrypted data[sdkver] with DES W/dalvikvm( 369): TaintLog: Decrypted data[autosdkver] with DES W/dalvikvm( 369): TaintLog: Decrypted data[latitude] with DES W/dalvikvm( 369): TaintLog: Decrypted data[longitude] with DES W/dalvikvm( 369): TaintLog: Decrypted data[debug_outer] with DES W/dalvikvm( 369): TaintLog: Decrypted data[debug_internel] with DES
```
 
Further implementations to the sandbox include tainting data retrieved from the phone database by modifying [TaintDroid](http://appanalysis.org/tdroid10.pdf). Other features are: logging attempts to send SMS, emails and phone calls and also to log behavior related to file operations.
