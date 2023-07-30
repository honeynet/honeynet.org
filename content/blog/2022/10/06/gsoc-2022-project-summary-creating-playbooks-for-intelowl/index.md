---
title: "GSoC 2022 Project summary: Creating Playbooks for IntelOwl"
date: "2022-10-06"
coverImage: "intel_owl_positive_reduced.png"
tags: ["gsoc", "intelowl", "threatintel"]
---

Our [GSoC](https://summerofcode.withgoogle.com/) student [Aditya Narayan Sinha](https://github.com/0x0elliot) was working for three months under the supervision of Matteo Lodi on the OSINT platform [IntelOwl](https://github.com/intelowlproject/IntelOwl), specifically on introducing playbooks that define automated actions associated with the observation of a specific indicator of compromise.

Read on for an overview of their achievements and how they successfully contributed towards IntelOwl and some considerations for the future.

<!--more-->

**Student**: Aditya Narayan Sinha ([0x0elliot](https://github.com/0x0elliot))

**Mentor**: Matteo Lodi, Eshaan Bansal, Simone Berni and Daniele Rosetti

**Organization**: The Honeynet Project

**Project**: [IntelOwl](https://github.com/intelowlproject/IntelOwl)

### **Aditya’s GSoC Proposal:**

As cited in my original proposal’s overview:

I propose working on a new component for IntelOwl this summer - Playbooks which would help people share and run automatically, the exact analyzers/connectors they like on a particular kind of observable. This would help IntelOwl strengthen its community while achieving its goal of helping burnt-out CyberSecurity professionals do their job more easily.

### **Pre GSoC Commits:**

- RIPE API analyzer - ([#763](https://github.com/intelowlproject/IntelOwl/pull/763))
- BitcoinAbuse Analyzer - ([#764](https://github.com/intelowlproject/IntelOwl/pull/764))
- CAPE sandbox analyzer - ([#836](https://github.com/intelowlproject/IntelOwl/pull/836))
- Analyzer for mnemonic PDNS - ([#785](https://github.com/intelowlproject/IntelOwl/pull/785))

## **GSoC Tasks and Deliverables**

### 1. Playbooks Manager and changes in the IntelOwl core

A sub-app that had ready-to-use serializers to parse a playbooks\_config.json file along with all the necessary classes and data classes. While implementing this sub-app, I had to make some changes in the core of IntelOwl as well to accommodate for the feature.

I had to tackle multiple problems which came up while implementing this part of the issue. Lots of edge cases here & there and lots of code reviews. This was so integral that I found myself starting GSoC with figuring this out and ending GSoC with debugging something about it. Throughout my tenure, I found myself coming back to the core changes I made. Either working on changes suggested by my wonderful mentors Matteo, Eshaan, Simone, or Daniele Rosetti.

Other than that, I built up the job serializers for Playbooks and worked on the analyzer/connector filtering logic.

### 2. Tests and docs

After iterating through a couple of options, We settled on writing test classes for Files and Observables for Playbooks which used the same logic as Analyzers and Connectors. Like a lot of the development I did on making Playbooks, where I was writing one function which was used for both analyzers/connectors and Playbooks somewhere (usually after my mentors pointed out that I was still rewriting code that could be reused), I found myself doing the same here.

And then, of course, I updated the documentation appropriately for the feature.

### 3. Free to use Analyzers Playbook

This was the least time-consuming portion of the work. My aim was to provide a base playbook that consisted of a collection of free-to-use analyzers. To solve this, I wrote a quick script that looked through analyzers\_config.json for analyzers that did not have an API key associated with them and then dumped it in the playbooks config file in the appropriate format with the parameters associated with it.

### 4. IntelOwl UI changes

All frontend changes to support Playbooks were made as well (Accommodating in job reports, Adding an option for running Playbooks in the frontend, and A table in the plugins section)

This was a part we had to redo neatly another time to make the UX the best we could pull off. By the end, We settled on the current version which includes a simple radio option you can use to shift to the Playbooks tab.

### 5. PyIntelOwl Changes

I made all the corresponding changes to support Playbooks in PyIntelOwl.

Added CLI methods and easy-to-use functions for fetching playbook configs and running appropriate playbooks. After the Free to use Analyzers Playbook work, this was the simplest to pull off.

### Pull Requests

Mid development, I figured out that it’s best to have one PR for both frontend & backend (https://github.com/intelowlproject/IntelOwl/pull/1123) and another for PyIntelOwl (https://github.com/intelowlproject/pyintelowl/pull/176).

### Problems Encountered:

One of the main problems I encountered while working was syncing up with the other contributors working on the same issues as me. There were lots of merge conflicts and points where I had to rewrite things to match their changes.

### Next Steps

I am thankful for my supportive and brilliant mentors for giving me this chance and being there every step of the way. If they weren't there, I am sure I wouldn't have it made it so far. Someone trusting in you always pushes you ahead more than you can think.

I want to be there more with HoneyPot to accommodate in developing the projects they look forward to developing with my special interest being in [GreedyBear](https://github.com/honeynet/GreedyBear/). It is a project that is still being developed and has a lot of scopes for things to build.

I also want to help out with providing Go-IntelOwl support for Playbooks. It is something that wasn’t planned or promised in my original proposal. But Hussain, one of the other contributors to the IntelOwl project, ended up completing the CLI by the time we all finished with our GSoC projects. As of now, it lacks Playbook support. So that would be the natural thing for me to move forward to adding.
