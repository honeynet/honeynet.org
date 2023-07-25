---
title: "Lion and iOS 5"
date: "2011-06-07"
tags: 
  - "security"
---

Today Apple unveiled the next generation of OS X, Lion and new iOS 5. Among the features, I'm concerned about two features: AriDrop and iCloud.  
  
My worry for AriDrop comes from its automatic discover ability. While services like Bonjour also has automatic discover ability, they are passive. On the contrary, AriDrop is active, allows user to send (drop) a file to another user. Sounds pretty convenient. But this just reminds the old Bluetooth worms. Although saving a file requires user's permission, the worm continually pings the victim for 'dropping' the file, and most users will then get annoyed and permit the saving. So without further restriction, I would say AirDrop opens a new door for worms. Cheers!  
  
Another concern is iCloud. As mentioned in [this paper](http://www5.rz.rub.de:8032/imperia/md/content/wolf/ieee_mobile.pdf) at Oakland '11, the old Hiptop/T-mobile attack may happen again. Apple has failed [once](http://news.cnet.com/8301-13579_3-20009658-37.html) on protecting user's account, and most user's are not good at choosing strong password. So this time they don't need to steal the top stars' phone to get those photos, they just need to get their user account and Apple will automatically push those photos to them.  
  
Hope this is just my paranoia. Good luck, Apple.
