---
title: "GSoC 2021 Project Summary: IntelOwl Improvements"
date: "2021-08-20"
coverImage: "intel_owl_positive_reduced.png"
tags: ["gsoc", "intelowl", "threatintel"]
---

Our [GSoC](https://summerofcode.withgoogle.com/) student [Sarthak Khattar](https://github.com/m0mosenpai) was working for three months under the supervision of Matteo Lodi on the OSINT platform [IntelOwl](https://github.com/intelowlproject/IntelOwl), specifically overhauling the analyzer configuration, API and test suite refactoring, and the integration of new analyzers.

Read on for an overview of their achievements and how they successfully contributed towards IntelOwl and some considerations for the future.

<!--more-->

**Student:** Sarthak Khattar ([GitHub](https://github.com/m0mosenpai))

**Mentors:** [Matteo Lodi](https://twitter.com/matte_lodi) and [Eshaan Bansal](https://twitter.com/mask0fmydisguis)

**Organization:** The Honeynet Project

**Project:** [IntelOwl](https://github.com/intelowlproject/IntelOwl)

### **Project Overview**

IntelOwl is an Open Source Intelligence, or OSINT solution to get threat intelligence data about a specific file, an IP or a domain from a single API at scale. It integrates a number of analyzers available online and is for everyone who needs a single point to query for info about a specific file or observable.

### **Sarthak’s GSoC Proposal**

_I proposed a new, more robust way of verifying analyzers’ configurations via strict rules through database models/serializers and a new configuration format, allowing support for real-time feedback of configuration status/errors in the frontend. This involved refactoring a major part of the codebase, improving and redesigning the test suite for the backend, creating a new test suite for the SDKs along with the necessary changes across all repositories for the new features added. A few new analyzers were also implemented._

The overall goal was to improve the resilience of the application and make it more configurable and accessible for the end-user_._

### **Pre-GSoC Commits**

List of pull requests merged before GSoC’s coding period:

- Analyzer integrations for **DNSTwist** ([#243](https://github.com/intelowlproject/IntelOwl/pull/243))**, tria.ge API** for file ([#253](https://github.com/intelowlproject/IntelOwl/pull/253)) and observable ([#283](https://github.com/intelowlproject/IntelOwl/pull/283)) scanning.
- **codecov.io** support in IntelOwl ([#305](https://github.com/intelowlproject/IntelOwl/pull/305)), **new PR Template** ([#338](https://github.com/intelowlproject/IntelOwl/pull/338)).
- **More robust testing** for REST API/ new test cases [(#317](https://github.com/intelowlproject/IntelOwl/pull/317)).
- Refactoring **action buttons** ([#83](https://github.com/intelowlproject/IntelOwl-ng/pull/83)) and **theme switching logic** ([#90](https://github.com/intelowlproject/IntelOwl-ng/pull/90)) to separate components in IntelOwl-ng.

### **GSoC Tasks and Deliverables**

I made over **100** commits and **30** pull requests spanning over 3 project repositories, namely: **IntelOwl (Django app)**, **IntelOwl-ng (Angular app)** and **pyintelowl (CLI client)**.

The following major tasks were completed and maintained over time:

#### 1\. **New Analyzer Config Format & Verification**

Previously, IntelOwl used a fairly simple JSON format for storing the configuration information for each and every analyzer. While this worked fine functionally, it lacked verification for it’s contents allowing typos and unsupported values going unnoticed till the analyzers were actually executed. This also meant that certain analyzers that required API Keys and other secrets were able to run, even if they were missing those secrets.

A new format was developed after a discussion with the mentors which allowed us to better express the information analyzers required to function as well as verify their integrity.

**Challenges faced:**

- I originally proposed adding tooltips to the Angular based frontend which would display the configuration status of each analyzer in the drop-down list. However, since misconfigured analyzers were disabled in the list, it prevented any click-event to register on the disabled analyzers. This meant that the tooltips would not show on these disabled elements. This limitation forced us to show the errors below each Analyzer’s name in the list as a workaround.

**Coding milestones**

The Connectors parts were handled by Shubham and our mentors helped out a lot with code review and clearing all the doubts throughout the process.

- Script to convert old format to new format.([#526](https://github.com/intelowlproject/IntelOwl/pull/526))
- Create separate sub-apps: **_analyzers\_manager_** and **_connectors\_manager_** and refactoring the codebase, new database models for generating job reports, serializers and verification functions for the new configuration format. ([#498](https://github.com/intelowlproject/IntelOwl/pull/498))([#518](https://github.com/intelowlproject/IntelOwl/pull/518))([#523](https://github.com/intelowlproject/IntelOwl/pull/523))
- Adding tooltips in the frontend, that display configuration status of the analyzer/connector and disable it, if misconfigured. [(#116](https://github.com/intelowlproject/IntelOwl-ng/pull/116))([#109](https://github.com/intelowlproject/IntelOwl-ng/pull/109))
- Updating the Python SDK in lieu of all the major refactoring ([#98](https://github.com/intelowlproject/pyintelowl/pull/98))([#115](https://github.com/intelowlproject/pyintelowl/pull/115))([#116](https://github.com/intelowlproject/pyintelowl/pull/116))

#### 2\. **Refactoring major API Endpoints**

IntelOwl provided an **_/api/send\_analysis\_request_** endpoint for scanning files and observables. This was slightly convoluted and lacked verification for certain request data parameters. With the recent major refactoring, it was the perfect opportunity to split this endpoint and use DRF’s serializers to enforce verification on the request parameters.

As a result, 2 endpoints were created in place of a single one: **_/api/analyze\_file_** and **_/api/analyze\_observable._** New serializer classes were made, each for file and observable analysis containing verification functions for request data.

**Challenges faced:**

- IntelOwl was my first true exposure to Django. As a result, implementing the required Serializers for the above endpoints proved to be somewhat confusing and timetaking. However, my mentors were extremely helpful in clearing all the doubts and pushing me in the right direction. I was able to successfully implement the task and develop a greater understanding of the working of the framework.

**Coding milestones:**

- Creating the new endpoints and refactoring the backend. ([#551](https://github.com/intelowlproject/IntelOwl/pull/551))
- Refactoring frontend & SDK in lieu of the new scanning endpoints. ([#121](https://github.com/intelowlproject/IntelOwl-ng/pull/121))([#98](https://github.com/intelowlproject/pyintelowl/pull/98))
- Adding support for downloading job sample from the SDK (previously missing feature) ([#100](https://github.com/intelowlproject/pyintelowl/pull/100))

#### 3\. **Rewriting IntelOwl’s Test Suite**

Eshaan, one of my mentors, suggested improving the existing testing suite by making it almost completely dynamic. Earlier, everytime a developer would add a new analyzer, they would have to add a new test for it as well. However, dynamic testing would allow iterating through existing as well as new analyzers, removing the need to explicitly define new tests. Moreover, the tests were now to be run asynchronously as celery tasks, decreasing the overall time of execution significantly. This would also address a number of issues in the previous testing suite ([#229](https://github.com/intelowlproject/IntelOwl/issues/229)) like missing coverage for certain generic functions as well as tests for groups/permissions.

For this to be implemented, the entire testing suite had to be written from scratch while keeping in mind the recent refactoring changes, new config format as well as the requirements of the new test suite.

**Challenges faced:**

As [#558](https://github.com/intelowlproject/IntelOwl/issues/558) details, several issues occurred after the testing changes were implemented. These included:

- Codecov.io started reporting incomplete test coverage due to the tests running a separate **_celery_** container, whereas the analyzers ran in the **_uwsgi_** container.
- Celery also refused to run in a separate **_test_** database. Instead, we were forced to temporarily run the tests in the main database which led to a lot of database related errors.
- Since the tests ran dynamically now, we needed a way to make sure each and every analyzer was executed.

I’m grateful to our mentor, Eshaan, who spent a great amount of time and effort to solve most of the above-mentioned issues which significantly sped up the process.

**Coding milestones:**

- Fixing tests for file and observable analyzers, updating GitHub Actions([#532](https://github.com/intelowlproject/IntelOwl/pull/532))
- Refactoring and addressing the issues.([#606](https://github.com/intelowlproject/IntelOwl/pull/606))([#599](https://github.com/intelowlproject/IntelOwl/pull/599))([#607](https://github.com/intelowlproject/IntelOwl/pull/607))
- Fixing the 2 pending points of [#229](https://github.com/intelowlproject/IntelOwl/issues/229), which I had been working on since pre-GSoC period.

#### 4\. **Implementing Test Suite for pyintelowl**

IntelOwl’s Python SDK, [pyintelowl](https://github.com/intelowlproject/pyintelowl), was missing a robust testing suite - Class based test cases, support for running tests on GitHub CI, lack of coverage reports etc. ([#65](https://github.com/intelowlproject/pyintelowl/issues/65))([#106](https://github.com/intelowlproject/pyintelowl/issues/106))([#59](https://github.com/intelowlproject/pyintelowl/issues/59)). Moreover, previously written CLI tests were superficial and lacked coverage for major functionality of the SDK.

As a result, these tests were replaced by a new and more thorough testing suite. More than **50 new tests** were implemented with a coverage of almost **_80%_** (connector related tests were added by Shubham). **_Tox_** support was added to run the tests on GitHub with **_codecov.io_** for reporting the coverage changes.

**Coding milestones:**

- Adding a new PR Template for contributors ([#99](https://github.com/intelowlproject/pyintelowl/pull/99)),
- Adding class based tests for jobs/tags & generic functions ([#102](https://github.com/intelowlproject/pyintelowl/pull/102)) ([#117](https://github.com/intelowlproject/pyintelowl/pull/117))
- Adding Tox and Codecov support ([#107](https://github.com/intelowlproject/pyintelowl/pull/107))
- Updating documentation in lieu of the new testing suite ([#110](https://github.com/intelowlproject/pyintelowl/pull/110))

#### 5\. **Integrating new Analyzers**

Some important analyzers like **_VirusTotal_** needed to be updated and others like **_ClamAV_** were planned to be integrated for a long time. Thus, this opportunity was taken to implement 2 new endpoints into VirusTotal as well as integrate ClamAV into IntelOwl. 

**Challenges faced:**

- The free API VirusTotal provides is very limited with their premium services being relatively expensive. This meant that we had to be extra careful in making sure our analyzer implementation did not waste any extra quota than what was necessary. The previous implementation had been done with that in mind and made it tricky to add the new endpoints. Eshaan was really helpful in refactoring the previous code to make way for the new changes.
- ClamAV Analyzer is a complex application that requires a separate daemon running in the background with specific user and permissions in order to perform scans on files. Even though it provides a one-time scan command that doesn’t require running the daemon in the background, the constant loading of Virus databases means it’s not a scalable solution for IntelOwl.

**Coding milestones:**

- Integrated **_behavioral analysis_** and **_sigma analysis_** reports in VirusTotal. ([#617](https://github.com/intelowlproject/IntelOwl/pull/617))
- Integrated ClamAV analyzer. ([#633](https://github.com/intelowlproject/IntelOwl/pull/633))

### **Next Steps**

I’m very glad to have worked on this amazing project and would continue to do so in the future. It has been a major source of learning for me. Some of the things I hope to tackle in the future are:

- Automated and customized workflows for analyzers and connectors ([#628](https://github.com/intelowlproject/IntelOwl/issues/628))
- Social Authentication support ([#121](https://github.com/intelowlproject/IntelOwl/issues/121))
- Gointelowl - IntelOwl's client library/SDK in go-lang ([#3](https://github.com/intelowlproject/go-intelowl/issues/3))

I would like to thank **The Honeynet Project** and **Google Summer of Code** for providing me with this opportunity. Special thanks to my mentors **Eshaan Bansal** and **Matteo Lodi** for being kind and helpful to me throughout this amazing journey.
