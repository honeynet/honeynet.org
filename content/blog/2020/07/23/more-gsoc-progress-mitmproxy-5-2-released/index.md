---
title: "More GSoC Progress: Mitmproxy 5.2 released!"
authors: ["Maximilian Hils"]
date: "2020-07-23"
categories: 
  - "gsoc"
  - "news"
coverImage: "logo-brand-inverted-1.png"
---

We are excited to announce the release of [mitmproxy 5.2](https://github.com/mitmproxy/mitmproxy/releases/tag/v5.2), a free and open source interactive HTTPS proxy! As the first part of his Google Summer of Code (GSoC) at the Honeynet Project, our student [Martin Plattner](https://mplattner.at/) ([@MartinPlattnr](https://twitter.com/MartinPlattnr)) has completely revamped mitmproxy's replacement feature, which is a powerful tool to modify and redirect HTTP messages.

As a small demonstration, Martin showed us how we can make these turbulent times much more bearable with a simple mitmproxy invocation:

![](images/mapremote_bbc_dogs.jpg)

`mitmproxy --map-remote "|^.+\.jpg$|https://placedog.net/640/480?random"`

Well... please look at the dogs, not the headlines. :)

If you are interested in learning more, head over to Martin's post on the [mitmproxy blog](https://mitmproxy.org/posts/releases/mitmproxy52/)!
