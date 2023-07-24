---
title: "Visualization Experiments"
date: "2009-07-14"
coverImage: "vis1.png"
---

Most of my work in the past few weeks has been focusing on the visualization aspect of the project.  One thing that I am trying to avoid is simply making graphs/charts and that sort of visualization.  Those sorts of things are incredibly useful since anyone can understand them, on the other hand they're trivial to make.  I've been making a few basic visualizations, but the two that, so far, have the most merit are delinating the events based on color (each group of events is a separate color) and the other separates them based on height (each y position is a different event).  I'll admit that these are very rudimentary, but I think they get the idea across.  Each attached picture is broken into two visualizations, the top is based on color, the bottom on position.  One picture also experiments with size, basically if there are similar groups near one event, that node on the graph gets wider.  It's pretty basic at the moment, if there is a match for a group in the current event, and the one ahead of it, than it gets wider.  Since I only have one data source on my test data (one IP address) there's only one band, but with more data sources, more bands would appear, so one could compare and contrast data between different machines.  Grey nodes in both graphs are any data that doesn't match a group, basically I was trying to pick a neutral color that doesn't pop out when a user looks at the graph.  Ungrouped data isn't particularly interesting, aside from trying to see if an abscene of something indicates a trend.

  

  

Other features that I want to add are mouse-overs, so that one can tell what each event actually is, as well as what group it matched to.  So if you have a group of (ps ls), then it should only match if the event has a ps or ls in there.  Another visualization experiment I want to try is to break up the data in discrete time chunks, maybe 2 minute chunks, and just do a series of bar graphs that show how many matches for each group there are in each 2 minute chunk, animating through a bunch of these graphs to see if any trends pop up.
