---
title: "DRAKVUF Rust & Python bindings"
date: "2024-01-29"
project_url: "https://github.com/tklengyel/drakvuf"
hours: "90, 175 or 350 hours"
mentor: "Tamas Lengyel"
project_type: "Improving an existing tool"
---

DRAKVUF is a hypervisor-based malware analysis system written in mostly C & C++. It is designed to be high performant and stealthy, so malware won't be able to detect the analysis tools.

This project will focus on creating automatic Rust & Python binding generators for the core DRAKVUF libraries (libdrakvuf & libinjector). The goal is to automate the binding generation process, so future changes to the core library APIs will get automatically adjusted in the respective language bindings. Test-cases will need to be created and added to the CI to ensure the bindings remain operational.

The ideal candidate for this project should be at least on an intermediate level in either C, C++, Python or Rust, and will be willing to learn the others on the go.
