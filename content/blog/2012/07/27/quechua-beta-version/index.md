---
title: "Quechua - beta version"
authors: ["zaccone"]
date: "2012-07-27"
categories: 
  - "data-mining"
  - "gsoc"
tags: 
  - "c"
  - "data-mining-d11"
  - "framework"
  - "gsoc-d20"
  - "machine-learning-d25"
  - "python-d32"
---

**Quechua beta version**  
  
  
**Hello World!**  
  
  

All GSoC 2012 students, including those working for HoneyNet, started their projects a long time ago. Since “Midterm evaluation” has passed too, I would like to share some experience and code with you. Please keep in mind this is still a beta version and some things may change during the second part of coding period, however comments and tips will be helpful, as always :-)

  
  
  
**Before we start**  
  
  

My initial project proposal included building one dedicated tool doing one thing - analyzing information about logged connections, stored in a PostgreSQL database. This included applying [apriori](http://rakesh.agrawal-family.com/papers/vldb94apriori.pdf) or similar data mining algorithm. The algorithm itself finds frequent itemsets, quite helpful in analyzing correlations between used protocols, ports (which may help determining malware/virus used in this particular attack), as well as source and destination addresses. Since dionaea sensors may log thousands of connections it’s almost impossible to observe them manually. In other words - it should allow users to watch for network anomalies, like excessive connections from one network segment, or suspiciously big volume of connections from address X, port Y to one dionaea sensor with address M and port N.

  

Some may say this can be done with just simple counting. Well, yes and no. If we count just one property this is simple, true. You can easily count number of connections from address X, count number of connections with source port Y. This is, however, more complicated, when one would like to check the number of connections/itemsets including many properties . Finding all frequent itemsets can be done automatically with data-mining algorithm. Data mining is all about answering the question “let’s check this data and see if we find something” not “let’s check if we find something interesting when we use property A, property B and property C”

  
  

In the initial proposal all the results (frequent itemsets) would be stored in a dedicated database schema. However my mentor, Mario, suggested building the whole application on top of the light framework, letting future users to switch particular components (for example algorithms used) easily. I thought this could be a great idea and we changed (or rather extended) project goals and moved to defining requirements as well as projecting low level architecture, choosing the technology and 3rd party libraries.

  
  

So far we are done with beta version of the framework and will move to the next part - building particular components reading and writing from and to the databases and looking for interesting data.

  
  
**The framework**  
  

Just before the midterm evaluation I finished coding the beta version of the framework.  
As I wrote above this is still a beta version, thus couple of bugs are probably still hiding between code lines. On the other hand I believe it’s ready enough and one can write some modules doing real work.  
So, what does it do?  
The framework can be used to apply data-mining/machine learning algorithms on various data formats and sources. It should be flexible enough to switch particular components - channels, processors, algorithms and loggers. Thanks to that, switching the algorithm or any other component should be as easy as loading another shared (.so) library and changing the configuration file. Basically, the framework should also allow to read from many data sources, files, databases or sockets and log the results in the same way. The only limit is the plugin’s programmer imagination or requirements.  
In most of the cases data mining or machine learning process consists of couple of steps:  
\- data retrieval step  
\- preprocessing step  
\- data-mining/machine learning  
\- postprocessing step  

  
  

Quechua architecture is also similar. It is build on top of 3 main components:

  
  
_Channel_  

Reads data from various sources. Channels open files, connect to databases, open network sockets and ‘understands’ raw input data. Channels also may ‘decide’ when the input pack is ready to be passed forward.

  
_Workflow_  

Workflows are components including Processor and Algorithm objects. They also register themselves in Channels. This way, channel will pass the pack with previously fetched data to every registered workflow.

  
  
_Logger_  

When workflow finishes its work the results can be logged. This is a perfect task for Logger component. It does the opposite way Channel does. Loggers know where to log the formatted output.

  
  
  
  

There are some constraints of course. Since this is a framework that can be used with many data formats, for many purposes it is the plugin programmer to take care and build plugins that that ‘understand’ format of the data received from adjacent component. And this needs to be done on low-level, C++ class definition level. That is, when you build a Channel that sends data to Processor component, you have to make sure that Channel will wrap it in a class that Processor ‘knows’ (just include header with class definition). I believe this constraint is much better that forcing everybody to use one universal format.

  
  
You can reach Quechua [here](https://bitbucket.org/zaccone/quechua)
