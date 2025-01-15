---
title: "VM image for Network Analyzer and installation howto"
authors: ["Oguz Yarimtepe"]
date: "2012-08-19"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

There is a vm image, that you can import the appliance and see the application at your own machine. You may download the ova file here: [http://www.loopbacking.info/ovizart/](http://www.loopbacking.info/ovizart/)  
  
To import the image, you will need VirtulBox installed.  
  
It is a virtual machine image, and Ubuntu server 12.04 is installed on it. To login the system you will need username and password. Use _demo_ as username and _ovizartdemo_ as password. After logged in, become root by using _sudo su_ command and learn your IP address (use _ifconfig_ command at the command line). I used my eth0 as bridged mode. So plug a cable to your ethernet card while running the application.  
  
Edit your /etc/hosts file. Change the IP address where the ovizart.foo.com stays. After that, at your host machine, add the same line to your hosts file also. When you open your browser and enter ovizart.foo.com you will see the Network Analyzer main screen.  
  
You may try to install the application to your host machine also, instead of using the VM image. The [README](https://github.com/oguzy/ovizart/blob/master/README.md) file is pretty detailed. Pelase feel free to contact with me whenever you got an error or problem about installation. Use http://about.me/oguzy or oguzyarimtepe (at) gmail.com
