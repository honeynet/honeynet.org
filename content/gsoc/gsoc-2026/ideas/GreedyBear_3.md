---
title: "Greedybear: Access payload files"
date: "2025-01-23"
project_url: "https://github.com/intelowlproject/Greedybear"
hours: "175 - 350 based on received proposal"
mentor: "Tim Leonhard, Matteo Lodi"
project_type: "Improving an existing tool"
---

### Project Overview
Currently GreedyBear obtains all its data from T-Pots Elastic stack. Some data that is collected by T-Pot however is not available there. Some honeypots, like Dionaea, collect payloads that are only written to the filesystem, that is to `~/tpotce/data`. It would be great to make those artifacts available in GreedyBear. This project might not be limited to work on GreedyBear but can also include tinkering with the configuration of T-Pot itself or even introducing changes to T-Pot.

Related issues:
https://github.com/intelowlproject/GreedyBear/issues/558
https://github.com/telekom-security/tpotce/discussions/1653

### Goal
Have a clean and reliable way to
* access or extract payload files and other samples from T-Pot
* present them to the user in a safe manner


### Required Skills
* basic knowledge of Python, Linux and Docker
* motivation to deeply dive into both projects, GreedyBear and T-Pot, to create a stronger integration