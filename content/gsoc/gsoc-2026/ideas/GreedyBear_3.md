---
title: "Greedybear: Cross-Platform Payload & Artifact Integration"
date: "2025-01-23"
project_url: "https://github.com/intelowlproject/Greedybear"
hours: "175 - 350 based on received proposal"
mentor: "Tim Leonhard, Matteo Lodi, Federico Gibertoni"
project_type: "Improving an existing tool"
---

### Project Overview
The goal of this project is to bridge the gap between T-Pot’s local filesystem and GreedyBear’s centralized interface. Currently, valuable forensic artifacts—such as malware payloads collected by the Dionaea honeypot—are stored locally within the T-Pot environment and remain inaccessible to GreedyBear analysts.

By establishing a secure pipeline to extract these files from the `~/tpotce/data directory`, we aim to transform GreedyBear from a metadata-only dashboard into a comprehensive malware repository, allowing researchers to download and analyze the actual samples captured in the wild.

### Key Objectives
* Payload Extraction Pipeline: Develop a reliable mechanism to monitor and extract raw payload files from T-Pot's Dockerized filesystem and transmit them to GreedyBear.

* T-Pot Configuration & Optimization: Tinkering with T-Pot’s internal configurations or proposing upstream changes to ensure artifacts are exposed in a way that is both accessible and secure.

* Safe Artifact Management: Implement a secure storage and delivery system within GreedyBear that allows users to view and download samples without compromising the security of the host platform.

* Deep Service Integration: Create a tighter coupling between the T-Pot sensor nodes and the GreedyBear management server, ensuring that every event in the Elastic stack can be linked back to its original raw artifact.

### Contributor Profile & Required Skills
This project is ideal for a "full-stack" security developer who enjoys working at the intersection of infrastructure and application development. We are looking for a contributor who demonstrates:

* Systems & DevOps Fluency: You are comfortable navigating Linux environments and managing Docker containers, as much of this work happens at the OS and container orchestration level.

* Python Backend Skills: You can write clean, efficient Python code to handle file transfers, data validation, and API integration.

* Technical Curiosity & Grit: You have the motivation to dive deep into two different codebases (GreedyBear and T-Pot) to understand their inner workings and propose structural improvements.

* Security Awareness: You understand the risks associated with handling live malware samples and are committed to implementing "safe-by-design" workflows for file handling and presentation.