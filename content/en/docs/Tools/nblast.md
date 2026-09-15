---
title: "Running NBLAST"
linkTitle: "NBLAST"
weight: 658
description: >
  Scoring morphological similarity yourself, in navis or nat.nblast, rather than using
  VFB's precomputed scores.
---

VFB precomputes NBLAST scores and exposes them through the "find similar" queries on the
website, so you do not need to run NBLAST yourself to use them — the
[NBLAST concept page](/docs/concepts/nblast/) explains what is covered and how to tell whether
a given neuron has scores. This page is for when you want to score your own neurons, or score
against a set VFB does not cover.

NBLAST works on **dotprops**: neurons resampled into points with associated tangent vectors.
Scoring is therefore a two-step business — convert, then compare — and both the resampling
distance and the neighbourhood size affect the result. Neurons must also be in the same
template space before the comparison means anything, which is where
[flybrains](/docs/tools/navis-flybrains/) or `nat.flybrains` come in.

## In Python, with navis

```python
import navis

nl = navis.example_neurons(5)

# Convert to dotprops first; resample and k affect the scores
dps = navis.make_dotprops(nl, resample=1, k=5)

scores = navis.nblast_allbyall(dps)
```

`navis.nblast()` compares one set against another where you do not want the all-by-all matrix.
Scores are conventionally normalised against a self-self comparison, so a perfect match scores
1.

## In R, with nat.nblast

`nat.nblast` is part of the [natverse](/docs/tools/natverse/) and installs with it.

## Where next

The [NBLAST tutorial](/docs/tutorials/apis/nblast/) works through a real comparison end to end,
including preparing the dotprops and interpreting the resulting scores. For what the scores
mean and how VFB uses them, see [NBLAST](/docs/concepts/nblast/).

The method is described in
[Costa et al. (2016)](https://doi.org/10.1016/j.neuron.2016.06.012).
