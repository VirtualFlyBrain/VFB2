---
title: "Datasets by developmental stage"
linkTitle: "Datasets by stage"
weight: 511
date: 2026-08-31
description: >
    Every VFB dataset grouped by developmental stage — embryo, larva (L1 and L3 instars),
    pupa and adult — with the number of datasets at each stage.
keywords: ["larval", "larva", "embryo", "embryonic", "pupa", "pupal", "adult", "instar", "L1", "L3", "developmental stage", "datasets"]
---

<img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Drosophila_melanogaster_life_cycle.jpg" alt="Drosophila melanogaster life cycle: egg, larval instars, pupa, adult" style="max-width:50%">

*Drosophila melanogaster* is holometabolous: it passes from egg through three larval
instars, pupates, and emerges as an adult -- the whole cycle takes about 10 days at
25°C. Image: [Allocca, Zola & Bellosta, 2018](https://doi.org/10.5772/intechopen.72832),
CC BY 3.0, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Drosophila_melanogaster_life_cycle.jpg).

VFB's datasets are documented by [technique](/docs/data/em/) and by
[source](/docs/data/lm/) elsewhere on this site; this page groups them by the
developmental stage of the animal they came from, so a question like *"how many larval
datasets does VFB hold, and which is newest?"* has one place to look. Stage labels are
now being added to dataset entities in the knowledge base itself, so the grouping below
will also become queryable through the API and the VFB chat as that release propagates.

The page lists all 210 dataset entities currently in the VFB knowledge base (`DataSet`
individuals — the same list `search_terms` returns when filtered to `dataset`), grouped
by developmental stage, with a link to each dataset's own page.

**At a glance.** Of the 210 dataset entities, 2 are embryonic, 36 are larval
(27 first-instar, 5 third-instar, and 4 larval with no instar stated), 2 are pupal and
170 are adult (134 brain, 9 ventral nerve cord, 6 leg, head and thorax, and 21 full CNS or
whole body). None are stage-agnostic. The newest larval datasets by publication year are
the split-GAL4 lines of Meissner et al. (`SplitMeissner2024`, L3, 2024) and, for
connectomics, the L1 CNS reconstruction of Winding, Pedigo et al. (`WindingPedigo2023`,
2023).

| Stage | Datasets |
|---|---|
| Embryo | 2 |
| Larva — L1 (first instar) | 27 |
| Larva — L3 (third instar) | 5 |
| Larva — instar not stated | 4 |
| Pupa | 2 |
| Adult | 170 |

**How this was built.** This table was compiled from each dataset's name, description
and publication, cross-checked against a structured signal where one exists: which
[template](/docs/data/templates/) a dataset's images are registered to. Registration is
stage-specific — the L1 CNS template (`Seymour`, VFB\_00050000) only ever receives
first-instar larval images, the L3 CNS template (`Wood2018`, VFB\_00049000) only
third-instar images — so a dataset's `AlignedDatasets` membership on those templates is
firmer evidence than its name. That check changed three classifications from the first,
label-only pass: the `TrumanWood2018`/`TrumanWood2018public` Truman Larval Flip-Out
Collection and `SplitMeissner2024` are all registered to the L3 template rather than an
unspecified larval stage or, in Meissner's case, no stage at all. Stage labels are being
added to the dataset entities themselves in the current data release; once those are
through, this page should be regenerated from them rather than maintained by hand. Until
then, a dataset missing from a future release, or one whose stage was misjudged, should
be corrected here directly.

## Embryo

Approximately 0–22 hours after egg laying, from fertilisation to hatching. The two
datasets here are single-cell/single-nucleus transcriptomic surveys of the whole embryo;
VFB holds no embryonic imaging data at this time.

| Dataset | Short form |
|---|---|
| [Single-cell RNA-seq study of gastrulating embryos](https://flybase.org/reports/FBlc0006191) | `FBlc0006191` |
| [The continuum of Drosophila embryonic development at single-cell resolution](https://flybase.org/reports/FBlc0007797) | `FBlc0007797` |

## Larva

The larval period runs from hatching to pupariation and is divided into three instars —
L1, L2 and L3 — separated by moults. VFB's larval holdings cluster almost entirely at the
first and third instars; no dataset here is recorded as L2. VFB holds 36 larval datasets
in all: 27 at L1, 5 at L3 and 4 with no instar stated. Anatomy differs enough
between instars that a "larval" dataset with no instar stated should not be assumed
comparable to one that states it, particularly for connectomic data.

### L1 (first instar)

The stage most larval EM connectomics is drawn from: the larval CNS is small enough for
a first-instar animal to be reconstructed at synaptic resolution in a single study. Most
entries below are single-paper EM reconstructions built on the `l1em` connectome
(Ohyama et al. 2015 and the studies that extended it) and registered to the L1 CNS
template.

| Dataset | Short form |
|---|---|
| [Comparative Connectomics Reveals How Partner Identity, Location, and Activity Specify Synaptic Connectivity in Drosophila (Valdes-Aleman et al. 2021)](https://virtualflybrain.org/reports/Valdes_Aleman2021) | `Valdes_Aleman2021` |
| [EM L1 Andrade et al. 2019](https://virtualflybrain.org/reports/Andrade2019) | `Andrade2019` |
| [EM L1 Barnes et al., 2022](https://virtualflybrain.org/reports/Barnes2022) | `Barnes2022` |
| [EM L1 Carreira-Rosario, Arzan Zarin, Clark et al. 2018](https://virtualflybrain.org/reports/CarreiraRosario2018) | `CarreiraRosario2018` |
| [EM L1 Eschbach et al 2020](https://virtualflybrain.org/reports/Eschbach2020) | `Eschbach2020` |
| [EM L1 Eschbach et al 2020b](https://virtualflybrain.org/reports/Eschbach2020b) | `Eschbach2020b` |
| [EM L1 Imambocus et al., 2022](https://virtualflybrain.org/reports/Imambocus2022) | `Imambocus2022` |
| [EM L1 Jovanic et al. 2019](https://virtualflybrain.org/reports/Jovanic2019) | `Jovanic2019` |
| [EM L1 Mark et al. 2019](https://virtualflybrain.org/reports/Mark2019) | `Mark2019` |
| [EM L1 Miroschnikow et al. 2018](https://virtualflybrain.org/reports/Miroschnikow2018) | `Miroschnikow2018` |
| [EM L1 Tastekin et al 2018](https://virtualflybrain.org/reports/Tastekin2018) | `Tastekin2018` |
| [EM L1 Winding, Pedigo et al., 2023](https://virtualflybrain.org/reports/WindingPedigo2023) | `WindingPedigo2023` |
| [EM L1 Zarin, Mark et al. 2019](https://virtualflybrain.org/reports/Zarin2019) | `Zarin2019` |
| [Eve+ neurons, sensorimotor circuit - EM (Heckscher2015)](https://virtualflybrain.org/reports/Heckscher2015) | `Heckscher2015` |
| [Full CNS EM, sparse (manually traced) reconstruction (L1 larva)](https://virtualflybrain.org/reports/Ohyama2015) | `Ohyama2015` |
| [larval hugin neurons - EM (Schlegel2016)](https://virtualflybrain.org/reports/Schlegel2016) | `Schlegel2016` |
| [Larval MB neurons - EM (Eichler2017)](https://virtualflybrain.org/reports/Eichler2017) | `Eichler2017` |
| [Larval motor circuit neurons (Zwart2016)](https://virtualflybrain.org/reports/Zwart2016) | `Zwart2016` |
| [Larval olfactory system neurons - EM (Berck2016)](https://virtualflybrain.org/reports/Berck2016) | `Berck2016` |
| [Larval peristaltic locomotor system neurons - EM (Fushiki2016)](https://virtualflybrain.org/reports/Fushiki2016) | `Fushiki2016` |
| [larval sensorimotor decision pathways (Jovanic2016)](https://virtualflybrain.org/reports/Jovanic2016) | `Jovanic2016` |
| [larval visual circuit neurons (Larderet2017)](https://virtualflybrain.org/reports/Larderet2017) | `Larderet2017` |
| [Larval wave neurons and circuit partners - EM (Takagi2017)](https://virtualflybrain.org/reports/Takagi2017) | `Takagi2017` |
| [Nociceptive circuit neurons - EM (Gerhard2017)](https://virtualflybrain.org/reports/Gerhard2017) | `Gerhard2017` |
| [Nociceptive system neurons - EM (Burgos2017)](https://virtualflybrain.org/reports/Burgos2018) | `Burgos2018` |
| [Single-cell RNA-seq study of first instar larval brains upon starvation](https://flybase.org/reports/FBlc0005362) | `FBlc0005362` |
| [Unveiling the sensory and interneuronal pathways of the neuroendocrine connectome in Drosophila (Hueckesfeld et al. 2020)](https://virtualflybrain.org/reports/Hueckesfeld2020) | `Hueckesfeld2020` |

### L3 (third instar)

The last and largest larval instar, imaged shortly before pupariation. VFB's L3 material
is registered to the Wood2018 L3 CNS template and includes the Truman Larval Flip-Out
Collection (`TrumanWood2018`, published 2018) and the split-GAL4 lines of Meissner et al.
(`SplitMeissner2024`, published 2024) — currently the newest of VFB's larval datasets by
publication year.

| Dataset | Short form |
|---|---|
| [L3 Larval CNS Template (Truman2016)](https://virtualflybrain.org/reports/Truman2016) | `Truman2016` |
| [L3 neuropils (WoodHartenstein2018)](https://virtualflybrain.org/reports/WoodHartenstein2018) | `WoodHartenstein2018` |
| [Split-GAL4 lines from Meissner et al., 2024](https://virtualflybrain.org/reports/SplitMeissner2024) | `SplitMeissner2024` |
| [Truman Larval Flip-Out Collection](https://virtualflybrain.org/reports/TrumanWood2018) | `TrumanWood2018` |
| [Truman Larval Flip-Out Collection](https://virtualflybrain.org/reports/TrumanWood2018public) | `TrumanWood2018public` |

### Larva (instar not stated)

Larval by name, publication or genetic targeting, but without enough evidence in VFB to
assign a specific instar — none of these are registered to either larval template, most
likely because they are driver-line metadata without their own aligned images. Treat the
instar as unknown rather than assuming L1 or L3.

| Dataset | Short form |
|---|---|
| [MCFO images of GMR-GAL4 lines from Jovanic et al., 2019](https://virtualflybrain.org/reports/Gen1MCFOJovanic2019) | `Gen1MCFOJovanic2019` |
| [Single-cell RNA-seq study of larval optic lobes](https://flybase.org/reports/FBlc0006404) | `FBlc0006404` |
| [Split-GAL4 lines from Jovanic et al., 2019](https://virtualflybrain.org/reports/SplitJovanic2019) | `SplitJovanic2019` |
| [Split-GAL4 lines from Takagi et al., 2017](https://virtualflybrain.org/reports/SplitTakagi2017) | `SplitTakagi2017` |

## Pupa

Metamorphosis, from pupariation to eclosion. Both datasets here are transcriptomic
surveys of the optic lobe spanning the pupal-to-adult transition; VFB holds no
pupal-only imaging data.

| Dataset | Short form |
|---|---|
| [Single-cell RNA-seq study of pupal and adult optic lobes](https://flybase.org/reports/FBlc0005659) | `FBlc0005659` |
| [Single-cell RNA-seq study of the pupal optic lobe](https://flybase.org/reports/FBlc0006237) | `FBlc0006237` |

## Adult

By far VFB's largest holding: 170 of the 210 dataset entities.
Almost everything here is light-microscopy driver-line and split-GAL4 material from
FlyLight, VDRC, FlyCircuit and individual labs, plus the per-paper EM connectome
datasets (FAFB, hemibrain and their derivatives) and the adult-focused Fly Cell Atlas /
Aging Fly Cell Atlas scRNAseq series. Sex is usually stated for the EM connectomes (FAFB
and hemibrain are each a single traced female brain; MANC and Male-CNS are male) and
usually unstated for driver-line collections, which typically pool both sexes.

### Brain

The overwhelming majority of VFB's adult data: everything above that targets or images
central brain and optic lobe circuitry, without a more specific VNC, leg or whole-body
grouping below.

| Dataset | Short form |
|---|---|
| [Adult Brain fru clones (Cachero2010)](https://virtualflybrain.org/reports/Cachero2010) | `Cachero2010` |
| [AMMC local and projection neurons (Matsuo2016)](https://virtualflybrain.org/reports/Matsuo2016) | `Matsuo2016` |
| [BrainName neuropils and tracts - Ito half-brain](https://virtualflybrain.org/reports/BrainName_Ito_half_brain) | `BrainName_Ito_half_brain` |
| [BrainName neuropils on adult brain JFRC2 (Jenett, Shinomya)](https://virtualflybrain.org/reports/JenettShinomya_BrainName) | `JenettShinomya_BrainName` |
| [BrainTrap lines (Knowles-Barley2010)](https://virtualflybrain.org/reports/Knowles_Barley2010) | `Knowles_Barley2010` |
| [central brain neurons by lineage, Lee2020](https://virtualflybrain.org/reports/Lee_Lineage2020) | `Lee_Lineage2020` |
| [Dickson lab VT line collection - VDRC images](https://virtualflybrain.org/reports/Dickson_VT) | `Dickson_VT` |
| [Dickson lab VT lines - FlyLight/Janelia images (2017)](https://virtualflybrain.org/reports/Dickson2017) | `Dickson2017` |
| [EM FAFB Baltruschat et al 2021](https://virtualflybrain.org/reports/Baltruschat2021) | `Baltruschat2021` |
| [EM FAFB Bates and Schlegel et al 2020](https://virtualflybrain.org/reports/BatesSchlegel2020) | `BatesSchlegel2020` |
| [EM FAFB Coates et al 2020](https://virtualflybrain.org/reports/Coates2020) | `Coates2020` |
| [EM FAFB Dolan and Belliart-Guerin et al. 2018](https://virtualflybrain.org/reports/Dolan2018) | `Dolan2018` |
| [EM FAFB Dolan et al. 2019](https://virtualflybrain.org/reports/FafbDolan2019) | `FafbDolan2019` |
| [EM FAFB Dombrovski et al 2023](https://virtualflybrain.org/reports/Dombrovski2023) | `Dombrovski2023` |
| [EM FAFB Engert et al. 2022](https://virtualflybrain.org/reports/Engert2022) | `Engert2022` |
| [EM FAFB Erginkaya et al 2025](https://virtualflybrain.org/reports/Erginkaya2025) | `Erginkaya2025` |
| [EM FAFB Felsenberg et al. 2018](https://virtualflybrain.org/reports/Felsenberg2018) | `Felsenberg2018` |
| [EM FAFB Gorko et al 2024](https://virtualflybrain.org/reports/Gorko2024) | `Gorko2024` |
| [EM FAFB Hampel and Eichler et al 2020](https://virtualflybrain.org/reports/HampelEichler2020) | `HampelEichler2020` |
| [EM FAFB Kim et al 2020](https://virtualflybrain.org/reports/Kim2020) | `Kim2020` |
| [EM FAFB Kind et al. 2021](https://virtualflybrain.org/reports/Kind2021) | `Kind2021` |
| [EM FAFB Marin et al 2020](https://virtualflybrain.org/reports/Marin2020) | `Marin2020` |
| [EM FAFB Morimoto et al 2020](https://virtualflybrain.org/reports/Morimoto2020) | `Morimoto2020` |
| [EM FAFB Otto et al 2020](https://virtualflybrain.org/reports/Otto2020) | `Otto2020` |
| [EM FAFB Sayin et al 2019](https://virtualflybrain.org/reports/Sayin2019) | `Sayin2019` |
| [EM FAFB Shiu et al. 2022](https://virtualflybrain.org/reports/Shiu2022) | `Shiu2022` |
| [EM FAFB Taisz and Galili et al., 2022](https://virtualflybrain.org/reports/TaiszGalili2022) | `TaiszGalili2022` |
| [EM FAFB Turner-Evans et al 2020](https://virtualflybrain.org/reports/Turner_Evans2020) | `Turner_Evans2020` |
| [EM FAFB Wang et al 2020a](https://virtualflybrain.org/reports/Wang2020a) | `Wang2020a` |
| [EM FAFB Wang et al 2020b](https://virtualflybrain.org/reports/Wang2020b) | `Wang2020b` |
| [EM FAFB Wang et al 2020c](https://virtualflybrain.org/reports/Wang2020c) | `Wang2020c` |
| [EM FAFB Zhao et al., 2023](https://virtualflybrain.org/reports/Zhao2023) | `Zhao2023` |
| [EM FAFB Zheng et al 2020 (published 2022)](https://virtualflybrain.org/reports/Zheng2020) | `Zheng2020` |
| [FlyCircuit 1.0 - single neurons (Chiang2010)](https://virtualflybrain.org/reports/Chiang2010) | `Chiang2010` |
| [FlyLight - Gen1 GAL4/LexA collection (exported 2019)](https://virtualflybrain.org/reports/FlyLightGen1Set2019) | `FlyLightGen1Set2019` |
| [FlyLight - GMR GAL4 collection (Jenett2012)](https://virtualflybrain.org/reports/Jenett2012) | `Jenett2012` |
| [FlyLight split-GAL4 lines for Lateral Horn](https://virtualflybrain.org/reports/FlyLight2019LateralHorn2019) | `FlyLight2019LateralHorn2019` |
| [FlyLight split-GAL4 lines for Lateral Horn (LateralHorn2019)](https://virtualflybrain.org/reports/LateralHorn2019) | `LateralHorn2019` |
| [Full brain EM connectome, dense reconstruction (adult female)](https://virtualflybrain.org/reports/Dorkenwald2023) | `Dorkenwald2023` |
| [Full brain EM, sparse (manually traced) reconstruction (adult female)](https://virtualflybrain.org/reports/Zheng2018) | `Zheng2018` |
| [GAL4 Split expression patterns from Dolan et al. 2019](https://virtualflybrain.org/reports/Dolan2019) | `Dolan2019` |
| [Grooming neurons and drivers (Hampel 2015)](https://virtualflybrain.org/reports/FlyLight2019Hampel2015) | `FlyLight2019Hampel2015` |
| [Grooming neurons and drivers (Hampel 2015)](https://virtualflybrain.org/reports/Hampel2015) | `Hampel2015` |
| [Images of aSP22 descending neuron from McKellar et al., 2019](https://virtualflybrain.org/reports/McKellar2019) | `McKellar2019` |
| [Ito lab adult brain lineage clone image set](https://virtualflybrain.org/reports/Ito2013) | `Ito2013` |
| [JRC 2018 templates & ROIs](https://virtualflybrain.org/reports/JRC2018) | `JRC2018` |
| [JRC_FlyEM_Hemibrain painted domains](https://virtualflybrain.org/reports/Xu2020roi) | `Xu2020roi` |
| [Lee lab adult brain lineage clone image set](https://virtualflybrain.org/reports/Yu2013) | `Yu2013` |
| [LexA driver targetting mechanosensory eye bristles (Hampel2017)](https://virtualflybrain.org/reports/Hampel2017) | `Hampel2017` |
| [MBONs and split-GAL4 lines that target them (Aso2014)](https://virtualflybrain.org/reports/Aso2014) | `Aso2014` |
| [MCFO images of GMR-GAL4 lines from Dionne et al., 2018](https://virtualflybrain.org/reports/Gen1MCFODionne2018) | `Gen1MCFODionne2018` |
| [MCFO images of GMR-GAL4 lines from Jenett et al., 2012](https://virtualflybrain.org/reports/Gen1MCFOJenett2012) | `Gen1MCFOJenett2012` |
| [MCFO images of GMR-GAL4 lines from Pfeiffer et al., 2010](https://virtualflybrain.org/reports/Gen1MCFOPfeiffer2010) | `Gen1MCFOPfeiffer2010` |
| [MCFO images of VT-GAL4 lines from Tirian et al., 2017](https://virtualflybrain.org/reports/Gen1MCFOTirian2017) | `Gen1MCFOTirian2017` |
| [Optic lobe EM connectome, dense reconstruction (adult male)](https://virtualflybrain.org/reports/Nern2024) | `Nern2024` |
| [Partial brain EM connectome, dense reconstruction (adult female)](https://virtualflybrain.org/reports/Xu2020NeuronsV1point2point1) | `Xu2020NeuronsV1point2point1` |
| [RNAseq_2020_Davis](https://virtualflybrain.org/reports/PRJNA480794) | `PRJNA480794` |
| [Single-cell RNA-seq study of adult brain without alcohol exposure](https://flybase.org/reports/FBlc0005420) | `FBlc0005420` |
| [Single-cell RNA-seq study of adult brain without cocaine exposure](https://flybase.org/reports/FBlc0005515) | `FBlc0005515` |
| [Single-cell RNA-seq study of the aging brain](https://flybase.org/reports/FBlc0006090) | `FBlc0006090` |
| [Single-cell RNA-seq study of visual motion-sensing neurons](https://flybase.org/reports/FBlc0006305) | `FBlc0006305` |
| [Single-nucleus RNA-seq on cells from 30-days old male flies](https://flybase.org/reports/FBlc0006611) | `FBlc0006611` |
| [Split GAL4 lines for dopaminergic neurons, Xie2018](https://virtualflybrain.org/reports/Xie2018) | `Xie2018` |
| [split-GAL4 lines for  EB neurons (Robie2017)](https://virtualflybrain.org/reports/Robie2017) | `Robie2017` |
| [split-GAL4 lines for dopaminergic neurons (AsoRubin2016)](https://virtualflybrain.org/reports/AsoRubin2016) | `AsoRubin2016` |
| [split-GAL4 lines for dopaminergic neurons (AsoRubin2016)](https://virtualflybrain.org/reports/FlyLight2019AsoRubin2016) | `FlyLight2019AsoRubin2016` |
| [split-GAL4 lines for EB neurons (Robie2017)](https://virtualflybrain.org/reports/FlyLight2019Robie2017) | `FlyLight2019Robie2017` |
| [split-GAL4 lines for LC VPNs (Wu2016)](https://virtualflybrain.org/reports/FlyLight2019Wu2016) | `FlyLight2019Wu2016` |
| [split-GAL4 lines for LC VPNs (Wu2016)](https://virtualflybrain.org/reports/Wu2016) | `Wu2016` |
| [Split-GAL4 lines from Aso et al., 2014b](https://virtualflybrain.org/reports/SplitAso2014b) | `SplitAso2014b` |
| [Split-GAL4 lines from Baker et al., 2022](https://virtualflybrain.org/reports/SplitBaker2022) | `SplitBaker2022` |
| [Split-GAL4 lines from Bogovic et al., 2020](https://virtualflybrain.org/reports/SplitBogovic2020) | `SplitBogovic2020` |
| [Split-GAL4 lines from Cheong et al., 2023](https://virtualflybrain.org/reports/SplitCheong2023) | `SplitCheong2023` |
| [Split-GAL4 lines from Cheong et al., 2024](https://virtualflybrain.org/reports/SplitCheong2024) | `SplitCheong2024` |
| [Split-GAL4 lines from Dag et al., 2019](https://virtualflybrain.org/reports/SplitDag2019) | `SplitDag2019` |
| [Split-GAL4 lines from Davis et al., 2020](https://virtualflybrain.org/reports/SplitDavis2020) | `SplitDavis2020` |
| [Split-GAL4 lines from Ehrhardt et al., 2023](https://virtualflybrain.org/reports/SplitEhrhardt2023) | `SplitEhrhardt2023` |
| [Split-GAL4 lines from Feng et al., 2014](https://virtualflybrain.org/reports/SplitFeng2014) | `SplitFeng2014` |
| [Split-GAL4 lines from Gao et al., 2019](https://virtualflybrain.org/reports/SplitGao2019) | `SplitGao2019` |
| [Split-GAL4 lines from Garner et al., 2023](https://virtualflybrain.org/reports/SplitGarner2023) | `SplitGarner2023` |
| [Split-GAL4 lines from Giraldo et al., 2018](https://virtualflybrain.org/reports/SplitGiraldo2018) | `SplitGiraldo2018` |
| [Split-GAL4 lines from Hattori et al., 2017](https://virtualflybrain.org/reports/SplitHattori2017) | `SplitHattori2017` |
| [Split-GAL4 lines from Hulse et al., 2021](https://virtualflybrain.org/reports/SplitHulse2021) | `SplitHulse2021` |
| [Split-GAL4 lines from Isaacson et al., 2023](https://virtualflybrain.org/reports/SplitIsaacson2023) | `SplitIsaacson2023` |
| [Split-GAL4 lines from Kind et al., 2021](https://virtualflybrain.org/reports/SplitKind2021) | `SplitKind2021` |
| [Split-GAL4 lines from Klapoetke et al. 2017](https://virtualflybrain.org/reports/FlyLight2019Klapoetke2017) | `FlyLight2019Klapoetke2017` |
| [Split-GAL4 lines from Klapoetke et al. 2017](https://virtualflybrain.org/reports/Klapoetke2017) | `Klapoetke2017` |
| [Split-GAL4 lines from Klapoetke et al., 2022](https://virtualflybrain.org/reports/SplitKlapoetke2022) | `SplitKlapoetke2022` |
| [Split-GAL4 lines from Lillvis et al., 2022](https://virtualflybrain.org/reports/SplitLillvis2022) | `SplitLillvis2022` |
| [Split-GAL4 lines from Liu et al., 2019](https://virtualflybrain.org/reports/SplitLiu2019) | `SplitLiu2019` |
| [Split-GAL4 lines from Longden et al., 2021](https://virtualflybrain.org/reports/SplitLongden2021) | `SplitLongden2021` |
| [Split-GAL4 lines from Longden et al., 2023](https://virtualflybrain.org/reports/SplitLongden2023) | `SplitLongden2023` |
| [Split-GAL4 lines from Mais et al., 2021](https://virtualflybrain.org/reports/SplitMais2021) | `SplitMais2021` |
| [Split-GAL4 lines from Masek et al., 2015](https://virtualflybrain.org/reports/SplitMasek2015) | `SplitMasek2015` |
| [Split-GAL4 lines from Meissner et al., 2018](https://virtualflybrain.org/reports/SplitMeissner2018) | `SplitMeissner2018` |
| [Split-GAL4 lines from Minegishi et al., 2023](https://virtualflybrain.org/reports/SplitMinegishi2023) | `SplitMinegishi2023` |
| [Split-GAL4 lines from Montague et al., 2019](https://virtualflybrain.org/reports/SplitMontague2019) | `SplitMontague2019` |
| [Split-GAL4 lines from Morimoto et al., 2020](https://virtualflybrain.org/reports/SplitMorimoto2020) | `SplitMorimoto2020` |
| [Split-GAL4 lines from Nallasivan et al 2025](https://virtualflybrain.org/reports/SplitNallasivan2025) | `SplitNallasivan2025` |
| [Split-GAL4 lines from Nern et al., 2025](https://virtualflybrain.org/reports/SplitNern2025) | `SplitNern2025` |
| [Split-GAL4 lines from Nojima et al., 2021](https://virtualflybrain.org/reports/Nojima2021) | `Nojima2021` |
| [Split-GAL4 lines from Ribeiro et al., 2018](https://virtualflybrain.org/reports/SplitRibeiro2018) | `SplitRibeiro2018` |
| [Split-GAL4 lines from Rubin et al., 2024](https://virtualflybrain.org/reports/SplitRubin2024) | `SplitRubin2024` |
| [Split-GAL4 lines from Schlichting et al., 2019](https://virtualflybrain.org/reports/SplitSchlichting2019) | `SplitSchlichting2019` |
| [Split-GAL4 lines from Schretter et al., 2020](https://virtualflybrain.org/reports/SplitSchretter2020) | `SplitSchretter2020` |
| [Split-GAL4 lines from Schretter et al., 2024](https://virtualflybrain.org/reports/SplitSchretter2024) | `SplitSchretter2024` |
| [Split-GAL4 lines from Shao et al., 2017](https://virtualflybrain.org/reports/SplitShao2017) | `SplitShao2017` |
| [Split-GAL4 lines from Shuai et al., 2023](https://virtualflybrain.org/reports/SplitShuai2023) | `SplitShuai2023` |
| [Split-GAL4 lines from Sitaraman et al., 2015](https://virtualflybrain.org/reports/SplitSitaraman2015) | `SplitSitaraman2015` |
| [Split-GAL4 lines from Sterne et al., 2021](https://virtualflybrain.org/reports/SplitSterne2021) | `SplitSterne2021` |
| [Split-GAL4 lines from Sun et al., 2017](https://virtualflybrain.org/reports/SplitSun2017) | `SplitSun2017` |
| [Split-GAL4 lines from Takemura et al., 2017](https://virtualflybrain.org/reports/SplitTakemura2017) | `SplitTakemura2017` |
| [Split-GAL4 lines from Tanaka et al., 2008](https://virtualflybrain.org/reports/SplitTanaka2008) | `SplitTanaka2008` |
| [Split-GAL4 lines from Triphan et al., 2016](https://virtualflybrain.org/reports/SplitTriphan2016) | `SplitTriphan2016` |
| [Split-GAL4 lines from Turner-Evans et al., 2017](https://virtualflybrain.org/reports/SplitDavis2017) | `SplitDavis2017` |
| [Split-GAL4 lines from Turner-Evans et al., 2017](https://virtualflybrain.org/reports/SplitTurner_Evans2017) | `SplitTurner_Evans2017` |
| [Split-GAL4 lines from Turner-Evans et al., 2020](https://virtualflybrain.org/reports/SplitTurner_Evans2020) | `SplitTurner_Evans2020` |
| [Split-GAL4 lines from Vijayan et al., 2023](https://virtualflybrain.org/reports/SplitVijayan2023) | `SplitVijayan2023` |
| [Split-GAL4 lines from Vogt et al., 2014](https://virtualflybrain.org/reports/SplitVogt2014) | `SplitVogt2014` |
| [Split-GAL4 lines from Vogt et al., 2016](https://virtualflybrain.org/reports/SplitVogt2016) | `SplitVogt2016` |
| [Split-GAL4 lines from Wang et al., 2020a](https://virtualflybrain.org/reports/SplitWang2020a) | `SplitWang2020a` |
| [Split-GAL4 lines from Wang et al., 2020b](https://virtualflybrain.org/reports/SplitWang2020b) | `SplitWang2020b` |
| [Split-GAL4 lines from Wang et al., 2020c](https://virtualflybrain.org/reports/SplitWang2020c) | `SplitWang2020c` |
| [Split-GAL4 lines from Wolff et al., 2025](https://virtualflybrain.org/reports/SplitWolff2025) | `SplitWolff2025` |
| [Split-GAL4 lines from Xie et al., 2021](https://virtualflybrain.org/reports/SplitXie2021) | `SplitXie2021` |
| [Split-GAL4 lines from Yamagata et al., 2015](https://virtualflybrain.org/reports/SplitYamagata2015) | `SplitYamagata2015` |
| [Split-GAL4 lines from Yoo et al., 2023](https://virtualflybrain.org/reports/SplitYoo2023) | `SplitYoo2023` |
| [Split-GAL4 lines from Zhao et al., 2023](https://virtualflybrain.org/reports/SplitZhao2023) | `SplitZhao2023` |
| [Split-GAL4 lines from Zhao et al., 2025](https://virtualflybrain.org/reports/SplitZhao2025) | `SplitZhao2025` |
| [Splits targetting CX neurons, Wolff2018](https://virtualflybrain.org/reports/FlyLight2019Wolff2018) | `FlyLight2019Wolff2018` |
| [Splits targetting CX neurons, Wolff2018](https://virtualflybrain.org/reports/Wolff2018) | `Wolff2018` |
| [Splits targetting the visual motion pathway, Strother2017](https://virtualflybrain.org/reports/FlyLight2019Strother2017) | `FlyLight2019Strother2017` |
| [Splits targetting the visual motion pathway, Strother2017](https://virtualflybrain.org/reports/Strother2017) | `Strother2017` |
| [Third order olfactory neurons involved in pheromone response - backfills (Kohl2013)](https://virtualflybrain.org/reports/Kohl2013) | `Kohl2013` |

### VNC (ventral nerve cord)

Datasets specific to the adult ventral nerve cord — MANC and FANC on the EM side, the
Court VNC/VNS templates and neuropils, and the handful of driver-line and scRNAseq sets
built around VNC circuits (walking, courtship song, neck motor control).

| Dataset | Short form |
|---|---|
| [Adult VNC neuropils (Court2020)](https://virtualflybrain.org/reports/Court2020) | `Court2020` |
| [Adult VNS neuropils (Court2017)](https://virtualflybrain.org/reports/Court2017) | `Court2017` |
| [Full VNC EM connectome, dense reconstruction (adult male)](https://virtualflybrain.org/reports/Takemura2023) | `Takemura2023` |
| [Full VNS EM, sparse reconstruction (adult female)](https://virtualflybrain.org/reports/Maniates_Selvin2020) | `Maniates_Selvin2020` |
| [Single-cell RNA-seq study of adult ventral nerve cords](https://flybase.org/reports/FBlc0005603) | `FBlc0005603` |
| [Split-GAL4 lines from Bidaye et al., 2014](https://virtualflybrain.org/reports/SplitBidaye2014) | `SplitBidaye2014` |
| [Split-GAL4 lines from Bidaye et al., 2020](https://virtualflybrain.org/reports/SplitBidaye2020) | `SplitBidaye2020` |
| [Split-GAL4 lines from Gorko et al., 2024](https://virtualflybrain.org/reports/SplitGorko2024) | `SplitGorko2024` |
| [Split-GAL4 lines from Lillvis et al., 2024](https://virtualflybrain.org/reports/SplitLillvis2024) | `SplitLillvis2024` |

### Leg, head and thorax

Peripheral and body-wall datasets that are neither brain nor VNC proper: leg
proprioception and imaging, proboscis motor neurons, and thoracic scRNAseq.

| Dataset | Short form |
|---|---|
| [Biomechanical origins of proprioceptive maps in the Drosophila leg](https://virtualflybrain.org/reports/Mamiya2022) | `Mamiya2022` |
| [GAL4 lines from McKellar et al., 2020](https://virtualflybrain.org/reports/McKellar2020) | `McKellar2020` |
| [Images of proboscis muscles from McKellar et al., 2020](https://virtualflybrain.org/reports/HeadMusclesMcKellar2020) | `HeadMusclesMcKellar2020` |
| [Millimeter-scale imaging of a Drosophila leg at single-neuron resolution](https://virtualflybrain.org/reports/Kuan2020) | `Kuan2020` |
| [Single-cell RNA-seq study of the adult thorax](https://flybase.org/reports/FBlc0006361) | `FBlc0006361` |
| [Split-GAL4 lines from Tuthill et al., 2013](https://virtualflybrain.org/reports/SplitTuthill2013) | `SplitTuthill2013` |

### Full CNS and whole body

Resources that deliberately span more than one region: whole-CNS connectomes (BANC,
Male-CNS), descending-neuron driver-line sets that by design run from the brain into the
VNC, and the Fly Cell Atlas / Aging Fly Cell Atlas scRNAseq series, which sample the
whole animal rather than the nervous system alone.

| Dataset | Short form |
|---|---|
| [Full CNS EM connectome, dense reconstruction (adult female)](https://virtualflybrain.org/reports/Bates2025) | `Bates2025` |
| [Full CNS EM connectome, dense reconstruction (adult male)](https://virtualflybrain.org/reports/Berg2025) | `Berg2025` |
| [Neurons involved in courtship and song (Lillvis2018)](https://virtualflybrain.org/reports/Lillvis2018) | `Lillvis2018` |
| [Single-nucleus RNA-seq on cells from 30-days old female flies](https://flybase.org/reports/FBlc0006424) | `FBlc0006424` |
| [Single-nucleus RNA-seq on cells from 30-days old flies](https://flybase.org/reports/FBlc0006423) | `FBlc0006423` |
| [Single-nucleus RNA-seq on cells from 5-days old female and male flies](https://flybase.org/reports/FBlc0004785) | `FBlc0004785` |
| [Single-nucleus RNA-seq on cells from 5-days old female flies](https://flybase.org/reports/FBlc0003846) | `FBlc0003846` |
| [Single-nucleus RNA-seq on cells from 5-days old male flies](https://flybase.org/reports/FBlc0004307) | `FBlc0004307` |
| [Single-nucleus RNA-seq on cells from 50-days old female flies](https://flybase.org/reports/FBlc0006888) | `FBlc0006888` |
| [Single-nucleus RNA-seq on cells from 50-days old flies](https://flybase.org/reports/FBlc0006887) | `FBlc0006887` |
| [Single-nucleus RNA-seq on cells from 50-days old male flies](https://flybase.org/reports/FBlc0007071) | `FBlc0007071` |
| [Single-nucleus RNA-seq on cells from 70-days old female flies](https://flybase.org/reports/FBlc0007348) | `FBlc0007348` |
| [Single-nucleus RNA-seq on cells from 70-days old flies](https://flybase.org/reports/FBlc0007347) | `FBlc0007347` |
| [Single-nucleus RNA-seq on cells from 70-days old male flies](https://flybase.org/reports/FBlc0007532) | `FBlc0007532` |
| [split-GAL4 lines for descending neurons (Namiki2018)](https://virtualflybrain.org/reports/FlyLight2019Namiki2018) | `FlyLight2019Namiki2018` |
| [split-GAL4 lines for descending neurons (Namiki2018)](https://virtualflybrain.org/reports/Namiki2018) | `Namiki2018` |
| [Split-GAL4 lines from Feng et al., 2020](https://virtualflybrain.org/reports/SplitFeng2020) | `SplitFeng2020` |
| [Split-GAL4 lines from Liang et al., 2017](https://virtualflybrain.org/reports/SplitLiang2017) | `SplitLiang2017` |
| [Split-GAL4 lines from Namiki et al., 2022](https://virtualflybrain.org/reports/SplitNamiki2022) | `SplitNamiki2022` |
| [Split-GAL4 lines from Reyn et al., 2017](https://virtualflybrain.org/reports/SplitReyn2017) | `SplitReyn2017` |
| [Split-GAL4 lines from Zung et al., 2025](https://virtualflybrain.org/reports/SplitZung2025) | `SplitZung2025` |

## Stage-agnostic resources

A small number of dataset entities in VFB's knowledge base are reference resources
rather than material from an animal at a particular stage — reused across stages by
design. None fall in this bucket at the time of writing (VFB's templates and neuropil
domain sets are all stage-specific and appear above under their own stage), but the
category is kept here for anything added later that should not be forced into a stage
it does not have.
