---
title: "New Split-GAL4 report pages on FlyBase"
linkTitle: "FlyBase Split-GAL4 reports"
date: 2024-04-30
image: https://www.virtualflybrain.org/images/splits_images.png
description: >
    FlyBase now has 'Split System Combination' pages displaying curated information for Split-GAL4 lines.
---

FlyBase has added report pages for split driver lines, where two (or more) hemidrivers are combined to restrict functional driver expression to the intersection of the hemidriver expression patterns. These are predominantly ['split GAL4’](https://pubmed.ncbi.nlm.nih.gov/17088209/) system combinations using a DBD and AD line currently, but more complex combinations may be included in the future.

![example_hemi_combo](https://www.virtualflybrain.org/images/splits_images.png)

These new ‘split system combinations’ pages (e.g. [GAL4DBD.R72B05∩Hsap\RELAAD.ple](http://flybase.org/reports/FBco0000023)), include information specific to that combination. Currently these include the FlyBase identifier (FBco), synonyms, the transgenic hemidriver alleles that make up the combination, expression pattern data and links to stocks corresponding to the combination.

![example_FBco_report](https://www.virtualflybrain.org/images/FBco_report.png)

The combination pages have been added to hitlists, so if you search for a regulatory region that drives expression of one of the hemidrivers in a combination (e.g. R72B05, VT064569, ple) you will see the relevant combination(s) in the hitlist. Searching for combination names is also supported (e.g. MB195B). These new report pages will get improvements during the coming months, including images of expression patterns when available.

![example_FBco_hitlist](https://www.virtualflybrain.org/images/FBco_hitlist.png)
