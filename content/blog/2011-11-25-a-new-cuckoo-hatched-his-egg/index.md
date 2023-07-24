---
title: "A new Cuckoo hatched his egg!"
date: "2011-11-25"
tags: 
  - "dynamic-malware-analysis-virtuaization-cuckoo-gsoc"
---

#### Overview

  
  
Cuckoo Sandbox is an Open Source automated dynamic malware analysis system designed to analyze and report on suspicious files.  
Cuckoo started as a Google Summer of Code project in 2010 within The Honeynet Project. It was designed and developed by Claudio Guarnieri who still maintains the project and lead its development efforts.  
  
Cuckoo has been selected again this year for Google Summer of Code 2011 with The Honeynet Project and with Dario Fernandes who joined the team. The work being done in the last months lead to the release of the 0.2 version.  
  

#### What's new in 0.2 version ?

  
  
Basically Cuckoo has been completely rewritten since 0.1 and is now much more solid and easier to setup.  
It has been refactored to be purely Python and to use our new hooking engine, cHook.  
  
One of the most interesting aspects is the introduction of analysis packages.  
  
These packages provide scripting capabilities to Cuckoo's analysis process: through the use of three custom Python functions, users are now  
able to control the code injection, process monitoring, customize the conditions to terminate the analysis and allow to execute any code before, during and after the analysis within the virtualized environment.  
  
This feature allows users to adapt Cuckoo to their own needs in a clean and structured fashion and permits the creation of unique and  
unconventional use cases.  
  

#### Downloading Cuckoo

  
  
You can get your copy of Cuckoo Sandbox 0.2 from the official download page at:  
[http://cuckoobox.org/downloads.php](http://cuckoobox.org/downloads.php)  
  
Or by cloning the development GitHub repository (which already includes new features and improvements from the stable package) at:  
[https://github.com/cuckoobox/cuckoo/](https://github.com/cuckoobox/cuckoo/)  
  
You can get a preview of currently available default packages at:  
[https://github.com/cuckoobox/cuckoo/tree/master/shares/setup/packages](https://github.com/cuckoobox/cuckoo/tree/master/shares/setup/packages)  
  
The use of such packages can be specified at submission through the provided submit.py script or by interacting directly with the SQLite  
database.  
  
You can find more details as well as setup instructions in the official documentation at:  
[http://cuckoobox.org/documentation.php](http://cuckoobox.org/documentation.php)  
  
You can get in contact with developers and users on #cuckoobox at  
irc.freenode.net.
