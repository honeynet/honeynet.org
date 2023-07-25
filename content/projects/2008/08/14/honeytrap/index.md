---
title: "Honeytrap"
date: "2008-08-14"
---

[![honeytrap logo](images/logo.png)](https://github.com/tillmannw/honeytrap/blob/master/doc/logo.png)

## [](https://github.com/tillmannw/honeytrap#honeytrap)Overview

* * *

Honeytrap is a low-interaction honeypot and network security tool written to catch attacks against TCP and UDP services. It was developed by Tillmann Werner of the Giraffe Chapter. In its default configuration, it runs as a daemon and starts server processes on demand when a connection attempt to a port is made.

Different modes of operation are available that control how connections are handled. In _normal mode_, a server sends arbitrary data provided in template files as a basic means to emulate well-known protocols. Many automated attack tools will be fooled and continue with the attack dialog. A popular mode is the so-called _mirror mode_ in which incoming connections are proxied back to the initiator. This trick eliminates the need for protocol emulation in many cases. A third mode, the _proxy mode_, allows forwarding of specific sessions to other systems, e.g., high-interaction honeypots.

 

## Download

* * *

Honeytrap is available here: [https://github.com/tillmannw/honeytrap](https://github.com/tillmannw/honeytrap)

 

## [](https://github.com/tillmannw/honeytrap#plugins)Plugins

* * *

A module API provides an easy way to write custom extensions that are dynamically loaded into the honeypot. Aarriving attack data is assembled to a so-called _attack string_ that can be saved to files or a SQL database for manual investigation. Honeytrap comes with different plugins that run on these attack strings to extract additional information or emulate further actions. An example is the `httpDownload` module that extracts URL strings from attack data and invokes an external tool to automatically download respective resources.

 

## [](https://github.com/tillmannw/honeytrap#installation)Installation

* * *

Installing honeytrap is fairly straight forward. Simply run the following commands in the source tree root directory:

```
./configure  --with-stream-mon=<type>
make
sudo make install
```

The parameter `--with-stream-mon` specifies how honeytrap should look for incoming connection attempts. On Linux, the preferred choicde is `--with-stream-mon=nfq`, which instructs honeytrap to capture packets using the `iptables NFQUEUE`feature. When using this feature, an iptables rule like the following puts incoming TCP-SYN segments in a queue where they can be picked up by honeytrap:

```
sudo iptables -A INPUT -p tcp --syn --m state --state NEW --dport 445 -j NFQUEUE
```

Make sure not to queue packets to other critical services. Please refer to the INSTALL file and to the output of `./configure --help` for further information.

## [](https://github.com/tillmannw/honeytrap#an-example-attack)An Example Attack

* * *

Here's a captured attack by old-school IRC bot spreading via the all time classic MS04-011 LSASS exploit and a rudimentary FTP service built into the malware.

[![example attack](images/example.png)](https://github.com/tillmannw/honeytrap/blob/master/doc/example.png)
