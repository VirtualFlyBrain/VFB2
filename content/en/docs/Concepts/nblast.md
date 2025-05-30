---
title: "NBLAST"
linkTitle: "NBLAST"
weight: 50
tags: NBLAST
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

VFB provides precomputed NBLAST scores for all neurons in its database, making morphological similarity searches fast and accessible without requiring computational expertise.

### What's included

VFB NBLAST scores cover:

- **All individual neurons** from major connectome datasets including:
  - FAFB-FlyWire
  - Male-CNS optic lobe  
  - Hemibrain
  - FlyCircuit
  - FAFB-CATMAID datasets

- **Split-GAL4 expression patterns** from FlyLight, enabling discovery of potential driver lines that label specific morphological types

### Types of comparisons

1. **Neuron-to-neuron**: Find morphologically similar neurons within or across datasets
2. **Neuron-to-expression pattern**: Identify split-GAL4 lines that might label neurons similar to those in connectome datasets

## Using NBLAST on VFB

### Accessing NBLAST queries

NBLAST similarity searches are available directly in the VFB interface:

1. Navigate to any individual neuron or split-GAL4 image page
2. Scroll to the term info panel 
3. Look for NBLAST query options (only appears if results are available)
4. Click to see ranked lists of morphologically similar items

### Interpreting results

NBLAST scores range from -1 to 1:
- **1.0**: Perfect match (identical morphology)
- **0.5-1.0**: High similarity
- **0.0-0.5**: Moderate similarity  
- **Below 0.0**: Low similarity or dissimilar morphologies

Results are typically ranked by score, with the most similar items appearing first.

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

- [NBLAST tutorial](/docs/tutorials/apis/4_nblast/) - Detailed programming tutorial
- [Original NBLAST paper](https://doi.org/10.1016/j.neuron.2016.06.012) - Costa et al., 2016
- [VFB NBLAST announcement](/blog/2025/05/29/new-precomputed-neuron-and-expression-pattern-similarity-scores-on-vfb/) - Recent updates and expanded coverage
