---
title: "Open Source Licensing Madness"
authors: ["Sebastian Poeplau"]
date: "2012-06-25"
tags: 
  - "ghost-d68"
---

Before we released the [Ghost USB honeypot](http://code.google.com/p/ghost-usb-honeypot/) as open source software, we had quite some trouble to apply the GPL to our case. Since there wasn't much information available for the very particular case of using the GPL for a Windows driver, I'll discuss our issues and solutions in this article. This might not directly be applicable to other software, but it should provide the reader with general insights and will hopefully help people to sort out similar problems in the future.  
  
When we first published Ghost, our intention was to release the software under a license that allowed everyone to benefit from it free of charge. Also, the source code should be available as a reference and to allow for custom modifications. However, we wanted all development to be public, i.e. especially modified versions were to be released as open source software too.  
  
The first license that springs to mind in such a context is the [GNU General Public License (GPL)](http://www.gnu.org/copyleft/gpl.html) as provided by the Free Software Foundation (FSF). At its core lies the principle of copyleft: Everything is freely available, but any modified version ("Derived Work" in the GPL's language) has to be released under similar terms. Many well-known open source projects use the GPL for their software. Most prominently, the Linux kernel is licensed under GPLv2, as is a great amount of applications for Linux and other Unix systems.  
  
The GPL was a promising option, and we started to dive deeper into the subtleties of legal phrasing. An important prerequisite for publication under any license is the agreement of all copyright owners. Luckily, the copyright for Ghost belongs to a single person, so there was no need for further discussion there.  
  
However, the particular notion of copyleft and its phrasing in the GPL turned out to contain some obstacles for our project: If you distribute GPL-licensed software in binary form, then the GPL requires you to provide the so-called Corresponding Source as well. Basically, this is all the source code necessary to reproduce the binaries. Of course, freely available source code was exactly what we wanted, and at a first glance, it looked as if there was nothing wrong here. But unfortunately, things are not that simple when it comes to legally accurate texts...  
  
Imagine you've written a simple command-line tool and want publish it under the GPL. If it's written in C, then probably it uses printf and some other C standard library functions. In other languages, the situation may differ slightly, but it always boils down to your software using some standard functionality that is provided by the system. So let's stick to C for this example. Suppose you publish a binary version of your tool - then copyleft in theory requires you to publish all source code that is needed to reproduce the binary. Unfortunately, your binary is linked against the C standard library. Does that mean you have to make the standard library's source code available with your application's sources? Luckily, the answer is no: The GPL contains the so-called system library exception, which says that you don't have to provide source code for system libraries (we'll come back to the question what a system library actually is).  
  
Back to our concrete case: Ghost uses the Windows Driver Frameworks (WDF) by Microsoft, which basically introduces an abstraction layer on top of the Windows Driver Model (WDM) and thereby facilitates driver programming significantly when it comes to plug and play and power management. The library is available free of charge, but the source code is not public. Starting with Windows Vista, the WDF even comes preinstalled with the operating system.  
  
Now the question is whether or not the WDF qualifies as a System Library in the GPL's language. Why is that important at all? Well, if it wasn't a System Library and you chose to publish a binary version of Ghost, then the GPL would require you to provide the WDF's source code. Obviously, you couldn't comply with Ghost's license in that case (unless you're Microsoft, which doesn't apply to many readers).  
  
So what's a System Library? The GPL puts two requirements on a library in order for it to be a System Library.  

  
2. It has to be shipped with the operating system, compiler or interpreter (a "Major Component" in the GPL's language).
  
4. It has to meet one of the following two requirements.  
      
    2. Its only purpose is that of mediating between your application and the operating system, compiler, etc. For example, NTDLL provides your application with an interface to the operating system‘s functionality on Windows systems.
      
    4. It's an implementation of a widely used or standardized interface for which an open source implementation is available (which probably means that any closed source implementation of the C standard library qualifies as a System Library, since there are open source alternatives available).
      
    

  
  
Does this make the WDF a System Library? Briefly, we don't know for sure. As mentioned above, the WDF is shipped with the operating system starting with Windows Vista, so we meet condition 1 for those systems. But what about XP? And do we meet condition 2 at all? We didn't find clear answers to that. Fortunately, there's a clean way around the question: The GPL allows you to add exceptions to the copyleft. More specifically, one may add permission to link the licensed software against certain libraries under GPL-incompatible licenses (the FSF provides a [text template](http://www.gnu.org/licenses/gpl-faq.html#GPLIncompatibleLibs) for this). This is what we did in the end - we granted everyone permission to provide binaries of Ghost that are linked against the WDF (governed by Microsoft's license terms) without the need to ship source code for that particular library.  
  
When we thought we had finally settled the matter, yet another question came up. Ghost does not only link against the WDF, but also against the Windows kernel, as does every full Windows driver. Is this GPL-compliant? We think it is, because the kernel is obviously included in the operating system (condition 1), and with ReactOS there is an open source implementation of the interface that it exposes to drivers (condition 2.2). As a side note, I'd like to add that the developers of other open source drivers I know of must either have come to the same conclusion or just don't care, since I've never seen exceptional permission to link against the Windows kernel in any such driver's license...  
  
Finally, we were ready to publish Ghost under GPLv3 with some exceptional permission. The question that remains: Why is all this so complicated? Well, the GPL was written for software that works in a domain where everything is open source. Things become complicated quite naturally when proprietary software comes into play - but how would you avoid this if you wrote security software for a non-GPL operating system?  
  
Let me add a final remark: License violations can only be pursued by the copyright owners. Therefore, the considerations in this article don't directly affect you as a software author, since you probably wouldn't sue yourself for violating the license. Nevertheless, it's important to sort out the above issues, because releasing software as open source means that everybody is allowed to modify it and publish the modifications. If they can't do so for fear of violating your license, then how could one call your software open?  
  
_Disclaimer: I'm not a lawyer, so this article cannot be viewed as legal advice of any kind. I simplified several concepts for the sake of readability, which means that the text is not to be seen as a legally accurate document._
