---
title: "Overview"
linkTitle: "Overview"
weight: 100
description: >
  What Virtual Fly Brain is, what you can ask it, and where to go next.
---

Virtual Fly Brain is a knowledge base for the *Drosophila melanogaster* nervous system. It brings
together data produced by many different laboratories — electron microscopy reconstructions and the
connectomes derived from them, confocal images of driver line expression, single-neuron and clonal
morphologies, and single-cell transcriptomics — and makes them queryable together rather than one
study at a time.

Two things make that work. Images are registered onto a small set of
[standard templates](/docs/data/templates/), so material from different studies sits in the same
coordinate space and can be compared directly. And everything is classified with terms from the
Drosophila Anatomy Ontology, so a query for a cell type returns data from every study that reported
it, whatever that study happened to call it.

## What you can ask

- **Find a cell type or a region**, and see every neuron, image and dataset VFB holds for it.
- **Follow connectivity** — what synapses onto a neuron, what it synapses onto, and how that differs
  between connectomes.
- **Go from a neuron to a reagent.** Given a cell type, find the split-GAL4 or GAL4 lines reported to
  label it, and the stock that carries them.
- **Search by shape.** [NBLAST](/docs/concepts/nblast/) finds morphologically similar neurons across
  datasets, including matching an EM reconstruction against light-microscopy expression patterns.
- **Compare across datasets**, because the same ontology terms are applied to all of them.

## Where to go next

- [Concepts](/docs/concepts/) — the ideas the data model rests on: cell types, templates, bridging
  registrations, similarity scores and confidence values.
- [Data](/docs/data/) — what VFB actually holds, dataset by dataset, and where each came from.
- [Website features](/docs/website-features/) — how to drive the interface: search, Term Info and the
  viewers.
- [APIs](/docs/apis/) and [Tutorials](/docs/tutorials/) — the same data from Python, R or an AI
  assistant.

## A tour of the site

{{< youtube id="z2Cre6avnpk" class="video-embed" >}}

The walkthrough above covers the main interface. Note that it predates some later changes to the
site, so a few details will differ from what you see now.
