---
title: "IntelOwl improvements: refactor analyzer tests"
date: "2025-02-07"
project_url: "https://github.com/intelowlproject/IntelOwl"
hours: "175"
mentor: "Matteo Lodi, Daniele Rosetti, Federico Gibertoni"
project_type: "Improving an existing tool"
---

This projects aims to improve the tests implemented in IntelOwl, in particular the ones regarding the Analyzers.

Right now, the actual implementation is kinda limited due to the inheritance of a framework built years ago, based on monkey-patching the tests.

The goal is to refactor this framework in a way that is easier to use and, at the same time, that it allows better tests implementation.

A thorough explanation of the problem and deliverables is described [here](https://github.com/intelowlproject/IntelOwl/issues/2715).

This is a time-consuming project that requires focus and attention. We expect the contributor to refactor most of the analyzers' tests and write additional checks.

The ideal candidate for this project is someone who understand how IntelOwl's framework works and knows testing frameworks like `unittest` very well.
