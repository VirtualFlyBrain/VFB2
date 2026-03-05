---
title: ABD1.5 CATMAID Data Viewer
description: "This CATMAID (Collaborative Annotation Toolkit for Massive Amounts of Image Data) instance hosts the neuroanatomical data from wild-type Drosophila larval abdominal segments, providing reference datasets for mechanosensory and motor circuit studies."
---

## Access

The ABD1.5 CATMAID instance is hosted and maintained by Virtual Fly Brain (VFB) as part of their mission to integrate and preserve key Drosophila neuroscience datasets. The instance is accessible at:
[https://abd1.5.catmaid.virtualflybrain.org/](https://abd1.5.catmaid.virtualflybrain.org/?pid=1&zp=10485&yp=40560.65722061269&xp=42396.0789533435&tool=tracingtool&sid0=1&s0=4.5&help=true&layout=h(XY,%20%7B%20type:%20%22neuron-search%22,%20id:%20%22neuron-search-1%22,%20options:%20%7B%22annotation-name%22:%20%22papers%22%7D%7D,%200.6)#)

This resource provides wild-type reference data for the abdominal nerve cord of first instar Drosophila larvae, serving as a baseline for comparative connectomics studies. Virtual Fly Brain ensures its long-term availability to the research community.

## Source Publications

This dataset contains neuron reconstructions from multiple foundational connectomics studies:

1. Ohyama T, Schneider-Mizell CM, Fetter RD, Aleman JV, Franconville R, Rivera-Alba M, et al. (2015). A multilevel multimodal circuit enhances action selection in Drosophila. Nature, 520(7545), 633-639. https://doi.org/10.1038/nature14297

2. Schneider-Mizell CM, Gerhard S, Longair M, Kazimiers T, Li F, Zwart MF, et al. (2016). Quantitative neuroanatomy for connectomics in Drosophila. eLife, 5, e12059. https://doi.org/10.7554/eLife.12059

3. Valdes-Aleman J, Fetter RD, Sales EC, Heckman EL, Venkatasubramanian L, Doe CQ, et al. (2021). Comparative Connectomics Reveals How Partner Identity, Location, and Activity Specify Synaptic Connectivity in the Drosophila Motor System. Neuron, 109(1), 105-120.e7. https://doi.org/10.1016/j.neuron.2020.10.004

## Dataset Contents

The viewer provides access to:
- Serial section electron microscopy data of Drosophila 1st instar larval CNS (1.5-segment abdominal fraction, A2-A3 segments)
- Image resolution: 3.8 nm x 3.8 nm x 40 nm (x, y, z)
- Wild-type control neural tissue
- Hundreds of manually traced and reconstructed neurons
- Synaptic connectivity information
- Associated metadata and annotations

### Reconstructed Neuron Types

This dataset includes extensive reconstructions of:

**Sensory neurons:**
- Mechanosensory chordotonal neurons (lch5 subtypes)
- Nociceptive multidendritic neurons (ddaC, ddaD, ddaE, vdaB, v'ada)
- Polymodal sensory neurons (v'ch, vchA/B, vchB/A)

**Interneurons:**
- Basin (Bs) interneurons (excitatory modulation)
- Proprioceptive and intersegmental interneurons
- Premotor interneurons (extensive IS premotor reconstructions)
- Motor circuit interneurons (Looper, Pseudolooper, Scepter, Bowl, Chair classes)

**Motor neurons:**
- Identified motor neurons (aCC, RP2)
- Putative motor neurons and muscle-innervating neurons

**Other circuit elements:**
- Intersegmental connections
- Spillover neurons (anterior and posterior processes)
- Additional circuit fragments and auxiliary neurons

## Technical Details

The EM volume was prepared and imaged following protocols detailed in Ohyama et al. (2015). Neurons were reconstructed using CATMAID to obtain skeletonized structures and connectivity information. All synaptic connections represent chemical synapses.

Key neuron types identifiable in this dataset include:
- Mechanosensory chordotonal neurons (input sensory neurons)
- Basin (Bs) interneurons (excitatory integration)
- Drunken (Dr), Griddle (Gr), and Ladder (Ld) interneurons (inhibitory modulation)
- Nociceptive multidendritic neurons (noxious stimulus detection)
- Local and ascending interneurons

These neurons are uniquely identifiable based on:
- Nerve entry point of the main neurite into the neuropil
- Growth pattern of main axonal and dendritic branches
- Bilateral vs ipsilateral projections
- Position of terminal projections within the neuropil

## Features

This CATMAID instance enables:
- Browser-based visualization of serial section electron microscopy data
- Navigation through image stacks
- Viewing of neuron reconstructions
- Analysis of synaptic connectivity
- Data export functionality

### Available Tools
- Tracing tool for examining reconstructions
- Neuron search interface
- Connectivity analysis tools
- Skeleton visualization options
- API access for programmatic data retrieval (documentation: https://catmaid.readthedocs.io/en/stable/api.html): https://abd1.5.catmaid.virtualflybrain.org/apis/

## Citation Guidelines

When using this data, please cite the relevant research:

1. For mechanosensory and motor circuit data:
   Valdes-Aleman J, et al. (2021). Comparative Connectomics Reveals How Partner Identity, Location, and Activity Specify Synaptic Connectivity in the Drosophila Motor System. Neuron, 109(1), 105-120.e7. https://doi.org/10.1016/j.neuron.2020.10.004

2. For foundational circuit architecture and quantitative neuroanatomy:
   Ohyama T, et al. (2015). A multilevel multimodal circuit enhances action selection in Drosophila. Nature, 520(7545), 633-639. https://doi.org/10.1038/nature14297

3. For quantitative neuroanatomy methodology:
   Schneider-Mizell CM, et al. (2016). Quantitative neuroanatomy for connectomics in Drosophila. eLife, 5, e12059. https://doi.org/10.7554/eLife.12059

4. The CATMAID platform:
   Saalfeld S, Cardona A, Hartenstein V, Tomančák P (2009) CATMAID: collaborative annotation toolkit for massive amounts of image data. Bioinformatics 25(15): 1984-1986. https://doi.org/10.1093/bioinformatics/btp266

## Maintenance & Support

This resource is archived, hosted, and maintained by Virtual Fly Brain (VFB - https://virtualflybrain.org) as part of their commitment to preserving and making accessible critical Drosophila neuroscience data resources.
