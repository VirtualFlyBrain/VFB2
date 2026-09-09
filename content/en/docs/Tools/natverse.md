---
title: "natverse"
linkTitle: "natverse"
weight: 657
description: >
  The R toolchain — nat and its companion packages for importing, transforming, comparing
  and plotting neurons.
---

The natverse is a collection of interoperable R packages for working with 3D neuroanatomical
data. It covers much the same ground as [navis](/docs/tools/navis/) and its ecosystem does in
Python, so which you reach for is usually decided by what the rest of your analysis is written
in rather than by capability.

The pieces you are most likely to want:

`nat` is the core — reading, manipulating and plotting neurons and surfaces.
`nat.templatebrains` and `nat.flybrains` provide the template spaces and the bridging and
mirroring registrations between them, the R counterpart to
[flybrains](/docs/tools/navis-flybrains/). `nat.nblast` implements
[NBLAST](/docs/tools/nblast/). `neuprintr` queries [neuPrint](/docs/tools/neuprint/), and
`elmr` supports EM–light-microscopy comparison.

## Install

```r
install.packages('natmanager')
natmanager::install('core')      # nat and the essentials
natmanager::install('natverse')  # everything
```

## Transforms need CMTK

The VFB and Jefferis lab registrations that `nat.flybrains` uses are CMTK transforms, so
applying them needs [CMTK installed](/docs/tools/cmtk/) and its tools on your `PATH`. `nat`
locates them with `cmtk.bindir()`; if that returns nothing, CMTK is either not installed or not
where R can find it.

VFB publishes the same transform set to both ecosystems, so a route computed here and one
computed in Python agree — see [bridging registrations](/docs/concepts/bridging/) for what
those routes are and what chaining them costs in accuracy.

## Where next

Full documentation: [natverse.org](https://natverse.org/), which links the reference manuals
for each constituent package. The natverse paper is
[Bates et al. (2020)](https://doi.org/10.7554/eLife.53350).
