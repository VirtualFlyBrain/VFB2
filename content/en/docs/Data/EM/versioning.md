---
title: "Dataset Versions and Deprecation"
linkTitle: "Versions & Deprecation"
categories: ["overview","help"]
tags: ["EM","Connectomics","DataSet","Deprecation","Versioning","Site","Connectivity"]
weight: 5
date: 2026-06-30
description: >
  How Virtual Fly Brain handles neurons, connectivity, data sources and cross-references when new versions of connectomic datasets are released.
---

Connectomic datasets are not static: reconstructions are re-released as proofreading
improves, neurons are split, merged or re-identified, and the resources that host them
may occasionally move or shut down. When VFB ingests a new release, it must decide what
happens to the entities from the previous version. This page documents those policies so
that users understand why a neuron, link or connection may change, disappear, or persist
between releases.

## Affected entities

A connectomic dataset is represented in VFB by several types of graph node and edge:

| Node / edge                                            | What it represents                                                                                                                                                                                                              |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DataSet nodes**                                      | A specific released version of a dataset (e.g. a FlyWire release). Neurons are attached to it via `has_source`.                                                                                                                 |
| **Site (data source) nodes**                           | The external resource that hosts the data (e.g. Codex, NeuPrint, CATMAID). Holds the `link_base` used to build cross-reference links, and is flagged `is_data_source = [true]` when it is the canonical source for its neurons. |
| **Neuron (Individual) nodes**                          | A single reconstructed neuron, cell typed by linking to anatomy ontology (FBbt) nodes via `INSTANCEOF` edges, with other annotations (soma location, developmental origin, sex, etc.) linked via other edge types.               |
| **Image / Channel nodes**                              | The Neuron's aligned image(s) and the channel(s) registered to a template.                                                                                                                                                      |
| **Connectivity edges**                                 | Synaptic connectivity (`synapsed_to`) between Neurons, and [regional connectivity](/docs/data/em/region-connectivity/) — each Neuron's synapse tallies per neuropil region.                                                     |
| **Cross-reference edges** (`database_cross_reference`) | Links a Neuron to a Site, carrying the `accession` (the Neuron's ID in that resource).                                                                                                                                          |

## Core principle: Site and Neuron deprecation are independent

Whether a **Site** is deprecated and whether a **Neuron** is deprecated are decided
separately. A Neuron can be valid while its data source is deprecated, and a data source can
remain live while individual Neurons within it are retired. The two states are tracked
independently and have different consequences (below).

Deprecation does **not** delete a node. The node and its identifier are retained (so old
IDs resolve), but it is marked deprecated and treated accordingly.

## What happens when a new dataset version is released

For example, when BANC v626 (the *old* version) is replaced by v888 (the *new* version):

- New nodes are created for the new Site and DataSet, and for any new Neurons in the release (accessions that were not previously in VFB). The markers that identify a Site as the live, canonical connectome source — its symbol (the short dataset code listed in [EM Data](/docs/data/em/)), `Connectome` label and `is_data_source` flag — are transferred from the old Site to the new one (removed from the old, added to the new), so the new Site takes over as the canonical source.
- A `term_replaced_by` edge is added to link the old and new DataSet/Site.
- **Old DataSet** — **deprecated** (superseded by the new DataSet, which it links to via `term_replaced_by`).
- **Old Sites that still exist, i.e. links will still resolve** — _not_ deprecated.
- **Old Sites that no longer exist, i.e. links will not resolve** — **deprecated**.
- **Neurons with accessions that persist in the new data** — _not_ deprecated. They keep their `database_cross_reference` edge to the
  old Site **and** gain an edge to the new Site.
- **Neurons with accessions that are not present in the new data** — **deprecated**. They have no `database_cross_reference` edge to the new 
 Site; their only cross-reference is to the old, deprecated Site.
- **Connectivity edges** are replaced with edges from the new data for Neurons that are not deprecated.
- **Old images** are removed. Images from the new data are loaded for Neurons that are not deprecated.
- **Cell type / FBbt links** are replaced with annotations based on the new data for Neurons that are not deprecated. These may be removed from deprecated Neurons if they are incorrect based on the new data, or retained if they are still valid.
- **Channel** nodes are always retained (_not_ deprecated). Deprecation is not necessary, as all queries are keyed off of the Neuron node.

## What happens when a dataset/site is retired with no replacement

The Site is **deprecated** and there is no new Site.

- **Neurons** — remain valid (_not_ deprecated) and **remain valid query targets**.
  Their only data source is now a deprecated Site, so no link can be built to a live
  resource, but the Neurons, their connectivity and their images are still served.
- **The Site** — **deprecated**, but its `is_data_source` flag remains `[true]` so the Site stays the canonical source for its Neurons. That attribution is what keeps those Neurons discoverable: they continue to be picked up by queries even though their Site is deprecated.
- **The DataSet** — _not_ deprecated: with no replacement version to supersede it, it remains the current representation of the data.

## Effects on the website and queries

These follow from the states above and are enforced when results are generated:

- **Deprecated Neurons** are excluded from connectivity results and from the Neuron counts
  used in connectivity summaries (so they do not appear as partners and do not affect
  percentages).
- **Deprecated Sites** never produce a clickable external link. Where a results table has
  source / accession columns (e.g. instance and similar-neuron tables, connectivity
  tables), the source name and accession are still shown as **plain text** — they are just
  not linked. In the [Term Info](/docs/website-features/terminfo/) cross-reference list,
  whose entries exist specifically to be links, a deprecated Site's entry is omitted.
- **Neurons whose only data source is a deprecated Site** remain valid query
  targets and are returned normally; only their outbound link to the dead resource is
  suppressed.

## Technical note

Both `is_data_source` and the deprecation flag are stored as list-valued annotations in the
database (e.g. `is_data_source = [true]`). Deprecation also surfaces in the search index as
`Deprecated` within the node's `types` list. Result-generating code keys off these
annotations to apply the behaviours above; Site and Neuron deprecation are checked
independently.

## See also

- [EM Data](/docs/data/em/) — the integrated connectomic datasets and their versions.
- [Region Connectivity](/docs/data/em/region-connectivity/) — per-neuron regional synapse tallies, versioned alongside neurons.
- [Resources](/docs/resources/) — the external sites/resources that host the data.
- [Term Info](/docs/website-features/terminfo/) — where cross-references and connectivity are shown.
