---
title: "GreedyBear: Introducing the Event Collector API"
authors: ["Dorna Raj Gyawali"]
date: "2026-08-11T17:00:00+02:00"
tags: ["gsoc", "GreedyBear", "threatintel"]
---

Our [GSoC](https://summerofcode.withgoogle.com/) student **[Dorna Raj Gyawali](https://github.com/drona-gyawali)** spent three months working under the supervision of **[Tim Leonhard](https://github.com/regulartim)** on the **[GreedyBear](https://github.com/GreedyBear-Project/GreedyBear)** project, focusing on introducing an **Event Collector API** to make it easier for external honeypots and sensors to submit IOC events to GreedyBear.

Read on for an overview of their achievements and how they successfully contributed towards GreedyBear and some considerations for the future.

**Student:** Dorna Raj Gyawali ([drona-gyawali](https://github.com/drona-gyawali))

**Mentors:** Tim Leonhard

**Organization:** The Honeynet Project

**Project:** [GreedyBear](https://github.com/GreedyBear-Project/GreedyBear)

## **Dorna’s GSoC Proposal**

The goal of my GSoC project was to introduce an [**Event Collector API**](https://summerofcode.withgoogle.com/programs/2026/projects/4SAdqqai) for GreedyBear.

GreedyBear currently collects and processes threat intelligence from T-Pot through Elasticsearch. However, integrating data from other external honeypots and sensors required a dedicated way to push events into GreedyBear. The goal of this project was therefore to introduce a unified Event Collector API through which external sensors could submit events directly to GreedyBear.

## **GSoC Tasks and Deliverables**

### 1. Project Design and API Architecture

The first part of the project focused heavily on designing the API before implementation.

We spent significant time discussing the architecture, data flow, API fields, response formats, authentication, and how the new system should integrate with GreedyBear's existing event-processing pipeline.

The project design and discussion can be found in [Discussion #1348](https://github.com/GreedyBearProject/GreedyBear/discussions/1348).

This was also one of the most valuable parts of my GSoC experience. Working closely with my mentor during the design phase taught me that spending time on API design and discussing small details early can prevent much larger problems during implementation.

### 2. Core Data Models and Sensor API

Once the architecture was finalized, I implemented the core data models required by the Event Collector system and integrated them with Django's admin interface.

I then implemented the Sensor Creation API along with comprehensive test cases covering its expected behavior and validation rules.

These components established the foundation for external sensors to identify themselves and interact with GreedyBear.

-   [Core Data Models & Admin Integration - #1382](https://github.com/GreedyBear-Project/GreedyBear/pull/1382)
-   [Sensor Creation API & Tests - #1369](https://github.com/GreedyBear-Project/GreedyBear/pull/1369)

### 3. Asynchronous IOC Event Ingestion Pipeline

The main part of the project was implementing the event ingestion pipeline.

External sensors can submit IOC events through the Event Collector API. Incoming events are validated and stored before being processed asynchronously, allowing the API to return quickly while more expensive IOC processing happens in the background.

The pipeline also supports **batch event ingestion**, allowing sensors to submit multiple events efficiently instead of making a separate request for every event.

The complete implementation can be found in:
-  [Event Ingestion Pipeline  -  #1397](https://github.com/GreedyBear-Project/GreedyBear/pull/1397)

### 4. Security and Reliability Improvements

While implementing the asynchronous pipeline, I also worked on several related improvements.

A security fix was implemented for **distributed container task signing**, ensuring that asynchronous tasks could be verified correctly in the distributed environment.

I also added an automated reset mechanism for the `invalid_event_count` metric, making the metric more useful for monitoring the ingestion system over time.

-   [Distributed Container Task Signing — #1409](https://github.com/GreedyBear-Project/GreedyBear/pull/1409)
-   [Automated Metrics Reset — #1423](https://github.com/GreedyBear-Project/GreedyBear/pull/1423)

### 5. Data Lifecycle and Raw Event Retention

The Event Collector temporarily stores incoming events before processing them. Keeping these raw events indefinitely could result in unnecessary database growth, especially for sensors producing large volumes of events.

I implemented **retention-based cleanup for raw events**, allowing old records to be removed automatically according to the configured retention policy.

- [Retention Policy - #1436](https://github.com/GreedyBear-Project/GreedyBear/pull/1436).

### 6. IOC Enrichment from T-Pot Logs

Towards the end of the project, I also improved IOC enrichment from T-Pot logs.

The processing pipeline was extended to populate **protocol** and **CVE** information when available, providing additional context for the generated IOCs.

This change was implemented in 

- [IOC Enrichment - #1484](https://github.com/GreedyBear-Project/GreedyBear/pull/1484).

### 7. Documentation

The Event Collector API documentation is maintained through the project's GitHub Wiki. The documentation has already been prepared and referenced in the dedicated feature PRs.

The remaining step is to release the new version of GreedyBear, after which the documentation will be added to the Wiki as part of the release process.

For more information, please refer to the [documentation tracking issue #1487](https://github.com/GreedyBear-Project/GreedyBear/issues/1487).

## **Problems Encountered**


One of the main challenges was deciding which fields the Event Collector API should expose and ensuring that they mapped naturally to the existing database fields used by T-Pot. Since events from the API and T-Pot are stored in the same database, keeping these fields consistent was important for maintaining a unified data model.

Through discussions and communication with my mentor, I was able to resolve these design challenges and arrive at an API structure that fit naturally into the existing GreedyBear architecture.

## **Next Steps and Final Thoughts**

GSoC 2026 has been a great learning opportunity for me, both professionally and personally. Throughout the project, I gained valuable experience not only in technical areas such as API design, asynchronous processing, and backend development, but also in communication, collaboration, and working within an open-source project.

I am especially thankful to my mentor, **Tim Leonhard**, who was always available for important discussions and decisions throughout the project. He not only helped me when I was stuck but also encouraged me to research problems independently and come up with solutions before discussing them. I cannot imagine completing this project without his guidance and support.

There is still a lot that can be built on top of the Event Collector API. Future work could include improving observability around event ingestion, expanding event enrichment, supporting additional sensor types, and making the integration process easier for other contributors.

I am very thankful for the opportunity to be part of the GreedyBear project during GSoC, and I will definitely continue contributing to the project.