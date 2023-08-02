---
title: "PHoneyC DOM Emulation – Browser Personality"
authors: ["Angelo Dellaera"]
date: "2010-08-22"
tags: 
  - "phoneyc-d89"
---

A new improvement in PHoneyC DOM emulation code was committed in SVN [r1624](http://code.google.com/p/phoneyc/source/detail?r=1624). The idea is to better emulate the DOM behaviour depending on the selected browser personality. Let's take a look at the code starting from the personalities definition in _config.py_.  
  
`  
39 UserAgents = [  
40 (1,  
41 "Internet Explorer 6.0 (Windows 2000)",  
42 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",  
43 "Mozilla",  
44 "Microsoft Internet Explorer",  
45 "4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",  
46 "ie60",  
47 ),  
48 (2,  
49 "Internet Explorer 6.1 (Windows XP)",  
50 "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",  
51 "Mozilla",  
52 "Microsoft Internet Explorer",  
53 "4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",  
54 "ie61",  
55 ),  
56 (3,  
57 "Internet Explorer 7.0 (Windows XP)",  
58 "Mozilla/4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",  
59 "Mozilla",  
60 "Microsoft Internet Explorer",  
61 "4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",  
62 "ie70",  
63 ),  
64 (4,  
65 "Internet Explorer 8.0 (Windows XP)",  
66 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; (R1 1.5); .NET CLR 1.1.4322; .NET CLR 2.0.50727)",  
67 "Mozilla",  
68 "Microsoft Internet Explorer",  
69 "4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; (R1 1.5); .NET CLR 1.1.4322; .NET CLR 2.0.50727)",  
70 "ie80",  
71 ),  
72 ]  
`  
  
It's important to realize that each personality was added a tag (i.e. _ie80_). Taking a look at _DOM/Window.py_ the following code can be seen.  
  
`  
229 def __init_methods(self):  
230 for attr in dir(self):  
231 prefix = "_Window__window_%s_" % (config.browserTag, )  
232 if attr.startswith(prefix):  
233 p = attr.split(prefix)[1]  
234 self.__dict__['__cx'].add_global(p, getattr(self, attr))  
235 self.__dict__['__cx'].execute("window.%s = %s;" % (p, p, ))  
`  
  
Let's consider an example and assume the Internet Explorer 8.0 personality was selected. It's easy to realize that the prefix would assume the value _\_Window\_\_window\_ie80\__. A few simple wrappers were created, one per personality, to each method as shown in the following code.  
  
`  
340 def __window_back(self):  
341 """  
342 Returns the window to the previous item in the history.  
343 Syntax  
344  
345 window.back()  
346  
347 Parameters  
348  
349 None.  
350 """  
351 pass  
352  
353 def __window_ie60_back(self):  
354 self.__window_back()  
355  
356 def __window_ie61_back(self):  
357 self.__window_back()  
358  
359 def __window_ie70_back(self):  
360 self.__window_back()  
361  
362 def __window_ie80_back(self):  
363 self.__window_back()  
364  
365 def __window_firefox_back(self):  
366 self.__window_back()  
`  
  
This is a quite simple situation but what if you want to define _addEventListener_ method just for Firefox personalities and _attachEvent_ just for Internet Explorer ones? Really simple to do!  
  
`  
1191 def __window_attachEvent(self, sEvent, fpNotify):  
1192 if dataetc.isevent(sEvent, 'window'):  
1193 self.__dict__[sEvent] = fpNotify  
1194  
1195 def __window_ie60_attachEvent(self, sEvent, fpNotify):  
1196 self.__window_attachEvent(sEvent, fpNotify)  
1197  
1198 def __window_ie61_attachEvent(self, sEvent, fpNotify):  
1199 self.__window_attachEvent(sEvent, fpNotify)  
1200  
1201 def __window_ie70_attachEvent(self, sEvent, fpNotify):  
1202 self.__window_attachEvent(sEvent, fpNotify)  
1203  
1204 def __window_ie80_attachEvent(self, sEvent, fpNotify):  
1205 self.__window_attachEvent(sEvent, fpNotify)  
1206  
1207  
1208 def __window_detachEvent(self, sEvent, fpNotify):  
1209 if sEvent in self.__dict__ and self.__dict__[sEvent] == fpNotify:  
1210 del self.__dict__[sEvent]  
1211  
1212 def __window_ie60_detachEvent(self, sEvent, fpNotify):  
1213 self.__window_detachEvent(sEvent, fpNotify)  
1214  
1215 def __window_ie61_detachEvent(self, sEvent, fpNotify):  
1216 self.__window_detachEvent(sEvent, fpNotify)  
1217  
1218 def __window_ie70_detachEvent(self, sEvent, fpNotify):  
1219 self.__window_detachEvent(sEvent, fpNotify)  
1220  
1221 def __window_ie80_detachEvent(self, sEvent, fpNotify):  
1222 self.__window_detachEvent(sEvent, fpNotify)  
1223  
1224  
1225 def __window_addEventListener(self, type, listener, useCapture = False):  
1226 if dataetc.isevent(type, 'window'):  
1227 self.__dict__[type] = listener  
1228  
1229 def __window_firefox_addEventListener(self, type, listener, useCapture = False):  
1230 self.__window_addEventListener(type, listener, useCapture = False)  
1231  
1232  
1233 def __window_removeEventListener(self, type, listener, useCapture = False):  
1234 if type in self.__dict__ and self.__dict__[type] == listener:  
1235 del self.__dict__[type]  
1236  
1237 def __window_firefox_removeEventListener(self, type, listener, useCapture = False):  
1238 self.__window_removeEventListener(type, listener, useCapture = False)  
`  
  
Moreover this approach could allow to insert specific code within the wrappers if needed while implementing the method functionalities in the higher level _\_\_window\_<method\_name>_ wrapper.
