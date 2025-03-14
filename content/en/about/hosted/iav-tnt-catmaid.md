---
title: IAV-TNT CATMAID Data Viewer
description: "This CATMAID (Collaborative Annotation Toolkit for Massive Amounts of Image Data) instance hosts the neuroanatomical data from the IAV mechanosensory circuit study published in Valdes-Aleman et al. 2021."
---

## Access

The IAV-TNT CATMAID instance is hosted and maintained by Virtual Fly Brain (VFB) as part of their mission to integrate and preserve key Drosophila neuroscience datasets. The instance is accessible at:
[https://iav-tnt.catmaid.virtualflybrain.org/](https://iav-tnt.catmaid.virtualflybrain.org/?pid=4&zp=0&yp=28633&xp=45094.6&sid0=2&s0=4&tool=tracingtool&help=true&layout=h(XY,%20%7B%20type:%20%22neuron-search%22,%20id:%20%22neuron-search-1%22,%20options:%20%7B%22annotation-name%22:%20%22papers%22%7D%7D,%200.6)#)

This resource provides a direct view into the dataset used to study the organization of proprioceptive circuits in Drosophila larvae. Virtual Fly Brain ensures its long-term availability to the research community.

## Source Publication

This data is from the research published in:

Valdes-Aleman J, et al. (2021). Comparative Connectomics Reveals How Partner Identity, Location, and Activity Specify Synaptic Connectivity in the Drosophila Motor System. Neuron, 109(1), 105-120.e7. https://doi.org/10.1016/j.neuron.2020.10.004

## Dataset Contents

The viewer provides access to:
- Serial section electron microscopy data of Drosophila 1st instar larval CNS (Control 1: whole-CNS volume, A1 segment)
- Image resolution: 3.8 nm x 3.8 nm x 40 nm (x, y, z)
- Manually traced neuron reconstructions
- Synaptic connectivity information
- Associated metadata and annotations

## Technical Details

The EM volume was prepared and imaged following protocols detailed in Ohyama et al. (2015). Neurons were reconstructed using CATMAID to obtain skeletonized structures and connectivity information. All synaptic connections represent chemical synapses.

The neurons are uniquely identifiable based on key morphological features:
- Nerve entry point of the main neurite into the neuropil
- Growth pattern of main axonal and dendritic branches
- Bilateral vs ipsilateral projections
- Position of terminal projections within the medio-lateral, dorso-ventral and antero-posterior axes

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
- API access for programmatic data retrieval (documentation: https://catmaid.readthedocs.io/en/stable/api.html): https://iav-tnt.catmaid.virtualflybrain.org/apis/

## Citation Guidelines

When using this data, please cite both:

1. The original research:
   Valdes-Aleman J, et al. (2021). Comparative Connectomics Reveals How Partner Identity, Location, and Activity Specify Synaptic Connectivity in the Drosophila Motor System. Neuron, 109(1), 105-120.e7. https://doi.org/10.1016/j.neuron.2020.10.004

2. The CATMAID platform:
   Saalfeld S, Cardona A, Hartenstein V, Tomančák P (2009) CATMAID: collaborative annotation toolkit for massive amounts of image data. Bioinformatics 25(15): 1984-1986. https://doi.org/10.1093/bioinformatics/btp266

## Maintenance & Support

This resource is archived, hosted, and maintained by Virtual Fly Brain (VFB - https://virtualflybrain.org) as part of their commitment to preserving and making accessible critical Drosophila neuroscience data resources.
