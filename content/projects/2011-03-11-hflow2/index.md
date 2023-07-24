---
title: "HFlow2"
date: "2011-03-11"
---

## What is Hflow2

* * *

**Hflow2** is a data coalesing tool for honeynet/network analysis. It allows to coalesce data from snort, p0f, sebekd into a unified cross related data structure stored in a relational database.

There is a paper with a more detailed description can be found  [here](http://www.cs.indiana.edu/~cviecco/papers/hflow2.pdf).

The rationale for building hflow2 was the need to create a tool that had several features that were not available in other systems. In particular no tool existed that provided a sebek and network aware offline processing. A comparision of hflow2 with other similar systems follows:

<table class="wiki"><tbody><tr><td></td><td>Hflow2</td><td>Hflow + sebekd</td><td>sebekd</td><td>argus</td><td>netflow</td></tr><tr><td>Flow Type</td><td>Bidi</td><td>Bidi</td><td>none</td><td>Bidi</td><td>uni</td></tr><tr><td>Sebek Aware</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>P0f Aware</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Content Based marking</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Off line</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No runtime dependencies</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Fail Stop</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></tbody></table>

hflow2 however can appear to be MUCH slower than other systems than only analyze flow data such as argus or netflow. The main reason this happens with high-interaction honeynet data is that hflow also takes care of sebek data, which can be extremely voluminous. Internal tests of idle systems show that sebek data is 40 times larger than non-sebek data. This results in a much higher use of the DB and thus a really disturbing performance, packet captures with no sebek data should be processed faster than argus v2.

More information can also be found in the  [original hflow2 website](http://www.cs.indiana.edu/~cviecco/oscode/hflow2.html).
