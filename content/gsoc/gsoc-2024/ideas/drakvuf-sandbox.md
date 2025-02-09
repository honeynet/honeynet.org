---
title: "Extending the DRAKVUF Sandbox analytic pipeline"
date: "2024-02-05"
project_url: "https://github.com/CERT-Polska/drakvuf-sandbox/"
hours: "175 or 350 hours"
mentor: "Jarosław Jedynak"
project_type: "Improving an existing tool"
---

DRAKVUF Sandbox is an open source automated black-box malware analysis system using virtual machine introspection (VMI) with DRAKVUF (https://drakvuf.com) engine under the hood.

As DRAKVUF Sandbox monitors behavior of malware samples it collects a lot of detailed data, like API calls, syscalls, network traffic, etc., however despite this vast amount of information, most of it is not exposed directly to the first-line operators and analysts using the sandbox.

The goal of this project is to:

* extend DRAKVUF Sandbox with useful heuristics for detecting the most common malware types and behaviours
* detect typical malicious patterns like code injection, and create a behaviour graph that can be easily grokked by the analysts (currently a subset of this feature is provided by a thirdparty project proc2dot)
* improve the integration of DRAKVUF Sandbox with the rest of the analytic pipeline. This will make it possible to display the analysis results more directly in other tools

Primary required skill is Python programming and a familiarity with Linux environment. Knowledge of how OS works under the hood and other low-level topics is also very desired. Skill with malware analysis or IT security topics is nice to have, but absolutely not necessary - we will help with any malware-specific design issues.
