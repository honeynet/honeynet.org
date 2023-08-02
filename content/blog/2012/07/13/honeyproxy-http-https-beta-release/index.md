---
title: "HoneyProxy HTTP/HTTPS - Beta Release"
authors: ["Guillaume Arcas"]
date: "2012-07-13"
categories: 
  - "gsoc"
tags: 
  - "gsoc-d20"
  - "http-https-proxy-gsoc-honeyproxy-forensics"
---

At the middle of GSoC 2012, we are happy and proud to release a beta version of HoneyProxy, a lightweight tool that allows live HTTP and HTTPS traffic inspection and analysis.

Unlike other network tools like WireShark that display flow packet by packet, HoneyProxy only displays application layer data. Web objects then can be viewed through a browser.

HoneyProxy can be installed on a gateway or a bridge between analyzed computers and external networks like Internet, or on a Host to analyze HTTP/S connections from/to a Virtual Machine. It is intended to be used for malware analysis or network forensics/investigation.

Being compatible with [mitmproxy](http://mitmproxy.org/), HoneyProxy is also able to save HTTP conversations for later analysis as well as making scripted changes to HTTP traffic using Python (e.g. removing Cache headers to receive specific contents). It is developed as a HTML5 browser-based application working on top of a logging core written in Python. HoneyProxy GUI then is... a standard browser (see screenshots).

\[gallery link="none" size="large" columns="1" ids="6934,6935,6936,6937,6938,6939"\]

This released early beta version still lacks some features like running as a transparent web proxy or filtering/searching functions, but it works very nicely. :-)

Once installed and set up, HTTP/S flows can be viewed through a browser UI. Flows are listed line by line on a top panel. Clicking on a line displays a bottom panel with three tabs: a Raw tab that prints objects "as-is", a Preview Tab that shows the response in a human-readable way and a Header tab that prints... well, Headers data from both Client and Server, including Cookies and data posted through HTML forms. All objects - HTML code, JS snippets, images, binaries, uploaded files... - can be downloaded by clicking on a Download button or displayed in a pop-up window.

Future features will include a transparent proxy mode & filtering/searching/highlighting features. We also plan to bind HoneyProxy output to a tool like log2timeline so HTTP flows will be displayed like in this example: [log2timeline](http://log2timeline.net/browser.html).

Enough talk? Just jump over to our GitHub repo for the [installation instructions](https://github.com/mhils/HoneyProxy#quick-start)! If you want to check out how the project has developed over the last 6 weeks, check the [project page](https://honeynet.org/gsoc/slot10) for further details.

You can also download HoneyProxy in a single ZIP file here: [https://github.com/mhils/HoneyProxy/downloads](https://github.com/mhils/HoneyProxy/downloads).

Once installed, running HoneyProxy is as easy as typing: - `$ python honeyproxy.py` - `$ python honeyproxy.py -a xxx.xxx.xxx.xxx` (where xxx.xxx.xxx.xxx is the IP address you want HoneyProxy to be bound to). - `$ python honeyproxy.py -a xxx.xxx.xxx.xxx -w honeyproxy.log` (if you want to log web objects on disk). - `$ python honeyproxy.py --help`

By default HoneyProxy will listen on 8080/tcp port. That can be changed with -p option. Once launched, a new window will be open in your Internet brwser, displaying web flows that go through HoneyProxy.

For now, you'll have to configure the analyzed machine's browser to use HoneyProxy as HTTP/S proxy. As said, transparent proxy will soon be added so you will be able to redirect these flows to HoneyProxy with IPTables rules (on Linux) for example.

We love to hear from your experience with HoneyProxy. And if you have any feature suggestions, please get in touch.

Oh, and one more thing: Maximilian did a very nice job so far. :-)
