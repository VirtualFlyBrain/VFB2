---
title: "Confidence Values"
linkTitle: "Confidence Values"
categories: ["help"]
tag: ["GO", "classification"]
description: >
  Confidence values for predictions on VFB.
---

Some annotations on VFB are based on predictions, for example, predicted neurotransmitters for neurons in electron microscopy datasets (from [Eckstein et al., 2024](http://flybase.org/reports/FBrf0259490)). Where available, we include the confidence of these predictions (as a badge next to the annotation), as well as a link to the publication - in the example below, this would be by clicking on the 'DOI' badge.

<img src="/images/confidence_values.png" max-width="50%" alt="An example confidence value on VFB.">


## Neurotransmitter Prediction Confidence Values

Neurotransmitter predictions for neurons in the FlyWire FAFB and Hemibrain datasets are the 'conf_nt' predictions from [Eckstein et al. (2024)](http://dx.doi.org/10.1016/j.cell.2024.03.016). MANC predictions are from [Takemura et al. (2013)](http://dx.doi.org/10.1101/2023.06.05.543757), using the methodology of [Eckstein et al. (2024)](http://dx.doi.org/10.1016/j.cell.2024.03.016). This analysis only investigated a limited set of neurotransmitters and assumed a single neurotransmitter per neuron (see publications for further detail). Neurons with fewer than 100 presynapses are excluded.

