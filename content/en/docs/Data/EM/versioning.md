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
| **Neuron (Individual) nodes**                          | A single reconstructed neuron, cell typed by linking to anatomy ontology (FBbt) nodes via `INSTANCEOF` edges, with other annotations (soma location, developmental origin, sex etc.) linked via other edge types.               |
| **Image / Channel nodes**                              | The neuron's aligned image(s) and the channel(s) registered to a template.                                                                                                                                                      |
| **Connectivity edges**                                 | Synaptic connectivity (`synapsed_to`) between neurons.                                                                                                                                                                          |
| **Cross-reference edges** (`database_cross_reference`) | Links a neuron to a Site, carrying the `accession` (the neuron's ID in that resource).                                                                                                                                          |

## Core principle: site and neuron deprecation are independent

Whether a **site** is deprecated and whether a **neuron** is deprecated are decided
separately. A neuron can be valid while its data source is deprecated, and a data source can
remain live while individual neurons within it are retired. The two states are tracked
independently and have different consequences (below).

Deprecation does **not** delete a node. The node and its identifier are retained (so old
IDs resolve), but it is marked deprecated and treated accordingly.

## What happens when a new dataset version is released

e.g. BANC v626 to v888.

- New nodes are created for the new Site and DataSet, and for any new neurons in the release (accessions that were not previously in VFB). The new Site uses the same symbol as the old Site. The `is_data_source` flag, `Connectome` label and symbol are removed from the old Site.
- A `term_replaced_by` edge is added to link the old and new DataSet/Site.
- **Old DataSet** — **deprecated**.
- **Old Sites that still exist, i.e. linkouts will still resolve** — _not_ deprecated. 
- **Old Sites that no longer exist, i.e. linkouts will not resolve** — **deprecated**.
- **Neurons with accessions that persist in the new data** — _not_ deprecated. They keep their `database_cross_reference` edge to the
  old Site **and** gain an edge to the new Site.
- **Neurons with accessions that are not present in the new data** — **deprecated**. They have no `database_cross_reference` edge to the new 
 Site; their only cross-reference is to the old, deprecated Site.
- **Connectivity edges** are replaced with edges from the new data for neurons that are not deprecated.
- **Images** are replaced with images from the new data for neurons that are not deprecated, old Channel nodes are _not_ deprecated when their Neurons are.
- **Cell type / FBbt links** are replaced with annotations based on the new data for neurons that are not deprecated.

## What happens when a dataset/site is retired with no replacement

The site is **deprecated** and there is no new site.

- **Neurons** — remain valid (_not_ deprecated) and **remain valid query targets**.
  Their only data source is now a deprecated site, so no link can be built to a live
  resource, but the neurons, their connectivity and their images are still served.
- **The Site** — **deprecated**. But the `is_data_source` flag remains true, so the site is still treated as the canonical source for its neurons.
- **The DataSet** — _not_ deprecated.

## Effects on the website and queries

These follow from the states above and are enforced when results are generated:

- **Deprecated neurons** are excluded from connectivity results and from the neuron counts
  used in connectivity summaries (so they do not appear as partners and do not affect
  percentages).
- **Deprecated sites** never produce a clickable external link. Where a results table has
  source / accession columns (e.g. instance and similar-neuron tables, connectivity
  tables), the source name and accession are still shown as **plain text** — they are just
  not linked. In the [Term Info](/docs/website-features/terminfo/) cross-reference list,
  whose entries exist specifically to be links, a deprecated site's entry is omitted.
- **Neurons whose only data source is a deprecated site** remain valid query
  targets and are returned normally; only their outbound link to the dead resource is
  suppressed.

## Technical note

Deprecation is recorded with a `Deprecated` label on the node (Neo4j), which is also
surfaced in the search index as a `Deprecated` value in the node's types. Result-generating
code keys off this to apply the behaviours above. Site and neuron deprecation are checked
independently.

## See also

- [EM Data](/docs/data/em/) — the integrated connectomic datasets and their versions.
- [Resources](/docs/resources/) — the external sites/resources that host the data.
- [Term Info](/docs/website-features/terminfo/) — where cross-references and connectivity are shown.
