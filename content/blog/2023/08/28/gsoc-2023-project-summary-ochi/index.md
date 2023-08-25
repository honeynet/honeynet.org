---
title: "GSoC 2023 Project summary: Ochi"
authors: ["Lucas Rist"]
date: "2023-08-24T11:00:06+01:00"
# coverImage: "intel_owl_positive_reduced.png"
tags: ["gsoc", "ochi"]
---


Our [GSoC](https://summerofcode.withgoogle.com/) student [Kumiszhan Dybyspayeva](https://github.com/dkumiszhan) was working for three months under the supervision of Lukas Rist on [Ochi](https://github.com/honeynet/ochi/), specifically on introducing new features such as event filtering using a DSL, persisting filters and sharing an event. 

Read on for an overview of their achievements and how they successfully contributed towards Ochi and some considerations for the future.

<!--more-->

**Student**: Kumiszhan Dybyspayeva ([dkumiszhan](https://github.com/dkumiszhan))

**Mentor**: Lukas Rist

**Organization**: The Honeynet Project

**Project**: [Ochi](https://github.com/honeynet/ochi/)

### **Kumiszhan’s GSoC Proposal:**

As stated in my original proposal’s overview:

> Current version of the project is missing important features which will make the tool much more usable for security researchers. The features that I am planning to implement:
> - Persistence of events into DB
> - Persisting user created queries
> - Custom query language for easier filtering of events
> - Generating a dashboard with statistics
> - Permanent links to persisted events


### **Pre GSoC Commits:**

- [#41](https://github.com/glaslos/ochi/pull/41) - fixed typos
- [#42](https://github.com/glaslos/ochi/pull/42) - added documentation about connecting Glutton backend with Ochi
)
- [#150](https://github.com/mushorg/glutton/pull/150) - fixed Glutton configuration parser
- [#151](https://github.com/mushorg/glutton/pull/151) - fixed SSHProxy config

**Project Overview and Project Objectives**

Ochi is an UI for Honeypot events generated from [Glutton](https://github.com/mushorg/glutton).
The events are generated in real-time, and the majority of them are internet background noise.
Main goal of this project is to identify the events that are truly new
and contain valuable information for security researchers. This can be
accomplished by implementing features such as event filtering, query
persistence, permanent links for sharing and persising an event,
client-side and server-side statistics. 

## **GSoC Tasks and Deliverables**

Although I didn't implement all of the features stated in my GSoC proposal,
what I have accomplished gives a good start to Ochi's usability development.
I plan on contributing to the project after the end of GSoC term in some form.
I would like to work on the issues I created in the project repository on Github along the way and on features for improving user experience with Ochi. 

Below is the list of the goals accomplished in the scope of GSoC. 

### 1. Custom query language for easier filtering of events

The original logic was able to filter events either by source or destination
port only. In this task, I expanded the fitlering functionality by using
Wireshark query-like syntax and [chevrotain](https://chevrotain.io/docs/) for
parsing and interpreting the custom query syntax. With my changes the following
queries are supported:

- `ip.src == 192.168.1.1`
- `tcp.port ne 80 and ip.src == 192.168.1.1`
- `tcp.port eq 80 or tcp.port eq 8080`
- `payload contains "string"`

This task was implemented in [#46](https://github.com/honeynet/ochi/pull/46).

### 2. Persisting user created queries

To persist user created queries I used the same approach as in
[ochi/repos directory](https://github.com/glaslos/ochi/tree/main/repos)
by creating a `Query` repo. Currently, a user can save a query and view their
saved list of queries on `myqueries` page. A user can also edit and delete
using a modal window and apply the selected query to real-time events on
`myqueries` page. I used [routify](https://www.routify.dev/) for implementing
client side navigation. This task was addressed in [#83](https://github.com/honeynet/ochi/pull/83).

### 3. Permanent links to persisted events

By default events are streamed in realtime to frontend clients using
websocket connections and not persisted. When a user finds
an "interesting" event they should be able to persist and share those events.

This task is still pending. The implementation is split into 2 tasks:
* [#84](https://github.com/honeynet/ochi/pull/84) - implementation of backend storage and HTTP handlers
* TODO: add link once PR ready - implementation of frontend UI for sharing events and displaying them when visiting shared links.

### 4. Refactoring work

Even though this task wasn't a part of GSoC proposal, it was a useful step that
made a project a cleaner and more organised. I think it made the project more
maintainable by making it easier to understand for new contributors in future.
In the previous version of the project, components were part of a single
`App.svelte` file. As I started adding more logic, `App.svelte`  grew even
bigger. It made sense to split the huge file into smaller independent components.
I created two pull requests to address this: 
- moving config modal code into modal component in [#45](https://github.com/honeynet/ochi/pull/45)
- refactoring components from App.svelte in [#54](https://github.com/honeynet/ochi/pull/54)   

### Pull Requests

The list of all my pull requests for Ochi and Glutton projects can be found
[here](https://github.com/search?q=author%3Adkumiszhan+repo%3Ahoneynet%2Fochi+repo%3Amushorg%2Fglutton&type=pullrequests&p=1).

### Challenges and Important Takeaway:

Main challenge to me at the start of GSoC was learning big number of new
frameworks and libraries in a short period of time. It is, however, something
that I am very glad about right now and it helped me build my confidence in
what I was doing. Working on event filtering using DSL parser was the task
that was the most challenging and exciting. It made me understand how DSL
parsers work fundamentally and their limitations.
Refactoring work on splitting the biggest Svelte component into smaller pieces
was unexpectedly the most time consuming. It was challenging to decide on which
component should contain specific pieces of logic and keeping them independent.

What I learned from this project was that creating smaller pull requests
was more productive to me as a starting software developer. It allowed me not to get stuck and progress faster. I could get quicker feedback from
my mentor. When I was working on bigger pull requests, often I got stuck
and progressed slower.

I feel very grateful to my mentor for his support and responsiveness in my
journey with GSoC, for his competency and valuable advices. One of such advices
I try to remember whatever I work on is to split a task into small, clear
subtasks and try to finish them first, and the understanding that anything can
always be improved so there is no need to spend a lot of time trying to make
"a perfect version". 

### What's Left to Do

From the list of GSoC proposal tasks I did not complete everything. Persisting
events was one of them. After discussing about this feature with my mentor, we
decided that this task is not really neccessary. The main reason is that there 
is another project which can be used for persistent storage of all events and
offline processing.  The purpose of Ochi is to do real time analysis. We are
not interested in all of the events but just the ones that are new and have
some important features. If such events are found, a user should be able to
share it and only those events should be persisted. 

Generating dashboard with statistcs was also not accomplished since there was
not enough time, unfortunately. It is something that I would like to tackle
after GSoC as well as a few more tasks. 