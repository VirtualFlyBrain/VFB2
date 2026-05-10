---
title: "Cell Types"
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
 - Persistent, resolvable identifiers to uniquely identify cell types e.g. http://virtualflybrain.org/reports/FBbt_00100234


We also use terms from the Drosophila Anatomy Ontology to annotate CNS regions (for the `Template ROI Browser` tool and neuron `connectivity per region` query) and other anatomical features.
