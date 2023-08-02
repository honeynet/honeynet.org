---
title: "Precall and Postcall"
authors: ["Chengyu Song"]
date: "2009-06-14"
categories: 
  - "analysis"
tags: 
  - "qebek-sebek-qemu-windows"
---

When using hooking technology to intercept system calls, there are two different places to collect information: before the original function is called (precall) and after the original function returns (postcall). For example, in Sebek Win32 client, when callback function OnZwReadFile is called, it first calls the original function s\_fnZwReadFile, after the original function returns, it checks whether the original call succeeds,  if does, it then calls the data collection function LogIfStdHandle:

  

   
status = s\_fnZwReadFile(FileHandle,   
    Event,   
    ApcRoutine,   
    ApcContext,   
    IoStatusBlock,   
    Buffer,   
    Length,   
    ByteOffset,   
    Key);  
  
if(status == STATUS\_SUCCESS)   
    LogIfStdHandle(FileHandle, Buffer, Length);  
  

  

If the hook is done under Windows, or any other operating systems, breaking at precall and postcall is equally difficult, because the callback function is directly insert into the calling chain. In QEMU, supporting precall is easy and such mechanism has already been added to Qebek.  However, since the callback function is executed outside the VM, a ret instruction won't naturally be trapped into the postcall procedure. As a result, I need to find another way. 

  

Because Qebek will check the target EIP every time EIP is about to change, the simplest way to support postcall is to add the return address to the check list. This idea has been used in Ether\[1\] and proved to be feasible. The following code is a demo on hooking NtReadFile in Qebek (the full version can be found in the public [svn](https://projects.honeynet.org/sebek/browser/virtualization/qebek/trunk) )

  

   
// NtReadFile pre call  
if(eip == NtReadFile)  
{  
	// get file handle, buffer & buffer size from stack  
	qebek\_read\_ulong(env, env->regs\[R\_ESP\] + 4, &ReadHandle);  
	qebek\_read\_ulong(env, env->regs\[R\_ESP\] + 4 \* 6, &ReadBuffer);  
	qebek\_read\_ulong(env, env->regs\[R\_ESP\] + 4 \* 7, &ReadSize);  
  
	// set return address, so the VM will break when returne

<script src="/modules/tinymce/tinymce/jscripts/tiny_mce/themes/advanced/langs/en.js" type="text/javascript"><!--mce:0--></script>

d  
	qebek\_read\_ulong(env, env->regs\[R\_ESP\], &NtReadFilePost);  
}  
// NtReadFile post call  
else if(eip == NtReadFilePost)  
{  
	qemu\_printf("ReadPost\\n");  
	// if succeed  
	if(env->regs\[R\_EAX\] == 0)  
		OnNtReadWriteFile(env, ReadHandle, ReadBuffer, ReadSize);  
  
	NtReadFilePost = 0; //clear the break point  
}  
  

  

This code works well as a demo, but has obviously drawbacks: 1) when the system calls required to be hooked increases, the performance penalty of if-else structure will be unacceptable; 2) if the system call is reenterable, the postcall break point will mess up; 3) if there is context swith during the system call, which is true according to the test, the collected informaiton will mess up.

  

  

So next week I'll mainly focus on improving the hook infrastucture.

  

  

\[1\] Dinaburg, A., Royal, P., Sharif, M., Lee, W.: Ether: malware analysis via hardware virtualization extensions. In: CCS '08: Proceedings of the 15th ACM Conference on Computer and Communications Security, New York, NY, USA, ACM (2008) 51-62.
