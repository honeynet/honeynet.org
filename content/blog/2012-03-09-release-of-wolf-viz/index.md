---
title: "Release of WoLF Viz"
date: "2012-03-09"
tags: 
  - "forensic-challenge-d87"
---

Frasier, who participated in our recent [visualization forensic challenge](https://honeynet.org/challenges/attack_visualization_challenge) has released his visualization tool WoLF Viz at [http://code.google.com/p/wolf-viz/](http://code.google.com/p/wolf-viz/). _WoLF Viz works by parsing arbitrary text log files into a network (graph) of words, where the words are nodes and the edges are adjacent word pairs. The edge weights are based on how often the two words are seen next to each other. It then draws a map of log file, looking at each word-pair as it moves through the log file, using colours to represent the edge weights of each word-pair. Finally, it draws the selected log file text on top of the edge map and uses transparency to switch between views._ . A demo can be found at [http://3a29.net](http://3a29.net). Its pretty neat! Great work Frasier!
