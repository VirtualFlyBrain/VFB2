---
title: "New Precomputed Neuron and Expression Pattern Similarity Scores on VFB"
linkTitle: "Updated NBLAST scores"
date: 2025-05-29
description: >
    VFB neuron-to-neuron and neuron-to-expression pattern similarity scores (NBLAST) have been expanded to include the male-CNS optic lobe and FAFB-FlyWire connectome datasets.
---

VFB provides precomputed [NBLAST](https://virtualflybrain.org/docs/tutorials/nblast/) scores to assist in the discovery of 1) morphologically similar neurons within and across connectome datasets and 2) potential split-GAL4 driver lines which label neurons from connectomic datasets.

NBLAST queries can be accessed in the term info panel for individuals (neuron/split-GAL4 images) (at bottom of the example image below). The queries are only available if there are any results for that individual.

![NBLAST queries](https://www.virtualflybrain.org/images/NBLAST_Queries.png)

Neuron-to-neuron example match:

![NBLAST queries](https://www.virtualflybrain.org/images/Neuron-Neuron_NBLAST.png)

Neuron-to-split-GAL4 expression pattern example match:

![NBLAST queries](https://www.virtualflybrain.org/images/Neuron-Expression_NBLAST.png)

## Datasets included

VFB NBLAST scores cover all available neurons and expression patterns on VFB, including some of the largest and most comprehensive individual neuron datasets:

**Single Neuron/Connectome Datasets:**

- FAFB-FlyWire (v783) - [FlyWire Codex](https://codex.flywire.ai/?dataset=fafb)
- Male-CNS optic lobe (v1.0.1) - [neuprint optic-lobe](https://neuprint.janelia.org/?dataset=optic-lobe%3Av1.0.1&qt=findneurons)
- FlyCircuit (1.0) - [site](http://www.flycircuit.tw/v1.1/)
- FAFB-CATMAID (all datasets on the VFB server) - [CATMAID server](https://fafb.catmaid.virtualflybrain.org/?pid=1&zp=65720&yp=160350.0517811483&xp=487737.6942783438&tool=tracingtool&sid0=1&s0=3.1999999999999993&help=true&layout=h(XY,%20%7B%20type:%20%22neuron-search%22,%20id:%20%22neuron-search-1%22,%20options:%20%7B%22annotation-name%22:%20%22Published%22%7D%7D,%200.6))
- Hemibrain (1.2.1) - [neuprint hemibrain](https://neuprint.janelia.org/?dataset=hemibrain%3Av1.2.1&qt=findneurons)

**Split-GAL4 driver line images:**

- Images provided from [FlyLight Split-GAL4](https://splitgal4.janelia.org/cgi-bin/splitgal4.cgi). New images are being added to VFB regularly.