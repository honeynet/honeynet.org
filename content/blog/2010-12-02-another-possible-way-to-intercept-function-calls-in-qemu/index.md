---
title: "Another possible way to intercept function calls in QEMU"
date: "2010-12-02"
categories: 
  - "android"
tags: 
  - "qemu-hook"
---

I'm developing a syscall interception tool for Android as a course's project. While it is relatively simple to intercept calling into the system services (introduced at the end), it is harder to get the syscall return. The reason is, the latest Android emulator is build upon QEMU 0.10.50, meaning it's TCG based. So we cannot use the same way Qebek or TEMU uses to intercept the syscall return. Therefore I looked into the new code to find if I could find a way to solve this problem.  
  
Generally, in my understanding, in the old QEMU, the code translation is done as:  
**guest code -> host code snippet (or template?) -> compiled by gcc-3.4 -> translated code**  
  
So basically what Qebek does is modifying the snippet for `op_jmp_T0`, hence the translated code for 'call' instruction will include the `qebek_check_target` logic.  
  
But after moving to TCG, the translation is done as (see [QEMU internals](http://lugatgt.org/content/qemu_internals/downloads/slides.pdf)):  
**guest code -> Frontends -> TCG intermediate code -> Backends -> translated code**  
  
In this case, if we want to use the similar mechanism, we could either modify the Frontends to add the interception logic using TCG operations, or modify the Backends to emit the interception logic as host assembly code. Either way may requires a lot of effort because we now need to manually finish the task that is previously done by gcc-3.4. 
  
Although it may be possible to first compile the interception code then added it to the code cache of QEMU, I think there is a more elegant way which does not care what translation mechanism is used as long as we only cares control flow from basic block to basic block, such as function calls. Yes, as many of you may guess, we could modify the `cpu_exec` function so before a translated basic block is about to be executed, we could check the `pc` register to see if this basic block is what we are interested. The only problem is my mind now is to prevent QEMU from linking interested basic blocks to the end of other basic blocks, or fully disables this optimization.  
  
Anyway, I have an exam tomorrow so I haven't tested if this works or not. I will update the status once I get some time to do some experiments. If succeeds, maybe we could also port Qebek to newer QEMU versions.  
  
_Intercept ARM syscall_  
Syscall on ARM is done through `swi` instruction. In old ABI, the syscall number is encoded as part of the instruction, but in newer EABI, the syscall number is in `reg7`. So the interception is very easy: just add something to the `EXCP_SWI` handler in `do_interrupt function` in `target-arm/helper.c` (`do_interrupt` is never translated).
