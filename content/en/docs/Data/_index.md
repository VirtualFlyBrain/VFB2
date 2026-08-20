---
title: "Data on VFB"
linkTitle: "Data"
weight: 500
date: 2026-08-15
description: >
  Types of data and datasets that are available on Virtual Fly Brain.
cascade:
- type: "docs"
  target:
    path: "/**"
---

Virtual Fly Brain integrates *Drosophila melanogaster* nervous system data from many
laboratories into one queryable resource. Two things make that integration work, and
both apply to every datatype below: images are registered onto a small set of
[standard templates](/docs/data/templates/) so that data from different studies can be
compared in the same coordinate space, and everything is classified with terms from the
Drosophila Anatomy Ontology (DAO) so that a query for a cell type returns data from
every study that reported it, whatever that study called it.

{{< vfb-figures set="overview" >}}

The figures above come from the [content report](/blog/2022/01/01/vfb-content-report/),
which is regenerated against the production knowledge base after every data release.

## What is here

| Datatype | What it covers | Page |
|---|---|---|
| Electron microscopy | Dense and sparse EM reconstructions of the adult brain, VNC and larval CNS, with neuron morphology and synaptic connectivity | [EM data](/docs/data/em/) |
| Connectivity | Neuron-to-neuron and neuron-to-region synaptic connections derived from the EM datasets | [Connectivity data](/docs/data/connectivity/) |
| Light microscopy | Driver line expression patterns, split-GAL4 combinations, single-neuron and clonal images from confocal microscopy | [LM data](/docs/data/lm/) |
| Single-cell transcriptomics | Cell clusters and their gene expression from scRNAseq and snRNAseq studies | [scRNAseq data](/docs/data/scrnaseq/) |
| Templates and regions | The reference brains and VNCs everything is registered to, and the painted neuropil domains in each | [Templates](/docs/data/templates/) |

VFB also hosts the public [CATMAID instances](/hosted/) for several community EM
datasets, in some cases as the only remaining public copy after the original host went
offline.

## Where the data comes from, and where it goes

Most data on VFB is published data that VFB has registered, classified and indexed —
VFB is an integrator, not usually the originator. Every dataset therefore carries its
original publication, and every image links back to the resource it came from. Cite the
original study when you use the data, and cite
[Court et al. (2023)](https://doi.org/10.3389/fphys.2023.1076533) for VFB itself.

Data can be reached three ways: through the
[3D browser](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto),
programmatically through the [APIs](/docs/apis/) — `VFB_connect` for Python, the
knowledge graph, and the MCP server — and by download of individual images from their
[Term Info](/docs/website-features/terminfo/#data) pages, in NRRD, Woolz, OBJ and SWC as
available.

## Licences

Licence terms differ per dataset and are set by the original producer, not by VFB. Where
a dataset carries a licence it is shown on its Term Info page. Some older datasets
predate the practice and carry none recorded; absence of a stated licence on VFB is not
a grant of permission, so check with the original resource before redistributing.
