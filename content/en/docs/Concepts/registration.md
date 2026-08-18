---
title: "Image Registration"
linkTitle: "Registration"
weight: 305
date: 2026-08-18
categories: ["overview","help"]
tags: ["Registration","Template","Alignment","CMTK","ANTs","JRC2018"]
description: >
  How an image of one fly's brain is warped onto a standard template, why VFB depends on
  it, and what it costs in accuracy.
---

No two fly brains are the same shape. Two confocal stacks of the same driver line, from
two animals, differ in size, orientation and local geometry — enough that voxel *(x, y,
z)* in one is not the same anatomical place as voxel *(x, y, z)* in the other.

**Registration** is the step that fixes this: computing a spatial transformation that maps
each sample onto a common [template](/docs/data/templates/). It is the single operation
that makes VFB possible. Without it, an expression pattern from one lab and a neuron from
another are two unrelated pictures; with it, they are two objects in one coordinate space
that can be overlaid, scored for overlap and searched against each other.

## How it works

Registration is driven by a **reference channel** rather than by the signal you care
about. In fly work that is usually a neuropil counterstain — anti-Bruchpilot (nc82) is the
standard — which looks broadly the same in every animal and therefore gives the algorithm
something stable to match. The transformation computed from that channel is then applied
to the signal channel.

The transformation is found in stages of increasing freedom:

1. **Rigid** — rotate and translate to correct mounting orientation.
2. **Affine** — add scaling and shear to correct overall size and proportion.
3. **Non-rigid (deformable)** — a smooth, spatially varying warp that brings individual
   structures into correspondence.

The non-rigid step is what actually does the work, and it is why registration is expensive
and imperfect. Two toolkits dominate fly registration. **CMTK** is the more common; the
paper usually cited for it describes a parallel implementation of non-rigid registration,
demonstrated on clinical and other biomedical problems rather than on flies
([Rohlfing and Maurer, 2003](https://doi.org/10.1109/TITB.2003.808506)) — it was
[Jefferis et al. (2007)](https://doi.org/10.1016/j.cell.2007.01.040) who established the
approach for *Drosophila*, registering brains to a common template to build comparable maps
of olfactory projections. **ANTs** is the other, whose symmetric diffeomorphic model (SyN)
yields an invertible transformation
([Avants et al., 2008](https://doi.org/10.1016/j.media.2007.06.004)).

## Why templates are built from many brains

Registering to a single individual's brain bakes that individual's idiosyncrasies into
every result. Modern templates are therefore **averages**, built by groupwise registration
of many samples so that no one animal dominates.

JRC2018, the current standard, was constructed this way: 36 female and 26 male individuals
for the sex-specific central brain templates, and 62 individuals — 124 images counting
left–right flips — for the unisex template
([Bogovic et al., 2020](https://doi.org/10.1371/journal.pone.0236495)). Earlier standards
such as JFRC2010 were single representative brains, which is part of why registration onto
them is less accurate.

The templates VFB uses, and the painted neuropil domains in each, are listed on the
[Templates](/docs/data/templates/) page.

## Two registrations, not one

It is worth keeping these separate, because they fail differently:

| | Sample registration | [Bridging registration](/docs/concepts/bridging/) |
|---|---|---|
| Maps | One animal's image → a template | One template → another template |
| Computed | Per image, by the data producer | Once, and reused |
| Driven by | The sample's reference channel | The two templates themselves |
| Typical failure | Poor stain, damaged tissue, unusual morphology | Accumulated error when chaining transforms |

Data arrives on VFB already registered by the group that produced it, to whichever
template that group used. Bridging transforms are what let a neuron registered to one
template be compared against data in another; chaining several compounds the error, so a
comparison across two bridges is weaker evidence than one within a single space.

## What registration costs you

- **A registered neuron is an estimate.** Its position in template space is where the warp
  put it, not where it was in its own brain. Fine structures — thin neurites, small
  boutons — move most.
- **Accuracy is not uniform.** Registration is generally better in large, well-stained
  neuropils than at the brain surface, in the optic lobes, or anywhere the sample was
  torn or compressed during dissection.
- **Overlap is not contact.** Two registered objects occupying the same template voxels
  are near each other in a common space. That is a hypothesis about connectivity, not
  evidence of a synapse; for that you need EM
  ([connectivity data](/docs/data/connectivity/)).
- **EM volumes need their own alignment.** Bringing an EM reconstruction into a light
  microscopy template space is a separate, harder problem than registering one confocal
  stack to another, and the transforms involved are listed with the
  [templates](/docs/data/templates/).

## What VFB actually does

Most data arrives already registered by the group that produced it. Where it does not, VFB
registers it with **CMTK, using nine degrees of freedom followed by a non-rigid
registration**. Data can be moved to one side of the brain by flipping and applying a
mirroring registration, and bridging transforms are used wherever possible to bring images
from external templates, or from one VFB template to another, into a common space
([Court et al., 2023](https://doi.org/10.3389/fphys.2023.1076533)).

The point of all this is comparison at scale: VFB's main adult brain template carries
almost 100,000 cross-registered images from 64 datasets — EM reconstructions, single
neurons, lineage clones and expression patterns — in one coordinate space. Every image is
given a persistent, resolvable VFB URL, which matters because local identifiers from
source resources are not globally unique; the CATMAID instances VFB hosts have clashing
neuron IDs between them.

## Working with it

Transforms between the common fly template spaces are packaged for programmatic use in
the natverse ecosystem — `nat.templatebrains` and `navis-flybrains` — described in
[Bates et al. (2020)](https://doi.org/10.7554/eLife.53350). VFB's own
[APIs](/docs/apis/) return coordinates in template space, and the
[bridging registrations](/docs/concepts/bridging/) page shows which conversions exist.

## Sources

- Rohlfing T, Maurer CR (2003) Nonrigid image registration in shared-memory multiprocessor environments with application to brains, breasts, and bees. *IEEE Trans Inf Technol Biomed* 7:16–25. doi:10.1109/TITB.2003.808506
- Jefferis GSXE et al. (2007) Comprehensive maps of *Drosophila* higher olfactory centers: spatially segregated fruit and pheromone representation. *Cell* 128:1187–1203. doi:10.1016/j.cell.2007.01.040
- Avants BB et al. (2008) Symmetric diffeomorphic image registration with cross-correlation. *Med Image Anal* 12:26–41. doi:10.1016/j.media.2007.06.004
- Bates AS et al. (2020) The natverse, a versatile toolbox for combining and analysing neuroanatomical data. *eLife* 9:e53350. doi:10.7554/eLife.53350
- Bogovic JA et al. (2020) An unbiased template of the *Drosophila* brain and ventral nerve cord. *PLoS ONE* 15(12):e0236495. doi:10.1371/journal.pone.0236495
- Court R et al. (2023) Virtual Fly Brain — an interactive atlas of the *Drosophila* nervous system. *Front Physiol* 14:1076533. doi:10.3389/fphys.2023.1076533
