---
title: "AfterGlow Cloud: Initial release"
authors: ["Surya Nallu"]
date: "2012-07-10"
categories: 
  - "gsoc"
tags: 
  - "afterglow"
  - "afterglow-cloud"
  - "data-visualization-d98"
  - "gsoc-d20"
  - "gsoc2012"
coverImage: "firewall_preview.jpg"
---

With the marking of the mid-term milestone in GSoC 2012, we're happy to announce a first version release of AfterGlow Cloud. After a lot of discussions and review the project seems to be in a good position for an initial release. The project in essential is based on AfterGlow \[1\], a security visualization tool which facilitates generating visual graphs from data you upload. The tool described at \[1\] is originally command-line based, the aim of this project, in general is to bring this tool and its options to the cloud -- so as to provide a neat interface for on-the-fly visualizations.

Live demos of the project are currently available at:

- - [http://afterglow.ayrus.net:31080](http://afterglow.ayrus.net:31080)

- - [http://andromeda.ayrus.net:31337](http://andromeda.ayrus.net:31337) (mirror)

This release covers all the basic features discussed and agreed upon initially \[2\]. You can upload any comma-seperated file (only CSV files) as your log source to visualize it. The current version doesn't cover parsers for exporting logs from different sources (example tcpdump) into CSV -- but this is a future addition, likely in the next release. To have a feel of what the application is capable of, you can try uploading the sample "firewall.csv" file (in the attachments). This sample file contains some rules (pass, block) over different source and destination nodes. Getting any sense of what's exactly going on is difficult by merely inspecting the CSV file -- this is where AfterGlow is needed.

Labels "Settings" and "Advanced Settings" cover some rendering settings you might want to choose or override for better customization. For example, "Print Node Count" would append the number of times each source/destination node occurs in the log file provided -- this gives a sense of the frequency of the nodes. Similarly, "Text Label Colour" provides the option to override the default black colour of text on the graph (You can hover over the "?" next to any input for a description of what they exactly mean).

Configurations are used to further scrutinize the rendering of the graph, for example you might want to colour a set of source/destination nodes "red" if their IP is '68.xx.xx.xx'. Each of these configuration lines bring about several layers of visualization. For example, you'd probably want the 'size' of the node on the graph to be proportionate to the frequency they appear throughout the log (configuration under 'Node Sizes' - 'Predefined - Number of Occurrences'). You can remove or change the ordering (ordering of configurations matter) once a line is added. A detailed guide to the different configuration options available, would be added later.

A sample configuration file is added as an attachment (sample.properties). If you'd like to try this out with the sample "firewall.csv" data file, you could choose "Manual" under the configurations and paste the contents of the file (instead of manually feeding in every line). The application also provides the feature of "saving" your settings. All changes you make in "settings" and "advanced settings" pane are stored as a cookie (for four days) if the save feature is checked. AfterGlow populates your settings every time you visit the application with an active cookie.

Here's how a rendered graph looks like:

Original CSV data:

![](images/drupal_image_889.jpg)

Graph rendered by AfterGlow on the above data:

![](images/drupal_image_891.jpg)

The source for the entire projects rests at the [GitHub repository](https://github.com/ayrus/afterglow-cloud). If you choose to run your own local install of the project, detailed instructions are provided in the [README](https://github.com/ayrus/afterglow-cloud/blob/master/README). The instructions and requirements listed in the README cater to Ubuntu and run Django's development runserver module (instructions for a production like environment -- Apache would be added later).

With this release, we've started to list out the possible features and additions that can be brought on to the next version of AfterGlow cloud (API, adding parsers to convert data from tcpdump etc to CSV files, among others). There's still a lot to be covered and added so please let us know if you'd like to suggest new features on the project, report a bug or any general comments (a feedback form would soon be added to the current demos)!

Links:

\[1\] [http://afterglow.sourceforge.net/](http://afterglow.sourceforge.net/) \[2\] [https://www.honeynet.org/gsoc/slot6](https://www.honeynet.org/gsoc/slot6)
