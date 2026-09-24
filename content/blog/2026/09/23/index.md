---
title: "Extending the Artemis Scanner"
authors: ["Rafli Permana"]
date: "2026-08-17T17:00:00+02:00"
tags: ["gsoc", "Artemis","vulnerability scanner"]
---

Our [GSoC](https://summerofcode.withgoogle.com/) student Rafli Permana spent three months working under the supervision of Krzysztof Zając on [**Artemis Scanner**](https://github.com/CERT-Polska/Artemis).

Read about this summer project on [**CERT-Polska/Artemis**](https://imraflip.github.io/gsoc-artemis/).

**Student:** Rafli Permana

**Mentors:** Krzysztof Zając

**Organization:** The Honeynet Project

**Project:** [Artemis Scanner](https://github.com/CERT-Polska/Artemis)  
<!--more-->
---
## Overview
I spent this summer as a GSoC (Google Summer of Code) contributor on Artemis, a modular vulnerability scanner, under the mentorship of Krzysztof Zając. Artemis checks multiple aspects of website security and builds easy-to-read messages to send to organizations to get the vulnerabilities fixed - it’s the tool CERT Polska (Computer Emergency Response Team Poland) has used to find and report almost two million vulnerabilities and misconfigurations since 2023. I built a crawling pipeline and a frontend auth layer, added direct URL scanning, put CPE/CVE lookups on detected technologies, and more.

Artemis runs on Python 3.13 with Karton as the distributed task queue, Docker for the scanner modules, Redis for queueing and caching, and PostgreSQL for storing results. Every scanner module subclasses ArtemisBase, declares which Karton tasks it wants via filters, and saves findings that a separate reporting layer turns into HTML and email reports for the organization being scanned.

---
## Before GSoC
I opened my first Pull Request on Feb 22, 2026 - about two months before I was accepted. I didn’t know the codebase at all, so I started small: layout fixes, a redirect status code that was technically wrong (M2363), templates that hardcoded paths instead of using request.url_for (M2368). Some infra bugs too - an IPv6 crash in the blocklist range check (M2596), a flaky Grafana healthcheck (M2526).

Initially Artemis’s injection detectors would report every parameter they’d injected, even when only one of them was actually vulnerable - so a report might list five parameters when only one mattered. I added parameter minimization: after a hit, re-test each parameter individually and keep only the ones that independently reproduce the issue. Shipped it for LFI first (M2423, which also fixed a batching bug, capped further in M2525), then for SQL injection parameters (M2483) and SQL injection headers (M2584).

---
## The proposal
The project was split into two coding periods. Period 1 was infrastructure: direct URL scanning, a real crawling pipeline, a frontend authentication layer, and making Wappalyzer’s technology detection actually usable by downstream modules instead of just sitting in Postgres. Period 2 was supposed to build three new vulnerability detectors on top of that foundation - SSTI, OS command injection, and NoSQL injection.

The ordering wasn’t arbitrary. The crawl pipeline had to exist before any detector could use it, and technology tags had to flow through the task queue before anything could route on them. Build the plumbing first, then the things that use the plumbing.

---
## What I built
#### Frontend authorization layer

Every frontend route in Artemis was wide open. The only protection was CSRF on POST requests, which stops forged requests but does nothing if someone just browses to [ip]:5000 and reads your scan results directly. M2679 added a login page, session auth, and a FastAPI dependency on every frontend route.

I took this one first because it was a deployment blocker rather than a feature. Everything else on the roadmap puts more findings into that dashboard, so the longer an unauthenticated frontend stayed in place, the more there was behind it to walk into.


#### Crawling pipeline

This is the dependency the whole Period 2 plan sat on. A detector can only test the URLs it gets handed, so whatever coverage the crawler produced was the ceiling on every injection module I was going to write later - which is why it had to be rebuilt before any of them.

Artemis used to do single-page HTML parsing for crawling - no JS execution, no following links, no dedup. M2738 replaced that with Katana (run with -jc so it picks up endpoints buried in JS files) piped through uro for structural deduplication, cached in Redis behind a distributed lock so ten modules scanning the same host trigger exactly one crawl instead of ten, with a shorter cache TTL when the crawl times out so partial results don’t stick around for a full day. Four consumer modules migrated onto it in the same PR.

My original proposal had a third stage - gf for vulnerability-class filtering - and I dropped it. gf filters URLs by matching parameter names against English-language wordlists, but Artemis scans a lot of Polish infrastructure, where parameter names don’t reliably match those wordlists. A genuinely vulnerable parameter with an unusual name could get silently filtered out before any detector ever saw it - an optimization that can hide a real vulnerability isn’t a safe default.



#### Direct URL scanning

Artemis works out what to do with a target by classifying whatever you hand it, and each class drops into a fixed pipeline of modules. Direct URL scanning just means being able to hand it one exact address and have that address scanned as-is. I pulled it forward because it shortens the loop for everyone - my own testing for the rest of the project, and anyone who already knows the single endpoint they want checked.

Before this, Artemis’s classifier only understood domains, IPs, IP ranges, and ASNs. If we submitted a domain, it went through subdomain enumeration, then port scanning, then fingerprinting before any HTTP module ever saw a task - even if we already knew the exact URL we wanted scanned. M2899 taught the classifier to parse URLs directly and emit the TaskType.SERVICE task without the detour, so every HTTP module picks it up with zero changes - it’s the same task type the port scanner would eventually have produced anyway.

#### CPE tagging for detected technologies

This started small. Wappalyzer - the fingerprinting library Artemis uses to work out what software a site is running - detects things like Django or MongoDB on a target, but that result only went into Postgres for the report, so no downstream module could ever see it. M2978, fixed that: structured Technology objects carrying CPE (Common Platform Enumeration), version, and categories on the task payload, so downstream modules can route on what’s running on a target instead of reading it back out of the report. A CPE is the standardized name for one specific product at one specific version, and it’s the key vulnerability databases are indexed by - without it, “MongoDB 4.2” is just a string.

This is the tagging work only, with no vulnerability lookup yet, and splitting it out was deliberate. Same pattern as the crawler: the tags had to actually reach downstream modules through the task queue before anything could use them, so this had to land first - without it, the CVE lookup below would have no reliable way to know what product or version it was even checking.

#### CVE lookup for detected technologies

A CVE (Common Vulnerabilities and Exposures) is the public identifier for one specific known flaw in one specific piece of software, and it’s what makes the CPE strings from the previous deliverable worth carrying around. Building on that tagging from M2978, M2842 is an actual CVE discovery flow: switch the Go Wappalyzer wrapper to FingerprintWithInfo to get CPE strings, then query NVD (National Vulnerability Database) for known CVEs against them.

This is the payoff the tagging work was for, and it’s cheap in exactly the way the rest of the scanner isn’t: the target has already been fingerprinted, so turning “this host runs X 1.2” into “this host runs a version with known reported flaws” is a database question, not more probing traffic aimed at someone’s server.

#### OS command injection detector

With the crawler and the tagging in place, Period 2 was the detectors. I started with this one because it has the least ambiguous proof of the three: a command either executed on the target or it didn’t, so I could get the shared scaffolding right against a signal I trusted before moving to detectors that have to infer a result from error text.

M2947 implements two detection methods. Output-based: inject an echo of a random per-request marker through each shell separator (;, |, newline, $(...), backticks) and check whether the marker comes back - that proves execution actually happened, not just that the app returned a suspicious error string. Time-based blind: inject sleep N through the same separators and confirm a reproducible delay across several rounds measured against a baseline, for cases where there’s no visible output to check.

Since merging, the detector has already returned a real finding during production scanning - confirmation that the two detection methods hold up against live targets, not just the test suite.

#### Extracting shared logic

M3028 removed code instead of adding it. The SQL, ORM, and LFI detectors each ran the same sequence at the top of their run() method - crawl the target, add the seed URL back in, union in query-stripped variants, filter out static assets, cap the result - and the three copies had already started drifting apart from each other. I moved it into one function, get_links_to_scan(), in crawling.py, and all three detectors call it instead of carrying their own copy.

A further piece of sharing - a common result-building helper in injection_helpers.py and crawling.collect_parameters - landed inside O3051 (the NoSQL injection PR) instead of its own PR.

---

|  |  |
|---|---|
| Added / removed in merged code | **~5,403 / 457 lines** |
| More lines sitting in the open PR | **~1,951** |
| Total lines touched across merged and open PRs | **~7,811** |

---
## What I delivered in Artemis during GSoC
**11 delivered, 1 in review**
|         |                                                                      |                 |
| --------- | -------------------------------------------------------------------- | ----------------|
|    **M2738**|   Implement Katana + uro crawling pipeline with shared Redis cache   | May 22, 2026 |
|    **M2496**|    Implement ORM injection detector module                           | Jun 15, 2026 |
|    **M2883**|  Fix false positives from flaky services and save the probe URLs   | Jun 28, 2026 |
|    **M2844**|    Build all Go tools with one Go 1.25 toolchain                   | Jul 2, 2026  |
|    **M2899**|  Implement direct URL scanning                                     | Jul 8, 2026  |
|    **M2978**|  Add CPE information to detected web technologies                  |Jul 30, 2026|
|    **M3028**|    Extract shared crawl helpers from injection detectors | Aug 12, 2026|
|    **M2947**| Implement OS command injection detector module|Aug 19, 2026|
|    **M2842**|    Add CVE lookup for detected web technologies|Aug 25, 2026|
|    **O3051**|    NoSQL injection detectoropened | Aug 18, 2026|


---

## What’s still open / what’s next
NoSQL injection detector. Error-based detection with MongoDB operator payloads against both GET params and JSON bodies, matched against a clean baseline so normal error messages don't get flagged as vulnerable, plus blind detection for endpoints that swallow their errors and never surface a visible difference.

It had its first round of review and is now awaiting the follow-up changes. It also introduces injection_helpers.py, a new shared helper file for result-building and deduplication logic that used to be duplicated across detectors, plus a collect_parameters() helper in crawling.py.

---

## What I learned

A scanner that reports false positives is worse than one that reports nothing at all, because someone on the other end has to hand-verify every single finding before it goes out to an organization.

Shipping a detector or a feature is maybe 30% of the work. The reporter, the tests, the Docker integration, and the edge cases around it are the other 70%, and skipping any of them means it isn't actually done.

---

## Acknowledgements
Thanks to Krzysztof Zając for mentoring me through this, for the design pushback that made the final result better than what I would've shipped on my own. Thanks to Krzysztof Waliczek, who put in a lot of careful review time across the summer and caught things I would've missed. And I'm grateful to The Honeynet Project and CERT Polska for giving me the opportunity in the first place.
