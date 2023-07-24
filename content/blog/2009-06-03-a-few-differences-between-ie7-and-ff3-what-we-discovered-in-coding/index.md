---
title: "A few differences between IE7 and FF3, what we discovered in coding"
date: "2009-06-03"
tags: 
  - "project"
---

There are of course more of them, but we only list which will bring  
confusion to our code. Note that the current version is based on IE,  
not FF, since its more vulnerable.

  

I don't know how to write HTML in this blog, so i hope i can make them clear without examples.

  

1\. Both in IE and FF, we can use the ID of a DOM object to call it. But we cannot always use 'document.id' to call it. In FF, document.f (f is id of a form) is undefined, but in IE, document.i (i is id of an image) and some other DOMs is undefined.

  

2\. In FF, the assignment of innerHTML of a script object (s.innerHTML='alert(123)') will be executed, while in IE, such assignment is illegal.

  

3\. In FF, visit 's.src' while s is a script will return the absolute path: 'http://....../xxx.js', while in IE only return the relative path.

  

4\. Let b be the body object or other DOM object which has the attribute 'className'. But in a tag, we must write "body class='c'" instead of className='c'. It will be transformed into 'className' automatically. But in the method 'setAttribute', there is difference between IE and FF:

  

  
Note that the attribute 'class' in tag will be  
automatically transformed into 'className'. In FF, b.setAttribute('class', 'newclassname') will set b.className, while in IE, it is b.setAttribute('className', 'newclassname') will set it.

  

5\. Both in FF and IE, the onload method of a DOM object other than form and image will not be executed. But if we do define an onload method in the tag of other DOM object, we can 'alert(o.onload)' to see the difference: in FF it's a function, but in IE it's a string.

  

6\. In FF, body's onclick method is window.onclick, while in IE it is document.body.onclick.

  

These are for now. We'll update a blog if we find more.
