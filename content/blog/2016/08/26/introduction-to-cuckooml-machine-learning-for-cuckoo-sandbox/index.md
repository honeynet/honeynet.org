---
title: "Introduction to CuckooML: Machine Learning for Cuckoo Sandbox"
authors: ["Roberto Tanara"]
date: "2016-08-26"
categories: 
  - "gsoc"
tags: 
  - "cuckoo"
  - "gsoc"
coverImage: "cuckoo.png"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

CuckooML is a GSOC 2016 project by [Kacper Sokol](https://github.com/So-Cool/) that aims to deliver the possibility to find similarities between malware samples based on static and dynamic analysis features of binaries submitted to Cuckoo Sandbox. By using anomaly detection techniques, such mechanism is able to cluster and identify new types of malware and can constitute an invaluable tool for security researchers.

### It's all about data..

Malware datasets tend to be relatively large and sparse. They are mostly made of categorical and string data, hence there is a strong need for good feature extraction approaches to obtain numerical vectors that can be feed into machine learning algorithms \[e.g. Back to the Future: Malware Detection with Temporally Consistent Labels; Miller B., et al.\]. Another common problem is concept drift, the continuous variation of malware statistical properties caused by never ending arms race between malware and antivirus developers. Unfortunately, this makes fitting the clusters even harder and requires the chosen approach to be either easy to re-train or be adaptable to the drift, with the latter option being more desirable.

For such big datasets the choice of the clustering algorithm is critical as most of them require computation of a distance matrix for all the samples resulting in computational complexity of O(n2) and sometimes even O(n3). Furthermore, the dynamic evaluation of new samples can be overwhelming given the large number of submissions in short time.

There are variety of approaches that can be engineered to address these issues. For instance, to avoid re-training information about the model can be stored and updated only when a new unseen sample is submitted. The distances to existing samples are then computed and only the new entry has to be appended to the distance matrix. Additionally, to improve the overall performance, clustering algorithms can be initialised in a smart way and the algorithms can be parallelised, which is relatively easy thanks, for example, to scikit-learn's python implementation of most common clustering algorithms. Finally, other approaches like training the algorithm through sampling the data can be used.

### ...and features

To begin with, it is widely known that the performance of a classifier or a clustering algorithm depends largely on how the set of features is designed. For successful clustering representative features based on the malware analysis reports need to be well engineered.

Sometimes (v.i.) multiple sets of features have to be created to solve variations of the same problem. To better capture these variations it might be necessary to use a large number of features causing the clustering algorithm to suffer from the curse of dimensionality. This could result in the feature space being sparse and possibly, dimensionality reduction mechanisms need to be applied to improve the clustering process.

If the clustering algorithm is then successfully trained, it should deliver good results that reveal the inherent structure of the data representing the dynamic and static behavior of analysed malware samples.

### Clustering, Prototypes, and Anomaly Detection

The most popular clustering algorithms belong to the crisp family, which are designed to just assign a cluster to each sample. In our scenario simple clustering might not be enough. As we are dealing with uncertainty --- malware labelling can never be definitive, especially with new threats being created everyday --- it seems more natural to use fuzzy (soft) techniques which return the probability of a sample belonging to a particular cluster.

The latter approach also facilitates the possibility of calibrating the selected clustering algorithm, leading to the best possible result for a given problem. Moreover, probabilities returned by fuzzy clustering can be easily adapted for anomaly detection purposes by setting a calibrated rejection threshold. This creates plenty of interesting areas of application for our tool, especially early detection of new malware.

Finally, deriving prototypes from fuzzy clustering is as simple as finding the most probable sample from each cluster (distribution).

### Some Ideas and Open Problems

Unfortunately, our problem is not an exception and the “no free lunch” theorem applies to it. First of all, there are couple of caveats associated with choosing the appropriate clustering algorithm. The number of clusters pose a problem: either it needs to be fixed, hence the clustering problem has to be well defined in advance; or alternatively an algorithm has to detect the number of clusters by itself. Nevertheless, the latter approach might not be as effective as the first one. Furthermore, the high dimensionality of the feature space, calibration and overfitting might pose some problems.

Data clustering is usually very subjective. There are many categories by which malware can be categorised e.g. stealing data, removing data, encrypting data, altering data. Many more categories can be named like posing similar threats, altering similar files, attacking similar platforms, etc. It seems incredibly important to allow the user to choose the context of operation, or if possible define their own context, and then identify corresponding prototypes. Finally, it might be possible to use one clustering algorithm for all these contexts and avoid the costly retraining phase by creating a versatile (reusable) model.

An interesting approach that we plan to explore at some point is semi-supervised learning: active learning in particular. In this case, a small number of annotated samples can be used to transform a purely descriptive model into a somehow predictive one. Constrained clustering could also show how introducing some expert knowledge into the problem might sometimes yield significant improvements.

Clustering with reject option could be another approach. This is relatively easy to use with a classifier that returns probabilities and gives great results for detecting new classes and noise in the data. Alternatively, a subgroup discovery algorithm could be used to identify more complex structures in the data.

* * *

More information about the project can be found at its [GSoC 2016 summary site](https://honeynet.github.io/cuckooml/2016/08/21/gsoc16-summary/) and at the [blog](http://honeynet.github.io/cuckooml/blog/) where we are discussing the current development.Additionally, some of the above ideas are prototyped in the Jupyter Notebook that you can find on [GitHub](https://render.githubusercontent.com/view/ipynb?commit=50fb0eff5c0d702c1d60a44b189534489cd302e1&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f686f6e65796e65742f6375636b6f6f6d6c2f353066623065666635633064373032633164363061343462313839353334343839636433303265312f6578616d706c65732f6375636b6f6f6d6c2e6970796e62&nwo=honeynet%2Fcuckooml&path=examples%2Fcuckooml.ipynb&repository_id=56984886#cuckooml) and which is intended to showcase the possibilities of the current version ofCuckooML.
