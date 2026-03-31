---
title: "Split Driver Expression Patterns"
linkTitle: "Split Driver Expression"
categories: ["overview","help"]
tags: ["Split","Expression_pattern","transgene","FlyLight"]
weight: 30
description: >
  Split driver expression patterns in Virtual Fly Brain.
---

Split drivers comprise at least two partial transcription factors that can reconstitute an active transcription factor when expressed in the same cell. By using different regulatory regions for each component, functional driver expression can be restricted to the intersection of the expression patterns of these regulatory regions. A wide range of regulatory regions have been combined with transcription factor DNA binding domains (DBDs) and Activation Domains (ADs) to form thousands of distinct constructs, referred to as hemidrivers. Millions of combinations are therefore possible, each targeting some precise subset of the many thousands of neurons in the Drosophila nervous system.

<img src="/images/splits_images.png" max-width="50%" alt="A split-GAL4 expression pattern at the intersection of the expression patterns of two hemidrivers.">

Researchers can identify split drivers for neurons of interest from the `Targeting Splits` section of a cell type [Term Info](/docs/website-features/terminfo) page or by using [similarity scores](/docs/tutorials/website/similarityscore/) from a single neuron image. It is also possible to [search](/docs/website-features/search_query) directly for particular hemidrivers and combinations.

<img src="/images/splits_terminfo.png" max-width="50%" alt="Targeting Splits section of cell type Term Info page." >

Similar to [non-split drivers](/docs/concepts/transgene), VFB contains images and curated information about expression patterns for combinations. Each combination gets a standard name in VFB, reflecting the names of the component hemidrivers and any short names for the combination from the literature are added as synonyms (e.g. "[P{VT017411-GAL4.DBD} ∩ P{VT019018-p65.AD} expression pattern](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?id=VFBexp_FBtp0123314FBtp0119891)" has_exact_synonym: SS02256").

<img src="/images/split_vfb.png" alt="split expression shown in Virtual Fly Brain (VFB)" max-width="50%" >

VFB curation uses programmatic methods to generate expression statements for [FlyLight](https://www.janelia.org/project-team/flylight) hemidriver combinations. Combinations are validated against a local copy of the FlyLight dataset and loaded into FlyBase. VFB then links each expression pattern image and the curated expression information to an intersection of the two appropriate hemidrivers.

<img src="/images/splits_figure.png" alt="This techniques work by driving the expression of target transgenes at the intersection between the expression patterns of two hemidriver transgenes." max-width="50%" >





