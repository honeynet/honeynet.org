---
title: "Glutton 1.0"
date: 2023-08-03T20:41:27+02:00
authors: ["Lukas Rist"]
tags: ["honeypot", "glutton"]
---

I'd like to announce the 1.0 release of the server-side, low-interaction honeypot Glutton.

First commit was on [July 11th, 2016](https://github.com/mushorg/glutton/commit/adfbf78d9e226e76158a404634d062c6b2db7283)

<!--more-->

Initially we just redirected all incoming traffic:

```bash
$ iptables -t nat -A PREROUTING -p tcp -j REDIRECT --to-port 5000
$ iptables -t nat -A PREROUTING -p udp -j REDIRECT --to-port 5001
```
With [conntrack](https://blog.cloudflare.com/conntrack-tales-one-thousand-and-one-flows/) we were able to look up the original destination port. This is crucial when trying to identify the protocol but in order to set the correct source port when responding.

GSoC 2017 with [Mohammad Bilal](https://github.com/furusiyya) with his many [contributions](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2). As part of this project, we added TCP and SSH proxying. Allowing to place Glutton between the attacker and a real and potentially vulnerable system. At the same time, the Telnet worm Mirai (and Hajime) were making the rounds. We added a simple handler creating a login prompt and handling the rather simple tests the attackers used to verify the system.

On January 26th, 2017 we released the [reworked](https://github.com/mushorg/glutton/commit/df5efe922617ebe68312b3ccb5ea984265436507) networking stack using [Freki](https://github.com/kung-foo/freki) by [Jonathan Camp](https://github.com/kung-foo). Freki is a tool for manipulating packets in userspace. Using iptable's raw table, packets are routed down into userspace where Freki takes over. A set of rules is applied allowing for a large amount of flexibility. For example, you can forward all TCP ports to an HTTP honeypot and log the requests. Or you can proxy TCP port 22 into a docker container running an ssh honeypot.

```bash
$ iptables -A INPUT -j NFQUEUE --queue-num 0
$ iptables -A OUTPUT -j NFQUEUE --queue-num 0
```

SMB (EternalBlue by WannaCry), Jabber, MQTT

Introducing HPFeeds end of 2018: Basic Go client implementation of [hpfeeds](https://github.com/rep/hpfeeds), a simplistic publish/subscribe protocol, written by Mark Schloesser ([rep](https://github.com/rep/)), heavily used within the Honeynet Project for internal real-time data sharing. Now using the [version](https://github.com/d1str0/hpfeeds) by [Brady Sullivan](https://github.com/d1str0).

Mid 2019: StdOut and store TCP payloads

In 2021 Ethereum RPC, Hadoop, ADB, memcache and VMWare attack handlers

Mid 2022: replying to TCP requests with some random data.
```go
// sending some randome data
randomBytes := make([]byte, 12+rand.Intn(500))
if _, err = rand.Read(randomBytes); err != nil {
	return err
}
if _, err = conn.Write(randomBytes); err != nil {
	return err
}
```

Producing events to Ochi

[Switching](https://github.com/mushorg/glutton/commit/10f496130b1600460992dfb1102ff6cfbe67e94c) from nfqueues to TPROXY based on a [blog post](https://blog.cloudflare.com/how-we-built-spectrum/) on Cloudflare by [Marek Majkowski](https://twitter.com/majek04). Their Spectrum is surprisingly similar to how Glutton functions as a honeypot, listening on all ports and handling traffic transparently.

```bash
iptables -t mangle -I PREROUTING -p tcp -m state ! --state ESTABLISHED,RELATED \
-j TPROXY --on-port 5000 --on-ip 127.0.0.1
```
Fully supporting TCP and UDP. Highly recommend reading [this post](https://blog.cloudflare.com/everything-you-ever-wanted-to-know-about-udp-sockets-but-were-afraid-to-ask-part-1/) about UDP.