---
title: "Synchronous Communication between Kernel and User Space"
authors: ["Sebastian Poeplau"]
date: "2012-07-10"
tags: 
  - "ghost-d68"
---

In this post I'd like to describe some aspects of the communication between kernel and user mode in the Ghost USB honeypot. More specifically, I'll focus on how to realize blocking communication with the Windows Driver Frameworks (WDF).  
  
Ghost consists of a kernel-mode component that does the main work of emulating a USB flash drive and listening for attempts to write data to the device, and there is a user-mode component that allows the user to control the honeypot and to view the results. Now we want the (kernel-mode) driver to communicate any results to the (user-mode) frontend as soon as they're available. Unfortunately, there is no convenient way to call user-mode code from kernel space. So the frontend has to ask for the information.  
  
How can we do so? The most natural way for an application to call kernel-mode code is to use the interface exposed by NTDLL. However, there is no way to extend that interface, so this is not an option. Considering that we'd like to have a solution which is easy to implement, we're left with two possible ways:  

  
2. Read from a device.
  
4. Send I/O control codes (IOCTLs) to a device.
  

  
  
In either case, the kernel-mode component has to create a device. This is not a problem, because we create the virtual USB storage device anyway. But reading from this device in order to receive results turns out to be problematic, since the read function is already used to obtain data from the emulated storage device. Therefore, we chose to send IOCTLs back and forth.  
  
The standard way of doing so is to use the function `DeviceIoControl` from Kernel32.dll, which serves our purposes perfectly well. The function causes an I/O request packet (IRP) containing the control code to be sent to a specified device and receives the answer. By default, it blocks until IOCTL processing in the driver is finished. There is also a way to have it return immediately and invoke a callback when the results arrive, but we won't discuss this feature here.  
  
While the approach suits most of our needs, there is one thing we have to consider: We don't want to incur overhead by polling the kernel-mode component for results regularly. Instead, we'd like the IOCTL processing to be completed only if data is available. So let's now take a look at how this is achieved in kernel mode.  
  
Whenever a driver receives an IRP containing a device control code, a certain callback function for such control codes is called. The callback function then has to deal with the IOCTL and ultimately complete the request (meaning that some results are sent back to the originator). Obviously, if results are available already when our driver receives the IOCTL from the frontend, we can simply return the requested information. But how to proceed if no results have been produced yet?  
  
This is where the WDF comes in handy. It provides a concept of I/O queues, where each queue can have its own set of callback functions to process incoming requests. So if we receive a request from the frontend in the default queue and no information is available yet, we just requeue the request to a dedicated queue that is only used for such requests. If results become available at some later point in time, the driver checks whether there are any requests in the dedicated queue that it can process. It is even possible to search the queue and process requests out of order, so that we can answer those requests that we have results for and leave the others untouched for the moment.  
  
So using I/O queues provides us with a convenient way to delay requests within the driver until we have results to return. In the overall picture, this saves the user-mode frontend from the need to regularly poll the kernel-mode component for results. Instead, it can simply send a request, and the function that does so will only return when results are available.
