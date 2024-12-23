---
title: "ML-based Web-attack Classification for TANNER"
date: "2024-12-23"
project_url: "https://github.com/mushorg/tanner"
hours: "175 or 350 hours"
mentor: "Evgeniia Tokarchuk"
project_type: "Improving an existing tool"
---

The project aims to enhance the efficiency and accuracy of web attack detection in TANNER by replacing detection based on regular expressions with machine learning methods. The project will be divided into two main parts:

1. Research of existing solutions and/or data collection
2. Integration of the ML classifier into TANNER

Over the past few years, we have collected data from various SNARE sensors. This data is annotated using regular expressions and can be used for building a data-driven classification model of web-based attacks. However, since this data is noisy and imbalanced, it requires careful pre-processing and filtering. Moreover, curating the test set is essential to build a robust, high-quality model. External datasets can be used along with historical data from TANNER to enlarge the dataset and mitigate the noise. The resulting ML model must have accuracy above the regexp baseline and low latency to enable real-time analysis of the TANNER events.

Requirements: python3, machine learning
