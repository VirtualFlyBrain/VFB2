---
title: "Connectivity Data"
linkTitle: "Connectivity"
weight: 504
date: 2026-08-15
tags: ["connectome","EM","connectivity"]
description: >-
    Synaptic connectivity on Virtual Fly Brain — what an edge is, which connectomes
    contribute one, and how to query across them.
---

Connectivity is derived data: it comes out of the [EM datasets](/docs/data/em/), but VFB
holds and queries it separately from the images. Loading it into one knowledge graph,
with both ends of every edge classified against the Drosophila Anatomy Ontology, is what
makes it possible to ask a question once and have it answered across every connectome
at the same time, rather than once per resource in each resource's own vocabulary.

{{< vfb-figures set="connectivity" >}}

## What an edge means

A VFB connectivity edge records that a reconstruction reported synapses between two
neurons, and how many. It is evidence from one dataset, not a biological fact: two
neurons may be connected in the animal and unconnected in a partial reconstruction, and
a weak edge may be a segmentation artefact. Treat every count as attributable to the
connectome it came from.

VFB holds four kinds of connection:

| From | To | What it is |
|---|---|---|
| Neuron (individual) | Neuron (individual) | The connectome proper — one reconstructed neuron synapsing onto another |
| Neuron (individual) | Region (individual) | Synapses a neuron makes within a named neuropil, used for region-level input and output profiles |
| Neuron (class) | Muscle (class) | Curated motor innervation, from the literature rather than from EM |
| Neuron (class) | Sense organ (class) | Curated sensory innervation, likewise |

The first two are per-individual and come from EM. The last two are per-class and come
from curation, so they carry no synapse counts and cover far fewer entities. The
[content report](/blog/2022/01/01/vfb-content-report/) gives the current size of each.

## Which connectomes contribute

| Dataset | VFB symbol | Coverage |
|---|---|---|
| BANC v626 | `BANC` | Full CNS, adult female |
| FlyWire v783 (FAFB) | `fw` | Full brain, adult female |
| male-CNS v0.9 | `mc` | Full CNS, adult male |
| MANC v1.2.1 | `mv` | Full VNC, adult male |
| Optic-lobe v1.0.1 | `ol` | Optic lobe, adult male |
| hemibrain v1.2.1 | `hb` | Partial brain, adult female |
| FAFB (CATMAID) | `fafb` | Full brain, adult female — sparse reconstruction |
| L1 CNS (CATMAID) | `l1em` | Full CNS, first-instar larva |

Versions matter: a connectome is re-released as proofreading progresses, neuron
identifiers do not always survive between versions, and VFB states the version it holds.
See [EM dataset versioning](/docs/data/em/versioning/).

### Overlapping reconstructions

Several of these reconstruct the *same tissue*. The hemibrain, the sparse FAFB CATMAID
reconstruction and FlyWire all cover adult female brain, and a connection present in
more than one of them is one biological connection reported several times, not several
connections. Summing partner counts across all datasets therefore inflates them.

The convention VFB and `VFB_connect` follow is to exclude `hb` and `fafb` from
cross-dataset connectivity queries by default, leaving FlyWire as the adult female brain
source. Change that when the question calls for it — comparing reconstructions against
each other, for instance — but change it deliberately.

## Querying it

Connectivity queries are available from the Term Info pane of any neuron or region, and
programmatically through [`VFB_connect`](/docs/apis/) and the MCP server.

- **Partners of one neuron type.** Ask for its inputs or outputs. The default weight
  threshold is 5 synapses; lower it only if you are prepared to look at the weak edges
  individually.
- **Between two neuron types.** A pairwise query returns the edges between them in each
  contributing dataset separately, which is usually what you want to see.
- **For a region.** Regions take a different set of queries from neurons. Ask a
  neuropil for the neurons presynaptic or postsynaptic in it, not for its connectivity
  partners.

Direction is easy to invert, so it is worth stating plainly: neurons *presynaptic in* a
region have their presynaptic terminals there and are providing input to it; neurons
*postsynaptic in* a region receive there. A query for the inputs to a region returns the
presynaptic set.

## What the numbers do and do not say

The neuron counts above are the neurons VFB holds connectivity for, which is not the
number of neurons in a fly. Absence is likewise not evidence: a cell type with no
connectivity on VFB may simply not be reconstructed in any dataset VFB has loaded, or
may not yet be matched between the connectome's own naming and the ontology. Where a
connectome's identifiers have not been mapped onto ontology classes, the neurons are
still present and queryable individually.
