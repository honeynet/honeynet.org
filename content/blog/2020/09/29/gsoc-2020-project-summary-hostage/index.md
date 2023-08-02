---
title: "GSOC 2020 PROJECT SUMMARY: HosTaGe"
authors: ["Irini Lygerou"]
date: "2020-09-29"
categories: 
  - "gsoc"
  - "honeypot"
tags: 
  - "honeypot"
  - "mobile"
  - "mobile-hostage"
coverImage: "screen-7.jpg"
---

## HosTaGe: a mobile honeypot

### Why I choose this project

I am passionate about Network Security, Cybersecurity, and programming, and I wanted to get involved with a project that includes it all.  
  
**HosTaGe** project drew my attention because I found it really fascinating the idea that any android device can be turned into a honeypot and be transformed into an essential tool for attack detection.  
  
I wanted to work on this project because it allowed me to improve this new generation of mobile honeypots and consequently improve the security of the internet in general.

### Project Overview

**HosTaGe** is a low interaction mobile honeypot for Android devices. The idea is to have a fast, on-the-go honeypot that emulates most modern protocols. Hostage is already mature, and this project will  
be focusing on its improvement (e.g., IoT protocol support, visualizations, security features, etc.).

**Source code of this project can be found [here](https://github.com/aau-network-security/HosTaGe).**

### What did you do for the project, briefly? (TL;DR)

I simulated 3 new IoT Protocols (**MQTT, AMQP, CoAP**) and 4 new systems (**MQTT Broker, MQTT Temperature Sensor, ESP8266 Smoke Sensor** and an **Arduino system**).  
  
I also implemented the integration of Hpfeeds which publishes the attacks in a MongoDB database instance.I improved the app's UI and performance, in addition with fixing bugs , upgrading deprecated libraries and unit testing.  
  
And finally I prepared a successful launching for the Play Store!

### Goals and Challenges

The project goal was the improvement of HosTaGe and launching it as a part of the Google play store as well as part of the Honeynet Project's arsenal.

The completed challenges for the project are the following:

#### New Features

This challenge includes all the new features that are introduced.

- **New Protocols simulation**  
    The app now fully simulates 3 new IoT protocols: _MQTT_, _CoAP_, _AMQP_.  
    
- **New Systems Simulation**  
    Four new systems are added: MQTT Broker, MQTT Temperature Sensor, ESP8266 Smoke Sensor, and an Arduino system.  
    
- **Hpfeeds integration**  
    The app now integrates the hpfeeds publisher, which can be enabled from the Settings of the app. With this publisher, we can publish the attack records captured by honeypots to a central repository.  
    
- **Use on Unrooted devices**  
    The app can now simulate all the protocols in an un-rooted device, allocating all the <1024 to random ones with a more significant number.  
    
- **Compatibility for Cellular Networks**  
    Compatibility for cell networks was added. Now the user can use the app in a 4g or 3g network.  
    
- **GreenDao Integration**  
    **GreenDao ORM** integration was added for better performance and faster queries for the local database.  
    
- **Pagination**  
    Data pagination was implemented. The records are not all loaded simultaneously, but they are added gradually with scrolling when users access them.  
    
- **Crashlytics-Firebase**  
    Firebase and Crashlytics SDKs added.

#### **UI Improvements and Compatibility Checks**

This challenge focused on improving app UI and solving compatibility issues.

- **Material Design**  
    Material Design library was added, and UI improvements were implemented, including new buttons, colors, dialogs, etc.  
    
- **Compatibility**  
    The app now is targeting the latest 29 SDK with minimum support for 24 SDK. Also, Android X migration was added.  
    
- **Logging**  
    The logs are showing the IP address as a header.

#### **Bug Fixes & Maintenance**

This challenge involved bug fixing and maintenance of existing services of the app.

- **Bug Fixes – Issues**  
    A lot of bugs are fixed, including runtime errors from background services that needed new permissions.  
    
- **Fixing Broken Protocols**  
    The SMTP, SMB, and FTP protocols were broken due to old libraries or bugs. They are now fixed.  
    
- **Rooted phones issue**  
    There were issues for rooted phones, and therefore the services were not bound to the default ports. The script for the rooted phones needed an upgrade.  
    A significant issue was that a lot of phones were missing the iptables library. An API was introduced to install the needed libraries and execute every iptable's command separately.  
    
- **Permission Dialogs**  
    Permission dialog is now included with a redirection functionality in the App Settings when a user denies them. The permissions were for Location and External Storage writing.

#### **Maintenance**

Maintenance tasks included an upgrade and refresh of the API keys and references.

- **Update of API keys**  
    Google maps key was updated; also, the HTTPS certificate was replaced.  
    
- **Update of Libraries**  
    A lot of libraries were upgraded or removed.  
    
- **Deprecate old features**  
    This includes the synchronization of tracing monitors and the bro-signature feature. The GHOST protocol was also disabled.  
    
- **Test Libraries**  
    Test frameworks added to the main functionality of the app like Espresso, Robolectric, and PowerMock.  
    Also, a python script was added for a full live-attack test.  
    
- **Memory Leaks-Performance Optimization**  
    A lot of memory leaks are now fixed. Memory consuming MultiStage Service was disabled from default. Thread concurrent modification exception error fixed.

#### **Publishing on the Play Store**

The app is available on Google Play Store [here](https://play.google.com/store/apps/details?id=dk.aau.netsec.hostage&hl=el).

![](images/alert.gif)

#### **Challenges faced**

The biggest challenge that I faced was implementing iptables in phones that didn't have it pre-installed.  
After studying the topic, the AFWall+ API's modification, and my mentors' support I resolved it, which made me very happy :).

### Pull Requests

1. https://github.com/aau-network-security/HosTaGe/pull/7
2. https://github.com/aau-network-security/HosTaGe/pull/35
3. https://github.com/aau-network-security/HosTaGe/pull/57
4. https://github.com/aau-network-security/HosTaGe/pull/93

### Mentors

- [Emmanouil Vasilomanolakis](https://mvasiloma.com/)
- [Shreyas Srinivasa](https://sastry17.github.io/)

### Next Steps

I learned many things in this project, and I am thrilled that I was part of it, and I would like to continue contributing even after GSoC.

New features that can be introduced:

1. Production Mode Settings
2. IPv6 Support

### Conclusion

Overall it was an incredible and educational experience working with **The Honeynet Project** organization these past three months.  
  
I also wanted to thank **The Honeynet Project** and **Google Summer of Code** for providing me with this opportunity and especially my mentors, for being supportive and motivated me through all this process! :)
