---
title: "GSoC 2021 Project Summary: IntelOwl Connectors Manager and Integrations"
date: "2021-08-20"
categories: 
  - "gsoc"
tags: 
  - "gsoc-d20"
  - "intelowl"
  - "threatintel"
coverImage: "intel_owl_positive_reduced.png"
---

Student: Shubham Pandey ([@sp35](https://github.com/sp35/))

Mentor: [Eshaan Bansal](https://twitter.com/mask0fmydisguis) and [Matteo Lodi](https://twitter.com/matte_lodi)

Organization: The Honeynet Project

Project: [Intel Owl](https://github.com/intelowlproject/IntelOwl)

Tag: Information Security

### **Project Overview**

Intel Owl is an Open Source Intelligence or OSINT solution to get threat intelligence data about a specific file, an IP, or a domain from a single API at scale. It integrates a number of analyzers available online and is for everyone who needs a single point to query for info about a specific file or observable.

### **Shubham's GSoC Proposal**

As cited in my original proposal’s overview:

_I propose a new component of the project - a connectors manager which would help IntelOwl connect with any external tool for enhancing the data it generates or performing automated analysis on the data it generates, or facilitate the integration with other threat intelligence platforms. Along with this, I would also add the integrations for MISP and OpenCTI platforms which the community has been eagerly waiting for._

So the main objective was to develop a connectors manager which would help IntelOwl connect with any SOAR/SIEM platform, particularly for threat-intel sharing purposes.

### **Pre GSoC Commits**

List of pull requests merged before GSoC’s coding period:

- Analyzer integration for Google’s Rendertron to detect phishing campaigns using screenshots ([#370](https://github.com/intelowlproject/IntelOwl/pull/370)), IBM’s X-Force Exchange’s API ([#362](https://github.com/intelowlproject/IntelOwl/pull/362)), screenshotapi.net ([#372](https://github.com/intelowlproject/IntelOwl/pull/372)), ThreatFox’s API ([#414](https://github.com/intelowlproject/IntelOwl/pull/414)), Malpedia’s API ([#425](https://github.com/intelowlproject/IntelOwl/pull/425)) 
- REST API to kill any ongoing analysis ([#337](https://github.com/intelowlproject/IntelOwl/pull/337), [#339](https://github.com/intelowlproject/IntelOwl/pull/339))
- CLI commands and library methods for the python client - kill ongoing analysis ([#68](https://github.com/intelowlproject/pyintelowl/pull/68)) and delete a job ([#71](https://github.com/intelowlproject/pyintelowl/pull/71))
- Reusable UI components for image(base64) visualization ([#88](https://github.com/intelowlproject/IntelOwl-ng/pull/88)), social links ([#91](https://github.com/intelowlproject/IntelOwl-ng/pull/91))

### **GSoC Tasks and Deliverables**

#### 1\. Connectors Manager

A common pattern observed in analyzers’ python modules was the validation of secrets configured via a JSON configuration file. Also, a user while requesting an analysis, couldn’t know if an analyzer was configured properly or not. This was something that would affect the new component - connectors as well.

I and Sarthak (who worked on the analyzers part of this issue) used DRF’s serializers to validate the configuration file initially and cached it for the rest of the application’s lifecycle while invalidating the cache if the file was changed. We used the design pattern \`Abstract Factory\` and created abstract classes to extend this for both analyzers and connectors ([#499](https://github.com/intelowlproject/IntelOwl/pull/499), [#518](https://github.com/intelowlproject/IntelOwl/pull/518)).

#### 2\. Plugin, Connector, controllers, data classes

- Initially, I refactored the existing workflow for running analyzers and tried extending it to run connectors as well. Knowing that it was a temporary solution, after discussion with Eshaan and Sarthak, we decided to create an abstract class \`Plugin\` providing a common base which the subclasses \`BaseAnalyzer\` and  \`Connector\` would extend upon. This required a lot of refactoring and was a conflicting task which blocked the addition of new features as well. Even though Eshaan was our mentor, he gave a significant contribution through code as well, so that we could manage to wrap this up quickly ([#524](https://github.com/intelowlproject/IntelOwl/pull/524)).
- Used python data classes for handling config dictionaries and enums wherever possible so as to avoid incorrect property references ([#530](https://github.com/intelowlproject/IntelOwl/pull/530), [#544](https://github.com/intelowlproject/IntelOwl/pull/544)).

#### 3\. MISP, OpenCTI, YETI connectors

Finally, it was time to work on some integrations using connectors. Integrations were added for threat-intel sharing platforms - MISP ([#528](https://github.com/intelowlproject/IntelOwl/pull/528)), OpenCTI ([#602](https://github.com/intelowlproject/IntelOwl/pull/602)), YETI ([#631](https://github.com/intelowlproject/IntelOwl/pull/631)). It also made sense to leverage the opportunity to add analyzers that would search for observables/threat-intel reports available on these platforms - OpenCTI ([#603](https://github.com/intelowlproject/IntelOwl/pull/603)), YETI ([#632](https://github.com/intelowlproject/IntelOwl/pull/632)).

#### 4\. Plugins Actions - kill, retry, health-check

I proposed that connectors would have a \`kill\` feature to stop any ongoing/pending connector run and \`retry\` to restart any failed/killed connector run. Another action health-check was considered to check if the associated instances (docker containers and external platforms) were up or not, anytime, instead of finding out later in a failed analysis. Once again abstract classes were used to extend these to both analyzers and connectors.

1. The \`kill\` was made on top of \`celery.app.control\`, the celery tasks were revoked by their corresponding task ids, and the connector report was marked as killed ([#572](https://github.com/intelowlproject/IntelOwl/pull/572)). 
2. Since celery tasks cannot be restarted, retry was implemented by constructing the same arguments and starting a new celery task ([#582](https://github.com/intelowlproject/IntelOwl/pull/582)). 
3. The health check feature was added to docker-based analyzers and connectors ([#627](https://github.com/intelowlproject/IntelOwl/pull/627)).

#### 5\. IntelOwl-ng (UI changes)

All the corresponding user interface changes were committed to the repo [IntelOwl-ng (Angular app)](https://github.com/intelowlproject/IntelOwl-ng).

1. Added table views and services for fetching connector reports, connectors data along with configuration status ([#109](https://github.com/intelowlproject/IntelOwl-ng/pull/109)).
2. Added components and services for kill/retry ([#125](https://github.com/intelowlproject/IntelOwl-ng/pull/125)), and health-check ([#135](https://github.com/intelowlproject/IntelOwl-ng/pull/135)) actions.
3. Other improvements and refactors ([#129](https://github.com/intelowlproject/IntelOwl-ng/pull/129), [#137](https://github.com/intelowlproject/IntelOwl-ng/pull/137), [#119](https://github.com/intelowlproject/IntelOwl-ng/pull/119))

#### 6\. Pyintelowl client

All the corresponding changes to the python client were committed to the repo [Pyintelowl (python client)](https://github.com/intelowlproject/pyintelowl).

Added CLI commands and library methods for fetching connectors’ configuration ([#112](https://github.com/intelowlproject/pyintelowl/pull/112)), plugin actions kill/retry ([#113](https://github.com/intelowlproject/pyintelowl/pull/113)), and health-check ([#114](https://github.com/intelowlproject/pyintelowl/pull/114)).

### **Next Steps**

I’m very glad to have worked on this amazing project and would continue to do so even after GSoC. In the future, we shall be working on these features:

- Automated and customized workflows for analyzers and connectors ([#628](https://github.com/intelowlproject/IntelOwl/issues/628)).
- TLP support for analyzers and connectors ([#638](https://github.com/intelowlproject/IntelOwl/issues/638)).
- Gointelowl - IntelOwl's client library/SDK in go-lang ([#3](https://github.com/intelowlproject/go-intelowl/issues/3)).

I would like to thank The Honeynet Project and Google Summer of Code for providing me with this opportunity and especially my mentors Eshaan Bansal and Matteo Lodi for being kind and helpful mentors to me along this amazing journey.
