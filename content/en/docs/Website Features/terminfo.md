---
categories: ["overview","help"]
tags: ["term","tools"]
title: "The Term Info tab"
linkTitle: "Term Info"
description: >
   Term Info displays information on the currently selected entity.
weight: 50
---
<link rel="stylesheet" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto/node_modules/@geppettoengine/geppetto-client/geppetto-client/style/css/gpt-icons.css">

## Names

Each entity in VFB has a unique `Name`. The `Name` field also shows semantic tags, to provide additional at-a-glance information, and the identifier (e.g. FBbt_00003823) for the entity. Many entities also have a `Symbol`, which is a more compact name that has been used in the literature. Synonyms are shown in the `Alternative Names` field along with references, where available.

<p align="center">
  <img src="/images/terminfo/terminfo-names.png" alt="Entity Names in Term Info." style="max-width=50%" />
</p>

## Ontology terms and Graphs

`Classification` and `Relationships` fields show parent and related ontology classes for the selected entity. Click to navigate to the Term Info pages for these terms. The `location` and `classification` [Term Context](../termcontext) graphs show partonomy relationships and parentage of the selected entity, respectively.

<p align="center">
  <img src="/images/terminfo/terminfo-ontologies.png" alt="Classification, Relationships and Graphs in Term Info." style="max-width=50%" />
</p>

<i class="far fa-hand-pointer"></i>   Click on terms to select them

## Data

[`Thumbnails`](../thumbnails) show available images (as a carousel if multiple). These can be clicked to add the image to the 3D viewer.

<i class="far fa-hand-pointer"></i>   Click on thumbnails to add an image to the 3D viewer

[Queries](../search_query/#queries-from-term-info) relevant to the selected entity can find related entities and other relevant information. Some EM neurons also have an option to add the neuron to the [Circuit Browser](../circuitbrowser) tool to explore connectivity data. Queries are specialised for different types of entity, for example, the Term Info page for a neuronal cell type may have queries to find images, transgene expression and transcriptomics data, whereas an EM image may have queries to find connectivity data.

<i class="fab fa-quora"></i>   Run term related [queries](../search_query/#queries-from-term-info)

Images (and citation information) can be downloaded from the `Downloads` section and their source dataset, template, and licence information can be found in their own Term Info fields.

<p align="center">
  <img src="/images/terminfo/terminfo-downloads.png" alt="Image downloads and related metadata." style="max-width=50%" />
</p>

<i class="far fa-hand-pointer"></i>   Click on download items to begin downloading

## References and Linkouts
Linkouts to external sites with further information about the selected entity can be found in the `Cross Refernces` section where appropriate. Literature references are in the `References` section, with links to the articles themselves and the FlyBase bibliography pages where available.

<p align="center">
  <img src="/images/terminfo/terminfo-xrefs.png" alt="Cross References and Linkouts in Term Info." style="max-width=50%" />
</p>
