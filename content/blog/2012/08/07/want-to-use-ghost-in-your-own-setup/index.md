---
title: "Want to Use Ghost in Your Own Setup?"
authors: ["Sebastian Poeplau"]
date: "2012-08-07"
tags: 
  - "ghost-d68"
---

This is a short introduction to one of the features that the upcoming Ghost 0.2 will offer. I expect to release the new version in late August or early September.  
  
There is a command-line frontend for Ghost already that controls the honeypot's operation, but its capabilities are limited. In particular, the only way to get feedback from Ghost is to read the command-line output. That's only slightly inconvenient if you run the tool manually, but it's not at all suitable for automation, and it makes integrating Ghost into individual analysis setups unnecessarily complicated.  
  
Therefore, I've written a Windows library that encapsulates all communication with Ghost's kernel-mode components. The new frontend (also part of version 0.2) will be based on that library, and you can use it in your own applications to integrate Ghost into your setup.  
  
Using the library (surprisingly named "GhostLib", by the way), controlling Ghost is as easy as this:  
  
`  
#include "ghostlib.h"  
  
#include  
#include  
  
  
void Callback(int DeviceID, int IncidentID, void *Context) {  
  
// Data was written to the emulated device - 
// obtain information about the write request  
  
printf("Infection!\n");  
printf("Process ID: %d\n",  
GhostGetProcessID(DeviceID, IncidentID));  
printf("Thread ID: %d\n",  
GhostGetThreadID(DeviceID, IncidentID));  
}  
  
  
int main(int argc, char *argv[]) {  
int ID;  
  
printf("Mount the device\n");  
ID = GhostMountDevice(Callback, NULL);  
// Error handling  
  
// Wait for the malware to infect the device  
Sleep(10 * 1000);  
  
printf("Unmount the device\n");  
GhostUmountDevice(ID);  
// Error handling  
  
return 0;  
}  
`  
  
This will mount an emulated device, wait for 10 seconds and unmount it. If any process writes data to the device, the callback function is invoked immediately.  
  
Have a look at [ghostlib.h](http://code.google.com/p/ghost-usb-honeypot/source/browse/GhostLib/ghostlib.h) for more details on the API. You can build the DLL by running `build` in the directory GhostLib. Also, I'll publish binaries with the new release.  
  
The next step on the way to version 0.2 is to facilitate the installation of the honeypot by having GhostLib take care of putting the drivers in place...
