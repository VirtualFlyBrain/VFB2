---
title: "Bridging Registrations"
weight: 304
date: 2026-08-18
tag: [Template,Registration,Alignment,nat,navis,flybrains,Transforms]
description: >
  Transformations to map between different canonical Drosophila templates, and where VFB
  keeps them.
---

A [registration](/docs/concepts/registration/) puts one animal's image into a template's
coordinate space. A **bridging registration** does something different: it maps one
template space onto another, so data registered to different standards can still be
compared.

This matters because no single template ever won. Data on VFB arrives registered to
whichever standard its producers used — JRC2018 unisex, JRC2018F or M, JFRC2, a
connectome's own space such as the hemibrain or FAFB — and the only way to put a FlyWire
neuron next to a split-GAL4 expression pattern is to bridge between them.

## Where the transforms live

VFB does not keep a private set of these. The bridging and mirroring transforms are
maintained in the community packages — **navis-flybrains** for Python and
**nat.flybrains** for R — so that the same transform is available to anyone, and everyone
chaining between two spaces gets the same answer. A registration that only exists inside
one resource is a registration nobody else can check.

Between them these packages cover 30-odd template and connectome spaces — including
JRC2018F/M/U, JFRC2, FAFB14, FlyWire, the hemibrain (JRCFIB2018F), maleCNS
(JRCFIB2022M), MANC, FANC and BANC — and wrap several kinds of transform: CMTK
registrations, H5 deformation fields, Elastix transforms and landmark-based mappings.
Which underlying technology is used is mostly invisible in normal use.

<p align="center">
<img src="https://github.com/schlegelp/navis-flybrains/blob/main/_static/bridging_graph.png?raw=true" width="800">
</p>

## It is a graph, and the route is computed

The picture above is not an illustration — it is the data structure. Each template space
is a node, each registration an edge, and a conversion between two spaces is a **path**
through it. Most useful pairs are not directly connected, so the transform you actually
apply is usually a **sequence of several**, assembled on demand.

The routing is what makes this practical:

- **Shortest path, by weight.** Every edge carries a cost, and the route is the
  cheapest path from source to target — not necessarily the one with fewest hops.
  Lower weight wins.
- **Edges can be traversed backwards.** Many registrations are invertible, so a
  transform registered as A→B can be used to get from B to A. Running one in reverse
  carries its own cost, so the router can be told to detour rather than go backwards.
- **A purpose-built registration beats an inverted one.** Where two spaces are joined
  both by a registration made for that direction and by the inverse of its counterpart,
  the purpose-built one is used regardless of which is cheaper.
- **Some hops are free.** Aliases — the same space under another name, or the same data
  in different units — are registered at zero cost, so they never distort a route.
- **A single registration may itself be multi-stage.** Some CMTK transforms need an
  affine applied before or after the main warp; these are modelled as extra intermediate
  nodes, so what looks like one edge can be several transforms deep.
- **Units are explicit.** EM datasets are natively in nanometres or voxels rather than
  microns, so their spaces are registered under unit-tagged names to stop a
  correctly-routed transform silently producing a result off by a factor of a thousand.

You can ask for the route before running it, and force it through a particular
waystation if you need to.

## Using them

In Python, importing `flybrains` registers the transforms with
[navis](https://navis.readthedocs.io/en/latest/source/tutorials/transforming.html), after
which a conversion is one call:

```python
import navis, flybrains

# run a conversion — the route is worked out for you
navis.xform_brain(neuron, source='FAFB', target='JRC2018F')

# or ask what it would do first
navis.transforms.registry.shortest_bridging_seq(source='FAFB', target='JRC2018F')
```

In R the equivalent lives in [nat.flybrains](https://natverse.org/nat.flybrains/index.html),
part of the natverse ([Bates et al., 2020](https://doi.org/10.7554/eLife.53350)).

## What it costs

- **Chaining compounds error.** Each bridge is an approximation, and a route of four hops
  applies four of them in series. A comparison made within one space is stronger evidence
  than one made across a long path — and because the route is computed rather than
  declared, it is worth checking how long it actually is before trusting a fine-grained
  result.
- **Coverage is not uniform.** Transforms exist between the spaces people needed to
  connect. Some pairs are reachable only by a long path, and some not at all.
- **A bridged position is still an estimate.** See
  [registration](/docs/concepts/registration/) for what that means for fine structures,
  and [templates](/docs/data/templates/) for the spaces themselves.
