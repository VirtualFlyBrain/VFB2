---
title: "VFB at the ISN Neurochemistry School 2026 in Port Harcourt"
linkTitle: "ISN Neurochemistry School 2026"
date: 2026-10-28
description: >
    Douglas Armstrong and Robert Court gave the Virtual Fly Brain lecture at the ISN Neurochemistry School 2026, 'Neurogenetics for Brain Health', at the University of Port Harcourt, Nigeria, on 27 October 2026.
---

On 27 October 2026 Virtual Fly Brain (VFB) gave Lecture 4 of the ISN Neurochemistry School 2026, 'Neurogenetics for Brain Health', hosted by the Provictoire Research Hub at the [University of Port Harcourt](https://www.uniport.edu.ng), Nigeria. Douglas Armstrong (Principal Investigator at Edinburgh) and Robert Court (Lead DevOps) joined remotely from Edinburgh to present 'Virtual Fly Brain: A Hub for *Drosophila melanogaster* Neural Anatomy, Imaging Data and Connectomics'.

## The school

The [International Society for Neurochemistry](https://www.neurochemistry.org) (ISN) funds [schools](https://www.neurochemistry.org/school-support-grant/) that bring training in current methods to regions where neuroscience is growing, and has supported a series of them in Nigeria. The Port Harcourt school ran from 25 to 31 October and took its students from first principles to working with public data in a week: why the fly is a model for the brain, how to handle flies and run behavioural assays, the genetic toolkit, omics, connectomics, regulatory genomics and neurotoxicology. The thread through all of it was brain health: fly models of neurodevelopmental and neurodegenerative disease, and what they can say about people.

It is a school that builds capacity. The students had been introduced to *Drosophila* as a model the day before our lecture, and ours was the first session of the week to show a connectome.

## Our lecture

We did not teach a tool. Every kind of data the students would meet during the week has a place in VFB, so we gave a tour with one stop for each, so that by Friday they would know where to look.

Douglas opened with why one atlas matters: sixty years of fly neuroscience, from light microscopy and genetic driver lines to electron microscopy connectomes, registered to one brain and described with one vocabulary. He then followed a path the students could take themselves, from a disease gene and its fly model in [FlyBase](https://flybase.org), to where that gene is expressed, to the lines that reach those neurons, to what those neurons connect to.

Robert took the six stops, using one worked example throughout: the PAM dopaminergic neurons, the dopamine input to the mushroom body, and the cells behind many of the learning, ageing and Parkinson's disease models the students would hear about later in the week. Each stop was a short recorded demo of the live site, built to survive a single projected laptop on variable bandwidth.

1. **The brain itself.** The JRC2018 unisex reference brain with its named regions painted in, each one an ontology term with a mesh you can download.
2. **Cell types.** Whatever a paper called a neuron, its term page gives one stable identifier, a curated definition, the references and the synonyms, with the images behind it.
3. **The genetic toolkit.** From one PAM neuron type to the nine split-GAL4 combinations that target it, an expression pattern in the same brain as the neuron it is meant to label, and the Bloomington stock numbers to order.
4. **Transcriptomics.** Single cell RNA sequencing clusters from three atlases mapped to the same cell type, the genes they express, and *ple* (tyrosine hydroxylase), the gene behind the classic dopaminergic driver.
5. **Connectomics.** The same neuron type from three connectomes side by side in one brain, then its partners and the paths from it to the mushroom body output neuron of the same compartment.
6. **The literature behind it.** The same questions asked in plain English through [VFB chat](https://chat.virtualflybrain.org), with every answer linked back to the dataset or paper it came from.

We closed with three ways in to the same answers (the website, the chat and code) and with the point that all of it is open, credited and free to use.

## A shelf for every session

![A week planner titled 'Every session this week has a shelf in VFB', listing the school's lectures and practicals from Monday to Friday, each marked with coloured dots for the stops of the VFB tour it relates to](/images/isn2026/week-map.png)

*The week map from our lecture. Dots mark where each stop on the tour comes back during the school.*

We planned the lecture by reading the programme and asking, for every lecture and practical, what VFB could do for a student sitting in it. This is what we found.

| When | Session | Where VFB helps |
|---|---|---|
| Monday | Why the fly, classical genetics, behavioural assays | The fly brain is mapped and the major datasets share one coordinate space. Gene and allele terms link to FlyBase, and driver records link to the stock centres. Neurons implicated in behaviours such as courtship are curated with the papers behind them. |
| Tuesday | Omics, with [Niklas Kempynck](https://github.com/nkempynck) ([Aerts lab](https://aertslab.org), VIB-KU Leuven) | Single cell RNA sequencing clusters are mapped to cell types, so you can go from a gene to the neurons that express it, or from a neuron type to its expression profile. |
| Tuesday | GAL4/UAS, RNAi and CRISPR as disease models | More than 20,000 driver lines (October 2026) with expression images aligned to the template brain, and split-GAL4 combinations annotated with the neurons they target: find the line that reaches the cell you care about. |
| Tuesday | Open science, with [André Maia Chagas](https://www.sussex.ac.uk/research/centres/sussex-neuroscience/research/openscience) (University of Sussex) | VFB as a worked case: open licences, persistent identifiers, credit to the people who produced the data, and an open source stack. |
| Wednesday | Comparative connectomics, with [Lucia Prieto Godino](https://www.crick.ac.uk/research/labs/lucia-prieto-godino) (Francis Crick Institute) | Several connectomes in one coordinate space, so the same neuron type can be compared across datasets, sexes and individuals. |
| Wednesday | Public neurogenomics repositories | VFB is the fly neuroanatomy node in that landscape, with links out to FlyBase, neuPrint, FlyWire Codex and FlyLight. |
| Wednesday | Enhancers and regulatory genomics, and the [CREsted](https://github.com/aertslab/CREsted) enhancer modelling practical with Niklas Kempynck | The enhancer fragment GAL4 collections are the reagents whose expression images VFB serves, so a predicted enhancer can be checked against an imaged expression pattern. |
| Wednesday | Analysing public omics data, with Niklas Kempynck | The cluster to cell type mapping gives the anatomical label for a differential expression result. |
| Wednesday | Gene to circuit with neuPrint | VFB tells you which neuron to look up, next to its light microscopy images and driver lines, before you query its connections. |
| Thursday | Neurotoxicology: experimental design, oxidative stress and mitochondria | Dopaminergic neuron clusters are a standard readout in fly models of Parkinson's disease and of toxicity. Their images, drivers and connectivity sit in one place, on standard templates that make imaging comparable. |
| Thursday | 3D printing and brain dissection practicals | Template brain and brain region meshes download as files that print, and the painted regions are an orientation guide for the dissection. |
| Friday | From flies to brain health | Dopaminergic and mushroom body circuits as the readouts for disease models, with FlyBase links from fly genes to their human orthologues. |

The match was closest where the school came back to our worked example. The students' group project in the omics practicals was 'The fly brain in five models of Parkinson's disease' ([course materials](https://github.com/nkempynck/isn-school-2026)), which starts from the same dopaminergic neurons we had used for every stop of the tour.

## Try it yourself

Every stop on the tour has a step by step session in the [VFB Self-led Learning Sessions](https://workshop.virtualflybrain.org), which are free, open to anyone and need little or no setup. Start with the one that matches the work in front of you.

Our thanks go to Chinna Orish and the organising team for the invitation, and to the students for their time.
