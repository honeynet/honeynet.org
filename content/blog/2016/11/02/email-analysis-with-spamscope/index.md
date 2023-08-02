---
title: "Email analysis with SpamScope"
authors: ["Fedele Mantuano"]
date: "2016-11-02"
categories: 
  - "analysis"
tags: 
  - "email"
  - "spam"
  - "spamscope"
coverImage: "spamscope.png"
---

SpamScope (https://github.com/SpamScope/spamscope) is a fast and advanced tool for email analysis developed by Fedele Mantuano ([@fedelemantuano](https://twitter.com/fedelemantuano)).  The analysis engine it’s based on Apache Storm and Streamparse.

Why use Apache Storm?

Apache Storm works with streams, and in this case we analyze a stream of email messages.  Apache Storm allows you to start small and scale horizontally as you grow. Simply add more workers, that can be on different hosts.

An application is designed as a "topology" in the shape of a directed acyclic graph (DAG) with spouts and bolts acting as the graph vertices. Together, the topology acts as a data transformation pipeline. 

![](images/schema_topology.png)

Input data enter in a spout (orange edge), an example are email files.  Inputs are acted upon until they get out of the stream from an output bolt. Bolts contain functionalities while spouts are the different inputs.

The main bolts of SpamScope are:

1. tokenizer: based on mail-parser ([https://github.com/SpamScope/mail-parser](https://github.com/SpamScope/mail-parser)), this bolt splits the email in different components (body, header, attachments, etc), generate the stream for the others bolts and can filter emails and attachments already analyzed, without accessing the DB but only looking up RAM structures.
    
2. attachments: this bolt ingests the files contained in email attachments, and adds the hashes (also fuzzy hash), Apache Tika analysis ([https://tika.apache.org/](https://tika.apache.org/)) and VirusTotal reports.
    
3. url-handlers: these bolts extract the urls from body and attachments and are very important for the phishing bolt.
    
4. phishing: this bolt looks for phishing in body, header, url and attachment and use a bitmap to give a phishing score to the mail. See [the code](https://github.com/SpamScope/spamscope/blob/develop/src/modules/phishing_bitmap.py) for more details. The score it’s very important to avoid false positive.
    
5. json: all the streams are merged to become a JSON
    
6. output: SpamScope comes with Elasticsearch, Redis and a Debug (files on disk) output.
    

All these bolts work in parallel and you can choose input sources (with spouts) and functionalities (with bolts),  and also add more functionalities (more bolts) if you want.

Why use Streamparse?

Streamparse allows you to use Python to develop spouts, bolts and topology.

Why should you use SpamScope?

![](images/spamscope.png)

SpamScope is fully configurable and can  analyze millions of emails a day. The main configuration file is spamscope.yml, you can find it in the [conf](https://github.com/SpamScope/spamscope/tree/develop/conf) folder. Using the tick function of Apache Storm you don’t need to restart the topology, every x seconds the configuration it’s automatically reloaded. For more details see the conf folder.

It’s easy to install and it's possible to use a complete Docker image with Apache Storm and SpamScope. [Download it here](https://hub.docker.com/r/fmantuano/spamscope/).

All the project is on GitHub: [https://github.com/SpamScope](https://github.com/SpamScope), any feedback is welcome!

[@fedelemantuano](https://twitter.com/fedelemantuano)
