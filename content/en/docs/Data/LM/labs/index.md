---
title: "Contributing laboratories"
linkTitle: "Contributing labs"
weight: 55
tags: ["Expression_pattern","single_neuron","clone","lineage","dataset"]
description: >
    Light microscopy datasets deposited directly by the laboratory that produced them, rather than through an imaging facility.
---

## Introduction

These datasets did not come to VFB through one of the large imaging projects. Each was
produced by the laboratory that published it and deposited directly, so VFB carries no
site cross-reference for the images. The imaging source below was established by reading
each dataset's cited paper — the methods, author affiliations and acknowledgements — not
from VFB metadata.

Entries marked † are inferred from affiliations and funding because the paper does not
name an imaging facility outright. Everything else is stated in the paper.

## Datasets

| Dataset | Contents | Imaging source | Records |
|---|---|---|---|
| [Lee_Lineage2020](http://virtualflybrain.org/reports/Lee_Lineage2020) | central brain neurons by lineage, Lee2020 | Tzumin Lee lab, Janelia Research Campus | 462 |
| [Cachero2010](http://virtualflybrain.org/reports/Cachero2010) | Adult Brain fru clones (Cachero2010) | Jefferis lab, MRC Laboratory of Molecular Biology, Cambridge † | 119 |
| [Kohl2013](http://virtualflybrain.org/reports/Kohl2013) | Third order olfactory neurons involved in pheromone response - backfills (Kohl2013) | Jefferis lab, MRC Laboratory of Molecular Biology, Cambridge | 111 |
| [Ito2013](http://virtualflybrain.org/reports/Ito2013) | Ito lab adult brain lineage clone image set | Kei Ito lab, Institute of Molecular and Cellular Biosciences, University of Tokyo | 96 |
| [Yu2013](http://virtualflybrain.org/reports/Yu2013) | Lee lab adult brain lineage clone image set | Tzumin Lee lab, Janelia Research Campus | 95 |
| [Xie2018](http://virtualflybrain.org/reports/Xie2018) | Split GAL4 lines for dopaminergic neurons, Xie2018 | Mark Wu lab, Johns Hopkins University School of Medicine | 78 |
| [Matsuo2016](http://virtualflybrain.org/reports/Matsuo2016) | AMMC local and projection neurons (Matsuo2016) | Kamikouchi lab, Nagoya University, with the Ito lab, University of Tokyo † | 41 |
| [HeadMusclesMcKellar2020](http://virtualflybrain.org/reports/HeadMusclesMcKellar2020) | Images of proboscis muscles from McKellar et al., 2020 | Simpson and Dickson labs, Janelia Research Campus | 18 |
| [Nojima2021](http://virtualflybrain.org/reports/Nojima2021) | Split-GAL4 lines from Nojima et al., 2021 | Goodwin lab, Centre for Neural Circuits and Behaviour, University of Oxford † | 15 |
| [SplitNallasivan2025](http://virtualflybrain.org/reports/SplitNallasivan2025) | Split-GAL4 lines from Nallasivan et al 2025 | Soller lab, University of Birmingham † | 6 |
| [McKellar2020](http://virtualflybrain.org/reports/McKellar2020) | GAL4 lines from McKellar et al., 2020 | Simpson and Dickson labs, Janelia Research Campus | 5 |
| [Lillvis2018](http://virtualflybrain.org/reports/Lillvis2018) | Neurons involved in courtship and song (Lillvis2018) | Stern and Dickson labs, Janelia Research Campus | 2 |

Records are the individuals VFB holds from each dataset.

## How each attribution was established

| Dataset | Paper | Basis |
|---|---|---|
| Lee_Lineage2020 | Lee et al., 2020, eLife | acknowledges Janelia Workstation, FlyLight and Fly Core for technical support |
| Cachero2010 | Cachero et al., 2010, Curr. Biol. | stacks acquired on the lab's own Zeiss 710; single LMB affiliation |
| Kohl2013 | Kohl et al., 2013, Cell | stacks acquired on a Zeiss 710; LMB is the only affiliation on the paper |
| Ito2013 | Ito et al., 2013, Curr. Biol. | all authors at the University of Tokyo; imaging on the lab's Zeiss LSM 510 |
| Yu2013 | Yu et al., 2013, Curr. Biol. | acknowledges the Janelia fly core and FlyLight team for support in data production |
| Xie2018 | Xie et al., 2018, Cell Rep. | stacks acquired in house on a Zeiss LSM510/LSM700; raw files released by the lab |
| Matsuo2016 | Matsuo et al., 2016, J. Comp. Neurol. | Japanese affiliations and funding only; methods text not openly accessible |
| HeadMusclesMcKellar2020 | McKellar et al., 2020, eLife | stacks acquired on Janelia Zeiss confocals with Project Technical Resources support |
| Nojima2021 | Nojima et al., 2021, Curr. Biol. | stacks acquired on a Leica TCS SP5; no external imaging provider acknowledged |
| SplitNallasivan2025 | Nallasivan et al., 2026, eLife | stacks acquired on a Leica SP8 by the authors; driver lines from VDRC and Janelia |
| McKellar2020 | McKellar et al., 2020, eLife | same study as the head muscle set; Janelia confocals and Fly Core |
| Lillvis2018 | Ding et al., 2019, Curr. Biol. | acknowledges Janelia Project Technical Resources for dissection, histology and confocal imaging |

Two recurring traps are worth naming, because both would give the wrong answer. Several of
these studies use driver lines from Janelia or VDRC while acquiring their own images —
`Xie2018` and `SplitNallasivan2025` both do — so the origin of a reagent is not the origin
of an image. And several use FlyCircuit or FlyLight material as a reference for annotation
rather than as source imagery.

Citations are on each dataset's own page on VFB; cite the original study rather than VFB
when you use the images.
