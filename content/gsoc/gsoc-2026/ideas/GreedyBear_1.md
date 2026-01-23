---
title: "Greedybear: Injection / Event Collector API"
date: "2025-01-20"
project_url: "https://github.com/intelowlproject/Greedybear"
hours: "175 - 350 based on received proposal"
mentor: "Tim Leonhard, Matteo Lodi"
project_type: "Improving an existing tool"
---

### Project Overview
The goal of this project is to expand GreedyBear’s data ingestion capabilities by developing a robust, standalone Injection / Event Collector API. Currently, GreedyBear relies solely on pulling data from T-Pot instances; this project will transform it into a versatile data hub capable of receiving telemetry from diverse external sources.

By creating a secure gateway for authenticated applications, we aim to empower honeypot developers to leverage GreedyBear as a centralized frontend and data store for their own security research.

### Key Objectives
* API Architecture Design: Design a scalable and secure API endpoint specifically tailored to handle incoming event data in a structured format.

* Authentication & Security: Implement a reliable authentication layer to ensure that only verified, external applications can inject data into the GreedyBear database.

* Data Processing Pipeline: Build the logic to validate, process, and save incoming event data, ensuring it remains consistent with GreedyBear’s existing schema.

* Honeypot Ecosystem Expansion: Enable third-party honeypots to use GreedyBear as a reliable backend, moving beyond the current T-Pot-centric model.

### Contributor Profile & Required Skills
* Building a public-facing API for security data requires a blend of precision and architectural foresight. We are looking for a contributor who possesses:

* Technical Proficiency in Python: You have a solid grasp of Python and are comfortable working within modern web frameworks to build backend services.

* Architectural Diligence: You have the motivation to thoroughly design an API from the ground up, considering edge cases, data validation, and long-term maintainability.

* Security Mindset: You understand the importance of safe data ingestion and are committed to implementing reliable, tested code that protects the integrity of the database.

* Documentation Excellence: You recognize that an API is only as good as its documentation, and you are eager to provide clear, actionable guides for future integrators.