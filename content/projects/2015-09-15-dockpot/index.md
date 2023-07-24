---
title: "Dockpot - high interaction SSH honeypot"
date: "2015-09-15"
---

## What is dockpot?

* * *

Dockpot is a high interaction SSH honeypot based on Docker. It's basically a NAT device that has the ability to act as an SSH proxy between the attacker and the honeypot (Docker container in that case) and logs the attacker's activities. It will create a new docker container for the first connection it gets, NAT the SSH connections to it, destroy the container when the number of the connections to it is zero.

 

## Download

* * *

Dockpot is available on [https://github.com/eg-cert/dockpot](https://github.com/eg-cert/dockpot)
