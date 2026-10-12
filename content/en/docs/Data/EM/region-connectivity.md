---
title: "Regional Synaptic Connectivity from Connectome Datasets"
linkTitle: "Region Connectivity"
categories: ["overview","help"]
tags: ["EM","Connectomics","Connectivity","Neuropil","Synaptic_neuropil","ROI","DataSet"]
weight: 4
date: 2026-10-12
description: >
  Per-neuron summaries of how many synapses each connectome neuron makes in each neuropil region, and in total, how they are represented on Virtual Fly Brain, and the sources they are derived from.
---

Alongside neuron-to-neuron [connectivity](/docs/data/em/versioning/) (`synapsed_to`),
each EM connectome carries **regional connectivity**: for every neuron, a summary of how
many synapses it makes in each [neuropil region](/docs/data/em/neuropil-regions/) — that
is, the neuron's input and output synapse tallies **per region**, rather than per partner
neuron. This lets a neuron be characterised by *where* in the brain or VNC its inputs and
outputs lie (for example "this cell has most of its postsynaptic sites in `AL_R` and its
outputs in `LH_R`"), and lets regions be compared by how much synaptic traffic they carry.
Each neuron also carries its [whole-neuron synapse totals](#whole-neuron-synapse-totals).

Every count includes **every synapse on the neuron, whatever the partner** — partners
that are unproofread fragments, or that VFB has not loaded, included — and there is **no
connection-count threshold**, so the counts mean the same thing in every dataset.

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
FlyWire's and BANC's unassigned buckets (`UNASGD`, `*_unassigned_*`), and neuprint's
`NotPrimary` and `*-unspecified` catch-alls — and are flagged in the build's
ROI-mapping report.

### neuprint counts are multi-level (nested), not a single partition

For the neuprint datasets (Hemibrain, MANC, male-CNS, Optic-lobe), the region
individuals VFB loads span **several nesting levels** — coarse grouping
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
rather than adding a parent and its children together — or, for a whole-neuron
total, use the [synapse totals](#whole-neuron-synapse-totals).

FlyWire and BANC instead assign every synapse to exactly one neuropil, so their
region counts form a single partition: a neuron's regional counts sum to its total,
less the synapses in no named neuropil.

## Representation

Each neuron–region edge is one of two relations, carrying the counts as edge properties:

| Relation | Direction | Counts |
|----------|-----------|--------|
| **has postsynaptic terminal in** (`RO:0002110`) | inputs the neuron receives in the region | `upstream` — number of the neuron's postsynaptic sites (inputs) in the region |
| **has presynaptic terminals in** (`RO:0002113`) | outputs the neuron makes in the region | `Tbars` — number of presynaptic release sites (T-bars); `downstream` — number of downstream synaptic connections |

The counts are stored as numeric edge properties, matching the representation VFB already
uses for these regional tallies. A presynaptic edge is only asserted where the neuron
actually has output structure in the region (a T-bar count for the neuprint datasets, or an
output-synapse count for FlyWire and BANC, which have no T-bars), and likewise a postsynaptic edge requires an input count
— so an edge always means the neuron genuinely has terminals of that polarity in the region.

## Datasets and sources

| Dataset | VFB symbol | Count source | Regions |
|---------|-----------|--------------|---------|
| Hemibrain | hb | neuprint `hemibrain:v1.2.1` `roiInfo` | brain neuropils (incl. glomeruli, MB slices, FB layers, EB domains) |
| MANC | mv | neuprint `manc:v1.2.1` `roiInfo` | VNC neuropils, tracts and nerves |
| male-CNS | mc | neuprint `male-cns:v1.0` `roiInfo` | brain + VNC neuropils |
| Optic-lobe | ol | neuprint `optic-lobe:v1.0.1` `roiInfo` | optic-lobe neuropils and layers |
| FAFB (FlyWire) | fw | FlyWire 783 per-neuron neuropil synapse counts ([Zenodo](https://zenodo.org/records/10676866)) | lateralised brain neuropils |
| BANC | BANC | BANC v888 per-neuropil connection counts (v1 synapse set) | Ito brain/optic neuropils and Court VNC neuropils |

The source version is taken from the VFB **Site** node for each dataset (the neuprint
`dataset=`, or the FlyWire/BANC `data_version=`, in its `link_base`), so the regional
counts always come from the same release VFB is pinned to — see
[Dataset Versions and Deprecation](/docs/data/em/versioning/).

### Sources

- **neuprint** ([neuprint.janelia.org](https://neuprint.janelia.org)) — for the Janelia
  datasets (Hemibrain, MANC, male-CNS, Optic-lobe), the per-region input/output tallies
  come from each neuron's `roiInfo` (`upstream`, `pre`/T-bars and `downstream` per ROI).
- **FlyWire** — for FAFB, the counts come from the FlyWire 783 release's per-neuron
  neuropil synapse counts (`per_neuron_neuropil_count_post_783.feather` and
  `per_neuron_neuropil_count_pre_783.feather`,
  [Zenodo 10676866](https://zenodo.org/records/10676866)): the synapses each neuron
  receives and makes in each neuropil, with any partner (cleft score ≥ 50). These replaced
  the Codex neuropil synapse table, which only counts connections of five or more synapses
  between proofread neurons. FlyWire does not annotate T-bars, so its presynaptic edges
  carry the output-synapse count as `downstream` (no `Tbars`); its postsynaptic edges carry
  the input-synapse count as `upstream`.
- **BANC** — the counts come from the v888 per-neuropil connection counts in the public
  bucket (`gs://lee-lab_brain-and-nerve-cord-fly-connectome/neuron_connectivity/v888/synapses_v1_human_readable_sizethresh3_connectioncountsperneuropil.parquet`):
  the v1 synapse set (the one VFB's BANC connectivity is built from), summed per neuron
  and neuropil, with any partner, including unsegmented ones. BANC assigns each synapse to
  one neuropil built from the Ito (brain) and Court (VNC) meshes of its `region_outlines`
  layer, under its own names (e.g. `CB_SLP_R`, `VNC_T1-ProNm_L`); these are mapped back
  to the [region individuals](/docs/data/em/neuropil-regions/) curated from the same
  meshes. Where VFB has one unsided region for a neuropil BANC splits by side (e.g.
  `GNG`, `ProNM-T1`), both sides' synapses are counted on it; `IntTct` and `LTct` map to
  the Court versions. BANC's partition has no glomeruli, tracts or nerves and uses Court
  rather than MANC meshes in the VNC, so those BANC regions carry no counts. There are no
  T-bars, so presynaptic edges carry `downstream` only.

## Whole-neuron synapse totals

Each connectome neuron also carries its **total** synapse counts as properties of the
neuron itself:

| Property | Meaning |
|----------|---------|
| `total_upstream` | all input synapses on the neuron (postsynaptic sites) |
| `total_downstream` | all output synapses (downstream connections) — not available for the CATMAID datasets |
| `total_Tbars` | presynaptic release sites (T-bars) — neuprint and CATMAID datasets only |

Like the regional counts, these include every synapse, whatever the partner, with no
threshold. They come from the neuprint `:Neuron` node's own totals, the FlyWire and BANC
per-neuropil counts summed over neuropils, and — for the sparse CATMAID reconstructions
(FAFB, L1 larval CNS), which carry totals but no regional counts — each skeleton's
connectors on the VFB CATMAID servers.

Their main use is to **normalise connectivity by input**: dividing a `synapsed_to` weight
by the target neuron's `total_upstream` gives the fraction of that neuron's input coming
from the partner, which is comparable between neurons and datasets. They cannot be
recovered by summing regional counts (nested regions double-count; unassigned synapses
are dropped) or by summing `synapsed_to` weights (see below).

## Relationship to neuron-to-neuron connectivity

Regional connectivity is a **per-region summary**, not a per-partner one: it says how many
synapses a neuron has in a region, but not which other neurons it connects to there. For
neuron-to-neuron connections (with partner identities and weights) see the `synapsed_to`
connectivity described under [Versions & Deprecation](/docs/data/em/versioning/).

The regional tallies and totals count the same kind of synapses as `synapsed_to`, but
**more of them**: `synapsed_to` only links neurons VFB has loaded and leaves out the
weakest connections, while the tallies also include synapses with fragments, unloaded
neurons and single-synapse partners. A neuron's summed `synapsed_to` input is therefore
typically well below its `total_upstream` (around 40–85% of it, depending on the
dataset). Both are refreshed together when a dataset version changes, following the same
deprecation rules (counts are only loaded for non-deprecated neurons).

## See also

- [Neuropil Regions](/docs/data/em/neuropil-regions/) — the region individuals these counts are attached to
- [EM Data](/docs/data/em/) — the neuron and connectivity datasets
- [Dataset Versions and Deprecation](/docs/data/em/versioning/) — how connectivity is versioned and deprecated
