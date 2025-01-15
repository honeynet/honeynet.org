---
title: "PHoneyC DOM Emulation - Window"
authors: ["Angelo Dellaera"]
date: "2010-08-10"
tags: 
  - "phoneyc"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

A few weeks ago I started reviewing the PHoneyC DOM emulation code and realized it was turning to be hard to maintain and debug due to a huge amount of undocumented (and sometimes awful) hacks. For this reason I decided it was time to patch (and sometimes rewrite from scratch) such code. These posts will describe how the new DOM emulation code will work. The patch is not available right now since I'm testing the code but plans exists to commit it in the [PHoneyC SVN](http://code.google.com/p/phoneyc/) in the next days.  
  
In this first post we will take a look at the Window object in DOM/Window.py. During object inizialization, the following code is executed.  
  
`  
  
156 def __init_context(self):  
157 """  
158 Spidermonkey Context initialization.  
159 """  
160 document = Document(self)  
161 self.__dict__['__cx'] = self.__dict__['__rt'].new_context(alertlist = [])  
162 self.__dict__['__sl'] = []  
163 self.__dict__['__fl'] = [document]  
164  
165 self.__init_properties(document)  
166 self.__init_methods()  
167 self.__finalize_context()  
  
`  
  
Let's go into further details. First of all Window object properties are initialized through the \_\_init\_properties method.  
  
`  
181 def __init_properties(self, document):  
182 self.__dict__['__cx'].add_global('window', self)  
183 self.__dict__['__cx'].add_global('self' , self)  
184 self.__dict__['__cx'].execute("window.window = window;")  
185  
186 self.__dict__['__cx'].add_global('document', document)  
187 self.__dict__['__cx'].execute("window.document = document;")  
188  
189 self.__dict__['__cx'].add_global('location', document.location)  
190 self.__dict__['__cx'].execute("window.location = location;")  
191  
192 self.__dict__['__cx'].add_global("ActiveXObject", ActiveXObject)  
193  
194 self.__dict__['__cx'].add_global("navigator", Navigator())  
195 self.__dict__['__cx'].execute("window.navigator = navigator;")  
196  
197 self.__dict__['__cx'].add_global("screen", unknown())  
198 self.__dict__['__cx'].execute("window.screen = screen;")  
199  
200 if 'top_window' in self.__dict__['__root'].__dict__:  
201 if self.__dict__['__referrer']:  
202 top = self.__dict__['__referrer']  
203 else:  
204 top = self.__dict__['__root'].top_window  
205 else:  
206 top = self  
207  
208 self.__dict__['__cx'].add_global("top", top)  
209 self.__dict__['__cx'].execute("window.top = top;")  
210  
211 self.__dict__['__cx'].add_global("parent", top)  
212 self.__dict__['__cx'].execute("window.parent = parent;")  
213  
214 self.__dict__['__cx'].add_global("history", History(document))  
215 self.__dict__['__cx'].execute("window.history = history;")  
216  
217 self.__dict__['__cx'].execute("window.innerWidth = 400;")  
218 self.__dict__['__cx'].execute("window.innerHeight = 200;")  
219  
220 self.__init_undefined_properties()  
221  
222 def __init_undefined_properties(self):  
223 properties = ('external', 'opera', )  
224  
225 for prop in properties:  
226 self.__dict__['__cx'].execute("window.%s = undefined;" % (prop, ))  
`  
  
The code should be straightforward to understand. The idea beyond it is really simple. Simply stated this code allows Python objects' variables and methods to be accessible from JS. Let's move to most interesting stuff. Following the \_\_init\_methods method is called.  
  
`  
228 def __init_methods(self):  
229 for attr in dir(self):  
230 if attr.startswith('_Window__window'):  
231 p = attr.split('_Window__window_')[1]  
232 self.__dict__['__cx'].add_global(p, getattr(self, attr))  
233 self.__dict__['__cx'].execute("window.%s = %s;" % (p, p, ))  
`  
  
Not so easy to understand? Let's take a look to the definition of a method.  
  
`  
322 def __window_back(self):  
323 """  
324 Returns the window to the previous item in the history.  
325 Syntax  
326  
327 window.back()  
328  
329 Parameters  
330  
331 None.  
332 """  
333 pass  
`  
  
This is a private class method since its name starts with \_\_. "If you try to call a private method, Python will raise a slightly misleading exception, saying that the method does not exist. Of course it does exist, but it's private, so it's not accessible outside the class. Strictly speaking, private methods are accessible outside their class, just not easily accessible. Nothing in Python is truly private; internally, the names of private methods and attributes are mangled and unmangled on the fly to make them seem inaccessible by their given names." (taken from [Dive Into Python](http://diveintopython.org)).  
  
We can access the \_\_window\_back method of the Window class by the name \_Window\_\_window\_back. This is the black magic \_\_init\_methods use for initializing methods. It's quite easy to realize that adding a new method is really easy. All you need is to simply define a method named _\_\_window\__ and match the signature of such method. How to emulate such method it's up to you but a simple _pass_ could do the trick.  
  
The last step happens in \_\_finalize\_context method.  
  
`  
169 def __finalize_context(self):  
170 self.__dict__['__cx'].execute("Event = function(){}")  
171 self.__dict__['__cx'].execute("function CollectGarbage() {};")  
172 self.__dict__['__cx'].execute("function quit() {};")  
173 self.__dict__['__cx'].execute("function prompt() {};")  
174  
175 for clsname in dataetc.classlist:  
176 inits = {'window' : self,  
177 'tagName': dataetc.classtotag(clsname),  
178 'parser' : None}  
179 self.__dict__['__cx'].add_global(clsname, DOMObjectFactory(clsname, inits))  
`  
  
The most interesting code is in lines 175-179. First of all let's take a look at the DOMObjectFactory code (DOM/ClassFactory.py) which is a genuine Python hack.  
  
`  
3 class DynamicDOMObject(DOMObject):  
4 def __init__(self):  
5 self.__dict__.update(self.inits)  
6 DOMObject.__init__(self, self.window, self.tagName, self.parser)  
7  
8 def DOMObjectFactory(name, initializers):  
9 return type(name, (DynamicDOMObject,), {'inits' : initializers})  
`  
  
After reading Python documentation it should be easy to understand how this code works and how it's able to dynamically add new DOM objects to the context.  
  
**type**(_name_, _bases_, _dict_)  
  
_Return a new type object. This is essentially a dynamic form of the class statement. The name string is the class name and becomes the \_\_name\_\_ attribute; the bases tuple itemizes the base classes and becomes the \_\_bases\_\_ attribute; and the dict dictionary is the namespace containing definitions for class body and becomes the \_\_dict\_\_ attribute. For example, the following two statements create identical type objects:  
\>>> class X(object):  
... a = 1  
...  
\>>> X = type('X', (object,), dict(a=1))  
_  
  
What about the Window event handlers? They are handled with a different mechanism which can be fully understood just by analyzing how the new DOM emulation code preparses the pages deferring code execution until the last possible moment. I'll analyze such feature in a future post in greater detail. Right now what you have to know is that if the handler for the event is set, the Window attribute _on<event>_ is set and contains the handler code. Once you understand it, the following code in DOM/DOM.py used for event handling should be easy to understand.  
  
`  
171 def get_event_func(self, name, f):  
172 begin = str(f).index('{') + 1  
173 s = str(f)[begin:].split('}')  
174 script = '}'.join(s[:-1]) + s[-1]  
175 return script  
176  
177 def event_handler(self, window, name, f):  
178 if name in window.__dict__:  
179 try:  
180 script = self.get_event_func(name, f)  
181 window.__dict__['__cx'].execute(script)  
182 except:  
183 #print str(f)  
184 traceback.print_exc()  
185 pass  
186  
187 def handle_events(self, window):  
188 window.__dict__['__warning'] = False  
189 self.event_handler(window, 'onabort' , window.onabort)  
190 self.event_handler(window, 'onbeforeunload' , window.onbeforeunload)  
191 self.event_handler(window, 'onblur' , window.onblur)  
192 self.event_handler(window, 'onchange' , window.onchange)  
193 self.event_handler(window, 'onclick' , window.onclick)  
194 self.event_handler(window, 'onclose' , window.onclose)  
195 self.event_handler(window, 'oncontextmenu' , window.oncontextmenu)  
196 self.event_handler(window, 'ondragdrop' , window.ondragdrop)  
197 self.event_handler(window, 'onerror' , window.onerror)  
198 self.event_handler(window, 'onfocus' , window.onfocus)  
199 self.event_handler(window, 'onhashchange' , window.hashchange)  
200 self.event_handler(window, 'onkeydown' , window.onkeydown)  
201 self.event_handler(window, 'onkeypress' , window.onkeypress)  
202 self.event_handler(window, 'onkeyup' , window.onkeyup)  
203 self.event_handler(window, 'onload' , window.onload)  
204 self.event_handler(window, 'onmousedown' , window.onmousedown)  
205 self.event_handler(window, 'onmousemove' , window.onmousemove)  
206 self.event_handler(window, 'onmouseout' , window.onmouseout)  
207 self.event_handler(window, 'onmouseover' , window.onmouseover)  
208 self.event_handler(window, 'onmouseup' , window.onmouseup)  
209 self.event_handler(window, 'onmozorientation', window.onmozorientation)  
210 self.event_handler(window, 'onpaint' , window.onpaint)  
211 self.event_handler(window, 'onpopstate' , window.onpopstate)  
212 self.event_handler(window, 'onreset' , window.onreset)  
213 self.event_handler(window, 'onresize' , window.onresize)  
214 self.event_handler(window, 'onscroll' , window.onscroll)  
215 self.event_handler(window, 'onselect' , window.onselect)  
216 self.event_handler(window, 'onsubmit' , window.onsubmit)  
217 self.event_handler(window, 'onunload' , window.onunload)  
218 self.event_handler(window, 'onpageshow' , window.onpageshow)  
219 self.event_handler(window, 'onpagehide' , window.onpagehide)  
220 window.__dict__['__warning'] = True  
`  
  
([Original post](http://buffer.antifork.org/blog/2010/08/10/phoneyc-dom-emulation-window/))
