---
title: "Scanners: a new plugin type for IntelOwl"
date: "2024-01-29"
project_url: "https://github.com/intelowlproject"
hours: "175"
mentor: "Matteo Lodi, Daniele Rosetti, Simone Berni"
project_type: "Improving an existing tool"
---

Right now there are many possible types of [plugins](https://intelowl.readthedocs.io/en/latest/Usage.html#plugins) in IntelOwl.

This project aims to add a new plugin type to the already existing ones in IntelOwl:
* The **"Scanner"** type would be a subtype of the “[Analyzers](https://intelowl.readthedocs.io/en/latest/Usage.html#analyzers)” ones with special configuration. In that way, IntelOwl could be used not only for classic data enrichment with external services but as either a vulnerability scanner or a scraper too. Refer to the [Github Issue for more details](https://github.com/intelowlproject/IntelOwl/issues/1393)

Like we have similarly done with other GSoC projects in the past that added new plugin types, we expect the contributor to add the most important new scanners (like [this](https://github.com/intelowlproject/IntelOwl/issues/1021)) to IntelOwl once he finishes building the framework to provide a base of tools which can be used by the users.

The candidate would have the chance to work through all the application stack (backend and frontend).
The ideal candidate for this project is someone who is familiar with how IntelOwl works and its core concepts.