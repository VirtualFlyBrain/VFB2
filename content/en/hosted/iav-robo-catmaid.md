---
title: IAV-ROBO CATMAID Data Viewer
description: "This CATMAID (Collaborative Annotation Toolkit for Massive Amounts of Image Data) instance hosts the neuroanatomical data from the IAV mechanosensory circuit study published in Valdes-Aleman et al. 2021."
---

## Access

The IAV-ROBO CATMAID instance is hosted and maintained by Virtual Fly Brain (VFB) as part of their mission to integrate and preserve key Drosophila neuroscience datasets. The instance is accessible at:
[https://iav-robo.catmaid.virtualflybrain.org/](https://iav-robo.catmaid.virtualflybrain.org/?pid=2&zp=18360&yp=25383.555362060197&xp=40676.497110038756&tool=tracingtool&sid0=1&s0=4&help=true&layout=h(XY,%20%7B%20type:%20%22neuron-search%22,%20id:%20%22neuron-search-1%22,%20options:%20%7B%22annotation-name%22:%20%22papers%22%7D%7D,%200.6)#)

This resource provides a direct view into the dataset used to study the organization of proprioceptive circuits in Drosophila larvae. Virtual Fly Brain ensures its long-term availability to the research community.

## Source Publication

This data is from the research published in:

Valdes-Aleman J, et al. (2021). Comparative Connectomics Reveals How Partner Identity, Location, and Activity Specify Synaptic Connectivity in the Drosophila Motor System. Neuron, 109(1), 105-120.e7. https://doi.org/10.1016/j.neuron.2020.10.004

## Dataset Contents

The viewer provides access to:
- Serial section electron microscopy data of Drosophila 1st instar larval CNS (1.5-segment fraction, A1/A2 segment)
- Image resolution: 3.8 nm x 3.8 nm x 40 nm (x, y, z)
- Genotype: w;; iav-GAL4/UAS-FraRobo
- Manually traced neuron reconstructions showing shifted mechanosensory projections
- Synaptic connectivity information
- Associated metadata and annotations

## Technical Details

The EM volume was prepared and imaged following protocols detailed in Ohyama et al. (2015). Neurons were reconstructed using CATMAID to obtain skeletonized structures and connectivity information. All synaptic connections represent chemical synapses.

Despite the FraRobo-induced lateral shift in terminal projections, neurons remain uniquely identifiable based on:
- Nerve entry point of the main neurite into the neuropil
- Growth pattern of main axonal and dendritic branches
- Bilateral vs ipsilateral projections

For example, mechanosensory chordotonal neurons can be identified by their:
- Eight stereotypic entry points per hemisegment
- Most lateral position among sensory neurons in their nerve bundle
- Further lateral shift due to FraRobo expression

## Features

This CATMAID instance enables:
- Browser-based visualization of the serial section electron microscopy data
- Navigation through image stacks
- Viewing of neuron reconstructions
- Analysis of synaptic connectivity
- Data export functionality

### Available Tools
- Tracing tool for examining reconstructions
- Neuron search interface
- Connectivity analysis tools
- Skeleton visualization options
- API access for programmatic data retrieval (documentation: https://catmaid.readthedocs.io/en/stable/api.html): https://iav-robo.catmaid.virtualflybrain.org/apis/

## Citation Guidelines

When using this data, please cite both:

1. The original research:
   Valdes-Aleman J, et al. (2021). Comparative Connectomics Reveals How Partner Identity, Location, and Activity Specify Synaptic Connectivity in the Drosophila Motor System. Neuron, 109(1), 105-120.e7. https://doi.org/10.1016/j.neuron.2020.10.004

2. The CATMAID platform:
   Saalfeld S, Cardona A, Hartenstein V, Tomančák P (2009) CATMAID: collaborative annotation toolkit for massive amounts of image data. Bioinformatics 25(15): 1984-1986. https://doi.org/10.1093/bioinformatics/btp266

## Maintenance & Support

This resource is archived, hosted, and maintained by Virtual Fly Brain (VFB - https://virtualflybrain.org) as part of their commitment to preserving and making accessible critical Drosophila neuroscience data resources. 