---
title: "GSoC 2017 Project Summary:  Glutton improvements, the new “all eating honeypot”"
authors: ["Roberto Tanara"]
date: "2017-10-23"
categories: 
  - "gsoc"
tags: 
  - "gsoc-d20"
  - "gsoc-glutton"
  - "gsoc2017"
---

#### Student [Mohammad Bilal](https://gist.github.com/furusiyya) contributed this post as a project summary of his GSoC2017 experience. 

# Merged Pull Requests

## [](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2#1--connection-timeout-added)[1- Connection Timeout Added](https://github.com/mushorg/glutton/pull/79)

Issues Resolved: [#72](https://github.com/mushorg/glutton/issues/72), [#59](https://github.com/mushorg/glutton/issues/59)  
Description Glutton support number of services (protocol handlers) so each service mean number of connection on that service. So It crash after some time with error: `[user.tcp] accept tcp [::]:5000: accept4: too many open files`, and this error was due to the allowance of limited number of open file descriptors by the operating system. There was no deadline set for opened connections so most of the connections never get closed. In result, the number of opened connections gradually cross the maximum open file descriptors limit and cause panic. So I added connection timeout = 72 second, number of opened connection will never reach the open file descriptor limit. Another reason was [Freki](https://github.com/kung-foo/freki/); Glutton useses freki as a networking core so freki handler crashes because of improper error handling in Glutton. So I improved error handling of protocol handlers and glutton stops crashing.

## [](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2#2--logrus-replaced-with-zap)[2- Logrus Replaced with ZAP](https://github.com/mushorg/glutton/pull/81)

Issues Resolved: [#66](https://github.com/mushorg/glutton/issues/66)  
Description  
Logrus replaced with [zap](https://github.com/uber-go/zap) because of the performance and effecient of structured logging zap. In this enhancement following magor improvements were made:

- Bumped up to Freki V2  
    Previously Glutton logging depends upon Freki because freki initializes logger and return to Glutton. In latest version Freki provide access to its logger module beyond API boundaries so now glutton have own logger.
- Improved Error Formatting  
    Proper format for errors logging is now used by all modules of the system.

## [](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2#3--context-implementation)[3- Context Implementation](https://github.com/mushorg/glutton/pull/83)

Issues Resolved: [#75](https://github.com/mushorg/glutton/issues/75), [#82](https://github.com/mushorg/glutton/issues/82)  
Description Following Packages are added:

- [Context](https://golang.org/pkg/context/)Glutton spawn a lot of go-routines so it was becoming challenging to keep go-routines in the application context, and because go-routines are not covered by garbage collector. So I used context package for having more control on go-routines so now glutton closes all go-routines gracefully on shutdown signal. Now its easier to pass values (flags) to any level in the application context hierarchy because it also support for carrying values and provide abstraction.
- [Docopt](https://github.com/docopt/docopt.go)  
    Docopt is used for automatically parsing flags for command line interface.

# [](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2#pull-request-submitted-for-review)Pull Request submitted for review

## [](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2#1--enhancement-plus-tcp-proxy)[1- Enhancement Plus TCP Proxy](https://github.com/mushorg/glutton/pull/91)

Issues Resolved: [#85](https://github.com/mushorg/glutton/issues/85)  
Description  
TCP Proxy is added. TCP Proxy was used from freki so it was a kind of dependency, we cannot add glutton formatted logging or for any enhancement it required us to make a PR to Freki. Another factor, freki open a separate port for TCP Proxy but we can have this with conn\_handler so tcp proxy is now a handler just like others, no need open other port.  
Furthermore documentation examples for using glutton as SSH Proxy and TCP Proxy are added. Some code refactoring is done for removing some confusing configurations.

# [](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2#closed-pull-requests)Closed Pull Requests

## [](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2#1--http-proxy-added)[1- HTTP Proxy Added](https://github.com/mushorg/glutton/pull/87)

Description  
I got success with HTTP MITM but couldn't bring HTTPS MITM in work. In meantime we found some enhancement issues with existing modules like: no event based logging in SSH MITM and no examples/docs for existing proxies. So I closed this PR and saved it into TODO list.

# [](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2#on-going-development)On Going Development

## [](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2#1--ssh-proxy-enhancement)[1- SSH Proxy Enhancement](https://github.com/furusiyya/glutton/tree/ssh-Proxy-Enhancement)

Description  
Right now I am working on enhancement of SSH MITM. It logs every thing going between attacker and SSH Server but logs are not in consumable format. I am trying to add event based logging. So first I refactored code and writing it by following Decorator Design Pattern so that in future it support dependencies injection.

# [](https://gist.github.com/furusiyya/38e8ca7963fd94ffc253e8b22e3338f2#others)Others

I tried to integrate container spawning feature on base of new connection but I couldn't due to limited documentation of Docker Client Moby and different version of docker client used in Freki. So I discussed this issue with Freki author and also opened an [issue](https://github.com/kung-foo/freki/issues/23) and so in response he updated Freki existing docker client (deprecated) to Moby Docker and he is planning for Freki further enhancement.
