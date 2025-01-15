---
title: "Improve the security of unlocking your smartphone"
authors: ["Chengyu Song"]
date: "2011-02-07"
categories: 
  - "android"
tags: 
  - "smartphone"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

There is a [paper](https://www.usenix.org/events/woot10/tech/techAbstracts.html#Aviv) at WOOT 10' described how to use smudges on the touch sceen of a smartphone to get largely decrease the time an attacker need to guess the right password to unlock the screen. For example, by for 4 passcode based iPhone, one just need to try at most P(4,4) = 4! = 24 times before he get the right one.  

But I think this situation had happened on PC and we already have a solution. Long time ago, we have Trojan that steals the password. To combat with it, people invented virtual keyboard (like used by many online bank in China). But the attacker then upgraded their program to record the mouse coordinates so they still know which character you entered. Isn't this sounds familiar? Yes, these coordinates are just like the smudges you left on your screen! So what happened next? We have randomized virtual keyboard.  

By far I think everyone has the answer. Why couldn't we use randomized keyboard to unlock the screen? For iPhone, we could randomize the position of the keyboard and the position of the numbers, so what an attacker get? A screen full of smudges. This could also apply to Android, Google just need to add some features to the dots, like colors. So to unlock the screen, you need to link the dots in the right order, but every time the colors are randomly given.  

Will this be complete secure? No, of course not. As attackers can capture the screen when you click on the virtual keyboard, they can also capture how you unlock you phone, but this time, it will be much much harder.
