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

Two confocal stacks of the same driver line, taken from two animals, will differ in size,
orientation and local geometry. No two fly brains are quite the same shape, so voxel *(x, y,
z)* in one stack is not the same anatomical place as voxel *(x, y, z)* in the other.

Registration corrects for this by computing a spatial transformation that maps each sample
onto a common [template](/docs/data/templates/). That is what allows an expression pattern
from one lab and a neuron from another to be overlaid, scored for overlap and searched
against each other, and most of what VFB does depends on it.

## How it works

Registration works from a **reference channel** rather than from the signal you are
interested in. In fly work that is usually a neuropil counterstain, most often
anti-Bruchpilot (nc82), which looks broadly the same in every animal and so gives the
algorithm something stable to match on. The transformation computed from that channel is then
applied to the signal channel.

The transformation is found in stages of increasing freedom:

1. **Rigid**: rotate and translate to correct mounting orientation.
2. **Affine**: add scaling and shear to correct overall size and proportion.
3. **Non-rigid (deformable)**: a smooth, spatially varying warp that brings individual
   structures into correspondence.

The non-rigid step does most of the work, and is also why registration is computationally expensive and never exact. Two toolkits dominate fly registration. [**CMTK**](/docs/tools/cmtk/) is the more common; the paper usually cited for it describes a parallel implementation of non-rigid registration, demonstrated on clinical and other biomedical problems rather than on flies ([Rohlfing and Maurer, 2003](https://doi.org/10.1109/TITB.2003.808506)) — it was [Jefferis et al. (2007)](https://doi.org/10.1016/j.cell.2007.01.040) who established the approach for *Drosophila*, registering brains to a common template to build comparable maps of olfactory projections.
[Jefferis et al. (2007)](https://doi.org/10.1016/j.cell.2007.01.040) who established the
approach for *Drosophila*, registering brains to a common template to build comparable maps
of olfactory projections. The other is **ANTs**, whose symmetric diffeomorphic model (SyN)
yields an invertible transformation
([Avants et al., 2008](https://doi.org/10.1016/j.media.2007.06.004)).

## Why templates are built from many brains

If you register to a single individual's brain, that individual's idiosyncrasies end up in
every result. Modern templates are therefore **averages**, built by groupwise registration of
many samples so that no one animal dominates.

JRC2018, the current standard, was constructed this way: 36 female and 26 male individuals
for the sex-specific central brain templates, and 62 individuals (124 images, counting
left–right flips) for the unisex template
([Bogovic et al., 2020](https://doi.org/10.1371/journal.pone.0236495)). Earlier standards
such as JFRC2010 were single representative brains, which is part of why registration onto
them is less accurate.

The templates VFB uses, and the painted neuropil domains in each, are listed on the
[Templates](/docs/data/templates/) page.

## Two registrations, not one

These two are worth keeping separate, as they fail in different ways:

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

- A registered neuron's position is an estimate. It sits where the warp put it, rather than
  where it was in its own brain, and fine structures such as thin neurites and small boutons
  move the most.
- Accuracy varies across the brain. Registration is generally better in large, well-stained
  neuropils than at the brain surface, in the optic lobes, or anywhere the sample was torn or
  compressed during dissection.
- Overlap does not demonstrate contact. Two registered objects occupying the same template
  voxels are near each other in a common space, which is a hypothesis about connectivity
  rather than evidence of a synapse. For that you need EM
  ([connectivity data](/docs/data/connectivity/)).
- EM volumes need their own alignment. Bringing an EM reconstruction into a light microscopy
  template space is a separate and harder problem than registering one confocal stack to
  another, and the transforms involved are listed with the
  [templates](/docs/data/templates/).

## What VFB actually does

Most data arrives already registered by the group that produced it. Where it does not, VFB
currently registers it with **CMTK, using nine degrees of freedom followed by a non-rigid
registration**. Data can be moved to one side of the brain by flipping and applying a
mirroring registration, and bridging transforms are used wherever possible to bring images
from external templates, or from one VFB template to another, into a common space
([Court et al., 2023](https://doi.org/10.3389/fphys.2023.1076533)).

VFB publishes those bridging transforms through
[**navis-flybrains**](https://github.com/navis-org/navis-flybrains) and its R counterpart
[**nat.flybrains**](https://natverse.org/nat.flybrains/index.html), where they are a named
set retrievable with `flybrains.download_vfb_transforms()`. The same transform therefore
gives the same answer whether it runs inside VFB or in someone else's analysis. See
[bridging registrations](/docs/concepts/bridging/).

The result is comparison at scale. VFB's main adult brain template carries almost 100,000
cross-registered images from 64 datasets (EM reconstructions, single neurons, lineage clones
and expression patterns) in one coordinate space. Every image is given a persistent,
resolvable VFB URL, which matters because local identifiers from source resources are not
globally unique: the CATMAID instances VFB hosts have clashing neuron IDs between them.

## Working with it

Transforms between the common fly template spaces are packaged for programmatic use in
[navis-flybrains](https://github.com/navis-org/navis-flybrains) for Python and the natverse
packages `nat.templatebrains` / `nat.flybrains` for R
([Bates et al., 2020](https://doi.org/10.7554/eLife.53350)); the
[navis transforms tutorial](https://navis-org.github.io/navis/stable/generated/gallery/6_misc/tutorial_misc_01_transforms/)
covers applying them. VFB's own [APIs](/docs/apis/) return coordinates in template space,
and the [bridging registrations](/docs/concepts/bridging/) page shows which conversions
exist and how a route between two spaces is chosen.

## Sources

- Rohlfing T, Maurer CR (2003) Nonrigid image registration in shared-memory multiprocessor environments with application to brains, breasts, and bees. *IEEE Trans Inf Technol Biomed* 7:16–25. doi:10.1109/TITB.2003.808506
- Jefferis GSXE et al. (2007) Comprehensive maps of *Drosophila* higher olfactory centers: spatially segregated fruit and pheromone representation. *Cell* 128:1187–1203. doi:10.1016/j.cell.2007.01.040
- Avants BB et al. (2008) Symmetric diffeomorphic image registration with cross-correlation. *Med Image Anal* 12:26–41. doi:10.1016/j.media.2007.06.004
- Bates AS et al. (2020) The natverse, a versatile toolbox for combining and analysing neuroanatomical data. *eLife* 9:e53350. doi:10.7554/eLife.53350
- Bogovic JA et al. (2020) An unbiased template of the *Drosophila* brain and ventral nerve cord. *PLoS ONE* 15(12):e0236495. doi:10.1371/journal.pone.0236495
- Court R et al. (2023) Virtual Fly Brain — an interactive atlas of the *Drosophila* nervous system. *Front Physiol* 14:1076533. doi:10.3389/fphys.2023.1076533
