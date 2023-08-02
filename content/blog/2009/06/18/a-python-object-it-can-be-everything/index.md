---
title: "A python object: It can be everything!"
authors: ["Geng Wang"]
date: "2009-06-18"
tags: 
  - "project"
---

The code is like this:

  

class unknown\_obj(object):

  

    def \_\_call\_\_(self, \*arg): return unknown\_obj()

  

    def \_\_getitem\_\_(self, key): return unknown\_obj()

  

    def \_\_getattr\_\_(self, name): return unknown\_obj()

  

  

The three methods are: \_\_call\_\_ for function calls (\*arg means arg is the argument list), \_\_getitem\_\_ for the visit to members using '\[\]', such as a\[3\] and 3 is the key, \_\_getattr\_\_ just like we mentioned, for any visit to members using '.'. So almost every kind of codes is legal to an object like this. For example:

  

\>>>a = unknown\_obj()

  

\>>>print a.b\[123\].c\['abc'\].d(456, 'def').e

  

<\_\_main\_\_.unknown\_obj object at 0xb76b552c>

  

If we want to know exactly which member is called, we can modify the code above, like this:

  

  

class unknown\_obj(object):

  

    def \_\_call\_\_(self, \*arg):

  

        print arg

  

        return unknown\_obj()

  

    def \_\_getitem\_\_(self, key):

  

        print key

  

        return unknown\_obj()

  

    def \_\_getattr\_\_(self, name):

  

        print name

  

        return unknown\_obj()

  

  

\>>>a = unknown\_obj()

  

\>>>print a.b\[123\].c\['abc'\].d(456, 'def').e

  

b

  

123

  

c

  

abc

  

d

  

(456, 'def')

  

e

  

<\_\_main\_\_.unknown\_obj object at 0xb76b564c>

  

  

Such an object can be used for a COM simulation, so we don't need to implement everything for every kinds of COM, and a call to a function can be output for further analyze.
