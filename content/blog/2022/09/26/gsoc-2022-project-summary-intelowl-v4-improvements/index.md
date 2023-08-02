---
title: "GSoC 2022 Project Summary: IntelOwl v4 Improvements"
authors: ["Matteo Lodi"]
date: "2022-09-26"
coverImage: "intel_owl_positive_reduced.png"
tags: ["gsoc", "intelowl", "threatintel"]
---
Our [GSoC](https://summerofcode.withgoogle.com/) student [Aditya Pratap Singh](https://github.com/devmrfitz) was working for three months under the supervision of Matteo Lodi on the OSINT platform [IntelOwl](https://github.com/intelowlproject/IntelOwl), specifically on bulk analysis, single sign-on, and major improvements to the configurations and secrets.

Read on for an overview of their achievements and how they successfully contributed towards IntelOwl and some considerations for the future.

<!--more-->

**Student**: Aditya Pratap Singh ([devmrfitz](https://github.com/devmrfitz))

**Mentor**: Matteo Lodi, Simone Berni and Daniele Rosetti

**Organization**: The Honeynet Project

**Project**: [IntelOwl](https://github.com/intelowlproject/IntelOwl)

**Project Overview**

Intel Owl is an Open Source Intelligence or OSINT solution to get threat intelligence data about a specific file, an IP, or a domain from a single API at scale. It integrates a number of analyzers available online and is for everyone who needs a single point to query for info about a specific file or observable.

**Aditya’s proposal:**

_Improve existing functionalities and add new ones to IntelOwl for release of v4._

- Allow plugin secrets to be stored and managed from GUI #978_
- Allow analysis of multiple IOCs in one call #732_
- Add support for external authentication methods #121_
- Provide navigable JSON result for each analyzer #959_
- Add hashes to File\_Info analyzer #270_
- Allow plugin configurations to inherit (extend) from each other #752 - Allow editing plugin params from the GUI #433_

**Aditya's Journey**

I've been an avid open source contributor over the past year. It is a great experience finding interesting open source projects that I love and contributing to them in whatever small ways I can. Although development is satisfying in itself, open-source events like Hacktoberfest feel like a great opportunity to get recognised by the community for our contribution towards the codebase as well as other aspects of popular FOSS projects.

One such major opportunity is the Google Summer of Code. GSoC is a dream of most students engaged in development as it not only provides a major motivation to commit ourselves to open source development, but it is also one of the few internship-like experiences that many students get. Like most students, I was very eager to get accepted as a contributor in GSoC, not only this year, but the last one as well. However, due to multiple reasons, I was unable to get selected then. So from early this year, I started looking into past GSoC organizations whose tech stacks and field of work matched my interests and capabilities. I eventually narrowed down my search to two organizations - The Honeynet Project and CCExtractor. Both of these orgs are doing amazing work in their respective domains - The Honeynet Project has a variety of well-developed cybersecurity tools under its umbrella, while the prowess of CCExtractor is well known in its own right.

I started contributing to both these organizations from February of this year. A major mistake I'd made when trying for GSoC last year was not engaging with the project's community and maintainers and, beyond solving issues on your own, helping others solve their issues. This time, I ensured to be a part of both the projects' community from the very starting itself. I picked some issues from Github, worked on them, asked the community about the setbacks I faced and helped in some issues faced by other people. Actively engaging with the community made open source development a lot easier as well as less monotonic. I was able to solve more issues than I otherwise would have. I submitted proposals in both the organizations. Now the waiting period began...

The selections of GSoC were finally announced towards the end of May, and I anxiously checked the results. I was selected as a contributor with The Honeynet Project 🎉🎉🎉

The first step after the excitement phase calmed down was to look over the proposal I'd submitted and add it's sub-deadlines to my calendar. Then the coding finally began. Since this was my first time working a long project with a globally distributed community, I ran into some issues with properly communicating my progress as well as next intended steps to my GSoC mentor. However, after my first PR, my mentor, Matteo, promptly recognised the issues I was having and helped me address them. He told me where I was going wrong and how I could do better. My work began getting a lot smoother once I implemented his suggestions and I made a total of 5 major successful PRs by my mid-evaluation deadline.

Here's an overview of the features I had implemented by my mid-evaluation:

- Allowed bulk analysis of files as well as observables, leading to a more efficient workflow for IntelOwl users. [#1032](https://github.com/intelowlproject/IntelOwl/pull/1032)
- Improved the rendering of JSON job result data [#1051](https://github.com/intelowlproject/IntelOwl/pull/1051)
- Edited `FileInfo` analyzer to add some more potentially useful hashes. [#1073](https://github.com/intelowlproject/IntelOwl/pull/1073)
- Implemented a feature that facilitated editing of plugin parameters directly from GUI as well as setting of default parameters at organization level, thus making IntelOwl more customizable and easier to use. [#1095](https://github.com/intelowlproject/IntelOwl/pull/1095)
- Added an `extends` field of config files. This allowed configs to extend from other similar config, thus eliminating unnecessary code duplication. [#1119](https://github.com/intelowlproject/IntelOwl/pull/1119)

I still felt I was going slightly wrong somewhere. My mid-evaluation report directed me to the problem. I was again not communicating enough, the very same mistake I had made last year. Due to the distributed nature of any popular FOSS project's community, it is very essential that seemingly minor implementation decisions (like the positioning of a button) should be discussed before being actually coded. This helps the community's developers to avoid writing as well as peer-reviewing unnecessary code.

So, from the next PR onward, I started being much more involved in regular discussions about what I had done, and more importantly, what I was going to do. Instead of asking for the maintainers' peer review at the very end, I started pinging them whenever I felt a distinct enough sub-feature had been pushed. This allowed me to produce much more useful code in much lesser overall time.

Finally we come to today's status. I'm almost done with all the issues I set out to do. I've merged one more major PRs and there's another one still in the Pending for Review list. Hopefully, it will be merged soon too. The major features introduced in these PRs are:

- Added "Login with Google" support to IntelOwl to allow easier and secure user onboarding. [#1129](https://github.com/intelowlproject/IntelOwl/pull/1129)
- \[The pending one\] Allowed secure editing of plugin secrets from IntelOwl's GUI. Earlier, the secrets could only be edited by manually modifying a specific file on the server. Also, implemented organization-level secrets. [#1136](https://github.com/intelowlproject/IntelOwl/pull/1136)

The merging of this final PR will conclude my GSoC journey. I learnt a lot more than I initially set out to. The most valuable lessons are, in fact, not even technical in nature. I learnt how to better work with a team, especially one spread over various timezones.

As an ending note, I would like to give a huge thanks to my mentor, Matteo Lodi. He was with me every step of the way, even when my work was not up to the mark.  
Thanks a lot Matteo :)

Original post is available [here](https://dev.to/devmrfitz/to-gsoc-and-beyond-4m34)
