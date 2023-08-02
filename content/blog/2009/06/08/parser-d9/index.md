---
title: "Parser"
authors: ["Kevin Galloway"]
date: "2009-06-08"
tags: 
  - "sebek-visualization"
---

The first version of the parser is essentially finished. The main goal for the basic version of the parser is to take Sebek data and create two groups of data: one group is comprised of a data structure that holds an event's information, things like the timestamp, event type, what service the event was connected to, etc. The second group is simply a list of each unique event, basically what types of events happened, what ports were used, services used by the events, things of that nature. The more interesting challenge was to somehow create a way for users to group events that they want to group together, so if a user wants to lump certain tools together (say vulnerability scanners, so nmap and nessus together) then a user can do so. So there is GUI component to this that allows a user to do this, it dumps all the unique events into one window, and the user can drag and drop them into the other, push the return button (which I should probably change the label on...) and it will create a text file of groupings.  
  
There are a few improvements that need to be made, mainly being able to save and specify grouping files. The interface could look a bit nicer as well, so my focus tomorrow will be on that, and then after that will come the actual visualization attempts. After the interface has been cleaned up a bit, I'll post a screenshot.  
  
The next hurdle with visualizations is what data in Sebek is important to users. My main thought at the moment is data that can help identify attacking trends, for example what tools they use, what order attackers from different countries/locations use certain tools (scan everything first, then exploit, or find one vulnerability and try to hit it, etc), though any feedback here would be awesome.
