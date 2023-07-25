---
title: "Thug Plugin Framework"
date: "2012-05-20"
tags: 
  - "thug-d25"
---

In the last months I spent a lot of efforts in Thug development. During these months a few interesting features and improvements were introduced but right now I want to spend some time for taking a look at the new plugin framework introduced in the version 0.3.0. If you ever thought about extending Thug with additional features but didn’t know how to do it you should really keep on reading. Let’s start by taking a look a the code.  
  
Taking a look at src/thug.py we can now read these lines of code  
  
  
`  
216 if p:  
217 ThugPlugins(PRE_ANALYSIS_PLUGINS, self)()  
218 p(args[0])  
219 ThugPlugins(POST_ANALYSIS_PLUGINS, self)()  
`  
  
  
Please note that every operation done by Thug is started by line 218 but now you can see that two hooks exist in order to execute plugins in a pre and post-analysis stage. Let’s keep exploring the source code and let’s take a look at src/Plugins/ThugPlugins.py  
  
  
`  
34 class ThugPlugins:  
35 phases = {  
36 PRE_ANALYSIS_PLUGINS : ‘ThugPluginsPre’,  
37 POST_ANALYSIS_PLUGINS : ‘ThugPluginsPost’  
38 }  
39  
40 def __init__(self, phase, thug):  
41 self.phase = phase  
42 self.thug = thug  
43 self.__init_config()  
44  
45 def __init_config(self):  
46 self.plugins = set()  
47 config = ConfigParser.ConfigParser()  
48  
49 conf_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ‘plugins.conf’)  
50 config.read(conf_file)  
51  
52 plugins = config.get(self.phases[self.phase], ‘plugins’)  
53 for plugin in plugins.split(‘,’):  
54 self.plugins.add(plugin.strip())  
55  
56 def __call__(self):  
57 self.run()  
58  
59 def run(self):  
60 for source in self.plugins:  
61 module = __import__(source)  
62 components = source.split(‘.’)  
63 for component in components[1:]:  
64 module = getattr(module, component)  
65  
66 handler = getattr(module, “Handler”, None)  
67 if handler:  
68 p = handler()  
69 try:  
70 verifyObject(IPlugin, p)  
71 p.run(self.thug, log)  
72 except BrokenImplementation as e:  
73 log.warning(“[%s] %s” % (source, e, ))  
`  
  
  
and src/Plugins/plugins.conf  
  
  
`  
1 [ThugPluginsPre]  
2 plugins: Plugins.TestPlugin  
3  
4 [ThugPluginsPost]  
5 plugins: Plugins.TestPlugin  
`  
  
  
The configuration file plugins.conf defines which plugins are to be loaded in pre and post-analysis stage (you can specify many plugins by simply comma separating them). The plugins should contain a class named Handler which should be conform to this interface  
  
  
`  
21 class IPlugin(zope.interface.Interface):  
22 def run(thug, log):  
23 “”"  
24 This method is called when the plugin is invoked  
25  
26 Parameters:  
27 @thug: Thug class main instance  
28 @log: Thug root logger  
29 “”"  
`  
  
  
If the interface is correctly implemented the \`run’ method is called with two parameters: the Thug class main instance and the Thug root logger. Let’s see a really simple example of plugin  
  
  
`  
20 import zope.interface  
21 from .IPlugin import IPlugin  
22  
23 class Handler:  
24 zope.interface.implements(IPlugin)  
25  
26 def run(self, thug, log):  
27 log.debug(thug)  
28 log.debug(log)  
`  
  
  
This plugin just logs the parameters but you can do whatever you want. Do you want to pre-check if the URL domain is within a blacklist? Just do it with a pre-analysis plugin. Do you want to extract and/or correlate information from the MAEC log files? Just do it with a post-analysis plugin. Simply staten… have fun!
