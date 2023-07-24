---
title: "GSoC 2017 Project Summary: major SNARE/Tanner improvements"
date: "2017-10-23"
categories: 
  - "gsoc"
tags: 
  - "gsoc-d20"
  - "gsoc-snare-tanner"
  - "gsoc2017"
---

##### Student Ravinder Nehra contributed this post as a project summary of his GSoC2017 experience

## MySQL Emulator

Previously, Tanner supported SQL Injection using SQLITE but since MySQL is widely used so it is badly needed in my opinion. Also with MySQL, Time-based Blind SQLI can be emulated which can't be done in SQLITE based emulator. It is implemented using `aiosql` library using the same approach used in [SQLITE emulation](https://github.com/mushorg/tanner/wiki/Google-Summer-of-Code-2016-Work-Product-Submission#sql-injection-emulation) previously.

1. MySQLI emulator  [https://github.com/mushorg/tanner/commit/d79e1b6a34906d2527214ed19364c8d7f8edddc3](https://github.com/mushorg/tanner/commit/d79e1b6a34906d2527214ed19364c8d7f8edddc3)
2. Change default DB and update documentation  [https://github.com/mushorg/tanner/commit/7acfbc0792646a49be6f5330754b6cccabdcd3a1](https://github.com/mushorg/tanner/commit/7acfbc0792646a49be6f5330754b6cccabdcd3a1)
3. Add new SQLI tests  [https://github.com/mushorg/tanner/commit/19bfd57d73c74994533185e92f40d25428f3b31f](https://github.com/mushorg/tanner/commit/19bfd57d73c74994533185e92f40d25428f3b31f)

## [](https://github.com/mushorg/tanner/wiki/GSoC-2017-Work-Submission#command-execution-emulator)Command Execution Emulator

This emulator emulates [Command Execution/Injection](https://www.owasp.org/index.php/Command_Injection) vulnerability.It is implemented using docker considering its safety features. I used Busybox as default docker image which provides a nice Linux shell, file system and most importantly very light in size. Attack is identified using the regex `.*(alias|cat|cd|cp|echo|exec|find|for|grep|ifconfig|ls|man|mkdir|netstat|ping|ps|pwd|uname|wget|touch|while).*` and then injected in the `busbox` docker image to get command injecion results.

1. Command exec emulator  [https://github.com/mushorg/tanner/commit/6beb6275c5a10954ff5402e1ff04941213ffe42e](https://github.com/mushorg/tanner/commit/6beb6275c5a10954ff5402e1ff04941213ffe42e)
2. Docs  [https://github.com/mushorg/tanner/commit/cc769fdf64b91d9369847c1a61923f1c2534315a](https://github.com/mushorg/tanner/commit/cc769fdf64b91d9369847c1a61923f1c2534315a)
3. Fix Docker freezing  [https://github.com/mushorg/tanner/commit/9e20f5b880f9080e0d961ef3ae725519a25a9485](https://github.com/mushorg/tanner/commit/9e20f5b880f9080e0d961ef3ae725519a25a9485)
4. Tests  [https://github.com/mushorg/tanner/commit/8f096c728e4fd013f9cf3e75f4c6190d8cfc43ef](https://github.com/mushorg/tanner/commit/8f096c728e4fd013f9cf3e75f4c6190d8cfc43ef)

## [](https://github.com/mushorg/tanner/wiki/GSoC-2017-Work-Submission#base-emulator-architecture)Base Emulator Architecture

The previous base emulator didn’t specify a standard way of adding new emulator and the addition of each new emulator make it messier. So I designed a new architecture. This architecture follows `find and emulate` approach where each emulator has a `scan` method.

- The base emulator calls scan method of each emulator against each `GET`, `POST`parameter and `COOKIE` value.
- Then the base emulator calls the emulator's `handle` which returned a positive response.
- The `handle` method returns payload and a boolean value that tells whether we have to inject the payload into the same page or a new page.
- Depending upon the boolean value, the payload is injected into the most recently visited page.

1. Architecture  [https://github.com/mushorg/tanner/commit/6471d69c560b580b21106282f895f50021dc4310](https://github.com/mushorg/tanner/commit/6471d69c560b580b21106282f895f50021dc4310)
2. Cookie support for attacks  [https://github.com/mushorg/tanner/commit/4df7fcbea6403711146a8a767e6a861c5e9da0e4](https://github.com/mushorg/tanner/commit/4df7fcbea6403711146a8a767e6a861c5e9da0e4)
3. Payload Injection page  [https://github.com/mushorg/tanner/commit/df372e53b83a1603239b14c3200e6b7149b4734b](https://github.com/mushorg/tanner/commit/df372e53b83a1603239b14c3200e6b7149b4734b)

## [](https://github.com/mushorg/tanner/wiki/GSoC-2017-Work-Submission#padding-oracle-emulator)Padding Oracle Emulator

I'm thinking of implementing padding oracle emulator through cookies but Tanner didn't support attacks through cookies, so first I implemented this feature. But then I was a little confused about what cookie should I set which can be attacked. It becomes a difficult task as we don't have an authentication mechanism which uses cookies. Currently, it has been left on hold.

1. Issue [#154](https://github.com/mushorg/tanner/pull/149)

## [](https://github.com/mushorg/tanner/wiki/GSoC-2017-Work-Submission#lfi-emulator)LFI Emulator

Previously LFI emulator didn't support proc emulation. So to fix it and make LFI emulator more efficient LFI emulator is reimplemented using docker.

1. Code  [https://github.com/mushorg/tanner/commit/64fcf8d549e30b5aa902a281187500d5dd37af47](https://github.com/mushorg/tanner/commit/64fcf8d549e30b5aa902a281187500d5dd37af47)

## [](https://github.com/mushorg/tanner/wiki/GSoC-2017-Work-Submission#tanner-api)Tanner API

It involves improving the functionality of tanner api by adding more methods to it. The following new functionalities were added:

- Get a session info from its `sess-uuid`
- Get all the sessions using the filters `ip`, `time-duration`, `user-agent` , `owner-type`, `attack_type`
- Get stats of a snare using its `snare-uuid` A new API server is formed to make it accesible only from localhost.

1. API functions  [https://github.com/mushorg/tanner/commit/d89834196cc36833cd5f0bbd38a1b3222db2aa6d](https://github.com/mushorg/tanner/commit/d89834196cc36833cd5f0bbd38a1b3222db2aa6d)
2. API docs  [https://github.com/mushorg/tanner/commit/fc9dc6f329bf66d627c631a1ec71a2530a802ae0](https://github.com/mushorg/tanner/commit/fc9dc6f329bf66d627c631a1ec71a2530a802ae0)
3. New API Server  [https://github.com/mushorg/tanner/commit/0297c84b92e344fda5c267a5dc5ab1d83e96192b](https://github.com/mushorg/tanner/commit/0297c84b92e344fda5c267a5dc5ab1d83e96192b)
4. Tests  [https://github.com/mushorg/tanner/commit/29da6bd41974acadce12c3bb1608ef6ae415dcdc](https://github.com/mushorg/tanner/commit/29da6bd41974acadce12c3bb1608ef6ae415dcdc)

## [](https://github.com/mushorg/tanner/wiki/GSoC-2017-Work-Submission#tanner-ui)Tanner UI

It involves building a UI for tanner so that data captured by the honeypot can be shown in a well-formatted manner. The following pages were developed :

- Page showing list of all snares connected to the Tanner
- Page showing stats of a particular snare
- Page showing list of session affiliated to a snare with custom filters
- Page showing detailed information about a session

Jinja template along with aiohttp server are used for development.

1. UI code  [https://github.com/mushorg/tanner/commit/fc629f030e78e76a120558b265c6f5b8540a1e8b](https://github.com/mushorg/tanner/commit/fc629f030e78e76a120558b265c6f5b8540a1e8b)
2. Docs  [https://github.com/mushorg/tanner/commit/bf04e93fa3bfa1563d9d893def832e4103bc27e4](https://github.com/mushorg/tanner/commit/bf04e93fa3bfa1563d9d893def832e4103bc27e4)
3. Improvements  [https://github.com/mushorg/tanner/commit/50b19e8bdf0ecf8f89b95e3e37992afc638c11e7](https://github.com/mushorg/tanner/commit/50b19e8bdf0ecf8f89b95e3e37992afc638c11e7)

## [](https://github.com/mushorg/tanner/wiki/GSoC-2017-Work-Submission#php-code-injection-emulator)PHP Code Injection Emulator

It emulates PHP code injection vulnerability. Usually, this type of vulnerability is found where user input is directly passed to functions like `eval`, `assert`. To mimic the functionality, user input is converted to the following code `<?php eval('$a = user_input'); ?>` and then passed to [phpox](https://github.com/mushorg/phpox) to get php code emulation results.

1. Code  [https://github.com/mushorg/tanner/commit/d063e77daf801082ddaafcc1e8cbb6400bc63326](https://github.com/mushorg/tanner/commit/d063e77daf801082ddaafcc1e8cbb6400bc63326)

## [](https://github.com/mushorg/tanner/wiki/GSoC-2017-Work-Submission#snare-tanner-communication)Snare-Tanner Communication

It provides a defined format of how Tanner's response should be structured so that snare can parse it easily. This is the new response structure. This also added the functionality to return payload in headers.

```
Case 1 (where you need to return the page normally)detection = {		type : 1        }Case 2 (inject payload in the page)detection = {		type : 2,payload = {		page : ‘/vuln.php’,		value : ‘<script>alert(1)</script>’		headers : {				new_header : ‘new_header_value’			     }	      }        }Case 3 (where input cause some error so return related to the type of error produced   e.g if input takes more time than expected then return 50X) detection = {		type : 3,                payload = {		                  status_code : 500/504                                 }        }
```

1. Tanner Code  [https://github.com/mushorg/tanner/commit/b3d5ec066e8f0e224a272c6c0827f0c62adb30e8](https://github.com/mushorg/tanner/commit/b3d5ec066e8f0e224a272c6c0827f0c62adb30e8)
2. Fix  [https://github.com/mushorg/tanner/commit/3dde5e70a05822faf08d6b841c203f9593b68425](https://github.com/mushorg/tanner/commit/3dde5e70a05822faf08d6b841c203f9593b68425)
3. Snare code  [https://github.com/mushorg/snare/commit/9a9797a64cf686e940dba920b7b46f248fb8d521](https://github.com/mushorg/snare/commit/9a9797a64cf686e940dba920b7b46f248fb8d521)

## [](https://github.com/mushorg/tanner/wiki/GSoC-2017-Work-Submission#crlf-emulator)CRLF Emulator

It emulates [CRLF vulnerability](https://www.owasp.org/index.php/CRLF_Injection). The attack is detected using `\r\n` pattern in the input. The parameter which looks suspicious is injected as a header with parameter name as header name and param value as header value.

1. Code  [https://github.com/mushorg/tanner/commit/4e3e4ae45e55589886531a1597e854add690c457](https://github.com/mushorg/tanner/commit/4e3e4ae45e55589886531a1597e854add690c457)
2. Tests  [https://github.com/mushorg/tanner/commit/3f1473126de5310234db751ced99749e4efd72a0](https://github.com/mushorg/tanner/commit/3f1473126de5310234db751ced99749e4efd72a0)
3. Docs  [https://github.com/mushorg/tanner/commit/d2bea46dd3588f30bd95c447f301fd72de00b9ea](https://github.com/mushorg/tanner/commit/d2bea46dd3588f30bd95c447f301fd72de00b9ea)

## [](https://github.com/mushorg/tanner/wiki/GSoC-2017-Work-Submission#other)Other

1. Fix docker issue  [https://github.com/mushorg/tanner/commit/5b0ed9ca91c7f08ac7101aa73ec2be957492b1e2](https://github.com/mushorg/tanner/commit/5b0ed9ca91c7f08ac7101aa73ec2be957492b1e2)
2. Fix session’s attack type attribute bug  [https://github.com/mushorg/tanner/commit/40062b8f28351b82a9b7e7cdd09ff47553a66e81](https://github.com/mushorg/tanner/commit/40062b8f28351b82a9b7e7cdd09ff47553a66e81)
3. The databases (used in SQLI) and dockers (used in LFI and CMD EXEC) remain in the system even after shutdown. It deletes these unwanted things.  [https://github.com/mushorg/tanner/commit/150c05caf945026836c5a9844540e4f93a66a976](https://github.com/mushorg/tanner/commit/150c05caf945026836c5a9844540e4f93a66a976)
4. Make emulator set flexible. Now user can select which vulnerabilities Tanner will emulate using config file easily.  [https://github.com/mushorg/tanner/commit/e82d5e49435a0fc073e7693743690aa93dc52bf9](https://github.com/mushorg/tanner/commit/e82d5e49435a0fc073e7693743690aa93dc52bf9)
5. Fix config structure  [https://github.com/mushorg/tanner/commit/79639f8c563565c6b7baedc1aa786855f87d9d27](https://github.com/mushorg/tanner/commit/79639f8c563565c6b7baedc1aa786855f87d9d27)
6. Add an option in config so that user can specify the size of poolsize used for Redis connection.  [https://github.com/mushorg/tanner/commit/a88bbdc31c1ebda0c00b57abfc033081e1821845](https://github.com/mushorg/tanner/commit/a88bbdc31c1ebda0c00b57abfc033081e1821845)
7. Add an option to get `phpox` address from config and return tanner version to snare  [https://github.com/mushorg/tanner/commit/00d0bede873bedcd832737ab49539ecfeaecb92d](https://github.com/mushorg/tanner/commit/00d0bede873bedcd832737ab49539ecfeaecb92d)
