---
title: "Glutton 1.0 Release"
date: 2023-09-23T20:41:27+02:00
authors: ["Lukas Rist"]
categories: ["honeypot"]
tags: ["honeypot", "glutton"]
---

{{<figure src="/2023/09/23/glutton-1.0/images/glutton.webp" alt="Glutton" width="30%">}}

I'd like to announce the 1.0 release of the server-side, low-interaction honeypot [Glutton](https://github.com/mushorg/glutton)!

We have built Glutton as a versatile honeypot, capable of receiving any network traffic by accepting connections on any port. Being very easy to adapt and extend, Glutton is a fantastic tool to understand network threats.

<!--more-->

First commit was on [July 11th, 2016](https://github.com/mushorg/glutton/commit/adfbf78d9e226e76158a404634d062c6b2db7283), the main objective was to receive traffic on every port without having to establish 65,535 listeners. This was initially achieved by just redirected all incoming traffic, regardless of their destination port:

```bash
$ iptables -t nat -A PREROUTING -p tcp -j REDIRECT --to-port 5000
$ iptables -t nat -A PREROUTING -p udp -j REDIRECT --to-port 5001
```

In order to make assumptions regarding the used network protocol, and in order to set the correct source port for the response packet, it is very advantageous to know the original request destination port. With [conntrack](https://blog.cloudflare.com/conntrack-tales-one-thousand-and-one-flows/) we were able to look up the original destination port.

Participating in Google Summer of Code 2017 with [Mohammad Bilal](https://github.com/furusiyya) with his many [contributions](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2). As part of this project, we added TCP and SSH proxying. Allowing to place Glutton between the attacker and a real, and potentially vulnerable system. At the same time, the Telnet worm Mirai (and Hajime) were making the rounds. We added a simple Telnet handler creating a login prompt and handling the rather simple tests the attackers used to verify the system and started capturing samples of the worm.

On January 26th, 2017 we released the [reworked](https://github.com/mushorg/glutton/commit/df5efe922617ebe68312b3ccb5ea984265436507) networking stack using [Freki](https://github.com/kung-foo/freki) by [Jonathan Camp](https://github.com/kung-foo). Freki is a tool for manipulating packets in userspace. Using iptable's raw table, packets are routed down into userspace using nfqueue where Freki takes over. A set of rules are applied, allowing for a large amount of flexibility. For example, you can forward all TCP ports to an HTTP honeypot and log the requests, or you can proxy TCP port 22 into a docker container running a SSH honeypot. We primarily used it to redirect the traffic to a honeypot server and binding it to a specific handler, based on the rule.

Here are the very basic iptables rules for nfqueue handling.

```bash
$ iptables -A INPUT -j NFQUEUE --queue-num 0
$ iptables -A OUTPUT -j NFQUEUE --queue-num 0
```

We quickly added more protocol handlers, specifically for SMB to handle EternalBlue/WannaCry (almost to the payload, contributions welcome), Jabber, and MQTT for IoT devices. Here it was that we started to use the flexibility of Glutton: Watching the TCP packets, we would identify a unknown protocol, investigate into the destination port and payload and start implementing a basic handler. Once deployed, we could incrementally expand the capabilities and the levels of interactions of our honeypot. Implement, observe, increment, observe, and so on.

Introducing HPFeeds end of 2018: Basic Go client implementation of [hpfeeds](https://github.com/rep/hpfeeds), a simplistic publish/subscribe protocol, written by Mark Schloesser ([rep](https://github.com/rep/)), heavily used within the Honeynet Project for internal real-time data sharing. Now using the excellent [fork](https://github.com/d1str0/hpfeeds) by [Brady Sullivan](https://github.com/d1str0). This is also how Glutton integrates into [T-Pot](https://github.com/telekom-security/tpotce) an open-source platform for multiple honeypots.

In an attempt to reduce the observe and implementation cycle, we added logging of TCP payloads to StdOut and storing them to disk in 2019. This allows for watching live traffic while tweaking the honeypot. The stored payloads can be used to quickly search the historic data for similar payloads to cross-reference. This lead to protocol handlers for Ethereum RPC, Hadoop, ADB, memcache, and VMWare attacks in the following two years.

Quite often we wouldn't be able to assume or guess the expected protocol, so in mid 2022 we made a small change, replying to TCP requests with some random data which occasionally lead to the attacking client sending additional packets, providing us with more clues on the protocol in question. Think of this as random server banners or an attempt to entice client error behavior.

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

Next up was a bigger change, after talking to the folks from [Shadowserver](https://www.shadowserver.org/) and running into some issues with setting up Glutton with traffic forwarding, we worked on [switching](https://github.com/mushorg/glutton/commit/10f496130b1600460992dfb1102ff6cfbe67e94c) from nfqueues to iptables' TPROXY, based on a Cloudflare [blog post](https://blog.cloudflare.com/how-we-built-spectrum/) by [Marek Majkowski](https://twitter.com/majek04). Their Spectrum is surprisingly similar to how Glutton functions as a honeypot, listening on all ports and handling traffic transparently. The rules employed more or less look like this:

```bash
iptables -t mangle -I PREROUTING -p tcp -m state ! --state ESTABLISHED,RELATED -j TPROXY --on-port 5000 --on-ip 127.0.0.1
```

This is approach is used to proxy both, TCP and UDP traffic to a single listener while keeping the original destination port in tact. This way we achieve what previously required the overhead of nfqueues with a mangle during pre-routing in iptables. This can also be converted to nft if required. We also highly recommend reading [this post](https://blog.cloudflare.com/everything-you-ever-wanted-to-know-about-udp-sockets-but-were-afraid-to-ask-part-1/) on the intricacies of UDP traffic.

Since this is running, we also started to produce events to our new front-end [Ochi](https://github.com/honeynet/ochi) which has a [publicly accessible](https://ochi.mushmush.org/) instance.
