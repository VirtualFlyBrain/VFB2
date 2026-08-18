---
title: "Binary Expression Systems"
linkTitle: "Binary Expression"
weight: 313
date: 2026-08-18
categories: ["overview","help"]
tags: ["GAL4","UAS","LexA","Q system","transgene","Expression_pattern"]
description: >
  GAL4/UAS and the other two-part systems that produced almost every driver line and
  expression pattern on VFB.
---

Almost every light microscopy image on Virtual Fly Brain exists because someone put a
reporter into a defined set of cells using a **binary expression system**. Understanding
the two-part structure explains what an expression pattern on VFB is an image *of*, and
why the same driver appears in dozens of different experiments.

## The two parts

A binary system separates *where* from *what*:

- A **driver** transgene puts a transcription factor under the control of a piece of
  genomic DNA — usually an enhancer fragment — so the factor is made in whatever cells
  that fragment is active in.
- An **effector** (or reporter) transgene puts the gene you actually want expressed
  downstream of a binding site for that factor. On its own it does nothing.

Cross the two lines, and the effector is expressed only where the driver is active. The
same driver can be crossed to a fluorescent reporter to image a pattern, to a silencer to
switch those cells off, or to an optogenetic channel to switch them on — without
rebuilding the driver.

Brand and Perrimon adapted the yeast GAL4 transcription factor and its UAS binding site
for exactly this ([Brand and Perrimon, 1993](https://doi.org/10.1242/dev.118.2.401)). It
remains the dominant system in fly neurobiology, and every `GAL4` line on VFB is an
instance of it.

## The systems you will meet on VFB

| System | Driver | Effector | Typical use |
|---|---|---|---|
| GAL4/UAS | GAL4 | UAS-*x* | The default; nearly all driver lines |
| LexA/LexAop | LexA | LexAop-*x* | A second, independent channel in the same animal |
| Q system | QF | QUAS-*x* | A third channel; repressible by QS |
| Split-GAL4 | GAL4-AD + GAL4-DBD | UAS-*x* | Intersection of two patterns — see [split driver expression](/docs/concepts/splits/) |

Having more than one orthogonal system matters because it lets you label two populations
in different colours, or drive an effector in one population while reporting activity in
another ([Lai and Lee, 2006](https://doi.org/10.1038/nn1681);
[Potter et al., 2010](https://doi.org/10.1016/j.cell.2010.02.025)).

## Control in time as well as space

GAL80 represses GAL4. A temperature-sensitive GAL80 therefore gates GAL4 activity by
temperature, which converts a spatial tool into a spatiotemporal one
([McGuire et al., 2003](https://doi.org/10.1126/science.1089035)). GAL80 is also what makes
MARCM work — see [stochastic labelling](/docs/concepts/stochastic-labelling/).

## Where the driver lines came from

Early drivers were enhancer traps: a transposon inserted at random, and the reporter
next to it reported on whatever regulatory element it landed near
([O'Kane and Gehring, 1987](https://doi.org/10.1073/pnas.84.24.9123)). Useful, but neither
systematic nor reproducible in insertion site.

This is also where the *w<sup>1118</sup>* background in so many stock genotypes comes
from. Transformation constructs carry a selectable marker, and the classical one is
**mini-*white***: the P{GawB} enhancer-trap construct behind many early GAL4 lines is
marked with *w<sup>+mW.hs</sup>*
([FBtp0000352](https://flybase.org/reports/FBtp0000352)). A *white*<sup>+</sup> marker
restores eye pigment, so it can only be scored in a *white*-mutant animal — which is why
driver line genotypes on VFB so often read `w[1118];P{w[+mW.hs]=GawB}…`, and why the first
*Drosophila* mutant ever described is still the standard way of telling that a transgene
went in.

Two changes made large collections possible. First, φC31 integrase allowed constructs to
be placed at a defined attP landing site, so lines differ only in their enhancer fragment
and not in where the construct sits
([Groth et al., 2004](https://doi.org/10.1534/genetics.166.4.1775)). Second, defined
genomic fragments were cloned systematically rather than trapped
([Pfeiffer et al., 2008](https://doi.org/10.1073/pnas.0803697105)).

The two collections that dominate VFB's light microscopy followed:

- The **Janelia GAL4 collection** — 7,000 lines, with CNS expression imaged and published
  for 6,650 ([Jenett et al., 2012](https://doi.org/10.1016/j.celrep.2012.09.011)).
- The **Vienna Tiles (VT)** collection — 7,705 enhancer candidates characterised in vivo
  ([Kvon et al., 2014](https://doi.org/10.1038/nature13395)).

Both are searchable on VFB, registered to the [standard templates](/docs/data/templates/)
and classified with anatomy ontology terms, so you can ask which lines label a region or
cell type rather than reading pattern images one at a time.

## What an expression pattern image is, and is not

- **It is the whole pattern of that driver**, not of one cell type. A GAL4 line usually
  labels several unrelated populations. Specificity is what split drivers address.
- **It is one animal.** Expression varies between individuals, and between rearing
  conditions. Patterns on VFB are registered so that many such images can be compared.
- **Absence of signal is weak evidence.** A pattern may fail to show a cell because the
  enhancer is not active there, or because the reporter was too dim, or because that part
  of the CNS was not imaged — see [FlyLight imaging tiles](/docs/concepts/flylight_tiles/).
- **Reporter choice changes what you see.** Membrane-targeted, nuclear and cytoplasmic
  reporters give visibly different images of the same driver.

## Effectors beyond reporters

The same drivers carry non-imaging effectors, which is why a driver line found on VFB is
usually the starting point for a functional experiment:

- **Silencing** — temperature-sensitive *shibire* to block synaptic vesicle recycling
  ([Kitamoto, 2001](https://doi.org/10.1002/neu.1018)), or Kir2.1 to hyperpolarise.
- **Activation** — channelrhodopsins such as CsChrimson
  ([Klapoetke et al., 2014](https://doi.org/10.1038/nmeth.2836)).
- **Activity imaging** — GCaMP calcium indicators
  ([Chen et al., 2013](https://doi.org/10.1038/nature12354)).
- **Knockdown** — UAS-RNAi from the VDRC and TRiP collections
  ([Dietzl et al., 2007](https://doi.org/10.1038/nature05954);
  [Perkins et al., 2015](https://doi.org/10.1534/genetics.115.180208)).
- **Connectivity reporters** — GRASP
  ([Feinberg et al., 2008](https://doi.org/10.1016/j.neuron.2007.11.030)) and trans-Tango
  ([Talay et al., 2017](https://doi.org/10.1016/j.neuron.2017.10.011)).

VFB indexes the expression patterns; the reagents themselves are catalogued in
[FlyBase](https://flybase.org) and distributed by the stock centres, and VFB links out to
both from each transgene record. See
[transgene expression curation](/docs/concepts/transgene/) for how that record is built.

## Sources

- Brand AH, Perrimon N (1993) Targeted gene expression as a means of altering cell fates and generating dominant phenotypes. *Development* 118:401–415. doi:10.1242/dev.118.2.401
- O'Kane CJ, Gehring WJ (1987) Detection in situ of genomic regulatory elements in *Drosophila*. *PNAS* 84:9123–9127. doi:10.1073/pnas.84.24.9123
- Kitamoto T (2001) Conditional modification of behavior in *Drosophila* by targeted expression of a temperature-sensitive *shibire* allele in defined neurons. *J Neurobiol* 47:81–92. doi:10.1002/neu.1018
- McGuire SE et al. (2003) Spatiotemporal rescue of memory dysfunction in *Drosophila*. *Science* 302:1765–1768. doi:10.1126/science.1089035
- Groth AC et al. (2004) Construction of transgenic *Drosophila* by using the site-specific integrase from phage φC31. *Genetics* 166:1775–1782. doi:10.1534/genetics.166.4.1775
- Lai S-L, Lee T (2006) Genetic mosaic with dual binary transcriptional systems in *Drosophila*. *Nat Neurosci* 9:703–709. doi:10.1038/nn1681
- Dietzl G et al. (2007) A genome-wide transgenic RNAi library for conditional gene inactivation in *Drosophila*. *Nature* 448:151–156. doi:10.1038/nature05954
- Feinberg EH et al. (2008) GFP reconstitution across synaptic partners (GRASP) defines cell contacts and synapses in living nervous systems. *Neuron* 57:353–363. doi:10.1016/j.neuron.2007.11.030
- Pfeiffer BD et al. (2008) Tools for neuroanatomy and neurogenetics in *Drosophila*. *PNAS* 105:9715–9720. doi:10.1073/pnas.0803697105
- Potter CJ et al. (2010) The Q system: a repressible binary system for transgene expression, lineage tracing, and mosaic analysis. *Cell* 141:536–548. doi:10.1016/j.cell.2010.02.025
- Jenett A et al. (2012) A GAL4-driver line resource for *Drosophila* neurobiology. *Cell Rep* 2:991–1001. doi:10.1016/j.celrep.2012.09.011
- Chen T-W et al. (2013) Ultrasensitive fluorescent proteins for imaging neuronal activity. *Nature* 499:295–300. doi:10.1038/nature12354
- Klapoetke NC et al. (2014) Independent optical excitation of distinct neural populations. *Nat Methods* 11:338–346. doi:10.1038/nmeth.2836
- Kvon EZ et al. (2014) Genome-scale functional characterization of *Drosophila* developmental enhancers in vivo. *Nature* 512:91–95. doi:10.1038/nature13395
- Perkins LA et al. (2015) The Transgenic RNAi Project at Harvard Medical School: resources and validation. *Genetics* 201:843–852. doi:10.1534/genetics.115.180208
- Talay M et al. (2017) Transsynaptic mapping of second-order taste neurons in flies by trans-Tango. *Neuron* 96:783–795. doi:10.1016/j.neuron.2017.10.011
