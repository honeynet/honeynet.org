---
title: "GSoC 2018 Project Summary: Conpot"
authors: ["Daniel Haslinger"]
date: "2018-08-18"
categories: 
  - "gsoc"
tags: 
  - "2018"
  - "conpot-d32"
  - "gsoc-d20"
  - "gsoc2018"
  - "ics-d114"
  - "python-d32"
  - "scada-d51"
coverImage: "conpot.jpeg"
---

Abhinav Saxena wrote this post as a project summary of his GSoC2018 experience.

### What did we achieve?

The following features and changes were implemented:

- - Migration of the codebase from Python 2.7 to Python 3.5 (issue [#358](https://github.com/mushorg/conpot/issues/358), code: [#374](https://github.com/mushorg/conpot/pull/374))

- - Implementation of FTP (RFC 959) and TFTP (RFC 1350) protocol stacks based on gevent (issue [#352](https://github.com/mushorg/conpot/issues/352), code: [ftp](https://github.com/mushorg/conpot/tree/master/conpot/protocols/ftp) and [tftp](https://github.com/mushorg/conpot/tree/master/conpot/protocols/tftp))

- - Implementation of an abstract filesystem that proxies and wraps an actual file system by providing os.\* wrappers (code: [#375](https://github.com/mushorg/conpot/pull/375) and [#382](https://github.com/mushorg/conpot/pull/382))

- - Wrote 123 unit tests and refactored all existing 44 unit tests, increasing coverage from 44% to 72% at the time of this writing  (code: [#374](https://github.com/mushorg/conpot/pull/374), [#375](https://github.com/mushorg/conpot/pull/375) and [#382](https://github.com/mushorg/conpot/pull/382))

- - Bug fixes and refactoring of the existing BACnet and IPMI protocol stacks (issue [#341](https://github.com/mushorg/conpot/issues/341), code [#382](https://github.com/mushorg/conpot/pull/382))

- - Bug fixes in auxiliary Docker files (issue: [#378](https://github.com/mushorg/conpot/issues/378), code: [#380](https://github.com/mushorg/conpot/pull/380) and  [#392](https://github.com/mushorg/conpot/pull/392))

- - Refactoring of an existing telnet library to be compatible to the Conpot codebase (issue [#285](https://github.com/mushorg/conpot/issues/285), code: [mushorg/telnetsrvlib](https://github.com/mushorg/telnetsrvlib/pull/1))

- - Wrote an internal interface implementation that introduces a decorator, allowing protocol servers to interact more deeply with each other.  (issue [#259](https://github.com/mushorg/conpot/issues/250), code [#375](https://github.com/mushorg/conpot/pull/375))

- - Helping users with issues and pull request reviews: [link](https://github.com/mushorg/conpot/search?q=%40xandfury+is%3Aissue+updated%3A2018-05-14..2018-08-14&unscoped_q=%40xandfury+is%3Aissue+updated%3A2018-05-14..2018-08-14&type=Issues)

_All commits can be seen [`here`](https://github.com/mushorg/conpot/search?q=author%3Axandfury+committer-date%3A2018-05-14..2018-08-14&unscoped_q=author%3Axandfury+committer-date%3A2018-05-14..2018-08-14&type=Commits) and [`here`](https://github.com/mushorg/telnetsrvlib/commits/master?author=xandfury)._

### Future Work:

In the course of the internship, we identified a couple of tasks that were out of scope but would further enhance Conpot:

- - Telnet server implementation: now that we have a Conpot compatible telnet library, we need to write a suitable handler and associated templates

- - Central authentication system: There can be common central authentication mechanism that can bring more consistency. (issue [#389](https://github.com/mushorg/conpot/issues/389), code: [auth.py](https://github.com/xandfury/conpot/blob/auth/conpot/core/auth.py))

- - Serial server implementation: I had already written the python 3 compatible code for this feature, I didn’t write any tests for it. (issue [#22](https://github.com/mushorg/conpot/issues/22), code [#356](https://github.com/mushorg/conpot/pull/356))

- - Generic database support for logging (issue [#60](https://github.com/mushorg/conpot/issues/60))

- - Support for type hints (issue [#393](https://github.com/mushorg/conpot/issues/393))
        

### Highlights and challenges:

The following tasks of the project were notably challenging: 

**Migrating Conpot from python 2.7 to python 3.5:** Before working on Conpot I had never migrated a project from python 2.7 and python 3.5. It took me some time to understand the key differences between the two that affect code. This is where I also learned about the importance of having a good coverage and keep a robust test suite.

**Internal Interface:** The solution required for this particular task led me deep into the realms of implementing decorators and why they are useful. This also led me to discover the dark arts of monkey patching and it’s potential pitfalls - something I had no experience with prior.

**Abstract File System:** It was definitely challenging to implement a robust and comprehensive system that could take place for the os.\* wrappers provided by python and produce fake results. This followed by writing a comprehensive test suite and integrating it as part of CI.

**TFTP server implementation:** Reading RFCs and finding a compatible library that could fit in a given project architecture and design.

**FTP server implementation:** Implementing a stable FTP server was the most challenging task I had throughout the summer. I had to learn about threading events and synchronization queues and event-driven programming.

**Misc:** Other highlights/challenges that I faced can be summarized as -

- - Collaborating with team for the release Conpot versions 0.5.2 and 0.6.0

- - Allowing Conpot to run with non sudo privileges.

- - Bug hunting and challenges while fixing IMPI/BACnet server implementation.

- - Understanding tox and migrating test suite from unit test to faster and more verbose pytest.

- - Reversing engineering packets using wireshark from available pacps and then reconstructing them.
        

### Learning outcomes:

Because GSoC's also about learning and polishing your skills

- - I acquired several skills during the internship including:

- - Much more comfortable at reading, writing and debugging valid python code.

- - Learned important differences between python2 and python3. Improved proficiency in the migration process.

- - Delivering an end product - starting from support documents (such as RFCs to implementing it and then support it with a good test suite.)

- - Got acquainted with Test Driven Development (TDD) and how it’s useful in pragmatic programming.

- - Improved my skills with asynchronous concurrent socket programming using gevent.

- - Learned about implementing file systems and the important factors that go with it.

- - Deepened my knowledge about industrial protocols and standards. Also learned about the tools used to test them.

- - Learned about importance of communication while working in a team.
        

### Conclusion:

I’ve had a wonderful time during these 3 months and have learned plenty of things. My special thanks goes to my mentor Daniel Haslinger, who has helped me tremendously throughout this journey.
