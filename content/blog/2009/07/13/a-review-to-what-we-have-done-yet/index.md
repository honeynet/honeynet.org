---
title: "A review to what we have done yet"
authors: ["Geng Wang"]
date: "2009-07-13"
tags: 
  - "project"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

Our work mainly focuses on DOM simulation. I believe the following is the most important for deobfuscation, but we also do lot more so that our program can handle normal web pages. We will not list them here.

  

Our code can be found at:

  

http://code.google.com/p/phoneyc/source/browse/phoneyc#phoneyc/branches/phoneyc\_wanggeng

  

1\. DOM tree generation.

  

We defined a class 'DOMObject' in python, it has a list 'children' as its member. We use SGMLParser to parse the html document and create a DOMObject when met a start tag. And the DOM tree can be output for further analysis.

  

2\. document.write

  

Each time the function document.write is called, its argument will be passed into a new parser to handle. This parser is linked with the script object, so it is able to handle special cases such as a tag split into several parts and written by document.write several times, or the written text itself contains a document.write.

  

3\. innerHTML

  

When change a DOMObject's innerHTML, the html text will be changed, and the new innerHTML will be parsed.

  

4\. Cross-site

  

The source file of an iframe object will be downloaded and parsed. Additionally, when document.location is changed, it will also download html document from the new location and parse it.

  

5\. unknownObject

  

An object tag (COM) will be considered as an unknownObject. Call its method or change its attribute will output a message for further analysis.
