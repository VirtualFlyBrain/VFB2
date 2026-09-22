---
title: "Classes and Individuals"
linkTitle: "Classes & Individuals"
weight: 301
categories: ["overview","help"]
tags: ["class","individual","instance","ontology","FBbt","term info"]
description: >
  The difference between a class (a type of thing) and an individual (a specific
  instance) in VFB.
---

VFB describes two kinds of thing, and it helps to know which you are looking at:
**classes** and **individuals**.

## Classes

A **class** is an ontology term — a general *type* of thing rather than any one
example of it. "Kenyon cell", "medulla" and "GABAergic neuron" are classes. Each
class:

- represents a concept, with a definition based on referenced publications;
- has a label and a set of synonyms;
- sits in a hierarchy — a specific class such as "MBON01" is a subclass of the
  more general "mushroom body output neuron", and so on up to "adult neuron";
- has a persistent, resolvable identifier (for example
  [FBbt_00100234](https://virtualflybrain.org/reports/FBbt_00100234)).

Most classes in VFB come from the Drosophila Anatomy Ontology (FBbt) for anatomy
and cell types; genes, developmental stages and biological processes are also
represented as classes. See [Cell Types](/docs/concepts/cell_types/) for how
neurons are classified.

## Individuals

An **individual** is a specific *instance* — one concrete example of one or more
classes. Individuals include:

- a single neuron reconstructed from an EM volume, or one confocal image of an
  expression pattern;
- a template brain;
- a dataset;
- an scRNAseq cluster;
- a publication.

An individual is an **instance of** one or more classes: a particular
reconstructed neuron is an instance of a neuron-type class, which is what tells
you what type of cell it is. A single individual can be an instance of several
classes at once.

## Telling them apart on VFB

Both classes and individuals have their own
[Term Info](/docs/website-features/terminfo/) pages. The `Name` field's tags,
together with the `Classification` and `Relationships` fields, show how an entity
is typed and how it relates to the classes above it. As a rough guide, anatomy
and cell-type **classes** carry ontology identifiers such as `FBbt_…`, while
**individuals** (images, templates, datasets) usually carry `VFB_…` identifiers.

The distinction matters when [querying](/docs/website-features/queries/): queries
are specialised by type, so some run on classes (for example *Subclasses of…* or
*Neurons with some part in…*) and others run on individuals (for example the
connectivity and similarity queries for a single reconstructed neuron).
