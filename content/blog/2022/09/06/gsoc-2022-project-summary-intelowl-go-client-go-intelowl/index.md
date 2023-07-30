---
title: "GSoC 2022 Project Summary: IntelOwl Go Client (go-intelowl)"
date: "2022-09-06"
coverImage: "intel_owl_positive_reduced.png"
tags: ["osint", "intelowl", "threatintel"]
---

**Student**: Hussain Khan ([@fear-the-reaper](https://github.com/fear-the-reaper))

**Mentor**: Shubham Pandey and Eshaan Bansal

**Organization**: The Honeynet Project

**Project**: [Intel Owl](https://github.com/intelowlproject/IntelOwl)

**Project Overview**

Intel Owl is an Open Source Intelligence or OSINT solution to get threat intelligence data about a specific file, an IP, or a domain from a single API at scale. It integrates a number of analyzers available online and is for everyone who needs a single point to query for info about a specific file or observable.

<!--more-->

**Hussain’s proposal:**

_I propose making a robust Go client library for OSINT Threat Intelligence Platform IntelOwl that easily communicates with their API. The Intelowl Go SDK will allow developers to communicate with the API so that they can easily develop and integrate IntelOwl with their own automated scripts, tools, and services._ 

So the main objective was to develop a robust Go client library that is easy to use for developers and easily extensible for adding new features.

**Pre GSoC Commits**

List of pull requests merged before GSoC’s coding period:

- Adding a new issue template where I added markdown templates for adding a new issue and analyzer [(#904](https://github.com/intelowlproject/IntelOwl/pull/904)).  
- Patching the FLOSS analyzer where I researched adding the eXpert flag. This was a really fun issue where I thoroughly understood how intelowl’s analyzers are configured and how they are executed ([#940](https://github.com/intelowlproject/IntelOwl/pull/940)).  
    

**GSoC Tasks and Deliverables**

I made 20 commits and over 20 pull requests in go-intelowl. The following major tasks were completed and maintained over time. You can see the release [here](https://github.com/intelowlproject/go-intelowl/releases).

## 1. Proper project structure and automated workflows

Previously the SDK was just a **client.go** and a **go.mod**. This lacked a proper structure and placement where adding new features or revisions would be a hassle. Now the project has a proper structure where you can easily add new features, examples, tests, and workflows. Furthermore I added Issue and PR templates that closely resembles IntelOwl's. In addition to this, I implemented a proper CI/CD so that with every pull request and push a linter, unit tests, dependabot, and codeql would run.  
  
**Code Milestones:**

-  Adding dependabot, codeql, PR template and setting up gh actions ([#28](https://github.com/intelowlproject/go-intelowl/pull/28))

## 2. Breaking down the API endpoints into service objects

Previously the SDK was only a client struct with every endpoint implemented as a method. This gave rise to repetitive code in most methods and couldn’t be easily extensible or maintainable as you’d need to keep track of many methods so debugging would be hard if not impossible.

**Challenges faced**

- After much discussion, I, Shubham, and Eshaan came to the consensus of using the **service objects** pattern where we divide and group together related endpoints to a struct for example all the _tag_ endpoints will be in the _tagService_ object. 
- There was a lot of redundant code regarding building and sending the request. To solve this problem we adapted the **builder pattern** where we can easily build a request according to that endpoint’s needs and requirements.
- There were many optional parameters required for a variety of endpoints. Hence with every service object, we established **optional** structs to easily cater to each endpoint with maximum flexibility and customizability.
- Lastly, we wanted to speed up the developer process. In order to achieve that we aimed to provide easy ways to instantiate the client and provide a verbose logger to easily debug any problems they faced.

**Working and solution**

For the above problems we first divided the API into 7 service objects where each has its own optional parameters. Furthermore, to adopt the builder pattern we opted on making an internal method for the client to easily facilitate the service objects. Lastly, we provided methods to easily instantiate the client through a JSON file representing the client’s own optional struct. In addition, to that, we built our own logger using [logrus](https://github.com/sirupsen/logrus). We opted to use logrus as it gave us great flexibility.

**Code milestones**

- Adding the tag [(#34](https://github.com/intelowlproject/go-intelowl/pull/34)), analyzer, and connector ([#35](https://github.com/intelowlproject/go-intelowl/pull/35)),  job ([#36](https://github.com/intelowlproject/go-intelowl/pull/36)), and analysis ([#42](https://github.com/intelowlproject/go-intelowl/pull/42), and [#43](https://github.com/intelowlproject/go-intelowl/pull/43)). Adding TLP enum ([#39](https://github.com/intelowlproject/go-intelowl/pull/39)), making a constant file for the endpoints ([#45](https://github.com/intelowlproject/go-intelowl/pull/45), and [#59](https://github.com/intelowlproject/go-intelowl/pull/59))
- Implementing the builder pattern ([#40](https://github.com/intelowlproject/go-intelowl/pull/40))
- Providing new ways to make the client ([#52](https://github.com/intelowlproject/go-intelowl/pull/52)), and developing the logger ([#48](https://github.com/intelowlproject/go-intelowl/pull/48))

## 3. Proper and thorough unit testing of each service object

Now in order to fully check and test the service objects we needed to perform adequate unit testing that can be easily added and flexible.

**Challenges faced**

I and Shubham discussed this at length on making a robust testing suite. Towards this, we looked at various methods of how tests are made in Go. We encountered a variety of problems as [#37](https://github.com/intelowlproject/go-intelowl/issues/37) 

- Properly mocking the test server
- Properly mocking each resource rather than just sending a JSON string
- Handling non-success cases to check if the client properly handles errors 

For this to be implemented we had to change our perspective and approach on how to do things

**Working and solution**

To achieve the aforementioned objectives we used Go’s **httptest** to properly mock IntelOwl server. Furthermore, we adapted Table Driven tests so that we can run multiple tests for an endpoint under a single method.

I’m grateful to our mentor, Shubham, who spent a great amount of time and effort to solve most of the above-mentioned issues which significantly sped up the process.

**Code milestones**

- Better tests to easily add and make new unit tests ([#56](https://github.com/intelowlproject/go-intelowl/pull/56))

## 4. Writing godoc documentation and proper examples

The last part was writing documentation, and easy-to-read examples to help developers understand to easily use our humble SDK. Now Go provides a way to document your Go package using the [godoc](https://pkg.go.dev/golang.org/x/tools/cmd/godoc) tool where it parses Go comments and presents them on a web page.

**Code milestones**

- Adding proper examples and a README to easily get started [(#51](https://github.com/intelowlproject/go-intelowl/pull/51/files), [#55](https://github.com/intelowlproject/go-intelowl/pull/55))
- Adding consistent godoc comments ([#54](https://github.com/intelowlproject/go-intelowl/pull/54))

### Next Steps

I’m very glad to have worked on this amazing project and would continue to do so in the future. It has been a major source of learning for me. Some of the things I hope to tackle in the future are

- Integrating [gorilla/mux](https://github.com/gorilla/mux) to add support for request method-based endpoints to improve our testing suite. ([#58](https://github.com/intelowlproject/go-intelowl/issues/58))
- Adding the playbooks endpoints. ([#60](https://github.com/intelowlproject/go-intelowl/issues/60))
- Developing Integration tests similar to [go-github](https://github.com/google/go-github/blob/master/test/README.md) ([#24](https://github.com/intelowlproject/go-intelowl/issues/24))

I would like to thank **The Honeynet Project** and **Google Summer of Code** for providing me with this opportunity. Special thanks to my mentors **Eshaan Bansal** and **Shubham Pandey** for being kind and helpful to me throughout this amazing journey.
