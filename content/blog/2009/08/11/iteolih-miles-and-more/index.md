---
title: "Iteolih: Miles and More"
authors: ["Markus Koetter"]
date: "2009-08-11"
tags: 
  - "iteolih"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

We got a new milestone due:

  

**10.08.2009**  

  

  
- thread-pool works
  
- stream recording works
  
- shellcode detection using libemu works
  
- shellcode emulation using libemu works
  
- compiles on linux&openbsd
  

  

  
An exploit taken from a public repository, run against the software, is detected and emulated.

  

To shorten things, basically all required points are hit with current svn.

  

So, given the time we just saved, some words about how it works.

  

The core functionality in dionaea is written in c, but python is embedded as scripting language and required parts of the c-api are exported to the embedded python, using cython bindings.

  

If you want to provide a service on a given port, you are free to write the service in python, or c. I prefer python, as it is more forgiving on programming errors and faster to develop than c.

  

So, an attacker connects the service, the connection is accepted from the c core, all io on the connection is done in c, and passed to the python protocol.

  

Now we want to detect shellcode in the network stream, protocol independent. At first we have to record the stream, this is optionally done in within the c core, if processing for the connection is requested by the protocol. We may want to run different checks to the stream to check for shellcode, and each check will require its own contextual data, as well as its own stream, addionally we want to run the detection/processing in threads.

  

For now, there are 2 useable processors we can run on streams, an libemu based detection processor, and a dumper, which writes the stream do the logfile.

  

If io comes in, it is appended to the processors own stream, and the stream processor is queued in the thread-pool to check the new data.

  

If the emu stream processor heuristics detect a shellcode, it will try to run the shellcode and create a profile for the shellcode. The profile contains all detected api calls, their args and return values. This profile is serialized to json, and emitted as incident.

  

The incident is delieverd to an incident handler, the incident handler reads the json profile, and -taking the api calls and args- tries to guess what the shellcode wants to do. If  the handler could make sense of the api calls, he will run the appropriate actions to satisfy the requirements, bind a 'shell' to a port, download something, or run a command.

  

For cmd.exe shellcommands, we have to parse the commands and take appropriate action. If the commands instruct to download a file, we emit an incident which includes the url.

  

This incident is delieverd to an appropriate handler, which will download the file. We use curl for http, modified tftpy code for tftp and self a scripted ftp client to deal with ftp.

  

Thats it.

  

There is lots of space for improvements, for example storing the files downloaded, dumping the streams in a binary format for further analysis, useful logging,  ..., but we started a completly new project, and I'm glad we got so far for now.
