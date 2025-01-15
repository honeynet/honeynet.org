---
title: "Introductions: Sebek Visualization Project"
authors: ["Kevin Galloway"]
date: "2009-05-24"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

Hello all,  
  
As today is the official start of the Google Summer of Code, an introduction both to the project, and for myself seems to be in order. My name is Kevin Galloway, and I'm currently a graduate student, in Computer Science at the University of Alaska, Fairbanks. Most of my background is more on the security side of things, although, at the start, graphics were one of the main reasons I chose computer science. This project was a way to combine those two passions of mine.  
  
A lot of my background is simulations is more on the physical side of things, modeling particles and physics, and I think a lot of the techniques and knowledge from that side lends itself well to dynamic data visualization, animation and movement help immensely when trying to analyze trends, and I hope to bring some of that knowledge to the project.  
  
The project itself is comprised of two main parts, a parser and then the visualizer. Since Sebek captures a wide variety of data, the parser needs to be more than just a way to extract events and IPs and the like, there has to be some way for a user to group the sorts of events (or any other piece of data gathered by Sebek) into some logical grouping. This is my first priority, and probably the subject of a future blog post, but creating a streamlined way to both let a user group data themselves, as well as attempting to have some sort of standard grouping, so users aren't bogged down in tedium, is the first step. The second part is the visualizer itself. There are many different ways to visualize data, and I'm the first to admit that I don't know the perfect way. I do know, that I am going to try to avoid simple graphing techniques. The first prototype will be a collection of essentially particles, each colored according to the data within, that will shift, flow, and disappear, to help analyze trends. After the initial visualization is done, I hope to have time to experiment with other techniques.
