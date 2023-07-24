---
title: "Something about python: __setattr__ and __getattr__"
date: "2009-06-03"
tags: 
  - "project"
---

It seems that there was some problems in this blog system, and i was busy with my final exam, so i haven't written blog a long time since the project starts.

  

But the work has been going on. I've been spent some time studying on the language faculty of javascript, and comparing it with python. Though this two are both scripting language, python is somehow much stronger. We'll see this from the differences between the setter/getter function and \_\_setattr\_\_/\_\_getattr\_\_ method in python.

  

First, let's see what's in javascript. Use the example from mozilla website:

  

  
  
  

  

o = {

  

a:7,

  

get b() { return this.a+1; },

  

set c(x) { this.a = x/2; }

  

};

  

o.c=8; alert(o.b);  

  

  

  

When we assign o.c=8, o.a will become 8/2=4, and o.b will returns o.a+1=5. This is easy to understand.

  

But such setter and getter function has its limits. It can only define on the member which its name is known to us, it will not intercept the visit to undefined members, which may troubles us. And the member which getter function is defined cannot be visited, not through any means possible.

  

Python can, however. The following passages are extracted from python 2.6.2 documentation:  
  
object.\_\_getattr\_\_(self, name)  
  
    Called when an attribute lookup has not found the attribute in the usual places (i.e. it is not an instance attribute nor is it found in the class tree for self). name is the attribute name. This method should return the (computed) attribute value or raise an AttributeError exception.  
  
object.\_\_setattr\_\_(self, name, value)  
  
    Called when an attribute assignment is attempted. This is called instead of the normal mechanism (i.e. store the value in the instance dictionary). name is the attribute name, value is the value to be assigned to it.  
  
So, we can write our code like this:  
  
class DOMObject(object):  
    ......  
    def \_\_setattr\_\_(self, name, val):  
        if name == 'src': #do something  
        self.\_\_dict\_\_\[name\]=val # this will assign the real object.name, despite \_\_setattr\_\_  
    def \_\_getattr\_\_(self, name):  
        return None  
  
It means that when the src of a DOM object is assigned, do something (output for analyzation, for example), and when visit a member of the object that doesn't exist, returns null instead of raise an error (this is what javascript do, but not what python do normally).  
  
We can use this two methods to do more, such as use window as global object (it really troubles us a long time). We will update a blog about this soon.
