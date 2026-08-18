---
title: "Bridging Registrations"
weight: 304
date: 2026-08-18
tag: [Template,Registration,Alignment,nat,navis,flybrains,Transforms]
description: >
  Transformations to map between different canonical Drosophila templates, where VFB keeps
  them, and how a route between two spaces is worked out.
---

A [registration](/docs/concepts/registration/) puts one animal's image into a template's
coordinate space. A **bridging registration** does something different: it maps one
template space onto another, so data registered to different standards can still be
compared.

This matters because no single template ever won. Data on VFB arrives registered to
whichever standard its producers used — JRC2018 unisex, JRC2018F or M, JFRC2, or a
connectome's own space such as the hemibrain, FAFB or MANC — and the only way to put a
FlyWire neuron next to a split-GAL4 expression pattern is to bridge between them.

## Where the transforms live

VFB keeps no private set. Its bridging and mirroring registrations are published through
the community packages — [**navis-flybrains**](https://github.com/navis-org/navis-flybrains)
for Python and [**nat.flybrains**](https://natverse.org/nat.flybrains/index.html) for R —
so the same transform is available to anyone and everyone chaining between two spaces gets
the same answer. A registration that exists only inside one resource is a registration
nobody else can check.

They are a named set in the package. Alongside the Jefferis lab and Janelia collections,
`flybrains` provides a one-off download of "various CMTK bridging and mirror transforms
generated or collated by VirtualFlyBrain.org":

```python
import flybrains

flybrains.download_jefferislab_transforms()   # CMTK, Jefferis lab
flybrains.download_jrc_transforms()           # H5, Janelia brain
flybrains.download_jrc_vnc_transforms()       # H5, Janelia VNC
flybrains.download_vfb_transforms()           # CMTK, VirtualFlyBrain.org

flybrains.report()   # what is actually available, Python and R downloads alike
```

If you already hold these registrations from the R side, `flybrains` will find and register
them rather than duplicating the download. Using the Jefferis lab or VFB transforms needs
[CMTK](https://www.nitrc.org/projects/cmtk/) installed; the FANC and BANC transforms need
[elastix](https://elastix.lumc.nl/index.php).

The package ships metadata and surface meshes for 31 light-level templates and connectome
datasets, and wraps several kinds of transform — CMTK registrations, H5 deformation
fields, elastix transforms and landmark-based (thin-plate spline) mappings. Which
technology underlies a given hop is mostly invisible in normal use.

## It is a graph, and the route is computed

<p align="center">
<img src="https://github.com/schlegelp/navis-flybrains/blob/main/_static/bridging_graph.png?raw=true" width="800" alt="Graph of bridging registrations between Drosophila template spaces">
</p>

The picture is not an illustration — it is the data structure. Each template space is a
node, each registration an edge, and a conversion between two spaces is a **path** through
it. Most useful pairs are not directly connected, so the transform you actually apply is
usually a **sequence**, assembled on demand. Asking navis to take a point from FAFB to
JRC2018F, for example, routes it through several intermediate spaces including a unit
conversion:

```
JRCFIB2018Fraw → JRCFIB2018F → JRCFIB2018Fum → JRC2018F
```

The routing rules are what make this practical:

- **Shortest path, by weight.** Every edge carries a cost and the route is the cheapest
  path from source to target, not necessarily the one with fewest hops.
- **Edges can be traversed backwards.** Many registrations are invertible, so a transform
  registered A→B can serve B→A. Running one in reverse has its own cost, so the router can
  be told to detour rather than invert.
- **A purpose-built registration beats an inverted one** where a pair of spaces is joined
  by both, regardless of which is cheaper.
- **Some hops are free.** Aliases — the same space under another name, or the same data in
  different units — are registered at zero cost so they never distort a route.
- **A single edge may itself be multi-stage.** Some CMTK registrations need an affine
  applied before or after the main warp; these become extra intermediate nodes.
- **Units are explicit.** EM datasets are natively in nanometres or voxels, so their spaces
  carry unit-tagged names. This is what stops a correctly-routed transform silently
  producing an answer off by a factor of a thousand.

## Using them

Importing `flybrains` registers everything with
[navis](https://navis-org.github.io/navis/stable/), after which a conversion is one call:

```python
import navis, flybrains
import numpy as np

points = np.array([[429536, 205240, 38400]])
navis.xform_brain(points, source='FAFB', target='JRC2018F')
# array([[241.53969657, 100.99399233, 35.96977733]])
```

`xform_brain` reports the path it took, so you can see how many hops a comparison actually
went through. To see what is registered before you start,
`navis.transforms.registry.summary()` tabulates every transform with its source, target,
invertibility and weight.

**Mirroring** is a related operation with its own transforms: `navis.mirror_brain()`
reflects coordinates about the midpoint of the mirror axis, then applies a warp to
compensate for asymmetry. A symmetrical template such as JRC2018F needs only the
reflection; an asymmetrical one benefits from the warp. Mirroring is how VFB brings data
onto one side of the brain so that left and right examples of a cell type can be compared.

Full detail is in the
[navis transforms tutorial](https://navis-org.github.io/navis/stable/generated/gallery/6_misc/tutorial_misc_01_transforms/).
The R equivalents live in [nat.flybrains](https://natverse.org/nat.flybrains/index.html),
part of the natverse ([Bates et al., 2020](https://doi.org/10.7554/eLife.53350)).

## What it costs

- **Chaining compounds error.** Each bridge is an approximation, and a four-hop route
  applies four of them in series. The navis documentation is explicit that longer paths
  risk greater spatial distortion. A comparison made within one space is stronger evidence
  than one made across a long path — and since the route is computed rather than declared,
  it is worth looking at how long it is before trusting a fine-grained result.
- **Coverage is not uniform.** Transforms exist between the spaces people needed to
  connect. Some pairs are reachable only by a long path, and some not at all.
- **Units must be consistent through the chain.** The unit-tagged spaces exist precisely
  because this is the easy mistake to make.
- **A bridged position is still an estimate.** See
  [registration](/docs/concepts/registration/) for what that means for fine structures, and
  [templates](/docs/data/templates/) for the spaces themselves.

## Sources

- navis-flybrains — [documentation and source](https://github.com/navis-org/navis-flybrains). Schlegel P, Court R. doi:10.5281/zenodo.4966640
- navis — [transforms tutorial](https://navis-org.github.io/navis/stable/generated/gallery/6_misc/tutorial_misc_01_transforms/)
- nat.flybrains — [documentation](https://natverse.org/nat.flybrains/index.html)
- Bates AS et al. (2020) The natverse, a versatile toolbox for combining and analysing neuroanatomical data. *eLife* 9:e53350. doi:10.7554/eLife.53350
