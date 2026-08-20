---
title: "Electron Microscopy Data"
linkTitle: "EM Data"
weight: 502
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
| BANC | `BANC` | v626 | Full CNS (adult female) | Dense | [Codex](https://codex.flywire.ai/) | [Bates et al. (2025)](https://doi.org/10.1101/2025.07.31.667571), published as [Bates et al. (2026)](https://doi.org/10.1038/s41586-026-10735-w) |
| male-CNS | `mc` | v0.9 | Full CNS (adult male) | Dense | [NeuPrint](https://neuprint.janelia.org/); [Codex](https://codex.flywire.ai/) | [Berg et al. (2025)](https://doi.org/10.1101/2025.10.09.680999) |
| Optic-lobe | `ol` | v1.0.1 | Optic lobe (adult male) | Dense | [NeuPrint](https://neuprint.janelia.org/); [Codex](https://codex.flywire.ai/) | [Nern et al. (2025)](https://doi.org/10.1038/s41586-025-08746-0) |
| FAFB (FlyWire) | `fw` | v783 | Full brain (adult female) | Dense | [Codex](https://codex.flywire.ai/) | [Dorkenwald et al. (2024)](https://doi.org/10.1038/s41586-024-07558-y); [Schlegel et al. (2024)](https://doi.org/10.1038/s41586-024-07686-5) |
| MANC | `mv` | v1.2.1 | Full VNC (adult male) | Dense | [NeuPrint](https://neuprint.janelia.org/); [Codex](https://codex.flywire.ai/) | [Takemura et al. (2024)](https://doi.org/10.7554/eLife.97769.1) |
| Hemibrain | `hb` | v1.2.1 | Partial brain (adult female) | Dense | [NeuPrint](https://neuprint.janelia.org/) | [Scheffer et al. (2020)](https://doi.org/10.7554/eLife.57443) |
| FAFB (CATMAID) | `fafb` | — | Full brain (adult female) | Sparse | [CATMAID (VFB)](/hosted/fafb-catmaid/) | [Zheng et al. (2018)](https://doi.org/10.1016/j.cell.2018.06.019) |
| L1 CNS (CATMAID) | `l1em` | — | Full CNS (female larva) | Sparse | [CATMAID (VFB)](/hosted/l1em-catmaid/) | [Ohyama et al. (2015)](https://doi.org/10.1038/nature14297) |
| FANC | — | — | Full VNS (adult female) | Sparse | [CATMAID (VFB)](/hosted/fanc-catmaid/) | [Phelps et al. (2021)](https://doi.org/10.1016/j.cell.2020.12.013) |

A neuron count, and often a neuron's identifier, is a property of a **release** rather than of a
dataset. The versions above are what VFB currently holds; see
[Connectome versioning](/docs/data/em/versioning/) for what changes between releases and how to
follow an identifier across them. The same version list, with the symbols used to include or exclude
a dataset from a query, is on the [Connectivity data](/docs/data/connectivity/) page.

FlyWire, hemibrain and FAFB (CATMAID) are reconstructions of the same tissue. Counting across them
double-counts neurons; [Connectivity data](/docs/data/connectivity/) explains how VFB handles that
and which datasets to exclude.

## Datasets Hosted by VFB

VFB runs the public CATMAID instances below. Several are archives of resources whose original
hosts have gone offline, and for some VFB is the only remaining public copy; others are served
here because VFB is where the dataset is published from. Each instance has its own page under
[sites hosted by VFB](/hosted/), giving what it contains, how to open it and how to cite it.

Hosting an instance is not the same as integrating its neurons. Only the datasets marked below
are registered in the VFB knowledge base and reachable from a VFB search, term page or API call;
for the rest, the CATMAID instance is the way in.

| Instance | Anatomy | In the VFB knowledge base | Original publication |
|---|---|---|---|
| [FAFB CATMAID](/hosted/fafb-catmaid/) | Full brain (adult female) | Neurons and connectivity (`fafb`) | [Zheng et al. (2018)](https://doi.org/10.1016/j.cell.2018.06.019); [FAFB project](https://flyconnecto.me/) |
| [L1EM CATMAID](/hosted/l1em-catmaid/) | Full CNS (first instar larva) | Neurons and connectivity (`l1em`) | [Ohyama et al. (2015)](https://doi.org/10.1038/nature14297); [Winding et al. (2023)](https://doi.org/10.1126/science.add9330) |
| [FANC CATMAID](/hosted/fanc-catmaid/) | Full VNS (adult female) | Neurons only — no connectivity | [Phelps et al. (2021)](https://doi.org/10.1016/j.cell.2020.12.013); [Lee lab resources](https://www.lee.hms.harvard.edu/resources) |
| [ABD1.5 CATMAID](/hosted/abd1-5-catmaid/) | Abdominal segments A2–A3 (first instar larva), wild type | No | [Ohyama et al. (2015)](https://doi.org/10.1038/nature14297); [Schneider-Mizell et al. (2016)](https://doi.org/10.7554/eLife.12059); [Valdes-Aleman et al. (2021)](https://doi.org/10.1016/j.neuron.2020.10.004) |
| [IAV-ROBO CATMAID](/hosted/iav-robo-catmaid/) | Abdominal segments A1–A2 (first instar larva), altered genotype | No — see note below | [Valdes-Aleman et al. (2021)](https://doi.org/10.1016/j.neuron.2020.10.004) |
| [IAV-TNT CATMAID](/hosted/iav-tnt-catmaid/) | Full CNS (first instar larva), altered genotype | No — see note below | [Valdes-Aleman et al. (2021)](https://doi.org/10.1016/j.neuron.2020.10.004) |
| [L3VNC CATMAID](/hosted/l3vnc-catmaid/) | Ventral nerve cord (third instar larva) | No | [Gerhard et al. (2017)](https://doi.org/10.7554/eLife.29089) |
| [Larva1099 CATMAID](/hosted/larva1099-catmaid/) | Full CNS (first instar larva), eFIB-SEM | No | [Randel et al. (2026)](https://doi.org/10.1101/2025.09.25.678485) |

The IAV-ROBO and IAV-TNT volumes were imaged from animals whose circuits had been altered
experimentally — a misexpression and a synaptic-silencing manipulation respectively — rather than
from wild-type animals. Their neurons carry projections that the manipulation moved, so they do
not correspond to the wild-type anatomy the Drosophila Anatomy Ontology describes and are
deliberately not registered as VFB individuals. Comparing them against the wild-type ABD1.5
reference is the point of the dataset; use the CATMAID instances directly to do it.

VFB also hosts two non-CATMAID resources: [BrainTrap](/hosted/braintrap/), a database of 3D
protein-trap expression patterns, and the [FLYBRAIN Neuron Database](/hosted/flybrainndb/).