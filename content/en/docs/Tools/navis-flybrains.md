---
title: "flybrains"
linkTitle: "flybrains"
weight: 653
description: >
  Template brains and bridging transforms for navis — move neurons and points between
  Drosophila template spaces.
---

`flybrains` supplies `navis` with the *Drosophila* template brains and the transforms between
them. Once it is imported, `navis.xform_brain` can move neurons, meshes or raw points between
template spaces — FAFB to JRC2018F, hemibrain to JRC2018F, and so on — by finding a route
through the registered transforms.

VFB publishes its own bridging and mirroring transforms through this package, so the transform
that moves a neuron inside VFB is the same one you get in your own analysis. The
[bridging registrations](/docs/concepts/bridging/) page explains what those transforms are and
how routes between spaces are chosen; this page is about installing and using them.

## Install

```sh
pip3 install flybrains
```

The package itself is small: the transforms are downloaded separately, on request.

## Quick start

```python
import navis
import flybrains
import numpy as np

# One-off downloads -- pick the collections you need
flybrains.download_jefferislab_transforms()   # CMTK, Jefferis lab
flybrains.download_jrc_transforms()           # H5, Janelia brain
flybrains.download_vfb_transforms()           # CMTK, VirtualFlyBrain.org
flybrains.register_transforms()

points = np.array([[429536, 205240, 38400]])
navis.xform_brain(points, source='FAFB', target='JRC2018F')
# array([[241.53969657, 100.99399233,  35.96977733]])
```

`flybrains.report()` lists what is actually available to you, across both the Python and R
downloads — worth running when a transform you expected is not found.

## CMTK is required for some transforms

The Jefferis lab and VFB transform collections are CMTK registrations, so using them needs
[CMTK installed](/docs/tools/cmtk/) and on your `PATH`. The Janelia H5 transforms do not. If a
transform route fails with CMTK missing, that is what it is telling you.

The FANC and BANC transforms need [elastix](/docs/tools/elastix/) instead.

## Where next

Full documentation and the list of supported spaces:
[navis-org/navis-flybrains](https://github.com/navis-org/navis-flybrains). The navis
[transforms tutorial](https://navis-org.github.io/navis/stable/generated/gallery/6_misc/tutorial_misc_01_transforms/)
covers applying them in practice.

On the R side, [nat.templatebrains and nat.flybrains](/docs/tools/natverse/) provide the
equivalent, drawing on the same transform collections.
