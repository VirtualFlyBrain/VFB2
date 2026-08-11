---
title: "Regional Synaptic Connectivity from Connectome Datasets"
linkTitle: "Region Connectivity"
categories: ["overview","help"]
tags: ["EM","Connectomics","Connectivity","Neuropil","Synaptic_neuropil","ROI","DataSet"]
weight: 4
date: 2026-07-28
description: >
  Per-neuron summaries of how many synapses each connectome neuron makes in each neuropil region, how they are represented on Virtual Fly Brain, and the sources they are derived from.
---

Alongside neuron-to-neuron [connectivity](/docs/data/em/versioning/) (`synapsed_to`),
each EM connectome carries **regional connectivity**: for every neuron, a summary of how
many synapses it makes in each [neuropil region](/docs/data/em/neuropil-regions/) — that
is, the neuron's input and output synapse tallies **per region**, rather than per partner
neuron. This lets a neuron be characterised by *where* in the brain or VNC its inputs and
outputs lie (for example "this cell has most of its postsynaptic sites in `AL_R` and its
outputs in `LH_R`"), and lets regions be compared by how much synaptic traffic they carry.

## What is loaded

For each neuron that VFB loads for a dataset — the cell-typed, non-deprecated neurons
cross-referenced to that dataset's [Site](/docs/data/em/versioning/) — VFB records the
neuron's synapse counts in each region as edges from the neuron to the corresponding
**region individual** (the same side-specific ROI individuals described in
[Neuropil Regions](/docs/data/em/neuropil-regions/)). Because each region individual is
side-specific (`part_of` a body side), left/right is carried by the target region and does
not need to be stored on the edge.

A neuron gets an edge for **every** region that resolves to a loaded region
individual. ROIs with no loaded individual are dropped — e.g. the fine-grained
optic-lobe columns (thousands of `ME/LO/LOP` columns that have no individual),
FlyWire's unassigned bucket (`UNASGD`), and neuprint's `NotPrimary` pseudo-ROI —
and are flagged in the build's ROI-mapping report.

### Counts are multi-level (nested), not a single partition

The region individuals VFB loads span **several nesting levels** — coarse grouping
neuropils (e.g. `SNP`, `INP`, `CX`), the primary neuropils within them (e.g.
`SLP`, `SIP`, `AL`), and finer subdivisions (antennal-lobe glomeruli,
mushroom-body lobe slices, fan-shaped-body layers, ellipsoid-body domains). A
region-connectivity edge is emitted at **every** level that has a loaded
individual, and the counts are **nested**: a synapse is counted at its finest
region **and** at each of its ancestors, so a parent region's count equals the
sum of its children (for example `AL(R)`'s `upstream` equals the sum over its
glomeruli). This mirrors how the source data (neuprint's `roiInfo`) reports
counts at every level of the ROI hierarchy.

This makes the tallies **multi-resolution rather than a sum-safe partition**: they
are correct *per region* at whichever granularity you query, but **summing across
nested regions double-counts** the shared synapses. Consumers that need a
non-overlapping total should pick a single level (e.g. the primary neuropils)
rather than adding a parent and its children together.

## Representation

Each neuron–region edge is one of two relations, carrying the counts as edge properties:

| Relation | Direction | Counts |
|----------|-----------|--------|
| **has postsynaptic terminal in** (`RO:0002110`) | inputs the neuron receives in the region | `upstream` — number of the neuron's postsynaptic sites (inputs) in the region |
| **has presynaptic terminals in** (`RO:0002113`) | outputs the neuron makes in the region | `Tbars` — number of presynaptic release sites (T-bars); `downstream` — number of downstream synaptic connections |

The counts are stored as numeric edge properties, matching the representation VFB already
uses for these regional tallies. A presynaptic edge is only asserted where the neuron
actually has output structure in the region (a T-bar count for the neuprint datasets, or an
output-synapse count for FlyWire), and likewise a postsynaptic edge requires an input count
— so an edge always means the neuron genuinely has terminals of that polarity in the region.

## Datasets and sources

| Dataset | VFB symbol | Count source | Regions |
|---------|-----------|--------------|---------|
| Hemibrain | hb | neuprint `hemibrain:v1.2.1` `roiInfo` | brain neuropils (incl. glomeruli, MB slices, FB layers, EB domains) |
| MANC | mv | neuprint `manc:v1.2.1` `roiInfo` | VNC neuropils, tracts and nerves |
| male-CNS | mc | neuprint `male-cns:v1.0` `roiInfo` | brain + VNC neuropils |
| Optic-lobe | ol | neuprint `optic-lobe:v1.0.1` `roiInfo` | optic-lobe neuropils and layers |
| FAFB (FlyWire) | fw | FlyWire [Codex](https://codex.flywire.ai/) neuropil synapse table (materialization 783) | lateralised brain neuropils |

The neuprint dataset version is taken from the VFB **Site** node for each dataset (the
`dataset=` in its `link_base`), so the regional counts always come from the same release
VFB is pinned to — see [Dataset Versions and Deprecation](/docs/data/em/versioning/).

### Sources

- **neuprint** ([neuprint.janelia.org](https://neuprint.janelia.org)) — for the Janelia
  datasets (Hemibrain, MANC, male-CNS, Optic-lobe), the per-region input/output tallies
  come from each neuron's `roiInfo` (`upstream`, `pre`/T-bars and `downstream` per ROI).
- **FlyWire Codex** ([codex.flywire.ai](https://codex.flywire.ai/)) — for FAFB, the counts
  come from the Codex per-neuron neuropil synapse table (input and output synapses per
  neuropil). The file is the public Google Cloud Storage object
  `https://storage.googleapis.com/flywire-data/codex/data/fafb/783/neuropil_synapse_table.csv.gz`
  (materialization 783). FlyWire does not annotate T-bars, so its presynaptic edges carry
  the output-synapse count as `downstream` (no `Tbars`); its postsynaptic edges carry the
  input-synapse count as `upstream`.

## Relationship to neuron-to-neuron connectivity

Regional connectivity is a **per-region summary**, not a per-partner one: it says how many
synapses a neuron has in a region, but not which other neurons it connects to there. For
neuron-to-neuron connections (with partner identities and weights) see the `synapsed_to`
connectivity described under [Versions & Deprecation](/docs/data/em/versioning/). The two
are consistent — the regional tallies aggregate the same underlying synapses — and both are
refreshed together when a dataset version changes, following the same deprecation rules
(counts are only loaded for non-deprecated neurons).

## See also

- [Neuropil Regions](/docs/data/em/neuropil-regions/) — the region individuals these counts are attached to
- [EM Data](/docs/data/em/) — the neuron and connectivity datasets
- [Dataset Versions and Deprecation](/docs/data/em/versioning/) — how connectivity is versioned and deprecated
