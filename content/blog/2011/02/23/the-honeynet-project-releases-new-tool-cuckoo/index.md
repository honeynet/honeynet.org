---
title: "The Honeynet Project Releases New Tool: Cuckoo"
authors: ["Anton Chuvakin"]
date: "2011-02-23"
tags: 
  - "malware"
  - "news"
  - "tool"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

Here is another tool release from The Honeynet Project: Cuckoo Box by Claudio Guarnieri. Cuckoo is a binary analysis sandbox, designed and developed with the general purpose of automating the analysis of malware. Read more about the tool [here](https://cuckoosandbox.org/), grab the tool [here](https://cuckoosandbox.org/downloadp) – but please read detailed setup guide [here](https://cuckoo.sh/docs/) (make sure to read it!). BTW, this tool is really well-documented, so make use of it before deploying it.

Cuckoo is a lightweight solution that performs automated dynamic analysis of provided Windows binaries. It is able to return comprehensive reports on key API calls and network activity. Current features are:

- Retrieve files from remote URLs and analyze them.
- Trace relevant API calls for behavioral analysis.
- Recursively monitor newly spawned processes.
- Dump generated network traffic.
- Run concurrent analysis on multiple machines.
- Support custom analysis package based on AutoIt3 scripting.
- Intercept downloaded and deleted files.
- Take screenshots during runtime.

Please [try the tool](https://cuckoosandbox.org/) and send the feedback [to the author](https://cuckoosandbox.org/) – or sign up for a mailing list devoted to this tool [here](https://public.honeynet.org/mailman/listinfo/cuckoo).
