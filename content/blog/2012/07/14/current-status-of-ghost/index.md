---
title: "Current Status of Ghost"
authors: ["Sebastian Poeplau"]
date: "2012-07-14"
tags: 
  - "ghost"
---

As the first half of the HP summer of code has passed, I'd like to give a short update on the current status of the Ghost USB honeypot.  
  
While Ghost has been able to report possible infections with USB malware by means of an emulated USB flash drive before, it is now able to collect information about the process that writes data to the bait device. This information includes the process ID and a list of all modules (i.e. executables, such as EXE and DLL files) that are currently loaded into the process. We extract the data directly from the kernel's internal structures, so it will be hard for malware to shield it from the honeypot. Knowing the process that the malware resides in is interesting for analysis, and having a list of modules that the process uses can give us a hint as to where the malicious code is stored on disk.  
  
The information that Ghost generates can now be transmitted to user space via blocking communication. See [my previous post](https://honeynet.org/node/888) for further details.  
  
Also, Ghost can be used on Windows 7. We fixed some issues with control codes that Windows 7 uses in a different way than XP. However, at the moment it's not yet possible to format emulated devices on Windows 7. This is usually not a problem, because we can just distribute a preformatted image file.  
The constraint is due to a deeper issue that will take some more time to fix: The disk class driver (and thus Ghost, which operates at the same level) is supposed to report disk devices, while the partition manager takes care of - guess what? - the partitions on the disk. Ghost does both, the disk class driver's and the partition manager's tasks, which works fine on Windows XP. On Windows 7, however, this results in two drive letters being assigned to every single emulated device, so we don't report partitions in this case. Unfortunately, this leads to the system not being able to format the device.  
In the long run, we will delegate the handling of partitions to the system's partition manager, but for the moment we'll just work around the restriction by using preformatted images on Windows 7. 
  
Finally, the location of the image files that Ghost uses for emulation is no longer fixed. It is now possible to set a file name pattern via the registry value `HKLM\System\CurrentControlSet\Services\GhostDrive\Parameters\ImageFileName`. Upon receipt of a mount command, the driver reads the desired file name from the registry, so that changing the pattern takes immediate effect at the next mount operation. If more security is desired, the user can still choose a fixed file name and compile it into the driver.  
  
That's about it regarding the results of the first half of the summer of code. In the second half, we'll create a better user interface that facilitates configuration and installs the drivers when it is used for the first time, so that the manual install procedure is no longer necessary.
