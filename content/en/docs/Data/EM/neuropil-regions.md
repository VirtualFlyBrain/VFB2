---
title: "Neuropil Regions from Connectome Datasets"
linkTitle: "Neuropil Regions"
categories: ["overview","help"]
tags: ["EM","Connectomics","DataSet","Neuropil","Synaptic_neuropil","ROI","Painted domain"]
weight: 3
date: 2026-07-27
description: >
  Neuropil, tract and nerve regions of interest (ROIs) that accompany each EM connectome dataset on Virtual Fly Brain, and the sources they are derived from.
---

As well as neurons and connectivity, each EM connectome is accompanied by a set of
**regions of interest (ROIs)** — the neuropils (and, for the ventral nerve cord, tracts
and nerves) used by that project to spatially organise its data. VFB loads these ROIs as
image individuals, each an instance of the corresponding FBbt
([Drosophila anatomy ontology](https://www.ebi.ac.uk/ols4/ontologies/fbbt)) anatomy term,
aligned to the same standard [template](/docs/data/templates/) as the
dataset's neurons. This lets a connectome's own region names (e.g. `AL_R`, `LegNp(T1)(L)`,
`PB(L3)`) be resolved to ontology terms and browsed alongside its neurons.

Each region individual records the source dataset's own region name (for example `AL_R`)
as an exact synonym, and is asserted to be `part_of` the relevant organism sex and body
side, so that left/right and male/female regions are distinguished.

Separately, the dataset-specific *typed* synonyms — *name_in_hemibrain*, *name_in_banc*
and so on — are held on the FBbt anatomy **classes**, not on the individuals: each region
term is annotated with the name that each connectome uses for it, recording cross-dataset
nomenclature at the ontology level.

## Summary of neuropil region sets

| Dataset | VFB symbol | ROI content | Region source | Alignment template(s) | Reference |
|---------|-----------|-------------|---------------|-----------------------|-----------|
| Hemibrain | hb | ~230 painted domains: brain neuropils incl. individual antennal-lobe glomeruli, protocerebral-bridge glomeruli, mushroom-body lobe slices, fan-shaped-body layers and ellipsoid-body domains (adult female) | neuprint `hemibrain:v1.2.1` painted domains | [JRC_FlyEM_Hemibrain](/docs/data/templates/) | [Scheffer et al. (2020)](https://doi.org/10.7554/eLife.57443) |
| MANC | mv | 59 VNC neuropils, tracts and nerves (adult male) | neuprint `manc:v1.2.1` `roiInfo` | [JRC2018 Unisex VNC](/docs/data/templates/) | [Takemura et al. (2024)](https://doi.org/10.7554/eLife.97769.1) |
| male-CNS | mc | ~400 brain + VNC neuropils incl. antennal-lobe & protocerebral-bridge glomeruli, mushroom-body slices, fan-shaped-body layers, ellipsoid-body domains and optic-lobe layers (adult male) | neuprint `male-cns:v1.0` `roiInfo` | [JRC2018 Unisex](/docs/data/templates/) (brain) + [JRC2018 Unisex VNC](/docs/data/templates/) (VNC) | [Berg et al. (2025)](https://doi.org/10.1101/2025.10.09.680999) |
| Optic-lobe | ol | ~106 optic-lobe neuropils and their layers (ME, LO, LOP layers) (adult male) | neuprint `optic-lobe:v1.0.1` `roiInfo` | [JRC2018 Unisex](/docs/data/templates/) | [Nern et al. (2025)](https://doi.org/10.1038/s41586-025-08746-0) |
| FAFB (FlyWire) | fw | 78 lateralised brain neuropils (adult female) | FlyWire [Codex](https://codex.flywire.ai/) neuropil synapse table (materialization 783) | [JRC2018 Unisex](/docs/data/templates/) | [Dorkenwald et al. (2024)](https://doi.org/10.1038/s41586-024-07558-y); [Schlegel et al. (2024)](https://doi.org/10.1038/s41586-024-07686-5) |
| BANC | BANC | ~305 regions: brain neuropils (Ito) and antennal-lobe glomeruli (Schlegel) plus VNC neuropils, tracts and nerves (Court and MANC atlases), warped into BANC space (adult female) | BANC `region_outlines` meshes (`v888`) | [JRC2018 Unisex](/docs/data/templates/) (brain) + [JRC2018 Unisex VNC](/docs/data/templates/) (VNC) | [Bates et al. (2026)](https://doi.org/10.1038/s41586-026-10735-w) |

Region names are mapped to FBbt terms during curation. Abbreviations that are ambiguous
between projects (for example `PB`, which can mean the protocerebral bridge or a
peripheral nerve) are resolved with an explicit lookup, and antennal-lobe glomeruli are
matched to their `antennal lobe glomerulus …` terms.

## Sources

- **neuprint** ([neuprint.janelia.org](https://neuprint.janelia.org)) — for the Janelia
  datasets (Hemibrain, MANC, male-CNS, Optic-lobe) the region list is taken from the
  dataset `Meta` node: the ROI names from `roiInfo` and their nesting from `roiHierarchy`.
  Individual optic-lobe columns (thousands of ME/LO/LOP columns) are excluded, as they do
  not correspond to FBbt terms.
- **FlyWire Codex** ([codex.flywire.ai](https://codex.flywire.ai/)) — for FAFB, the
  lateralised neuropil names are taken from the column headers of the Codex neuropil
  synapse table for the FlyWire full adult female brain.
- **BANC region outlines** — for BANC, the regions are neuroglancer meshes from the
  project's `region_outlines` layer, in the public Google Cloud Storage bucket
  `gs://lee-lab_brain-and-nerve-cord-fly-connectome/region_outlines/` (region names and
  segment IDs in `segment_properties/info`; meshes under `meshes/`). They are
  reference-atlas neuropils (Ito midbrain/optic-lobe, Court and MANC VNC, Schlegel
  antennal-lobe glomeruli) warped into BANC space. Because more than one atlas is included,
  a few VNC tracts appear in both the Court and MANC parcellations and are kept as distinct
  regions.

## Relationship to template painted domains

These connectome ROIs are distinct from the standard neuropil **painted domains** of the
[reference templates](/docs/data/templates/). The template painted domains provide a
canonical, coarse-grained parcellation of a standard brain or VNC, whereas the connectome
region sets follow each project's own — often finer — subdivision (individual glomeruli,
mushroom-body slices, neuropil layers, and so on) and are aligned into the shared template
space so that they can be compared.

## See also

- [EM Data](/docs/data/em/) — the neuron and connectivity datasets these regions accompany
- [Region Connectivity](/docs/data/em/region-connectivity/) — per-neuron synapse tallies attached to these regions
- [Templates](/docs/data/templates/) — reference templates and their painted domains
- [Dataset Versions and Deprecation](/docs/data/em/versioning/) — how region and neuron datasets change between releases
