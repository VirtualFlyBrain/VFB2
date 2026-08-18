---
title: "Curation of Transgene Expression in VFB"
linkTitle: "Transgene Expression Curation"
categories: ["overview","help"]
tags: ["Expression_pattern","transgene","FlyLight"]
weight: 312
description: >
  Details of the curation procedure for transgene expression patterns.
---

<img src="https://www.virtualflybrain.org/images/transgene_curation.png" max-width="100%" alt="Transgene expression into FlyBase and Virtual Fly Brain (VFB)" >

Virtual Fly Brain (VFB) and FlyBase curators record information from the literature about the expression of single transgenes using ontology terms and load this into FlyBase. VFB combines curated expression, genetic and publication data from FlyBase with 3D images of the expression patterns aligned to standard [templates](/docs/data/templates/). These annotated images can then be searched and queried via the [web interface](/docs/website-features/search_query/) or [APIs](/docs/apis/).

This arrangement goes back to the start of the project. VFB has run "a full instance of the FlyBase CHADO Postgres database, kept in sync with the FlyBase update cycle", since its first release, and the traffic is not one-way: the VFB project "extended the annotation of transgene expression in FlyBase for the adult brain to a near comprehensive set of published transgenes" ([Milyaev et al., 2012](https://doi.org/10.1093/bioinformatics/btr677)). Curation done for VFB lands in FlyBase, which is why the transgene record you reach from an image on VFB is the same record a geneticist would cite.

For what a driver line is and how these patterns are produced, see [binary expression systems](/docs/concepts/binary-expression/); for what "expression pattern" means formally on VFB — and why a single-neuron image is a *fragment* of one — see the same page.

