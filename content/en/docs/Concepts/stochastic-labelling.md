---
title: "Stochastic Labelling and Clonal Analysis"
linkTitle: "Stochastic Labelling"
weight: 315
date: 2026-08-18
categories: ["overview","help"]
tags: ["MCFO","MARCM","FLP-out","clone","single neuron","Expression_pattern"]
description: >
  How single neurons and clones are picked out of a driver's whole expression pattern —
  FLP-out, MARCM and MCFO — and what that means for the single-neuron images on VFB.
---

A driver line labels a population. Most of the interesting anatomy is in the individual
neurons inside it, and a confocal stack of fifty overlapping cells will not give you the
shape of any one of them. Stochastic labelling solves this by making the labelling event
itself random and rare, so that a small, resolvable subset of the population lights up in
each animal.

This is where a large fraction of the **single-neuron light microscopy** on VFB comes
from, and it is what makes LM morphologies comparable against EM reconstructions by
[NBLAST](/docs/concepts/nblast/).

## The mechanism

All of these methods use site-specific recombination. The FLP recombinase excises or
swaps DNA between FRT sites
([Golic and Lindquist, 1989](https://doi.org/10.1016/0092-8674(89)90033-0)). Give FLP only
a brief window or a weak promoter and it acts in some cells and not others — the
randomness is the point.

**FLP-out.** A transcription-terminating cassette flanked by FRT sites sits between the
promoter and the reporter. The reporter is silent until FLP removes the cassette. Because
excision is stochastic, only some cells in the driver's pattern ever express it.

**MARCM** (Mosaic Analysis with a Repressible Cell Marker) uses mitotic recombination at
an FRT to produce, from a heterozygous dividing cell, one daughter homozygous for the
absence of GAL80. Only that daughter and its progeny lose GAL4 repression and become
labelled ([Lee and Luo, 1999](https://doi.org/10.1016/S0896-6273(00)80701-1)). Because the
event happens at a cell division, the labelled unit is a **clone** — a neuroblast and its
progeny — which is why MARCM is the standard method for lineage work, and why VFB holds
clonal as well as single-cell images.

**MCFO** (MultiColor FlpOut) extends FLP-out with several differently epitope-tagged,
membrane-targeted reporters, each behind its own excisable cassette. Different cells end
up with different tag combinations, so neighbouring neurons are separable by colour as
well as by sparseness ([Nern et al., 2015](https://doi.org/10.1073/pnas.1506763112)). Using
two recombinases lets the number of labelled cells and the number of colour combinations
be tuned independently. Most of the Janelia single-neuron imagery on VFB is MCFO.

## Reading a stochastic image on VFB

- **The cell was chosen by chance, not by identity.** A single-neuron image tells you the
  morphology of one cell that happened to be labelled within a driver's pattern. Which
  cell type it is, is a downstream judgement — see [cell types](/docs/concepts/cell_types/).
- **Sparse does not mean single.** An image may contain two or three faintly overlapping
  cells. VFB records what was segmented; check the image before treating a morphology as
  one neuron.
- **A clone is a developmental unit, not a cell type.** MARCM clones group neurons by
  shared lineage. Neurons in one clone may belong to several types, and one type may be
  split across clones.
- **Coverage is biased by the driver.** You can only label stochastically within a pattern
  that the driver already produces, so cell types with no good driver are
  under-represented in the LM data regardless of how sparse the labelling is.
- **It is still one animal.** As with everything else on VFB, comparison across animals is
  possible because the images are [registered](/docs/concepts/registration/) to a common
  [template](/docs/data/templates/).

## Where it fits

| Question | Method | On VFB |
|---|---|---|
| What does this driver label? | Whole-pattern imaging | [Expression patterns](/docs/concepts/binary-expression/) |
| Can I get a driver for just this cell type? | Split-GAL4 intersection | [Split driver expression](/docs/concepts/splits/) |
| What does one of these cells look like? | FLP-out, MCFO | This page |
| Which cells share a lineage? | MARCM clones | This page |
| Is this LM neuron the same as that EM neuron? | Morphological comparison | [NBLAST](/docs/concepts/nblast/) |

## Sources

- Golic KG, Lindquist S (1989) The FLP recombinase of yeast catalyzes site-specific recombination in the *Drosophila* genome. *Cell* 59:499–509. doi:10.1016/0092-8674(89)90033-0
- Lee T, Luo L (1999) Mosaic analysis with a repressible cell marker for studies of gene function in neuronal morphogenesis. *Neuron* 22:451–461. doi:10.1016/S0896-6273(00)80701-1
- Nern A, Pfeiffer BD, Rubin GM (2015) Optimized tools for multicolor stochastic labeling reveal diverse stereotyped cell arrangements in the fly visual system. *PNAS* 112:E2967–E2976. doi:10.1073/pnas.1506763112
- Costa M et al. (2016) NBLAST: rapid, sensitive comparison of neuronal structure and construction of neuron family databases. *Neuron* 91:293–311. doi:10.1016/j.neuron.2016.06.012
