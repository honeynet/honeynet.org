---
title: "GSoC 2020 Project Summary: A new front-end and analyzers for IntelOwl"
date: "2020-08-26"
coverImage: "intel_owl.jpeg"
tags: ["gsoc", "intelowl", "threatintel"]
---

Our [GSoC](https://summerofcode.withgoogle.com/) student [Eshaan Bansal](https://github.com/Eshaan7) was working for three months under the supervision of Matteo Lodi on the OSINT platform [IntelOwl](https://github.com/intelowlproject/IntelOwl), specifically introducing a brand new front-end written in Angular and analyzers to automate integrations.

Read on for an overview of their achievements and how they successfully contributed towards IntelOwl and some considerations for the future.

<!--more-->

**Student**: Eshaan Bansal ([@Eshaan7](https://github.com/Eshaan7))  
**Mentor:** [Matteo Lodi](https://twitter.com/matte_lodi) and [Pietro Delsante](https://twitter.com/PietroDelsante)**  
Organization**: The Honeynet Project  
**Project**: [Intel Owl](https://github.com/intelowlproject/IntelOwl)  
**Tag**: Information Security

### Project Overview

Intel Owl is an Open Source Intelligence, or OSINT solution to get threat intelligence data about a specific file, an IP or a domain from a single API at scale. It integrates a number of analyzers available online and is for everyone who needs a single point to query for info about a specific file or observable.

#### Eshaan’s GSoC Proposal

As cited in my [original proposal’s overview](https://summerofcode.withgoogle.com/projects/#5634812913647616),

> I propose a Frontend Client Application (written in Angular 8) that provides a dashboard with visualizations of large sets of data, analyzer’s management, easy way to request new scans and a Tabular/Graph view of the analyzer’s report. A prototype of this web app can be found here: [https://intelowlclient.firebaseapp.com/](https://intelowlclient.firebaseapp.com/).   
> I will also work on adding new analyzers and observable types.

So the main objectives were a revamped web interface and, adding support for more threat Intel APIs and malware analyzers.

### Pre GSoC Commits

List of merged pull requests and tasks completed before GSoC’s coding period:

- Analyzer integrations for HoneyDB.io’s twitter threat API ([PR #20](https://github.com/certego/IntelOwl/pull/20)) and IP Lookup [(#51](https://github.com/certego/IntelOwl/pull/51)), Hunter.io's API ([#21](https://github.com/intelowlproject/IntelOwl/pull/21)), Malware Bazaar’s API ([#45](https://github.com/intelowlproject/IntelOwl/pull/45)), ONYPHE's API ([#46](https://github.com/certego/IntelOwl/pull/46)), GreyNoise API v2 ([#52](https://github.com/certego/IntelOwl/pull/52)) and URLhaus API ([#61](https://github.com/certego/IntelOwl/pull/61)).
- Added Tag model and custom fields in admin view. ([#76](https://github.com/intelowlproject/IntelOwl/pull/76)).
- Various Bug Fixes ([#17](https://github.com/intelowlproject/IntelOwl/pull/17), [#18](https://github.com/intelowlproject/IntelOwl/pull/18), [#41](https://github.com/intelowlproject/IntelOwl/pull/41)).
- A prototype for a new web interface [hosted on Firebase](https://intelowlclient.firebaseapp.com/). (Issue [#13](https://github.com/intelowlproject/IntelOwl/issues/13))

### GSoC Tasks and Deliverables

I made over 100 commits and 60 pull requests spanning over all 3 project repositories, namely: IntelOwl (Django app), IntelOwl-ng (Angular app) and PyIntelOwl (CLI client).

The following major tasks were completed and maintained over time.

#### (I) New Web Interface

Previously, Intel Owl had a very limited web interface written using Django’s template engine. Now we have a full-fledged front-end application (written in Angular 10 and Typescript) that interacts with the main IntelOwl’s Django API and provides authentication, visualizations of analysis data, analyzer’s management and easy-to-use forms for requesting new scans. For this purpose, a separate repository with the name [IntelOwl-ng](https://github.com/intelowlproject/IntelOwl-ng) was created and has been solely maintained by me. This new web interface was made available to users as soon as June 10th.

**Code Milestones:**

1. Dashboard Visualizations, Analyzer’s Management, Job Result Page. ([#6](https://github.com/intelowlproject/IntelOwl-ng/pull/6), [#10](https://github.com/intelowlproject/IntelOwl-ng/pull/10), [#13](https://github.com/intelowlproject/IntelOwl-ng/pull/13) respectively).
2. Switched the API to use JWT tokens for authentication for increased security so also had to make changes in both the clients. (IntelOwl-ng [#30](https://github.com/intelowlproject/IntelOwl-ng/pull/30), IntelOwl [#94](https://github.com/intelowlproject/IntelOwl/pull/94), PyIntelOwl [#8](https://github.com/intelowlproject/pyintelowl/pull/8))
3. IntelOwl-ng was marked ready for production and made the default web interface for Intel Owl. (IntelOwl [#93](https://github.com/intelowlproject/IntelOwl/pull/93)).

#### (II) Integrating More Analyzers

Intel Owl is not only composed of OSINT services available online (such as Shodan, VirusTotal, etc) but also binaries and tools (Stringsifter, Cuckoo, Thug) that are to be custom built, installed and requires setup on one’s system. There are a great deal of amazing security tools but not all are available via a public API on the web and that was a big challenge for us. To integrate such analyzers into IntelOwl, we had to be creative.

**Challenges Faced:** After much discussion, Matteo and I chose solve this via a micro-services architectural fashion. We decided to create separate docker images for heavy tools (such as Thug, PEframe, etc.) which could then be leveraged from the main IntelOwl’s API. The main challenge here was building configurable _micro_ images as docker services with 2 goals: the end-user can choose to enable or disable these and they can easily communicate to Intel Owl. The big question here was:  
_How do you execute a shell command in another docker service without doing docker in docker ?_

**Working and Solution:** For this purpose, I wrote a python module called [Flask-Shell2HTTP](https://github.com/Eshaan7/Flask-Shell2HTTP) that basically allows execution of shell commands asynchronously via a RESTful API interface (kind of like webhooks) so now we could just make HTTP calls to these micro services to use such tools. There were a lot of iterations of the same solution having to rewrite the functionality to keep making it better and better with each subsequent release, but today it works super well and is one of the proudest moments of my career.

**Code Milestones:**

1. PEframe was the first tool to be created as a micro service. ([#66](https://github.com/intelowlproject/IntelOwl/pull/66), [#103](https://github.com/intelowlproject/IntelOwl/pull/103)). 
2. Honeynet’s Project Thug ([#109](https://github.com/intelowlproject/IntelOwl/pull/109)), Box-JS ([#128](https://github.com/intelowlproject/IntelOwl/pull/128)), FireEye’s malware analysis tool, Capa. ([#127](https://github.com/intelowlproject/IntelOwl/pull/127)), APKiD which is an APK analyzer ([#132](https://github.com/intelowlproject/IntelOwl/pull/132)) were also added in the same fashion.
3. Pulsedive’s API for IoCs ([#154](https://github.com/intelowlproject/IntelOwl/pull/154)), Quark Engine for APKs ([#156](https://github.com/intelowlproject/IntelOwl/pull/156)) were added as inbuilt analyzers.

#### (IV) **Low Level API/ Base class for analyzers**

Code modularity is of utmost importance when it comes to building a software such as Intel Owl that has a lot of independent components working together.

**Challenges Faced:** As Intel Owl started growing in number of analyzers (modules), a pattern of repetitive code was observed. Each module was required to have the same interface and code was duplicated among them for common operations.

**Working and Solution:** Realizing that this would create problem with maintainability as the project matures over time, I decided to make use of the software design pattern commonly known as [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory) creational design pattern. Following this, base abstract classes were created: `ObservableAnalyzer` for observable and `FileAnalyzer` for file analyzers respectively. These base classes, with the help of [inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)), could be extended to create specific analyzer modules. This way each module only contains definitions for core functions (executing the analyzer, fetching result) and the common functionality (setting configuration, saving result to database) was dealt with in the base class. Also making it easier than ever for beginners to contribute a new analyzer.

**Code Milestones:**

1. All the existing (and new) modules were migrated to use this new pattern reducing about 1000 lines of duplicate code and code smells. ([#107](https://github.com/intelowlproject/IntelOwl/pull/107))

#### (V) **User Groups & Permissions System**

Someone [requested a feature via GitHub issue](https://github.com/intelowlproject/IntelOwl/issues/123) allowing to mark certain Jobs as "private" so they become inaccessible to other users.

**Working and Solution:** Added the ability to leverage _Django's permissions system_ to organize users into groups, allow/restrict certain permissions to different groups, mark particular jobs as private so they are not visible to other users. For example, whether or not a group of users are permitted to create a new scan or view a particular analysis.

**Code Milestones:**

1. Move the existing API to make use of Django's _Object Level Permissions ([#135](https://github.com/intelowlproject/IntelOwl/pull/135))_

#### (VI) **Elastic Search Support**

Elasticsearch is a search and analytics engine which is widely used by blue teams for threat intelligence operations.  
We wanted to allow IntelOwl users to analyze the results in a very custom and open manner so support for Elasticsearch was added making use of the [`django-elasticsearch-dsl`](https://github.com/django-es/django-elasticsearch-dsl) package.

**Code Milestones:**

1. Auto-sync for `Job` model in Django with a `Job` index in elasticsearch. ([#147](https://github.com/intelowlproject/IntelOwl/pull/147))

### Project Visibility & Growth

Back in march when I first started contributing, IntelOwl's GitHub repository had 70 stars and 100 pulls on the docker image. **Today it is over 1000** **stars** and **50,000** **pulls** on the docker image and we have the awesome infosec community to thank for that. Some milestones along the way:

1. [IntelOwl Release v1.0.0](https://www.honeynet.org/2020/07/05/intel-owl-release-v1-0-0/) published on honeynet.org,
2. Matteo and I were interviewed by a journalist over at The Daily Swig, a cybersecurity news site, and featured in "[Intel Owl – OSINT tool automates the intel-gathering process using a single API](https://portswigger.net/daily-swig/amp/intel-owl-osint-tool-automates-the-intel-gathering-process-using-a-single-api)" published on portswigger.net

### Next Steps

I am very glad to have been promoted to the maintainer status for the IntelOwl project repositories and would continue contributing to this amazing project even after GSoC.

There are certain issues and feature requests that I feel are quite important and requires attention:

1. [Integration/connectors for other threat intel projects](https://github.com/intelowlproject/IntelOwl/issues/144)
2. [Dynamic configuration at time of requesting scan](https://github.com/intelowlproject/IntelOwl/issues/111)
3. [OpenCTI connector](https://github.com/intelowlproject/IntelOwl/issues/11)
4. [MISP connector](https://github.com/intelowlproject/IntelOwl/issues/12)

I would very much like to thank The Honeynet Project and Google Summer of Code for providing me with this opportunity and especially [Matteo Lodi](https://twitter.com/matte_lodi) for being a kind and helpful mentor to me along this amazing journey.
