---
title: "Iteolih: Python Benchmark"
authors: ["Markus Koetter"]
date: "2009-05-24"
tags: 
  - "iteolih"
  - "python"
---

As the plan is to embedd python as scripting language into the honeypot, I ran a benchmark on a testsuite. The 'testsuite' is a c core which accepts connections, and allows python to deal with the input. The protocol used for benchmarking is http, the service serves a non static html page.

I tested

- - 2.6.2\_(release26-maint,\_Apr\_19\_2009,\_02:15:38)

- - 3.0.1+\_(r301:69556,\_Apr\_15\_2009,\_17:22:45)\_

- - 3.1a1+\_(py3k,\_Mar\_30\_2009,\_02:02:26)\_

To benchmark, I ran the apache benchmark tool **ab**

_ab -n 100000 -c 15 http://localhost:8080/bar_

The result:

| Server Software | 2.6.2 | 3.0.1 | 3.1a |
| --- | --- | --- | --- |
| Server Hostname | localhost | localhost | localhost |
| Server Port | 8080 | 8080 | 8080 |
| Document Path | /bar | /bar | /bar |
| Document Length | 191 bytes | 191 bytes | 191 bytes |
| Concurrency Level | 15 | 15 | 15 |
| Time taken for tests (seconds) | *28.47* | **102.15** | 31.8 |
| Complete requests | 100000 | 100000 | 100000 |
| Failed requests | 0 | 0 | 0 |
| Write errors | 0 | 0 | 0 |
| Total transferred (bytes) | 38600386 | 38200000 | 37600376 |
| HTML transferred (bytes) | 19100191 | 19100000 | 19100191 |
| Requests per second [#/sec] (mean) | *3512.04* | **978.95** | 3144.45 |
| Time per request [ms] (mean) | 4.27 | 15.32 | 4.77 |
| Time per request [ms] (mean, across all concurrent requests) | 0.29 | 1.02 | 0.32 |
| Transfer rate [Kbytes/sec] received | *1323.89* | **365.19** | 1154.61 |

Python 3.0.1 serves about 978 requests per second, where Python 2.6.2 does 3512 requests/second.

| Percentage of the requests served within a certain time (ms) | 2.6.2 | 3.0.1 | 3.1a |
| --- | --- | --- | --- |
| 50.00% | 3 | 15 | 4 |
| 66.00% | 4 | 15 | 5 |
| 75.00% | 4 | 15 | 5 |
| 80.00% | 4 | 16 | 5 |
| 90.00% | 4 | 16 | 5 |
| 95.00% | 5 | 16 | 5 |
| 98.00% | 5 | 17 | 6 |
| 99.00% | 6 | 19 | 6 |
| 100% (longest request) | 3004 | 3019 | 3006 |

![](images/drupal_image_443.jpg)

Obviously Python 3.0 does something wrong, talking about factor 4x, it is noticeably slower. But I'm  glad to see it is fixed in 3.1 already.

I tried to benchmark using unladen-swallow, the llvm based python project run by google, but was not able to link the code properly. (undefined symbol: \_ZTIN4llvm14ModuleProviderE)

As Python 3.1a is almost as fast as 2.6 for our needs, and it can be tricky to port python 2.6 code to 3.x, we will use python 3 as embedded scripting language.
