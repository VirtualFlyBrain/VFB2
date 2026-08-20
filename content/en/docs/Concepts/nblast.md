---
title: "NBLAST"
linkTitle: "NBLAST"
weight: 316
tag: [NBLAST,NBLASTexp]
description: >
  Understanding NBLAST morphological similarity scoring on VFB
---

## What is NBLAST?

NBLAST ([Costa et al., 2016](https://doi.org/10.1016/j.neuron.2016.06.012)) is a computational method to quantify morphological similarity between neurons. It provides an objective way to compare neuron shapes and identify morphologically similar cells within and across datasets.

## How NBLAST works

NBLAST operates on "dotprops" - a representation of neurons as tangent vectors that capture the local geometry of neuronal arbors. The algorithm:

1. **Converts neurons to dotprops**: Each neuron is represented as a set of points with associated directional vectors
2. **Compares vector pairs**: For each tangent vector in a query neuron, NBLAST finds the closest tangent vector in the target neuron
3. **Calculates similarity scores**: Scores are computed based on both the distance between vectors and their directional similarity (dot product)
4. **Normalizes results**: Final scores are typically normalized to a self-self comparison, where a perfect match equals 1

![NBLAST concept](https://github.com/schlegelp/navis/raw/master/docs/_static/NBLAST_neuron_comparison.png)

## NBLAST on VFB

VFB precomputes NBLAST scores so that morphological similarity searches are fast and need no
computational expertise. Coverage is not uniform: scores exist where a neuron has a registered
morphology in a template space that has been scored, and they are added as new data lands. The
reliable way to tell whether a given neuron has them is to open its
[Term Info](/docs/website-features/terminfo/) — the similarity query appears only when scores exist
for that neuron.

### What's included

Scores cover individual neurons from the EM connectome datasets listed on the
[EM data](/docs/data/em/) page, single neurons from the [FlyCircuit collection](/docs/data/lm/flycircuit/),
and split-GAL4 expression patterns from [FlyLight](/docs/data/lm/flylight/) — the last of these being
what lets you go from a neuron to a driver line that might label it.

The most recent expansion of coverage is described in the
[precomputed similarity scores announcement](/blog/2025/05/29/new-precomputed-neuron-and-expression-pattern-similarity-scores-on-vfb/).

### Types of comparisons

1. **Neuron-to-neuron**: Find morphologically similar neurons within or across datasets
2. **Neuron-to-expression pattern**: Identify split-GAL4 lines that might label neurons similar to those in connectome datasets

## Using NBLAST on VFB

### Accessing NBLAST queries

 See [Similarity Score Queries Guide](/docs/tutorials/website/similarityscore/) for details of how to find NBLAST similarity queries in the VFB interface.

### Interpreting results

Scores on VFB are normalised against a self-self comparison, so 1.0 is the score a neuron gets
against itself and is the practical ceiling. Higher is more similar; negative scores indicate
morphologies with little in common.

There is no universal threshold that separates a real match from a spurious one. The cut-off depends
on the neuron, the datasets being compared and the quality of the reconstructions, so a score should
be read against the other scores in the same ranked list rather than against a fixed scale. A hit at
the top of a list of otherwise low scores is worth inspecting; the same absolute value buried in a
list of high scores is not. Always look at the morphology before accepting a match.

## Applications

### Research applications
- **Cell type classification**: Group neurons by morphological similarity
- **Cross-dataset comparison**: Find corresponding cell types across different connectomes
- **Driver line selection**: Identify genetic tools for targeting specific morphological types
- **Evolutionary studies**: Compare homologous neurons across species

### Workflow integration
NBLAST results on VFB can be:
- Exported for further analysis
- Used to build custom neuron collections
- Combined with other search criteria (anatomy, connectivity)
- Accessed programmatically via VFB APIs

## Technical considerations

### Optimization for VFB
- All neurons are standardized to common template spaces
- Consistent spatial resolution across datasets
- Normalized scoring for cross-dataset comparisons
- Regular updates as new data becomes available

### Limitations
- Focuses purely on morphological similarity
- May not capture functional relationships
- Sensitive to differences in reconstruction quality
- Template registration accuracy affects cross-dataset comparisons

## Further reading

- [NBLAST tutorial](/docs/tutorials/apis/nblast/) - Detailed programming tutorial
- [Original NBLAST paper](https://doi.org/10.1016/j.neuron.2016.06.012) - Costa et al., 2016
- [VFB NBLAST announcement](/blog/2025/05/29/new-precomputed-neuron-and-expression-pattern-similarity-scores-on-vfb/) - Recent updates and expanded coverage
