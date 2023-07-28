---
title: "Capture BAT"
---

Capture BAT is a behavioral analysis tool of applications for the Win32 operating system family. Capture BAT is able to monitor the state of a system during the execution of applications and processing of documents, which provides an analyst with insights on how the software operates even if no source code is available. Capture BAT monitors state changes on a low kernel level and can easily be used across various Win32 operating system versions and configurations.

* * *

_Since the old NZ site is dead, I am adding the Capture-BAT binary and source for download here. Please refer to the paper [Capture - A Behavioral Analysis Tool for Applications and Documents](http://www2.honeynet.org/wp-content/uploads/attachments/p23-seifert.pdf) for more details on the tool**.**_

* * *

## Summary

Capture BAT provides a powerful mechanism to exclude event noise that naturally occurs on an idle system or when using a specific application. This mechanism is fine-grained and allows an analyst to take into account the process that cause the various state changes. As a result, this mechanism even allows Capture to analyze the behavior of documents that execute within the context of an application, for example the behavior of a malicious Microsoft Word document.

 

## **Prerequisites**

- Capture BAT requires a certain service pack patch level on the Windows system it is suppose to run on. For Microsoft Windows 2000, it requires service pack 4; for Microsoft Windows XP, it requires service pack 2; and for Microsoft Vista no service pack is needed.
- Further, Capture BAT requires that the Microsoft Visual C++ 2005 Redistributable Package is installed.
- Finally, if the network dump functionality is used, Capture BAT requires the WinPcap 4.0.1 libraries.

 

## **Installation**

Download Capture BAT setup file and execute it. The application will be installed into C:\\\\program files\\\\capture. Note that a reboot will be forced by the setup program.

- [CaptureBAT-Setup-2.0.0-5574.exe](https://www.honeynet.org/files/CaptureBAT-Setup-2.0.0-5574.exe) MD5: c1894e46ffe89be6ca35729d9dab6145[](http://www.mcs.vuw.ac.nz/~cseifert/Capture-BAT/CaptureBAT-Setup-2.0.0-5574.exe)

- [CaptureBAT-Setup-2.0.0-5574-src.zip](http://www2.honeynet.org/wp-content/uploads/attachments/CaptureBAT-Setup-2.0.0-5574-src.zip) MD5: 0086e7c01e481992284092ea0f9de20f
