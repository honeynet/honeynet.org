---
title: "Murofet, Zeus++ or just Zeus 2.1?"
authors: ["Guido Landi"]
date: "2010-10-15"
categories: 
  - "encryption"
tags: 
  - "murofet"
  - "zeus"
---

The first one writing about this new threat was [Marco Giuliani](http://www.prevx.com/blog/159/WinMurofetor-just-ZeuS.html). So, Murofet or Zeus++?

Taking a look at a couple of samples we were able to identify:

\- Same API hooks

\- Same encryption routine for configuration file (RC4)

\- Pretty much the same configuration file format

[Here](http://www.sysenter-honeynet.org/1e940baeb962042a6628f81c93aaecd1.raw) you can take a look at a decrypted configuration file. It's possible to realize that it makes use of the same block-based structure of Zeus configuration files. Just like any other Zeus it has a block with id 0x214e (at offset 0x1c) where the version of the builder used to create the bot is stored (at offset 0x2c). In our case that is 2.1.0.7.

So what about calling it just Zeus 2.1 ?
