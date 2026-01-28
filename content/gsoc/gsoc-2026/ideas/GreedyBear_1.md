---
title: "Greedybear: Injection / Event Collector API"
date: "2025-01-20"
project_url: "https://github.com/intelowlproject/Greedybear"
hours: "175 - 350 based on received proposal"
mentor: "Tim Leonhard, Matteo Lodi"
project_type: "Improving an existing tool"
---

### Project Overview
GreedyBear obtains all its data by pulling it from a T-Pot instance. While this will always be the main data source, it would be great to build an API where external, authenticated applications can inject data into GreedyBear’s database. This API would accept incoming event data in a specified format, process and save it. This would give honeypot developers the option to use GreedyBear as a frontend / data store.

### Goal
Have a documented and tested API endpoint that enables GreedyBear to receive event data from other sources than T-Pot in a safe and reliable manner.

### Required Skills
* basic knowledge of Python
* motivation to thoroughly design and implement an API endpoint