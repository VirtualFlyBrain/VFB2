---
title: "Electron Microscopy Data"
linkTitle: "EM Data"
weight: 1
description: >
    Electron Microscopy Data available on Virtual Fly Brain.

---

Virtual Fly Brain brings together data from multiple [electron microscopy (EM) resources](/docs/resources/), providing access to high-resolution neuroanatomical datasets. These datasets include complete EM volumes of Drosophila brains and ventral nerve cords, neuron reconstructions, connectivity information and neurotransmitter predictions. Data can be visualised using the web browser or accessed programmatically via APIs.

## Datasets Hosted by VFB

Virtual Fly Brain (VFB) hosts several CATMAID instances for exploring connectomic reconstruction data. These datasets provide access to neuroanatomical data from various Drosophila electron microscopy projects. Full details are available on our hosted pages:

### Adult full CNS
- BANC (Brain and Nerve Cord)

### Adult Brain
- FlyWire FAFB (Full Adult Fly Brain)
- [CATMAID FAFB (Full Adult Fly Brain)](/hosted/fafb-catmaid/) - Complete EM volume of an adult Drosophila melanogaster brain with manually traced neurons
- Hemibrain
- Optic-lobe

### Adult VNC
- MANC (Male Adult Nerve Cord)
- [FANC (Female Adult Nerve Cord)](/hosted/fanc-catmaid/) - Adult female ventral nerve cord with reconstructions in both original and template space

### Larval full CNS
- [L1EM (First Instar Larva)](/hosted/l1em-catmaid/) - Complete EM volume of a Drosophila first instar larva brain with manually traced neurons


## Comparison Table

The table below summarises EM datasets that have been integrated into VFB, including the portion of the organism covered (`Anatomy`), the resource(s) where the original data can be found, The level of reconstruction (sparse or dense) and the original publication for the dataset.

| Dataset | VFB symbol | Anatomy                      | Reconstruction | Resource(s) | Original Publication                                                                                                                         |
|------|------------|------------------------------|----------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------|
| BANC | BANC       | Full CNS (adult female)      | Dense         | Codex | [Bates et al. (2025)](https://doi.org/10.1101/2025.07.31.667571)                                                                             |
| Optic-lobe | ol         | Optic lobe (adult male)      | Dense         | NeuPrint; Codex | [Nern et al. (2025)](https://doi.org/10.1038/s41586-025-08746-0)                                                                             |
| FAFB (FlyWire) | fw         | Full brain (female larva)    | Dense         | Codex | [Dorkenwald et al. (2024)](https://doi.org/10.1038/s41586-024-07558-y); [Schlegel et al. (2024)](https://doi.org/10.1038/s41586-024-07686-5) |
| MANC | mv         | Full VNC (adult male)        | Dense         | NeuPrint; Codex | [Takemura et al. (2024)](https://doi.org/10.7554/eLife.97769.1)                                                                              |
| FANC | N/A        | Full VNS (adult female)      | Sparse         | CATMAID | [Phelps et al. (2021)](https://doi.org/10.1016/j.cell.2020.12.013)   |
| Hemibrain | hb         | Partial brain (adult female) | Dense          | NeuPrint | [Scheffer et al. (2020)](https://doi.org/10.7554/eLife.57443)       
| FAFB (CATMAID) | fafb       | Full brain (adult female)    | Sparse         | CATMAID | [Zheng et al. (2018)](https://doi.org/10.1016/j.cell.2018.06.019)                                                                            |
| l1em | l1em       | Full CNS (female larva)      | Sparse         | CATMAID | [Ohyama et al. (2015)](https://doi.org/10.1038/nature14297)                                                                                  |
