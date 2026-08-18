---
title: "Cell Types"
weight: 306
linkTitle: "Cell Types"
categories: ["overview","help"]
tag: ["FBbt", "Anatomy", "Ontology", "Typing", "Classification", "Class"]
description: >
  Cell type annotations on VFB.
---

Neurons on VFB are annotated with cell types from the Drosophila Anatomy Ontology (FBbt).

<img src="/images/cell_types/FW_MBON01-terminfo.png" max-width="50%" alt="A FlyWire MBON01 neuron">

## Why do we use ontology terms?

 - Each term represents a concept of a cell type, with a definition based on referenced publications:
 <img src="/images/cell_types/MBON01-definition.png" max-width="50%" alt="Definition for 'mushroom body output neuron 1'">
 - As well as a label, each term has a collection of synonyms, facilitating identification even when the same type has been referred to by different names in different sources:
 <img src="/images/cell_types/MBON01-synonyms.png" max-width="50%" alt="Label and synonyms for 'mushroom body output neuron 1'">
 - Hierarchical – e.g. specific terms for MBON01, MBON02 etc., but also grouped by a general MBON term and all under ‘adult neuron’
 - Neurons of the same type in multiple datasets can be linked to the same ontology term
 - Persistent, resolvable identifiers to uniquely identify cell types e.g. https://virtualflybrain.org/reports/FBbt_00100234


We also use terms from the Drosophila Anatomy Ontology to annotate CNS regions (for the `Template ROI Browser` tool and neuron `connectivity per region` query) and other anatomical features.

## What is in the ontology, and what is not

The DAO admits a named class only where there is good scientific evidence for the presence of that structure in wild-type animals, with links to the literature supporting it; classes added in error have been obsoleted. Much of the hierarchy is not asserted by hand but inferred — `part_of` and `capable_of` relations combined with Gene Ontology process terms let a reasoner derive classifications, and disjointness axioms catch contradictions ([Costa et al., 2013](https://doi.org/10.1186/2041-1480-4-32)).

At the time of the VFB 2023 paper the ontology covered around 13,000 neuroanatomical structures and cell types, including over 9,800 terms for neuron types, curated from more than 1,000 papers; over 3,800 of those neuron types are predicted from connectomics data, and over 2,750 have curated lineage ([Court et al., 2023](https://doi.org/10.3389/fphys.2023.1076533)).

For where the underlying data and the naming standards came from, see [which fly is this?](/about/whichfly/)
