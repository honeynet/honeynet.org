---
title: "HoneyProxy 1.1 - Dubai - released!"
authors: ["Maximilian Hils"]
date: "2013-01-24"
categories: 
  - "gsoc"
tags: 
  - "gsoc"
---

![](images/drupal_image_1019.png)

Ready for the Honeynet Project Meeting in February, we are pleased to announce our second release of HoneyProxy!

Started as a Google Summer of Code 2012 project, HoneyProxy is a lightweight tool that allows live HTTP and HTTPS traffic inspection and analysis. This release features a new Report Editor which allows you to analyze your flows, aggregate data or search for anomalies in your traffic dumps. It is our first independent release after GSoC 2012 and I'm happy to say that HoneyProxy has grown steadily over the last months.

You can find **the latest release**, **documentation** and a **live demo** on [honeyproxy.org](http://honeyproxy.org)!

Changelog:

- New Feature: **Report Editor - analyze & aggregate** your traffic ([docs](https://github.com/mhils/HoneyProxy/wiki/Report-Editor-Manual))
- New Feature: Search for **similar flows**
- New Feature: Display request and response **checksums**
- Improvement: PrettyPrint JSON responses
- Improvement: Show similar flows when hitting a **`HTTP 304 Not Modified`** response
- Improvement: Show subsequent flows when the response causes a redirect (**`HTTP 301/302/307`**)
- Bugfixes: Many!
- Internal Changes: Removed dependency on jQuery UI and Google Closure Library
- Internal Changes: Codebase is now completely AMD-modularized.
- Other: HoneyProxy 1.1 supports the latest versions of mitmproxy and netlib.

The release name is attributed to the HoneyNet [Project Workshop](http://dubai2013.honeynet.org) and Member Meetup in Dubai this February. Thank you for your support!
