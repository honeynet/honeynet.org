---
title: "IntelOwl: Integration Ecosystem and Connector Optimization"
authors: ["Sanjib Behera"]
date: "2026-08-18T07:30:00+05:30"
tags: ["gsoc", "intelowl"]
---


IntelOwl's analyzers do the heavy lifting of threat intelligence i.e. scanning observables against dozens of services and producing structured results. But analysis in isolation is only half the picture. The **connectors** are what close the loop: they take those results and push them out to external platforms like [MISP](https://www.misp-project.org/), [OpenCTI](https://filigran.io/solutions/open-cti/), and [YETI](https://yeti-platform.io/) for further correlation, or to communication tools like Slack for real-time alerting.

<!--more-->

My Google Summer of Code 2026 project with The Honeynet Project focused on making this connector layer more robust, more standardized, and easier to extend. The work touched testing infrastructure, health checks, a new base class for CTI connectors with data model enrichment, external API compatibility updates, and infrastructure additions - shipped across [IntelOwl v6.7.0](https://github.com/intelowlproject/IntelOwl/pull/3840) and [IntelOwl v6.8.0](https://github.com/intelowlproject/IntelOwl/pull/3941) releases.

---

## Pre-GSoC Contributions

My journey started in February when I cloned the repository and set up the local environment. While exploring the codebase, I found several things worth fixing:

- **Notification Formatting:** System notifications were rendering as raw HTML. Fixed in [#3350](https://github.com/intelowlproject/IntelOwl/pull/3350).
- **Recent Scans Bug:** File jobs never showed up in the "Recent Scans" tab - a small but surprisingly unnoticed bug. Fixed in [#3383](https://github.com/intelowlproject/IntelOwl/pull/3383).
- **Analyzer Refactoring:** Several analyzers relied on flat files to check if an observable was present. Migrated those checks to the database in [#3427](https://github.com/intelowlproject/IntelOwl/pull/3427) and [#3507](https://github.com/intelowlproject/IntelOwl/pull/3507).
- **Additional fixes:** [#3558](https://github.com/intelowlproject/IntelOwl/pull/3558), [#3613](https://github.com/intelowlproject/IntelOwl/pull/3613), [#3648](https://github.com/intelowlproject/IntelOwl/pull/3648).

These contributions gave me a solid understanding of the codebase, and the consistent support and encouragement from [Matteo Lodi (@mlodic)](https://github.com/mlodic) - my mentor and IntelOwl's maintainer - cemented my decision to focus my proposal here. I drafted a proposal centered on the connector ecosystem (the accepted outline is on the [projects page](https://github.com/orgs/intelowlproject/projects/17)), got feedback from Matteo on Slack, and submitted it.

---

## GSoC Deliverables

### Connector Testing Framework

The connector testing framework had a known problem. It was built on legacy monkeypatches - an issue raised in [#3662](https://github.com/intelowlproject/IntelOwl/issues/3662). Meanwhile, the analyzer testing framework had already moved to a cleaner, structured approach using `unittest` superclasses. The connectors were left behind.

I refactored the connector testing framework to align with the analyzer approach across multiple PRs:

| PR                                                             | Description                          |
| -------------------------------------------------------------- | ------------------------------------ |
| [#3723](https://github.com/intelowlproject/IntelOwl/pull/3723) | Initial framework introduction       |
| [#3778](https://github.com/intelowlproject/IntelOwl/pull/3778) | Extended coverage and migration      |
| [#3795](https://github.com/intelowlproject/IntelOwl/pull/3795) | Additional connector test migrations |
| [#3799](https://github.com/intelowlproject/IntelOwl/pull/3799) | Further refinements                  |
| [#3807](https://github.com/intelowlproject/IntelOwl/pull/3807) | Integration test additions           |
| [#3839](https://github.com/intelowlproject/IntelOwl/pull/3839) | Final cleanup and legacy removal     |

The result: a modernized testing architecture with reusable test superclasses, unit tests and integration tests for connectors that previously had none, and a migration path that retired the legacy monkeypatch-based tests.

### External Integration Updates

#### YETI

Yeti's API v2 introduced schema changes that broke both the connector and analyzer. I updated the YETI connector ([#3736](https://github.com/intelowlproject/IntelOwl/pull/3736)) to use the new `/api/v2/auth/api-token` authentication flow and the `/api/v2/observables/extended` endpoint, and separately updated the YETI analyzer ([#3741](https://github.com/intelowlproject/IntelOwl/pull/3741)) to query the v2 search endpoints.

#### MISP

The MISP connector's error handling was minimal compared to what the MISP analyzer already had. I improved it in [#3781](https://github.com/intelowlproject/IntelOwl/pull/3781) - the connector now catches specific failure modes (like sending HTTP to an HTTPS port) and provides actionable error messages with optional debug context, matching the robustness of the analyzer side.

### Connector Health Checks ([#3811](https://github.com/intelowlproject/IntelOwl/pull/3811))

Before this work, connector health checks did one thing: fire a `HEAD` request at the configured URL. If the server returned any response (even a 405), it was considered healthy. This told you almost nothing useful - the URL could be reachable but the API key invalid, the token expired, or the service misconfigured.

I overhauled the health check for every connector to actually validate the connection end-to-end:

- **MISP:** Instantiates a `PyMISP` client and queries `misp_instance_version` - a lightweight GET that exercises authentication and returns the MISP server version.
- **OpenCTI:** Creates a `pycti.OpenCTIApiClient` and calls its built-in `health_check()`, which validates the token and instance reachability.
- **YETI:** Posts the API key to the `/api/v2/auth/api-token` endpoint and verifies an access token is returned.
- **Slack:** Calls `auth_test()` on the Slack SDK client, which validates the bot token and returns identity info.

Each health check also validates that the required configuration parameters (URL, API key, token) are actually present before attempting a connection, returning a clear message like "Missing config api key" rather than a cryptic exception.

### Bug Fixes

Alongside the framework work, I fixed several bugs I had noticed during my initial connector exploration, including [#3705](https://github.com/intelowlproject/IntelOwl/issues/3705).

All of these changes were merged into the [v6.7.0 release](https://github.com/intelowlproject/IntelOwl/pull/3840), tracked under the umbrella PR [#3832](https://github.com/intelowlproject/IntelOwl/pull/3832).

#### Health Check Tuple Refactoring ([#3907](https://github.com/intelowlproject/IntelOwl/pull/3907))

The connector-specific health checks described above returned results inconsistently with the rest of the plugin system. This PR standardized the `health_check` method signature across **all** plugin types (not just connectors) to return a `tuple[bool, str]` - a boolean status and a descriptive message.

### Introducing `CTIConnector` ([#3891](https://github.com/intelowlproject/IntelOwl/pull/3891))

This was the most significant architectural change of the summer. Before this PR, the three CTI connectors - MISP, OpenCTI, and YETI - each independently extracted the same information from the job object. Every connector had its own way of getting the observable name, determining if it was a hash or an IP, building the analysis URL, and pulling tag labels. This meant duplicated logic, inconsistent behavior, and a steep learning curve for anyone wanting to add a new CTI connector.

The `CTIConnector` base class extends the existing `Connector` class and provides a standardized set of reusable properties, organized into two categories:

**Observable Metadata** - everything about the observable itself:

```python
class CTIConnector(Connector):
    @property
    def observable_name(self) -> str: ...
    @property
    def observable_value(self) -> str: ...
    @property
    def classification(self) -> str: ...
    @property
    def hash_type(self) -> Optional[str]: ...
    @property
    def ip_version(self) -> Optional[int]: ...
    @property
    def analysis_url(self) -> str: ...
    @property
    def tag_labels(self) -> List[str]: ...
    @property
    def analyzer_names(self) -> List[str]: ...
```

**Data Model Enrichment** - opt-in access to IntelOwl's normalized analysis results:

```python
    @property
    def evaluation(self) -> Optional[str]: ...       # malicious, trusted, etc.
    @property
    def malware_family(self) -> Optional[str]: ...
    @property
    def kill_chain_phase(self) -> Optional[str]: ...
    @property
    def reliability(self) -> Optional[int]: ...
    @property
    def related_threats(self) -> List[str]: ...
    @property
    def external_references(self) -> List[str]: ...

    def get_enrichment_summary(self) -> dict: ...
```

The enrichment properties are backed by IntelOwl's merged `DataModel` - the same normalized verdict the UI displays. Each property returns `None` or an empty list when no data model exists, so connectors can safely check `self.has_data_model` and conditionally include enrichment data without risking exceptions.

With this in place, I refactored all three connectors (MISP, OpenCTI, and YETI) to inherit from `CTIConnector`. The connectors went from duplicating metadata extraction logic to simply accessing `self.observable_value` or `self.evaluation`.

The practical impact: MISP now automatically tags events with `evaluation:malicious` and `malware-family:...` when a data model is available. OpenCTI appends enrichment summaries to report descriptions and creates corresponding labels. YETI includes enrichment fields in the observable context. All of this happens because the data is accessible through a clean, shared interface rather than being reimplemented per-connector.

Comprehensive unit tests were added covering metadata extraction, job context properties, and data model enrichment across all edge cases (samples vs. observables, IP v4 vs. v6, various hash types, missing data models).

### MISP as an Optional Container ([#3938](https://github.com/intelowlproject/IntelOwl/pull/3938))

Previously, using the MISP connector required access to an external MISP instance. As part of expanding the ecosystem, MISP was added as an optional Docker container within IntelOwl. Users and developers can now spin up a local MISP instance alongside IntelOwl's other services with a single compose configuration. The corresponding documentation was also updated.

---

## Summary of All Contributions

### Pre-GSoC

| PR                                                                                                                                                                                             | Description                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [#3350](https://github.com/intelowlproject/IntelOwl/pull/3350)                                                                                                                                 | Fix notification formatting (raw HTML -> formatted) |
| [#3383](https://github.com/intelowlproject/IntelOwl/pull/3383)                                                                                                                                 | Fix file jobs missing from Recent Scans             |
| [#3427](https://github.com/intelowlproject/IntelOwl/pull/3427), [#3507](https://github.com/intelowlproject/IntelOwl/pull/3507)                                                                 | Refactor analyzers: flat files -> database          |
| [#3558](https://github.com/intelowlproject/IntelOwl/pull/3558), [#3613](https://github.com/intelowlproject/IntelOwl/pull/3613), [#3648](https://github.com/intelowlproject/IntelOwl/pull/3648) | Additional bug fixes and enhancements               |

### GSoC (shipped in v6.7.0)

| PR                                                                                                                                                                                                                                                                                                                                                                                             | Description                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [#3705](https://github.com/intelowlproject/IntelOwl/issues/3705)                                                                                                                                                                                                                                                                                                                               | Bug fix found during connector exploration |
| [#3723](https://github.com/intelowlproject/IntelOwl/pull/3723), [#3778](https://github.com/intelowlproject/IntelOwl/pull/3778), [#3795](https://github.com/intelowlproject/IntelOwl/pull/3795), [#3799](https://github.com/intelowlproject/IntelOwl/pull/3799), [#3807](https://github.com/intelowlproject/IntelOwl/pull/3807), [#3839](https://github.com/intelowlproject/IntelOwl/pull/3839) | Connector testing framework refactoring    |
| [#3736](https://github.com/intelowlproject/IntelOwl/pull/3736)                                                                                                                                                                                                                                                                                                                                 | YETI connector update for API v2           |
| [#3741](https://github.com/intelowlproject/IntelOwl/pull/3741)                                                                                                                                                                                                                                                                                                                                 | YETI analyzer update for API v2            |
| [#3781](https://github.com/intelowlproject/IntelOwl/pull/3781)                                                                                                                                                                                                                                                                                                                                 | MISP connector error handling improvements |
| [#3811](https://github.com/intelowlproject/IntelOwl/pull/3811)                                                                                                                                                                                                                                                                                                                                 | Connector health check overhaul            |
| [#3832](https://github.com/intelowlproject/IntelOwl/pull/3832)                                                                                                                                                                                                                                                                                                                                 | Umbrella PR                                |

### GSoC (shipped in v6.8.0)

| PR                                                             | Description                                                           |
| -------------------------------------------------------------- | --------------------------------------------------------------------- |
| [#3891](https://github.com/intelowlproject/IntelOwl/pull/3891) | Introduce `CTIConnector` base class with data model enrichment        |
| [#3907](https://github.com/intelowlproject/IntelOwl/pull/3907) | Refactor health_check to return `tuple[bool, str]` across all plugins |
| [#3933](https://github.com/intelowlproject/IntelOwl/pull/3933) | Update Slack connector tests                                          |
| [#3938](https://github.com/intelowlproject/IntelOwl/pull/3938) | Add MISP as optional container + merge to develop                     |

---

## Reflections

If there is one takeaway from this summer, it is that the most impactful work is often not the most glamorous. Refactoring a testing framework or standardizing a return type does not make for exciting demos, but it is the kind of infrastructure that determines whether the next contributor can add a new connector in a day or struggles for a week. The `CTIConnector` base class is a good example - the three connectors it standardized already worked, but they worked _separately_, each carrying its own copy of logic that should have been shared.

Working with Matteo has been genuinely excellent. His reviews consistently pushed for cleaner abstractions and better error handling. More importantly, he trusted me to make architectural decisions while being available when I needed direction - a balance that is harder to get right than it sounds.

---

## Acknowledgements

Thank you to my mentor **Matteo Lodi ([@mlodic](https://github.com/mlodic))** for his continuous support, thorough code reviews, and guidance throughout this project. Thank you to **The Honeynet Project** and to **Google Summer of Code** for making this possible.

I plan to continue contributing to IntelOwl.
