---
title: "Electron Microscopy Data"
linkTitle: "EM Data"
weight: 1
description: >
    Electron Microscopy Data available on Virtual Fly Brain.

---

Virtual Fly Brain brings together data from multiple [electron microscopy (EM) resources](/docs/resources/), providing access to high-resolution neuroanatomical datasets. These datasets include complete EM volumes of Drosophila brains and ventral nerve cords, neuron reconstructions, connectivity information and neurotransmitter predictions. Data can be visualised using the web browser or accessed programmatically via [APIs](/docs/apis/).

{{< vfb-figures set="em" >}}

The synaptic connectivity derived from these datasets is described on its own page. See
[Connectivity data](/docs/data/connectivity/) for what an edge means, which connectomes
contribute one, and how to handle reconstructions that cover the same tissue.

## Comparison Table of Integrated Datasets

The table below summarises EM datasets that have been integrated into VFB, including the portion of the organism covered (`Anatomy`), the resource(s) where the original data can be found, The level of reconstruction (sparse or dense) and the original publication for the dataset.

| Dataset | VFB symbol | Version in VFB | Anatomy | Reconstruction | Resource(s) | Original Publication |
|---|---|---|---|---|---|---|
| BANC | `BANC` | v626 | Full CNS (adult female) | Dense | Codex | [Bates et al. (2025)](https://doi.org/10.1101/2025.07.31.667571), published as [Bates et al. (2026)](https://doi.org/10.1038/s41586-026-10735-w) |
| male-CNS | `mc` | v0.9 | Full CNS (adult male) | Dense | NeuPrint; Codex | [Berg et al. (2025)](https://doi.org/10.1101/2025.10.09.680999) |
| Optic-lobe | `ol` | v1.0.1 | Optic lobe (adult male) | Dense | NeuPrint; Codex | [Nern et al. (2025)](https://doi.org/10.1038/s41586-025-08746-0) |
| FAFB (FlyWire) | `fw` | v783 | Full brain (adult female) | Dense | Codex | [Dorkenwald et al. (2024)](https://doi.org/10.1038/s41586-024-07558-y); [Schlegel et al. (2024)](https://doi.org/10.1038/s41586-024-07686-5) |
| MANC | `mv` | v1.2.1 | Full VNC (adult male) | Dense | NeuPrint; Codex | [Takemura et al. (2024)](https://doi.org/10.7554/eLife.97769.1) |
| Hemibrain | `hb` | v1.2.1 | Partial brain (adult female) | Dense | NeuPrint | [Scheffer et al. (2020)](https://doi.org/10.7554/eLife.57443) |
| FAFB (CATMAID) | `fafb` | — | Full brain (adult female) | Sparse | CATMAID | [Zheng et al. (2018)](https://doi.org/10.1016/j.cell.2018.06.019) |
| L1 CNS (CATMAID) | `l1em` | — | Full CNS (female larva) | Sparse | CATMAID | [Ohyama et al. (2015)](https://doi.org/10.1038/nature14297) |
| FANC | — | — | Full VNS (adult female) | Sparse | CATMAID | [Phelps et al. (2021)](https://doi.org/10.1016/j.cell.2020.12.013) |

A neuron count, and often a neuron's identifier, is a property of a **release** rather than of a
dataset. The versions above are what VFB currently holds; see
[Connectome versioning](/docs/data/em/versioning/) for what changes between releases and how to
follow an identifier across them. The same version list, with the symbols used to include or exclude
a dataset from a query, is on the [Connectivity data](/docs/data/connectivity/) page.

FlyWire, hemibrain and FAFB (CATMAID) are reconstructions of the same tissue. Counting across them
double-counts neurons; [Connectivity data](/docs/data/connectivity/) explains how VFB handles that
and which datasets to exclude.

## Datasets Hosted by VFB

Virtual Fly Brain (VFB) hosts several CATMAID instances for exploring connectomic reconstruction data. These datasets provide access to neuroanatomical data from various Drosophila electron microscopy projects. Each instance has its own page under [sites hosted by VFB](/hosted/).