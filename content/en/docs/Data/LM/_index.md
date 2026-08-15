---
title: "Light Microscopy Data"
linkTitle: "LM Data"
weight: 508
date: 2026-08-15
description: >
    Light Microscopy Data available on Virtual Fly Brain.

---

Light microscopy is the largest body of data on VFB by number of source studies. It
answers a different question from EM: rather than what a neuron connects to, it tells
you which genetic reagent will let you see or manipulate a cell type, and what else that
reagent labels. VFB registers confocal image stacks from more than a hundred studies
onto the [standard templates](/docs/data/templates/), classifies what they label with
Drosophila Anatomy Ontology terms, and links each driver back to its FlyBase record and
stock centre.

{{< vfb-figures set="lm" >}}

## Kinds of LM data

The distinction that matters when searching is between an image of a *whole expression
pattern* — everything a driver labels — and an image of a *single neuron* or small
clone picked out of that pattern.

| Kind | What one image is | Typical use |
|---|---|---|
| Driver expression pattern | The full pattern of a GAL4 or LexA line in a CNS | Find a reagent that covers your region of interest, and see what else it hits |
| Split-GAL4 combination | The pattern of an AD/DBD hemidriver pair | Find a reagent specific enough to target one cell type |
| Expression pattern fragment | A segmented part of a driver's pattern | Compare a driver against a neuron or region without the rest of the pattern in the way |
| Single neuron | One neuron isolated by stochastic labelling (MCFO, FLP-out) or by single-cell clonal analysis | Get a morphology to compare against EM or by [NBLAST](/docs/website-features/) |
| Clone or lineage | A neuroblast clone or a *fru*-positive clone | Work with developmental units rather than single cells |
| Painted domain | A neuropil region drawn onto a template | Anatomical reference; see [Templates](/docs/data/templates/) |

Every one of these is registered to a template, so a single-neuron image from one study
can be compared directly against an EM reconstruction from another, and a driver's
pattern can be scored for overlap against any region or neuron.

## Data providers

VFB holds 125 light microscopy datasets. Each is grouped below by where its images were
produced. For the large collections that is recorded in VFB, through the source
cross-references carried by the images or the dataset's own description; for the
directly-deposited sets it was established by reading the cited paper.

| Provider | What it contributes | Datasets | Records in VFB |
|---|---|---|---|
| [Janelia FlyLight](/docs/data/lm/flylight/) | The Generation 1 GMR GAL4/LexA collection, its MCFO single-neuron derivatives, the Truman larval flip-out collection, and the per-paper split-GAL4 sets | 62 | 72,357 |
| [VDRC](/docs/data/lm/vdrc/) | The Dickson lab VT enhancer-fragment collection, imaged at VDRC and re-imaged at Janelia | 3 | 23,395 |
| [FlyCircuit](/docs/data/lm/flycircuit/) | Single neurons from the Chiang lab collection, one neuron per image | 1 | 16,127 |
| [Contributing laboratories](/docs/data/lm/labs/) | Lineage clone sets, *fru* clones and single-study collections deposited directly by the lab that produced them | 12 | 1,048 |
| [BrainTrap](/docs/data/lm/braintrap/) | Protein-trap expression patterns in the adult brain | 1 | 501 |
| [No images loaded](/docs/data/lm/other/) | Dataset records whose split combinations are searchable but whose imagery is not held by VFB | 37 | none |
| [Templates and painted domains](/docs/data/templates/) | Reference templates and the neuropil domains drawn onto them | 9 | 865 |

Records are the individuals VFB holds from a dataset — expression patterns, fragments,
single neurons or painted domains. They count what VFB has loaded, not what a collection
contains at source.

Every dataset that holds images has an attributed source. The 37 under *No images loaded*
are dataset records without imagery: their split combinations are recorded as FlyBase
features and are searchable, but there is no image data to attribute.

Citations are recorded on each dataset's own page on VFB rather than repeated here, so
that they stay correct if a record is updated. Cite the original study, not VFB, when you
use the images.

## Expression annotations

Registration puts an image in the right place; annotation is what makes it queryable.
VFB curators and pipelines record, for each driver, which anatomical structures it is
expressed in, as ontology-classified assertions rather than free text. That is what
lets a query for a cell type return the drivers that label it, and a query for a driver
return everything it is known to hit.

These annotations come from two sources: curation of the published literature, and
computed overlap between a registered expression pattern and the painted domains or
neuron images in the same template space. They are annotations of what has been
observed and recorded — a driver with no recorded expression in a region has not been
shown to be absent there.

## Finding LM data

- **From a cell type.** Open any neuron class and run the expression queries on its
  Term Info pane to get the drivers reported to label it.
- **From a region.** Open a neuropil and ask for the expression patterns that overlap
  it.
- **From an image.** Run [NBLAST](/docs/website-features/) from a single-neuron image
  to find morphologically similar neurons, LM or EM, across every registered dataset.
- **From a reagent name.** Search the line directly — `R81G11`, `VT061192`, `SS04495` —
  or the FlyBase identifier.
- **Programmatically.** `VFB_connect` exposes the same queries; see the
  [APIs](/docs/apis/) page.

Adult LM images are registered to
[JRC2018Unisex or JRC2018UnisexVNC](/docs/data/templates/) unless the study predates
them, in which case the older JFRC2 or Court2018 VNS template may be the only alignment
available. Check the template shown on the image's Term Info page before comparing
coordinates across studies.

## Data VFB does not hold

VFB indexes and registers LM images, and links out to the original collections for the
raw, unregistered data. For adult FlyLight material that means
[flweb.janelia.org](https://flweb.janelia.org/),
[gen1mcfo.janelia.org](https://gen1mcfo.janelia.org/) and
[splitgal4.janelia.org](https://splitgal4.janelia.org/); VFB hosts the raw larval
FlyLight images itself, at
[raw.larval.flylight.virtualflybrain.org](https://raw.larval.flylight.virtualflybrain.org/).
See [FlyLight](/docs/data/lm/flylight/) and the
[external resources](/docs/resources/) page.
