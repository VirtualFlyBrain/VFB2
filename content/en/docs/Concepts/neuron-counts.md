---
title: "How many neurons are in the fly brain?"
weight: 310
linkTitle: "Neuron counts"
categories: ["overview","help"]
tag: ["Connectome", "Neuron", "Counts", "FlyWire", "Hemibrain", "MANC", "BANC", "Optic lobe", "Larva"]
description: >
  Why there is no single neuron count for Drosophila, what each connectome
  actually counted, and how to quote a figure defensibly.
---

*Every figure on this page was checked against its primary paper. Where a figure could
not be verified from the original, it is marked.*

## The short answer

There isn't one number, and the reason is not evasion. Three things have to be pinned down before the
question has an answer at all:

**Which nervous system.** "Fly brain" can mean the cephalic brain alone, the brain plus the ventral
nerve cord (the whole central nervous system), or a subset such as the central brain without the optic
lobes. Published figures use all of these boundaries and rarely say which in the headline.

**Which animal.** Every modern count comes from a connectome, and a connectome is one individual —
one sex, one developmental stage, one specimen, at one moment in its life. None is a species average.

**Counted how.** What a dataset calls a neuron is a decision recorded in its methods: whether
boundary-truncated fragments count, whether unproofread segments count, whether glia are separated,
and where proofreading was stopped. These decisions move the total by tens of thousands.

If you need one number to quote and you must have one, the best-supported single figure for a whole
adult brain is **139,255 neurons** (Dorkenwald et al. 2024) — an adult female, both optic lobes
included, ventral nerve cord excluded. Everything below is why that sentence needs all of its
qualifiers.

---

## 1. The connectome answers

These are the datasets Virtual Fly Brain holds. Each row is one animal.

| Dataset | Neurons | Scope | Specimen | Primary source |
|---|---|---|---|---|
| **FlyWire** (FAFB) | **139,255** | Whole brain, both optic lobes included. VNC excluded | Adult **female**, ssTEM | Dorkenwald et al. 2024, *Nature* 634:124–138 · PMID 39358518 · doi:10.1038/s41586-024-07558-y |
| **Male CNS** v0.9 | **166,691** | **Whole CNS** — central brain + optic lobes + VNC, intact neck connective | Adult **male**, eFIB-SEM | Berg et al. 2025, bioRxiv · doi:10.1101/2025.10.09.680999 · **preprint** |
| **BANC** v626 | **155,916** | Brain + VNC in one animal. **Lamina and ocellar ganglion absent** (~9,390 lamina neurons missing) | Adult **female**, ssTEM (GridTape) | Bates et al. 2026, *Nature* · PMID 42259917 · doi:10.1038/s41586-026-10735-w |
| **Optic lobe** v1.0.1 | **~53,000** (732 cell types) | **Right optic lobe only.** Lamina incomplete; central brain not proofread | Adult **male**, FIB-SEM | Nern et al. 2025, *Nature* 641:1225–1237 · PMID 40140576 |
| **MANC** v1.2.1 | **~23,000** ("roughly 23 thousand") | **Ventral nerve cord only**, plus the neck connective | 5-day **male**, FIB-SEM | Takemura et al. 2024, *eLife* 13:RP97769 · **reviewed preprint, no version of record, no PMID** |
| **Hemibrain** v1.2.1 | **~25,000** | **A portion of the central brain** — see §2 | 5-day **female** Canton S, FIB-SEM | Scheffer et al. 2020, *eLife* 9:e57443 · PMID 32880371 |
| **L1 CNS** | **3,016** | **Larval brain only**, inside a whole-CNS EM volume | 6-hour-old **female** first instar | Winding et al. 2023, *Science* 379:eadd9330 |
| **FAFB** (CATMAID) | — | An EM *volume*, not a proofread census. FlyWire is the reconstruction of it | Adult female | Zheng et al. 2018, *Cell* 174:730 |

### Two of these rows are the same fly

The optic lobe connectome was traced from part of the male CNS volume, and the male CNS paper
describes itself as extending the right optic lobe connectome. **Nern et al.'s ~53,000 optic lobe
neurons are a subset of Berg et al.'s 166,691, not an addition to them.** That also explains why the
optic lobe specimen is male. Adding the two would double-count one animal's visual system.

### Aligned images are not neurons — the counts prove it

It is tempting to use VFB's own `DatasetImages` count as a quick neuron proxy, since in a connectome
dataset each reconstructed neuron has an image. It does not work, and the failure is not a constant
factor that could be corrected for:

| Dataset | VFB `DatasetImages` | Neurons per paper | Ratio |
|---|---|---|---|
| FlyWire | 208,210 | 139,255 | 1.50 |
| Hemibrain v1.2.1 | 69,578 | ~25,000 | 2.78 |
| Optic lobe v1.0.1 | 60,002 | ~53,000 | 1.13 |
| Male CNS v0.9 | 315,430 | 166,691 | 1.89 |
| **BANC v626** | **143,806** | **155,916** | **0.92** |

The ratio ranges from 0.92 to 2.78 — and BANC has *fewer* images than the paper reports neurons, so
the error does not even run in a consistent direction. Neurons are aligned to multiple template brains
(one neuron can appear as several images), while other neurons in a release may have no aligned image
at all. **An image count is a count of images.**

One practical note for anyone querying this: `get_term_info` reports `count: -1` for `DatasetImages`,
which is the unavailable sentinel and not zero. The real totals only come back from `run_query`.

### Three consequences

**Adding a brain count to a VNC count is not a CNS count.** FlyWire (139,255) is a female brain; MANC
(~23,000) is a male VNC. Summing them produces a number for an animal that does not exist. If you want
a whole-CNS figure from one animal, the male CNS dataset (166,691) and BANC (155,916) are the datasets
that provide it — and they disagree by about 11,000, in different sexes, with BANC missing its lamina.

**The larval figure is a different order of magnitude and a different structure.** 3,016 is the larval
*brain*; the ventral nerve cord of that animal was imaged but not reconstructed as part of that count.

**Two of the six adult figures are preprints.** The male CNS paper and MANC have no peer-reviewed
version of record. That does not make them wrong; it does mean a submitted manuscript should say so.

---

## 2. The hemibrain is not a brain

This is the most commonly misused number in the field, and the misuse is understandable: "~25,000
neurons in the fly brain" is a memorable sentence and the hemibrain paper is the most-cited source of
it. But the hemibrain is roughly half a cephalic brain — slightly over half, and irregularly so.

Scheffer et al. describe the volume as a portion of the central brain: most of the right hemisphere,
excluding the optic lobe, the periesophageal neuropils and the gnathal ganglia, plus part of the left
hemisphere. They quantify it — about 36% of all synaptic neuropil by volume, and 54% of the central
brain neuropils. The lamina is not in the volume at all. Many regions appear only fractionally, which
is why the paper reports a per-region inclusion percentage rather than a simple region list.

So ~25,000 is the count of reconstructed bodies in a bit over half of one hemisphere's central brain,
in a volume with no optic lobe and no ventral nerve cord, with an arbitrary cut through the left side.
It is not half of 139,255, and it should never be scaled up to estimate a whole brain.

The paper is also explicit that its own inclusion criterion is soft. Neurons are classed as traced,
uncropped or cropped depending on how much of the cell is inside the volume, the authors note the
cropped definition is somewhat subjective, and they record that some small fragments are known to be
distinct neurons. "≈25K" is the authors' own simplification, and they say so.

---

## 3. What the connectomes do not tell you

### Dense and sparse reconstruction

The distinction matters for what a count means, and the clearest definition in the fly literature is
in the hemibrain paper: earlier work was either *dense* in small volumes or *sparse* in large ones. A
dense reconstruction attempts every object in the volume; a sparse one traces selected neurons of
interest through it.

Worth noting for anyone comparing datasets: Scheffer et al. classify Zheng et al. 2018 — the FAFB
volume — as sparse. FlyWire is the dense proofreading of that volume, carried out later. Hemibrain,
MANC and the larval L1 brain describe their own reconstructions as dense. FlyWire's papers do not use
the dense/sparse vocabulary about themselves at all, so attributing a "dense reconstruction"
self-description to Dorkenwald et al. would be putting words in their mouths.

### Flood-filling and automated segmentation still miss things

The Janelia datasets use flood-filling networks; FlyWire uses a different automated segmentation
followed by proofreading. Both leave residue, and the papers quantify it.

Hemibrain reports its automated segmentation performance before human proofreading: the base
segmentation achieved an expected run length of 163 µm at a 0.25% false-merge rate, and aggressive
agglomeration raised run length to 585 µm at a **27.6% false-merge rate**. That figure is
pre-proofreading — quoting it as a residual error rate would be wrong — but it shows the scale of what
human proofreading is there to repair.

The stopping point is explicitly resource-bounded. Scheffer et al. record that proofreading every
small segment was prohibitive, that they aimed for a basic level of completeness with extra effort in
regions of biological interest, and that the final pass was done to reach the highest completeness
achievable *in the time allotted*.

The most telling numbers are the synapse attachment rates. In FlyWire's published whole brain, about
93.7% of presynapses are attached to a neuron — but only about **44.7% of postsynapses**, because
postsynapses sit predominantly on fine twigs that received less proofreading. In the larval brain,
reconstructed manually rather than automatically, more than 99% of neurons were traced to completion
but only 75% of annotated synaptic sites could be linked to a neuron, the remainder being mostly small
dendritic fragments.

Two very different methods, the same failure mode: thin distal neurites are where completeness goes.

### Counts move between versions — sometimes by a lot

This is the single most useful thing to know when quoting any connectome figure.

- **FlyWire's own count changed by more than 11,000 between preprint and publication** — 127,978 in the
  bioRxiv version, 139,255 in *Nature*. Same authors, same dataset, more proofreading. (The preprint
  notes a public release missing roughly 8,000 retinula cells.)
- **Shiu et al.'s model, built on FlyWire materialisation v630, used 127,400 neurons** — the same brain,
  a different materialisation, ~12,000 fewer neurons.
- **BANC's preprint reports 142,719 proofread neurons at v821; the *Nature* version reports 155,916**
  proofread plus roughly-proofread. The paper's analyses are performed on v626 — the version VFB holds
  — but no neuron total is ever published for v626 specifically.
- **The optic lobe cell-type count went from 727 to 732** between preprint (v1.0) and version of record
  (v1.1). VFB holds v1.0.1, which neither citation documents.
- **MANC's companion papers disagree with each other** by a handful of neurons per class, and Marin et
  al. warn that annotations changed substantially between v1.0 and v1.2.1.

A neuron count from a connectome is a property of a *release*, not of a fly.

### One animal, and what stereotypy does and does not buy you

Both major groups address this directly, and neither is complacent.

Scheffer et al. argue the single-animal design is a feature as well as a limit — circuitry depends on
nutritional history, age and circadian phase, and a single animal holds those constant — while
acknowledging that establishing stereotypy will eventually require more connectomes.

Dorkenwald et al. argue that variability between individuals and reconstruction noise are both modest
enough that a single wiring diagram is useful for wild-type flies generally, while flagging known
sex differences and high variability in mushroom body principal neurons.

The FlyWire companion paper (Schlegel et al. 2024) tests this quantitatively, and the result is
sobering. Comparing FlyWire and hemibrain hemispheres, over half the connectome graph's edges are not
reproducible between brains; the edges that survive a strong-connection criterion are 7–16% of edges
but 50–70% of synapses. Cell *numbers* per type are much more stable — a mean difference of 0.3 cells
within a brain and 0.7 across brains — with a striking exception: Kenyon cells are about 30% more
numerous per hemisphere in FlyWire than in hemibrain. Their recommendation is three or more hemispheres
before defining a cell type.

For counting purposes the encouraging finding is that cell numbers are among the *more* stereotyped
properties. The caution is that the exception is a well-studied, functionally central cell class.

---

## 4. What people said before connectomics

### "About 100,000 neurons" — a convention, not a measurement

The figure is not attached to a primary measurement in the papers that popularised it. It appears
without citation in work from the FlyCircuit group (Lee et al. 2012, *PLoS Comput Biol* 8:e1002658),
in the FAFB paper's abstract (Zheng et al. 2018), and in the hemibrain paper's lay summary. Where a
modern paper does attach citations to a range, they resolve to reviews or to measurements that give different numbers: Jiao et al. 2022 cite a 100,000–199,000 range to five
sources, of which only one is an actual measurement — and it reports 199,000.

~100,000 is an order-of-magnitude convention that became canonical by repetition. It is not wrong so
much as unsourced.

### The three non-connectome measurements disagree by 2.5×

| Figure | Method | Source |
|---|---|---|
| **88,290 ± 13,810 nuclei** (n = 13 brains) | Isotropic fractionator, DAPI-stained nuclei | Godfrey et al. 2021, *Proc R Soc B* 288:20210199, table S1 |
| 133,000 ± 3,000 nuclei, of which ≥87% neurons | CNN nuclear segmentation of the FAFB volume | Mu et al. 2021, bioRxiv 2021.11.04.467197 — **still a preprint** |
| 217,000 ± 4,000 cells; **199,380 ± 3,400 neurons** | Isotropic fractionator with elav/repo immunostaining | Raji & Potter 2021, *PLoS ONE* 16:e0250381 |

Godfrey et al. is a survey of 32 Hymenoptera species in which *Drosophila* is the dipteran control
for the method; a single sectioned-brain count of the same material came out about 5% higher. Two
studies using nominally the same technique — isotropic fractionation — differ by a factor of about
2.5 on total brain cells (88,290 against 217,000). Compare cells with cells: Godfrey et al. count
all nuclei and do not separate neurons from glia. Mu et al. observe that their own count lands
within 3% of the geometric mean of the two.

Raji & Potter's figure is brain only (optic lobes plus central brain, VNC excluded), which matters
because it is frequently misquoted as a CNS number. They also report the glia fraction directly:
neurons are 91.8% of brain cells, with roughly 18,000 non-neuronal cells.

Note what this means against the connectome answer: **199,380 (isotropic fractionator, brain) versus
139,255 (FlyWire, brain)** — a 43% discrepancy between the two best-documented adult brain figures,
using entirely different methods on different animals. Neither is obviously wrong. This is an open
question, not a settled one.

### Glia are not a rounding error

The conventional "glia ≈ 10% of neurons" holds up for the adult brain (Raji & Potter: 8.2% of cells).
It does not hold in the larva: Jiao et al. 2022 (*eLife* 11:e74968), counting nuclei in intact
third-instar CNS by light-sheet microscopy, report glia at about 37% of neuron number — roughly four
times the received figure — alongside 10,312 neurons in the female third-instar CNS and 9,396 in the
male, a sexual dimorphism in cell number at the larval stage.

---

## 5. How to answer the question properly

If someone asks how many neurons are in the fly brain, a good answer does four things.

1. **Names the scope.** Brain or CNS; adult or larva; with or without optic lobes.
2. **Names the animal.** One specimen, its sex, its stage.
3. **Names the release.** A connectome count belongs to a version, not to a species.
4. **Points at the methods.** The inclusion rules are in the paper, and they are where the number
   actually comes from.

And it keeps two kinds of number strictly apart:

- **A biological count** from a connectome or a cell-counting study — a property of one animal,
  measured a particular way.
- **A Virtual Fly Brain annotation count** — for example, 15,214 neuron *types* with some part in the
  adult central nervous system. This is a curated count over an ontology spanning many datasets, sexes
  and stages. It is not a census of cells in any animal, and it must never be added to or compared with
  the figures above.

---

## Sources

**Connectomes**

- Dorkenwald S et al. (2024) Neuronal wiring diagram of an adult brain. *Nature* 634(8032):124–138. PMID 39358518. doi:10.1038/s41586-024-07558-y
- Schlegel P et al. (2024) Whole-brain annotation and multi-connectome cell typing of *Drosophila*. *Nature*. doi:10.1038/s41586-024-07686-5
- Scheffer LK et al. (2020) A connectome and analysis of the adult *Drosophila* central brain. *eLife* 9:e57443. PMID 32880371. doi:10.7554/eLife.57443
- Nern A et al. (2025) Connectome-driven neural inventory of a complete visual system. *Nature* 641(8065):1225–1237. PMID 40140576. doi:10.1038/s41586-025-08746-0
- Takemura S et al. (2024) A connectome of the male *Drosophila* ventral nerve cord. *eLife* 13:RP97769. doi:10.7554/eLife.97769.1 — reviewed preprint
- Marin EC et al. (2024) Systematic annotation of a complete adult male *Drosophila* nerve cord connectome. *eLife* 13:RP97766. doi:10.7554/eLife.97766.1 — reviewed preprint
- Berg S et al. (2025) Sexual dimorphism in the complete connectome of the *Drosophila* male central nervous system. bioRxiv. doi:10.1101/2025.10.09.680999 — preprint
- Bates AS et al. (2026) Distributed control circuits across a brain-and-cord connectome. *Nature*. PMID 42259917. doi:10.1038/s41586-026-10735-w
- Winding M et al. (2023) The connectome of an insect brain. *Science* 379(6636):eadd9330
- Zheng Z et al. (2018) A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*. *Cell* 174(3):730–743

**Cell counting, non-connectome**

- Raji JI, Potter CJ (2021) The number of neurons in *Drosophila* and mosquito brains. *PLoS ONE* 16(5):e0250381. doi:10.1371/journal.pone.0250381
- Mu S et al. (2021) 3D reconstruction of cell nuclei in a full *Drosophila* brain. bioRxiv 2021.11.04.467197 — preprint
- Godfrey RK, Swartzlander M, Gronenberg W (2021) Allometric analysis of brain cell number in Hymenoptera suggests ant brains diverge from general trends. *Proc R Soc B* 288(1947):20210199. PMID 33757353. doi:10.1098/rspb.2021.0199
- Jiao W et al. (2022) Intact *Drosophila* central nervous system cellular quantitation reveals sexual dimorphism. *eLife* 11:e74968
- Kremer MC et al. (2017) The glia of the adult *Drosophila* nervous system. *Glia* 65(4):606–638. PMID 28133822

**A miscitation worth knowing about**

- Shiu PK et al. (2024) A *Drosophila* computational brain model reveals sensorimotor processing. *Nature*. PMID 39358519. — Describes ">125,000 neurons" as a *central brain* connectome. The number is FlyWire's **whole-brain** count (the paper's own model uses 127,400 neurons from FlyWire v630), and FlyWire reports only 32,388 neurons fully contained in the central brain. The scope label is wrong at source. Cite Dorkenwald et al. directly instead.
