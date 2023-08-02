---
title: "Parser Redux and Libraries"
authors: ["Kevin Galloway"]
date: "2009-06-21"
coverImage: "parser.png"
---

I know I said that I would post a screenshot a week ago, but it's been a little busy, but here's an older attached image. One of the reasons there was a delay is that the code that I was using was based on one of the wxPython demo programs, hence the RunDemo title bar. I'm in the process of revamping that code into something that's a little more standalone.  
  
At the moment I've decided to have the parser program separate from the imaging one. Given enough time, I would like for the parser section to be modular, that is, the user can specify what parser to use to generate a file that can be used by my visualizer. I plan on the visualizer to be fairly robust, with multiple visualization options, some people time graphs, as well as a few other methods, so hopefully the user can find one that's useful. One consideration that I have though, is the number of libraries that the visualizer will need. The parser for example uses python regex as well as wxPython. The visualizer, as currently envisioned will be written in C++ using OpenGL as most of my graphical programming experience is in that. However I know wxPython can handle some drawings, and there are a few other other libraries for graphical things in Python. The main fear that I have is library bloat, a user will need, so far at least, to download wxPython, Python if they don't really use that, followed by the OpenGL library as well as most likely some sort of regex library for the visualizer to read in the data. I don't like this library bloat, so I might try to see what sort of things Python can handle, if I can keep it all within Python I would be a lot happier.
