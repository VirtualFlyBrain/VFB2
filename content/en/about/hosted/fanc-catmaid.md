---
title: FANC CATMAID Data Viewer
description: "This CATMAID (Collaborative Annotation Toolkit for Massive Amounts of Image Data) instance hosts neuroanatomical data from the Female Adult Nerve Cord (FANC) electron microscopy dataset, available in both the original EM space and aligned to the JRC2018 VNC female template."
---

![Figure showing FANC Motor and sensory neuron reconstructions](https://flyemdev.mrc-lmb.cam.ac.uk/vnc1/2199/small.jpg)

## Access

The FANC CATMAID instance is hosted and maintained by Virtual Fly Brain (VFB) as part of their mission to integrate and preserve key Drosophila neuroscience datasets. The instance provides two views of the data:

1. Original EM stack and tracings (Project ID 1):
[https://fanc.catmaid.virtualflybrain.org/](https://fanc.catmaid.virtualflybrain.org/?pid=1&zp=55260&yp=512482.5999999994&xp=173092.19999999998&tool=tracingtool&sid0=1&s0=9&help=true&layout=h(XY,%20%7B%20type:%20%22neuron-search%22,%20id:%20%22neuron-search-1%22,%20options:%20%7B%22annotation-name%22:%20%22publication%22%7D%7D,%200.6))

2. Neurons aligned to JRC2018 VNC female template (Project ID 2):
[https://fanc.catmaid.virtualflybrain.org/](https://fanc.catmaid.virtualflybrain.org/?pid=2&zp=71600&yp=316800&xp=164400&tool=tracingtool&sid0=3&s0=1&help=true&layout=h(XY,%20%7B%20type:%20%22neuron-search%22,%20id:%20%22neuron-search-1%22,%20options:%20%7B%22annotation-name%22:%20%22publication%22%7D%7D,%200.6))

This resource provides access to both the original FANC dataset and template-aligned reconstructions. Virtual Fly Brain ensures its long-term availability to the research community.

## Source Publication

The data is from the research published in:

Fushiki A, et al. (2021) A circuit mechanism for the propagation of waves of muscle contraction in Drosophila. Cell, 184(3), 759-774.e20. https://doi.org/10.1016/j.cell.2020.12.013

see: https://www.lee.hms.harvard.edu/resources

## Dataset Contents

The viewer provides access to:
- Complete electron microscopy volume of an adult female Drosophila ventral nerve cord
- Manually traced neuron reconstructions in original EM space
- Template-aligned neurons in JRC2018 VNC female template space
- Synaptic connectivity information
- Associated metadata and annotations

## Features

This CATMAID instance enables:
- Browser-based visualization of the serial section electron microscopy data
- Navigation through image stacks
- Viewing of neuron reconstructions in both original and template space
- Analysis of synaptic connectivity
- Data export functionality

### Available Tools
- Tracing tool for examining reconstructions
- Neuron search interface
- Connectivity analysis tools
- Skeleton visualization options
- API access for programmatic data retrieval (documentation: https://catmaid.readthedocs.io/en/stable/api.html): https://fanc.catmaid.virtualflybrain.org/apis/

Note: Both views (original and aligned) can be accessed through the same API using different project IDs (pid).

## Citation Guidelines

When using this data, please cite:

1. The FANC dataset:
   Fushiki A, et al. (2021) A circuit mechanism for the propagation of waves of muscle contraction in Drosophila. Cell, 184(3), 759-774.e20. https://doi.org/10.1016/j.cell.2020.12.013

2. The CATMAID platform:
   Saalfeld S, Cardona A, Hartenstein V, Tomančák P (2009) CATMAID: collaborative annotation toolkit for massive amounts of image data. Bioinformatics 25(15): 1984-1986. https://doi.org/10.1093/bioinformatics/btp266

## Maintenance & Support

This resource is archived, hosted, and maintained by Virtual Fly Brain (VFB - https://virtualflybrain.org) as part of their commitment to preserving and making accessible critical Drosophila neuroscience data resources. The aligned neurons are also available through the Virtual Fly Brain website.
