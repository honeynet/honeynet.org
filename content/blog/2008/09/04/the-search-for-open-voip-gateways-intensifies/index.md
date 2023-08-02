---
title: "The search for open VoIP gateways intensifies!"
authors: ["Sjur Usken"]
date: "2008-09-04"
---

Got several calls from customers today. Their end-customers were calling them telling that their phone is ringing in the middle of the night. When some of them answers, there is no one there. We do some traces on it from our VoIP platform but can not find anything, and concludes there is random SIP INVITES beeing sent directly to the adapter.  
  
This is a common way of searching for open VoIP gateways. They send a SIP INVITE with a real number that they control. If the SIP INVITE is making a successful call to this destination, the traffic suddenly increases after a while.  
  
We went through the setup with those customers and locked down this possibility,... luckily it had not been abused economically this time...
