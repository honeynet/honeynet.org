---
title: "GSoC 2025 Project summary. Developing BuffaCLI for Command-Line Management and BuffaWatch for Real-Time Log Tracking"
authors: ["Onunwa Goodness"]
date: "2025-09-15T11:00:06+01:00"
tags: ["gsoc", "buffalogs"]
---

**Contributor**: Onunwa Goodness
**Mentors:** Lorena Goldoni, Federico Foschini

# My Google Summer of Code 2025 - The Honeynet Project (BuffaLogs)

September 1, 2025 officially marks the end of the Google Summer of Code (GSoC) 2025 coding period. Over the past four months, I've had the privilege of contributing as a developer to The BuffaLogs Project under The Honeynet Project. It's been four months of doing what I love most—building and shipping code.
<!--more-->

## The BuffaLogs Project

BuffaLogs is an open-source authentication protection tool built with Django that focuses on anomalous login detection and alerting. Its three core functionalities are Alerting, Ingestion, and Detection. On top of that, it ships with an interactive, web-based dashboard where users can view summaries of login activity and alerts.

## My GSoC Project: Extending BuffaLogs

For my GSoC proposal, I set out to extend BuffaLogs with two new tools that either enhanced its existing capabilities or introduced brand-new functionality. This led to the design and development of BuffaCLI and BuffaWatch, both of which are now part of the BuffaLogs ecosystem.

### BuffaCLI

BuffaCLI is a command-line interface tool that provides an alternative to the BuffaLogs web dashboard. Built in Python with Typer, Rich, and Requests, it allows users to interact with BuffaLogs directly from the terminal.

The key goals of BuffaCLI were to improve accessibility and flexibility, while also laying the groundwork for integration with future tools. But while providing this means, BuffaCLI also enables:

- Querying BuffaLogs data and piping results into other CLI tools with the `|` operator
- Secure remote connections to BuffaLogs when SSL is configured properly
- Serving as a central command tool for configuring future components of the ecosystem

### BuffaWatch

BuffaWatch is a real-time ingestion tool that improves upon BuffaLogs' ability to process log data. Instead of only handling static or stale logs, BuffaWatch continuously monitors specific log files and ingests new entries as they occur.

In addition, BuffaWatch provides middleware for popular web frameworks including FastAPI, Django, and Flask. This makes it possible for applications built on these frameworks to directly integrate with BuffaLogs in real time.

## Work Completed

Over the four months, I submitted more than 20 pull requests that spanned across:

- New API endpoints
- Codebase refactoring
- Feature implementation

These contributions not only added functionality but also improved the maintainability and scalability of the project.

## Current State

BuffaLogs now includes a working version of BuffaCLI, which was designed with a modular architecture to make it easily extensible. The current version of BuffaCLI supports:

- Log and alert querying
- Verbose output for deeper insights
- Flexible formatting of query results
- Query export to external files
- Integration with the Unix less pager
- Custom exception handling for better user experience

In addition to BuffaCLI, the BuffaLogs core has also been improved with:

- More robust APIs
- Friendlier endpoints and view functions
- Model serializers for consistent data representation
- A cleaner and more organized test code structure

## Challenges

One of the biggest challenges I faced was around code design and architecture. When building open-source projects from scratch, design decisions matter a lot. A poor structural choice can make the project hard to extend later or require significant effort to refactor down the road. Striking the balance between simplicity, flexibility, and long-term maintainability was an ongoing learning process.

## After GSoC

My contributions don't stop with the end of the GSoC coding period. I plan to continue supporting my organization and extending BuffaLogs. Some of the next steps I'd like to work on include:

- Adding an interactive shell for advanced and complex queries
- Implementing pagination in the current Alerts API
- Building a BuffaLog Monitor to extend BuffaWatch's real-time capabilities
- Continuing to refine and optimize the existing tools

The GSoC experience has been an important milestone, but for me, it's only the beginning of a longer journey with the project.

## Conclusion

Looking back, this GSoC journey has been incredibly rewarding. I joined the program hoping to improve my coding skills and contribute to meaningful open-source work, but I leave with much more: a deeper understanding of system design, better collaboration skills, and the confidence to tackle large-scale projects.

I'm grateful to my mentors Lorena and Federico and the Honeynet Project community for their support, guidance, and patience throughout this journey. This is not the end of my contributions to BuffaLogs—it's only the beginning. I look forward to continuing to build, refine, and grow alongside this amazing project. 🚀