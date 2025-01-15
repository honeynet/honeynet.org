---
title: "cuckooHide -  Hiding CuckooBox from trivial detection mechanism"
authors: ["Dario Fernandes"]
date: "2011-09-09"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

The last part of Google Summer of Code 2011 was used to implement  
a Windows Kernel Driver responsible for hiding files and folders.  
This new component will be used to conceal Cuckoo Box components,  
present in the environment analysis. With this measure it's possible to  
avoid that some malware detect CuckooBox through some environment check,  
looking for specific files or folders.  
  
The Driver was implemented as a Filter Driver to maintain it independent  
of the Windows version used in the environment, not using any kind  
of hooking which may cause problems when using different versions of  
Windows. The Filter Driver act on the file system IRP requisitions,  
checking if a process marked for monitoring is doing requests that  
involve opening an handle or searching for any file or folder that must  
be filtered.  
If so, the response is changed, informing the process that the file or  
folder doesn't exist. The IRP requisitions filtered are, IRP\_MJ\_CREATE,  
IRP\_MJ\_QUERY\_INFORMATION and IRP\_MJ\_DIRECTORY\_CONTROL, which are the  
most commonly used to search for files and opening handles.  
Processes and files inspected by the Filter Driver are passed by an  
user land program, using the communication port created by the Filter  
Driver. Messages accepted are only FileAdd and ProcAdd, which inform  
that a new file or folder must be filtered or an new process must be  
monitored.  
  
A DLL was developed to control the Filter Driver, which can  
load and unload the Filter Driver from the system and send messages  
to it, adding new files, folders and process which must be  
inspected. To integrate with CuckooBox, a python component is being  
developed, which will communicate with the Filter Driver instead of the DLL.  
  
You can see the source code, download the Driver, the DLL and also an example which shows how  
the Driver work in the github repository of cuckoobox [http://github.com/cuckoobox](http://github.com/cuckoobox).
