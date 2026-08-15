---
title: "Light Microscopy Data"
linkTitle: "LM Data"
weight: 5
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

## Major collections

Collections are grouped here by what they contain. VFB holds around 120 LM datasets in
total, most of them the per-paper split-GAL4 sets described below; the full list is
reachable from any template's `All datasets` query.

| Collection | Anatomy / stage | What the images show | VFB dataset | Publication |
|---|---|---|---|---|
| FlyLight Gen1 GAL4/LexA | Adult brain and VNC | Whole expression patterns of the GMR enhancer-fragment collection | [FlyLightGen1Set2019](http://virtualflybrain.org/reports/FlyLightGen1Set2019) | [Jenett et al., 2012](https://doi.org/10.1016/j.celrep.2012.09.011) |
| FlyLight Gen1 MCFO | Adult brain and VNC | Single neurons stochastically labelled within Gen1 lines | [Gen1MCFOJenett2012](http://virtualflybrain.org/reports/Gen1MCFOJenett2012) and four further sets | [Jenett et al., 2012](https://doi.org/10.1016/j.celrep.2012.09.011) |
| VT collection (Dickson lab) | Adult brain | Whole expression patterns of the VT GAL4, LexA and split lines, imaged at VDRC | [Dickson_VT](http://virtualflybrain.org/reports/Dickson_VT) | [Tirian and Dickson, 2017](https://doi.org/10.1101/198648) |
| FlyCircuit 1.0 | Adult brain | Single neurons from the Chiang lab collection, one neuron per image | [Chiang2010](http://virtualflybrain.org/reports/Chiang2010) | [Chiang et al., 2011](https://doi.org/10.1016/j.cub.2010.11.056) |
| *fru* clones | Adult brain | Clonal units of the *fruitless*-positive circuitry | [Cachero2010](http://virtualflybrain.org/reports/Cachero2010) | [Cachero et al., 2010](https://doi.org/10.1016/j.cub.2010.07.045) |
| Per-paper split-GAL4 sets | Mostly adult brain and VNC | Split combinations characterised in one publication each — around 70 sets, from Aso and Rubin's dopaminergic lines through to Nern, Wolff, Zhao and Zung in 2025 | Search `Split` in datasets | Per dataset page |
| Truman larval flip-out | Larval CNS | Single neurons and small clones in the larval CNS | [TrumanWood2018](http://virtualflybrain.org/reports/TrumanWood2018) | Per dataset page |
| Lineage and clone sets | Adult brain | Neuroblast lineage clones from the Ito, Yu and Lee collections | [Ito2013](http://virtualflybrain.org/reports/Ito2013), [Yu2013](http://virtualflybrain.org/reports/Yu2013), [Lee_Lineage2020](http://virtualflybrain.org/reports/Lee_Lineage2020) | Per dataset page |
| BrainTrap | Adult brain | Protein-trap expression patterns | [Knowles_Barley2010](http://virtualflybrain.org/reports/Knowles_Barley2010) | Per dataset page |

Where the Publication column says *per dataset page*, the citation is recorded on the
dataset's own page on VFB rather than repeated here, so that it stays correct if the
record is updated. Cite the original study, not VFB, when you use the images.

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
