---
title: "Progress so far at the Network Analyzer"
date: "2012-05-07"
categories: 
  - "gsoc"
tags: 
  - "flow"
  - "gsoc-d20"
  - "malware"
  - "network-traffic"
  - "protocols"
---

Although it is still time for the official coding period start at GSoC 2012, i started to make my commits for the Network Analyzer project . The output of the project will be a web based traffic analyzer. It is aimed to let people upload their files from web interface and see the results. Instead of the detail header information, network analyzer will be focusing on applicaiton level data for display. One will be able to find answer to questions like what is the response HTML, is there any malicous javascript files at the header of the HTML file, is there any binary attachment at the sent mail, is it malicious, etc. The project is aimed to display these results by using visualization. The visualization details can be found at the project site:  
  
The currrent development is going on at the Github repo\[1\]. Devel is the branch i am using for my commits right now. When the source is examined, it will be seen that the project is set up with buildout. The installation of buildout is defined at the [README](https://github.com/oguzy/openwitness/blob/devel/README) page. The commands should be run after the repo is cloned and the directory is changed to openwitness:  
  
`  
$ git clone git@github.com:oguzy/openwitness.git  
$ git checkout devel  
$ git pull  
$ cd openwitness  
`  
  
After the buildout is run, some new directories will be created. To start the server run  
  
`  
$ bin/django runserver  
`  
  
This will run the development server of the Django. The current Django release is 1.3. When you point out 127:0.0.1:8000 at your browser, it will display the main page. Click on the _PCAP_ menu at the top and then choose _Upload_. This will let you choose a pcap file for being upload. What is done at the background is  
  
\* Check the network layer protocol of the uploaded pcap file. Determining whether this file is TCP of UDP is necessary to get the flow traffic from inside. If the traffic is TCP, a flow extractor is being run. Each flow is saved as seperate pcap files.  
[Bro](http://bro-ids.org/) is used for detecting network layer protocol. Bro is mentioned as an IDS, which can use Snort signatures and user defined rules. After installing Bro, the command line tool of Bro generates _conn.log_ file that gives information about the pcap file.  
  
`  
$ bro -C -r flow.pcap | bro-cut proto  
`  
  
Bro-cut is an auxiliary command that can be found at the Bro source code after compilation finishes. It eases reading the conn.log file. A typical conn.log file is as below  
  
`  
$ cat conn.log  
#separator \x09  
#set_separator ,  
#empty_field (empty)  
#unset_field - 
#path conn  
#fields ts uid id.orig_h id.orig_p id.resp_h id.resp_p proto service duration orig_bytes resp_bytes conn_state local_orig missed_bytes history orig _pkts orig_ip_bytes resp_pkts resp_ip_bytes  
#types time string addr port addr port enum string interval count count string bool count string count count count count  
1230112979.451875 o68JslpuuHi 192.168.1.222 1109 192.168.1.64 8080 tcp http 5.442875 1642 9365 S1 - 9108 ShADad 8 1970 11 9818  
`  
  
One may read the fields and say that this is an HTTP traffic information, from 192.168.1.222 to 192.168.1.64. The connection is destined to 8080 and it is an established connection (S1 indicates it). The other fields are the sent and receive byte numbers. The detail information can be seen at the [old Bro wiki](http://www-old.bro-ids.org/wiki/index.php/Reference_Manual:_Analyzers_and_Events#Connection_summaries). There are examples also at the Bro site from [2011 workshop](http://bro-ids.org/bro-workshop-2011/solutions/logs/index.html)  
  
After the flows are saved, each flow file should be analyzed for application level protocol detection. According to the protocol detected, parsers related with the protocol will be hooked. Anyone can write its own protocol detectors, also. To use a custom protocol detector, base detector should be inherited:  
  
[Base detector](https://github.com/oguzy/openwitness/blob/devel/openwitness/modules/traffic/detector/base/handler.py)  
`  
from openwitness.modules.traffic.log.logger import Logger  
  
  
class Handler(object):  
def __init__(self):  
super(Handler, self).__init__()  
self.log = Logger("Base Protocol Handler", "DEBUG")  
self.log.message("base protocol handler called")  
  
def detect_proto(self,**params):  
pass  
  
def detect_appproto(self,**params):  
pass  
`  
  
The two functions should be owerritten at the custom protocol detector. Bro appplication level protocol detection is as below:  
  
`  
def detect_appproto(self, file_path, file_dir):  
self.log.message("file_path: %s file_dir: %s" % (file_path, file_dir))  
cmd = " ".join([self.bro_cmd, "-C -r", file_path])  
self.log.message("Bro command: %s" % cmd)  
output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, cwd=file_dir).communicate()[0]  
cmd = " ".join(["cat conn.log", "|", self.bro_cut_cmd, "service"])  
self.log.message("Bro-cut command: %s" % cmd)  
output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, cwd=file_dir).communicate()[0]  
return output  
`  
  
Bro uses dynamic protocol detection. It is possible to detect application level protocols regardless of protocol information, but from predefined traffic signature. It is also possible to define custom rules to detect undetected protocols. The current supported protocols are listed [here](http://www-old.bro-ids.org/wiki/index.php/DynamicProtocolDetection#Implementation_Status).  
  
After the protocol is detected, the parser related with it will be run to gather applicaiton level data. The gathered information will be saved at MongoDB. It is being used the MongoDB driver for Django, so database operations will be handled by using db api.
