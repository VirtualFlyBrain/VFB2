---
title: "EM Imaging and Reconstruction"
linkTitle: "EM Reconstruction"
weight: 318
date: 2026-08-18
categories: ["overview","help"]
tags: ["EM","ssTEM","FIB-SEM","segmentation","proofreading","connectome"]
description: >
  How a fly brain becomes a connectome — sectioning and imaging, segmentation,
  proofreading and synapse detection — and what each step means for the data you query.
---

Every neuron and synapse in VFB's [EM datasets](/docs/data/em/) came out of the same
four-stage pipeline: fix and section the tissue, image it at a resolution where synapses
are visible, decide which voxels belong to which neuron, and decide which pairs of neurons
are connected. Each stage introduces its own kind of error, and knowing which stage a
number came from is most of what you need to interpret it.

## 1. Imaging: two families of method

To see a synapse you need roughly single-digit nanometre resolution in the imaging plane,
across a volume hundreds of micrometres on a side. Two approaches get there.

**Serial-section TEM (ssTEM).** The tissue is physically cut into ultrathin sections,
which are then imaged in a transmission electron microscope. Parallel image formation
makes TEM fast, which is why it scaled to whole brains first: FAFB was cut at 40 nm and
imaged at 4 × 4 nm ([Bock et al., 2011](https://doi.org/10.1038/nature09802);
[Zheng et al., 2018](https://doi.org/10.1016/j.cell.2018.06.019)). The cost is that
sections can be lost, folded or distorted, and section thickness sets a coarse *z*
resolution.

**FIB-SEM.** A focused ion beam mills away a thin layer, the block face is imaged, and the
cycle repeats — so there are no physical sections to lose and *z* resolution is close to
isotropic. Historically it was too slow for large volumes; enhanced systems and
"hot-knife" partitioning, which splits a brain into thick slabs that are imaged separately
and stitched, made whole-region volumes practical
([Hayworth et al., 2015](https://doi.org/10.1038/nmeth.3292);
[Xu et al., 2017](https://doi.org/10.7554/eLife.25916)). The hemibrain, MANC and the optic
lobe volumes are FIB-SEM. Serial block-face SEM
([Denk and Horstmann, 2004](https://doi.org/10.1371/journal.pbio.0020329)) is the third
member of the family, less used for these datasets.

Which method was used is a property of the dataset and is listed on the
[EM data](/docs/data/em/) page.

## 2. Segmentation: which voxels are which neuron

Early reconstruction was manual: a human traced a skeleton through the volume, node by
node. CATMAID was built for exactly this, distributed across many annotators
([Saalfeld et al., 2009](https://doi.org/10.1093/bioinformatics/btp266);
[Schneider-Mizell et al., 2016](https://doi.org/10.7554/eLife.12059)), and VFB
[hosts CATMAID instances](/hosted/) for several of these datasets — in some cases as the
only remaining public copy.

Manual tracing does not scale to a whole brain, so modern reconstructions are automatic
first. Flood-filling networks segment neurons by iteratively growing a predicted object
through the volume ([Januszewski et al., 2018](https://doi.org/10.1038/s41592-018-0049-4)).
The output is never correct as produced: it contains **splits** (one neuron broken into
fragments) and **merges** (two neurons fused into one). Human **proofreading** then
corrects it, which for FlyWire was organised as a community effort over the FAFB volume
([Dorkenwald et al., 2022](https://doi.org/10.1038/s41592-021-01330-0);
[Dorkenwald et al., 2024](https://doi.org/10.1038/s41586-024-07558-y)).

This is why **dense** and **sparse** reconstruction mean very different things:

- **Dense** — the whole volume is segmented, so the dataset aims to contain every neuron.
- **Sparse** — only neurons someone chose to trace exist in the dataset. Absence of a
  neuron says nothing about the animal.

## 3. Synapse detection: which neurons are connected

Synapses are annotated separately from morphology. In the fly they are identified from
ultrastructure — a presynaptic T-bar and the postsynaptic profiles opposite it — and, at
whole-brain scale, by classifiers rather than by eye
([Buhmann et al., 2021](https://doi.org/10.1038/s41592-021-01183-7)).

Two consequences worth carrying:

- **An edge is a count of detected synapses**, subject to both false positives and misses.
  Weak edges (one or two synapses) are the least reliable and are commonly thresholded
  out. See [connectivity data](/docs/data/connectivity/) for what an edge means in VFB.
- **Connectivity inherits segmentation error.** A merge invents connections that the
  animal does not have; a split divides one neuron's connections between two objects.

## 4. Neurotransmitter prediction

The sign of a connection is not visible in the wiring diagram. Networks trained on EM
image features at presynaptic sites predict transmitter identity, reported at 87% accuracy
per synapse, 94% per neuron and 91% per known cell type across a whole-brain dataset
([Eckstein et al., 2024](https://doi.org/10.1016/j.cell.2024.03.016)). These are
**predictions**, and VFB labels them as such — see
[confidence values](/docs/concepts/confidence-value/).

## What this means for the data you query

- **Neuron identity is per-release.** Proofreading continues after publication, so
  identifiers and counts change between versions; see
  [connectome versioning](/docs/data/em/versioning/).
- **Counting across datasets double-counts.** FlyWire, the hemibrain and FAFB (CATMAID)
  are reconstructions of overlapping tissue — in the first two cases, of the same
  anatomical region in different animals. [Neuron counts](/docs/concepts/neuron-counts/)
  works through this in detail.
- **Cell typing is added, not observed.** The type attached to an EM neuron is an
  annotation made by matching morphology and connectivity against known types
  ([Schlegel et al., 2024](https://doi.org/10.1038/s41586-024-07686-5)); see
  [cell types](/docs/concepts/cell_types/).
- **The specimen matters.** Each volume is one individual of a particular sex, age and
  genotype — see [which fly is this?](/about/whichfly/).

## Sources

- Denk W, Horstmann H (2004) Serial block-face scanning electron microscopy to reconstruct three-dimensional tissue nanostructure. *PLoS Biol* 2(11):e329. doi:10.1371/journal.pbio.0020329
- Saalfeld S et al. (2009) CATMAID: collaborative annotation toolkit for massive amounts of image data. *Bioinformatics* 25:1984–1986. doi:10.1093/bioinformatics/btp266
- Bock DD et al. (2011) Network anatomy and in vivo physiology of visual cortical neurons. *Nature* 471:177–182. doi:10.1038/nature09802
- Cardona A et al. (2012) TrakEM2 software for neural circuit reconstruction. *PLoS ONE* 7(6):e38011. doi:10.1371/journal.pone.0038011
- Hayworth KJ et al. (2015) Ultrastructurally smooth thick partitioning and volume stitching for large-scale connectomics. *Nat Methods* 12:319–322. doi:10.1038/nmeth.3292
- Schneider-Mizell CM et al. (2016) Quantitative neuroanatomy for connectomics in *Drosophila*. *eLife* 5:e12059. doi:10.7554/eLife.12059
- Xu CS et al. (2017) Enhanced FIB-SEM systems for large-volume 3D imaging. *eLife* 6:e25916. doi:10.7554/eLife.25916
- Januszewski M et al. (2018) High-precision automated reconstruction of neurons with flood-filling networks. *Nat Methods* 15:605–610. doi:10.1038/s41592-018-0049-4
- Zheng Z et al. (2018) A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*. *Cell* 174(3):730–743. doi:10.1016/j.cell.2018.06.019
- Scheffer LK et al. (2020) A connectome and analysis of the adult *Drosophila* central brain. *eLife* 9:e57443. doi:10.7554/eLife.57443
- Buhmann J et al. (2021) Automatic detection of synaptic partners in a whole-brain *Drosophila* electron microscopy data set. *Nat Methods* 18:771–774. doi:10.1038/s41592-021-01183-7
- Dorkenwald S et al. (2022) FlyWire: online community for whole-brain connectomics. *Nat Methods* 19:119–128. doi:10.1038/s41592-021-01330-0
- Plaza SM et al. (2022) neuPrint: an open access tool for EM connectomics. *Front Neuroinform* 16:896292. doi:10.3389/fninf.2022.896292
- Eckstein N et al. (2024) Neurotransmitter classification from electron microscopy images at synaptic sites in *Drosophila melanogaster*. *Cell* 187:2574–2594. doi:10.1016/j.cell.2024.03.016
- Dorkenwald S et al. (2024) Neuronal wiring diagram of an adult brain. *Nature* 634:124–138. doi:10.1038/s41586-024-07558-y
- Schlegel P et al. (2024) Whole-brain annotation and multi-connectome cell typing of *Drosophila*. *Nature* 634:139–152. doi:10.1038/s41586-024-07686-5
