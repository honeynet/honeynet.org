---
title: "Vagrant configuration for Thug honeyclient"
date: "2014-07-26"
tags: 
  - "thug-d25"
  - "thug-vagrant"
  - "vagrant-d3"
---

Vagrant and Docker and wonderful tools that enable security practitioners to easily dive into the DevOps world and use them for InfoSec projects. Continuing from the previous blog post [Thug in 5 minutes](https://www.honeynet.org/node/1168), here is a Vagrant configuration to setup Thug honeyclient.  
  
It's essentially a simple shell script to automate the installation of Thug, which is applied to a virtual machine (created with VirtualBox) upon launch. To use it, first install VirtualBox and Vagrant itself for your OS version. The files are located in a GitHub repo here: [https://github.com/ikoniaris/thug-vagrant](https://github.com/ikoniaris/thug-vagrant)  
  
So, you can now have a working Thug VM up and running in minutes by simply issusing:  
$ git clone https://github.com/ikoniaris/thug-vagrant && cd thug-vagrant  
$ vagrant up  
  
This will download (only the first time) a virtual disk, create a new Ubuntu 12.04 LTS VM on the fly and start it, install Thug and all of its dependencies. And that’s it!  
  
You can then login into the machine by typing “vagrant ssh” or using an SSH client (e.g. PuTTY) and connecting to localhost:2222 — username: vagrant, password: vagrant. Once inside the VM, you will find Thug in the /opt/thug/ directory and the main script located at: /opt/thug/src/thug.py.  
  
If you want to stop the machine type “vagrant halt” (on the outer terminal, not inside the machine). Every time you want to start the honeypot VM a simple “vagrant up” issued inside the thug-vagrant directory is enough! (hint: see the list of CLI commands for more)
