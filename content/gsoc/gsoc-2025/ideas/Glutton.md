---
title: "Implementing Protocol Parsers for Glutton Using Spicy"
date: "2025-01-07"
project_url: "https://github.com/mushorg/glutton"
hours: "175 or 350 hours"
mentor: "Muhammad Bilal Arif"
project_type: "Improving an existing tool"
---

Glutton is a powerful Generic Low Interaction Honeypot designed to emulate various network services and capture malicious activity for security analysis. Its strength lies in its generic nature, supporting a wide range of network protocols.

**Goal of this project is to:**

1. Create Spicy-based parsers that replicate the functionality of Glutton's existing parsers
2. First implement an HTTP parser equivalent to the [current Go implementation](https://github.com/mushorg/glutton/blob/main/protocols/tcp/http.go)
3. Then implement a DNS parser following the same approach
4. For each protocol parser:
   - Write Spicy scripts that match the behavior of the existing Go parsers for HTTP and DNS
   - Generate parser code from the Spicy source and build an executable file 
   - Run executable and send test data streams to ensure its behavior matches Glutton parsers.
5. Document the implementation, testing methodology, and results as deliverables.

**Required Skills:**

- Proficiency in C++ programming
- Familiarity with Go programming language
- Understanding of Linux networking concepts
- Knowledge of HTTP and DNS protocols (or willingness to learn)

**Interested Students Should:**

1. Clone the [Glutton repository](https://github.com/mushorg/glutton)
2. Familiarize yourself with the [existing parsers](https://github.com/mushorg/glutton/tree/main/protocols)
3. Set up a [Spicy development environment](https://docs.zeek.org/projects/spicy/en/latest/installation.html)
4. Customize something in this example and submit as part of your proposal.
