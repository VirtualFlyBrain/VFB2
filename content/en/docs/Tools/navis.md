---
title: "navis"
linkTitle: "navis"
weight: 652
description: >
  The core Python library for reading, analysing, transforming and plotting neurons.
---

`navis` is the workhorse of the Python side of this toolchain. It represents neurons as
skeletons, meshes or dotprops, and provides the operations you then want to perform on them:
pruning and resampling, morphometrics, NBLAST similarity, plotting in 2D and 3D, and
transformation between template spaces.

Most of the other Python tools here produce or consume `navis` objects — `pymaid` returns
CATMAID skeletons as `navis` neurons, `neuprint-python` does the same for neuPrint bodies, and
[flybrains](/docs/tools/navis-flybrains/) plugs template-space transforms into
`navis.xform_brain`. Learning `navis` first therefore pays off across the rest.

## Install

```sh
pip3 install "navis[all]"
```

The `[all]` extra pulls in the optional dependencies, including those for 3D plotting. A plain
`pip3 install navis` works if you only need the core.

## Quick start

```python
import navis

# navis ships example neurons: olfactory projection neurons from the hemibrain
n = navis.example_neurons(1, kind='skeleton')
n
```

That prints a summary — node count, cable length, soma, units — and confirms the install is
working. `navis.example_neurons(5)` returns a `NeuronList`, the container used whenever you
work on more than one neuron at a time.

## Where next

Three tutorials here go further: [exploring neurons in navis](/docs/tutorials/apis/navis/)
covers the data types and how to manipulate them,
[plotting](/docs/tutorials/apis/plotting/) covers visualisation, and
[NBLAST](/docs/tutorials/apis/nblast/) covers morphological comparison. See also the
[NBLAST](/docs/tools/nblast/) page here.

Full documentation: [navis-org.github.io/navis](https://navis-org.github.io/navis/).
Source: [navis-org/navis](https://github.com/navis-org/navis).
