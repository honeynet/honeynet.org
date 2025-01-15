---
title: "DroidBox: alpha release"
authors: ["Patrik Lantz"]
date: "2011-07-14"
tags: 
  - "android"
  - "droidbox"
  - "dynamic-analysis"
  - "sandbox"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

The Android application sandbox is now ready for an alpha release. Details on how to get DroidBox running are available at the [project webpage](http://code.google.com/p/droidbox).

At the moment, the following actions are logged during runtime:

- File read and write operations
- Cryptography API activity
- Opened network connections
- Outgoing network traffic
- Information leaks through the following sinks: network, file, sms
- Attempts to send SMS
- Phone calls that have been made

An analysis output looks like the following sample report:

```
``____ __ ____ /\ _`\ [alpha] __ /\ \/\ _`\ \ \ \/\ \ _ __ ___ /\_\ \_\ \ \ \L\ \ ___ __ _ \ \ \ \ \/\`'__\ __`\/\ \ /'_` \ \ _ <' / __`\/\ \/'\ \ \ \_\ \ \ \/\ \L\ \ \ \/\ \L\ \ \ \L\ \ \L\ \/> \ \____/\ \_\ \____/\ \_\ \___,_\ \____/ \____//\_/\_\ \/___/ \/_/\/___/ \/_/\/__,_ /\/___/ \/___/ \//\/_/ ^C [*] Collected 36 sandbox logs``

`[File activities] -----------------

[Read operations] ----------------- [1310660567.27] /data/data/droidbox.tests/files/myfilename.txt Fd: 28 [1310660567.29] /data/data/droidbox.tests/files/myfilename.txt Fd: 28 [1310660567.29] /data/data/droidbox.tests/files/myfilename.txt Fd: 28 [1310660567.3] /data/data/droidbox.tests/files/myfilename.txt Fd: 28 [1310660567.3] /data/data/droidbox.tests/files/output.txt?A? Fd: 28 [1310660567.31] /data/data/droidbox.tests/files/output.txt Fd: 28 [1310660567.32] /data/data/droidbox.tests/files/output.txt?A? Fd: 28 [1310660567.41] /data/data/droidbox.tests/files/output.txt Fd: 28

[Write operations] ------------------ [1310660567.23] /data/data/droidbox.tests/files/myfilename.txt Fd: 28 [1310660567.25] /data/data/droidbox.tests/files/output.txt?A? Fd: 28 [1310660567.26] /data/data/droidbox.tests/files/output.txt Fd: 28

[Crypto API activities] ----------------------- [1310660567.47] Key:{0, 42, 2, 54, 4, 45, 6, 7, 65, 9, 54, 11, 12, 13, 60, 15} Algorithm: AES [1310660567.48] Operation:{encryption} Algorithm: AES Data:{000000000000000}

[1310660567.48] Key:{0, 42, 2, 54, 4, 45, 6, 7, 65, 9, 54, 11, 12, 13, 60, 15} Algorithm: AES [1310660567.49] Operation:{decryption} Algorithm: AES Data:{000000000000000}

[1310660567.5] Key:{0, 42, 2, 54, 4, 45, 6, 8} Algorithm: DES [1310660567.5] Operation:{encryption} Algorithm: DES Data:{000000000000000}

[1310660567.51] Key:{0, 42, 2, 54, 4, 45, 6, 8} Algorithm: DES [1310660567.51] Operation:{decryption} Algorithm: DES Data:{000000000000000}

[Network activity] ------------------

[Opened connections] -------------------- [1310660567.58] Destination: code.google.com Port: 80 [1310660570.07] Destination: pjlantz.com Port: 80 [1310660573.26] Destination: pjlantz.com Port: 80

[Outgoing traffic] ------------------ [1310660567.64] Destination: code.google.com Port: 80 Data: GET /p/droidbox/ HTTP/1.1

[Intent receivers] ------------------

[Permissions bypassed] ----------------------

[Information leakage] --------------------- [1310660567.26] Sink: File File descriptor: 28 Tag: TAINT_CONTACTS

[1310660567.29] Sink: File File descriptor: 28 Tag: TAINT_FILECONTENT

[1310660567.3] Sink: File File descriptor: 28 Tag: TAINT_FILECONTENT

[1310660567.31] Sink: File File descriptor: 28 Tag: TAINT_CONTACTS

[1310660567.41] Sink: File File descriptor: 28 Tag: TAINT_CONTACTS

[1310660570.2] Sink: Network Destination: pjlantz.com Port: 80 Tag: TAINT_IMEI Data: GET /imei.php?imei=c02c705e98588f724ca046ac59cafece65501e36

[1310660571.16] Sink: Network Destination: pjlantz.com Port: 80 Tag: TAINT_SMS Data: GET /phone.php?phone=0735445281

[1310660572.2] Sink: Network Destination: pjlantz.com Port: 80 Tag: TAINT_SMS Data: GET /msg.php?msg=Tjenare+hur+e+det

[1310660573.39] Sink: Network Destination: pjlantz.com Port: 80 Tag: TAINT_CONTACTS, TAINT_FILECONTENT Data: GET /file.php?file=Write+a+line&Peppe

[1310660574.39] Sink: Network Destination: pjlantz.com Port: 80 Tag: TAINT_PACKAGE Data: GET /app.php?installed=com.android.soundrecorder:com.android.gesture.builder:com.android.alarmclock:com.android.launcher:com.android.gallery:android:com.android.settings:com.android.providers.contacts:com.android.providers.applications:com.android.googlesearch:com.android.contacts:com.android.inputmethod.latin:com.android.phone:com.android.calculator2:droidbox.tests:com.android.providers.drm:com.android.htmlviewer:com.example.android.softkeyboard:com.android.term:com.android.providers.calendar:com.android.bluetooth:com.android.packageinstaller:com.android.development:com.android.calendar:com.android.browser:com.android.providers.telephony:com.android.music:com.android.providers.subscribedfeeds:com.svox.pico:com.android.camera:com.android.email:com.example.android.livecubes:com.android.providers.userdictionary:com.android.spare_parts:android.tts:com.android.providers.settings:com.android.mms:co

[1310660575.47] Sink: SMS Number: 123456789 Tag: TAINT_IMEI Data: dbd4e36bd5295531800c9596724361c4

[Sent SMS] ---------- [1310660575.45] Number: 0735445281 Message: Sending sms...

``[Phone calls] ------------- [1310660575.48] Number: 123456789 [1310660575.83] Number: 123456789`
```

The development continues with static analysis of Android packages. More specifically, permissions, activities and registered Intent receivers are to be parsed from the Manifest file to coordinate with the dynamic analysis. Some of the features planned to be implemented are:

- Log incoming network traffic
- Dump content of file operations
- Detect apps with Intent receivers (example: apps monitoring incoming SMS)
- Log possible permissions that have been bypassed

The last milestone period is soon starting and the coding in this phase includes generating API flow graphs to better understand in what order the logged actions are executed. Additionally, generating treemaps on the sample behavior might ease the malware classification but will initially function as a proof-of-concept implementation.
