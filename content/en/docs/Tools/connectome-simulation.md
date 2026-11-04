---
title: "Simulating circuits from connectome data"
linkTitle: "Connectome simulation"
weight: 660
description: >
  How researchers turn the connectomes VFB serves into running models of neural activity and behaviour, which tools exist, and what VFB does and does not provide.
---

Virtual Fly Brain holds the structure: neurons, their connectivity, and the ontology that names them, across the FlyWire (FAFB), hemibrain, MANC, FANC, BANC and male CNS connectomes. VFB does not hold simulations, recorded activity or behavioural data, and it does not run models. This page describes how others build models on the same data, so you know where to go next.

The video of a fruit-fly brain simulation on this site is from 2017. It shows the Lo lab's FlySim model built on FlyCircuit light-microscopy neurons with inferred synapses ([Huang et al. 2018](https://doi.org/10.3389/fninf.2018.00099)). Current models are built on electron-microscopy connectomes and are described below.

## Three kinds of model

**Whole-brain point-neuron models.** [Shiu et al. (2024)](https://doi.org/10.1038/s41586-024-07763-9) built a leaky integrate-and-fire model of the whole FlyWire central brain (about 125,000 neurons) with synaptic weight set by synapse count and sign taken from the neurotransmitter predictions of [Eckstein et al. (2024)](https://doi.org/10.1016/j.cell.2024.03.016). Activating sugar-sensing neurons in the model predicted the feeding circuit and motor output, confirmed optogenetically. [Pospisil et al. (2024)](https://doi.org/10.1038/s41586-024-07982-0) take a linear approach, using the connectome as a prior for causal weights to be fitted from perturbation experiments. In 2026, [Li et al.](https://doi.org/10.64898/2026.08.21.745055) (preprint) fitted the weights of a FlyWire-wide rate model to whole-brain calcium imaging for the first time.

**Connectome-constrained trained models.** Here the wiring and signs are fixed from the connectome and the remaining parameters are optimised on a task or on recordings. [Lappalainen et al. (2024)](https://doi.org/10.1038/s41586-024-07939-3) did this for the optic lobe and predicted the responses of visual cell types from a motion task alone. The same approach has been applied to the central-complex compass ([Beiran & Litwin-Kumar 2025](https://doi.org/10.1038/s41593-025-02080-4); [Duan et al. 2025](https://doi.org/10.1101/2025.05.26.655406)), to a FlyWire grooming network coupled to a simulated body ([Özdil et al. 2026](https://doi.org/10.1038/s41467-026-72152-x)), and to the leg circuits of the MANC nerve cord, where a descending-neuron screen in simulation found a minimal walking pattern generator that was then tested in flies ([Pugliese et al. 2025](https://doi.org/10.1101/2025.09.12.675944), preprint).

**Embodied simulation.** Two open physics models of the fly body exist: NeuroMechFly v2 / FlyGym ([Wang-Chen et al. 2024](https://doi.org/10.1038/s41592-024-02497-y)), with vision, olfaction, proprioception and leg adhesion, and flybody ([Vaxenburg et al. 2025](https://doi.org/10.1038/s41586-025-09029-4)), with learned walking and flight. Neither ships a connectome-derived controller; connecting the two is active work in several groups, and as of October 2026 no peer-reviewed study closes the loop from a nerve-cord connectome to a walking body.

## What the connectome does not tell you

Every model above inherits the same gaps, and the papers say so. Synapse sign comes from image-based neurotransmitter prediction (about 94% per neuron) and errors propagate. Electrical synapses are absent from every EM connectome, yet [Frighetto et al. (2026)](https://doi.org/10.1016/j.cub.2026.09.060) show they carry behaviourally necessary signal. Neuromodulation and peptide signalling are not modelled. Synapse count is not synaptic strength. Each connectome is one animal. Most importantly, wiring alone often does not determine dynamics: with the central-complex wiring fixed, untrained models do not form a ring attractor until a few neurons' activity is also known ([Beiran & Litwin-Kumar 2025](https://doi.org/10.1038/s41593-025-02080-4)); trained compass models break under 1% weight perturbation and do not transfer between reconstructions of the same circuit ([Yad & Nabila 2026](https://arxiv.org/abs/2610.29205), preprint); and a *C. elegans* connectome with a learned decoder can walk a simulated fly as well as a fly connectome can ([Brunton et al. 2026](https://doi.org/10.7554/eLife.111516)). A simulation that behaves plausibly is not evidence that it works the way the fly does.

## Tools you can run

Maintained, documented and installable from PyPI:

- [flyvis](https://turagalab.github.io/flyvis/) (Turaga lab): the connectome-constrained optic-lobe model with pretrained ensembles. Visual system only.
- [FlyGym / NeuroMechFly v2](https://neuromechfly.org/) (Ramdya lab): the simulated fly body with senses. You supply the controller; it does not read connectome files.
- The data layer every model consumes: [navis](https://navis-org.github.io/navis/), [fafbseg](https://fafbseg-py.readthedocs.io), [neuprint-python](https://github.com/connectome-neuprint/neuprint-python) and [CAVEclient](https://github.com/CAVEconnectome/CAVEclient), with downloads from [Codex](https://codex.flywire.ai), [neuPrint](https://neuprint.janelia.org) and the [male CNS portal](https://male-cns.janelia.org/). See [VFB_connect](../vfb-connect/), [navis](../navis/) and [neuPrint](../neuprint/) on this site.

Reference implementations:

- [Shiu et al. whole-brain LIF model](https://github.com/philshiu/Drosophila_brain_model): Brian2, FlyWire v630/v783, unchanged since 2024. [eonsystemspbc/fly-brain](https://github.com/eonsystemspbc/fly-brain) ports it to GPU backends (Brian2CUDA, PyTorch, NEST GPU, GeNN).
- [flybody](https://github.com/TuragaLab/flybody): the MuJoCo body and trained walking and flight policies.
- [FlyBrainLab](https://flybrainlab.fruitflybrain.org) (Lazar lab): executable hemibrain, FlyCircuit and larval circuits on GPU; feature-rich but with a slow release cadence.
- [connectome_interpreter](https://connectome-interpreter.readthedocs.io) (Jefferis lab): effective connectivity, path finding and a simple rate model over any adjacency matrix.

There is no web service that runs a fly-brain simulation for you. Codex, neuPrint, BrainCircuits.io and VFB itself query and visualise structure; to simulate you install one of the tools above and download the connectome it needs.

## Reading

Reviews: Wang-Chen & Ramdya 2026, 'The embodied brain' ([arXiv:2601.08056](https://arxiv.org/abs/2601.08056)); Scheffer & Meinertzhagen 2021, 'A connectome is not enough' (*J Exp Biol*); State of Brain Emulation Report 2025 ([arXiv:2510.15745](https://arxiv.org/abs/2510.15745)). This page was last revised in October 2026.
