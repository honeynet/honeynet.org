---
title: "nebula - Client library and revised signature segment selection"
authors: ["Tillmann Werner"]
date: "2009-06-08"
categories: 
  - "gsoc"
tags: 
  - "gsoc-d20"
  - "hpsoc-d78"
  - "nebula-d31"
---

[](/gsoc/project11 "HPSoc Project Description")![nebula Logo](images/nebula.png) [One project](/gsoc/project11 "HPSoc Project Description") mentored by the Honeynet Project during GSoC aims at improving [nebula](http://nebula.carnivore.it "nebula - An Intrusion Signature Generator"), an automated intrusion signature generator. There are two critical components in the signature generator: A clustering engine that groups similar attacks into classes, and a signature assembler that extracts common features and selects some of them for the actual signature.

  
  

The first work package's goal is to improve the overall signature quality. This can be achieved by tuning the core components, i.e. the clustering and the signature assembler. Further, nebula looses all states upon restart in its current version. The second goal is to make nebula state-aware and add the ability to save and load states.

  

I started working on improvements to the signature composition algorithm. The original routine simply selects entries from the list of all common substrings using a greedy strategy: It starts with the longest common substring, puts it in the signature, proceeds with the next-longest one, and so on. In case of a syntactical conflict (the current segment might overlap with a previous one if only the minimum and the maximum possible offset are evaluated) the substring is simply discarded. This obviously leaves room for optimization. The new routine follows basically the same principle, but it tries to solve conflicts by excluding some occurrences of the current segment. This is fine, as long as all input string are still contributing to the segment. Here is an example:

  

            \[segment c\]  
\[segment a\]                \[segment b\]  

  

In this situation segment a and segment b are already placed in the signature. Each segment is defined by the minimum offset and the maximum offset of the corresponding substring in the input strings. In the above example the intervals for a and c overlap - we have a conflict, and the original algorithm would skip c. But it might be possible to shrink the interval by removing the left-most offset. However, this offset corresponds to an occurrence of the corresponding substring in one of the inputs. We have to take care that each substring contributes at least one offset to the segment, otherwise it won't be a common substring anymore. If this can be guaranteed, the conflict can be solved and segment c can be inserted in the signature, wich obviously leads to much more accurate signatures:

  

\[segment a\]\[ment c\]    \[segment b\]  

  

While addressing the other part of work package 1 I realized that the effort is quite high. A lot of internal tracking is required to save and load overall states, like clusters, input hashes, signatures in all revisions etc. I have already implemented parts of it but I won't be able to finish it on time, so I decided to bring forward the second work package, the development of a nebula client library. Its code is already available in our [svn repository](http://svn.carnivore.it/browser/nebula/trunk/lib "nebula svn repository"). The [interface](http://svn.carnivore.it/browser/nebula/trunk/include/nebula.h "nebula svn repository") is quite simple, there is only a couple of functions, and I believe their usage is straight-forward. The repository contains a [simple command line client](http://svn.carnivore.it/browser/nebula/trunk/client "nebula svn repository") for submitting data to a nebula server that makes use of the library and can serve as an example (the [old client](http://svn.carnivore.it/browser/nebula/trunk/deprecated "nebula svn repository") is still available but considered obsolete).

  

What is next? I will keep working on state support and also already start with work package 3. It is going to be interesting to see how the snort plugin will work out.
