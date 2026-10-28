---
title: "Download the fly brain: bulk connectome data"
linkTitle: "Download connectomes"
weight: 45
description: >
  Where to download the whole fruit fly brain (and nerve cord) as data: the official sources, formats and bulk-download method for every Drosophila connectome VFB serves.
---

People find this site by searching for "fly brain download", "download fruit fly brain", "fruit fly brain scan download", "fruit fly brain map download" or "where can I download the fly brain". This page answers those questions directly.

## What you can and cannot download

There is no single file called "the fly brain". A connectome is a set of tables and volumes: which neurons exist, where their synapses are, which neuron connects to which, plus the electron microscopy (EM) images and 3D shapes (meshes and skeletons) they came from. Each connectome is published by the group that built it. Virtual Fly Brain (VFB) indexes and links them, but does not host the bulk files, so the links below go to the official sources.

You can download the **wiring diagram** of a fly brain: the "fruit fly brain map", "fly neuron map" or "mapped fly brain" in the sense of every neuron and synapse. You can also download the raw **scan**, meaning the EM volume, though the volumes run to many terabytes and are read in pieces rather than downloaded whole.

You cannot download a living "digital fly", a recording of a fly's thoughts, or anything that carries "fly consciousness" or a "fly mind" into a computer. The connectome is a structural map of one animal's wiring. It does not contain activity, and models built on it make assumptions the wiring alone cannot settle (see [Connectome simulation](/docs/tools/connectome-simulation/)). If you came looking to "simulate the fly brain", the [simulation section](#simulate-the-fly-brain-after-downloading-it) below shows how to run a ready-made model.

## Which fly brain do you want?

| You want | Dataset | Best official download |
|---|---|---|
| The whole adult fly brain ("full fly brain", "FAFB", "flygm" style whole-brain models) | FlyWire FAFB v783 | [Zenodo 10676866](https://zenodo.org/records/10676866) |
| The whole adult brain from a second animal, male | Male CNS v1.0 (brain and nerve cord) | [male-cns.janelia.org/download](https://male-cns.janelia.org/download/) |
| Brain and nerve cord together, female | BANC v888 | [Harvard Dataverse](https://doi.org/10.7910/DVN/7WTH1N) |
| Central brain, classic dataset | Hemibrain v1.2.1 | [Hemibrain release page](https://dvid.io/blog/release-v1.2) |
| Nerve cord ("ventral nerve cord", VNC), male | MANC v1.2.1 | [Janelia MANC page](https://www.janelia.org/manc-connectome) |
| Optic lobe (the fly's visual system), male | Male optic lobe v1.1 | [Janelia optic lobe page](https://www.janelia.org/project-team/flyem/optic-lobe) |
| Nerve cord, female | FANC | [FANC_auto_recon wiki](https://github.com/htem/FANC_auto_recon/wiki/) |
| Larval fly brain | L1EM (first-instar larva) | [L1EM CATMAID](https://l1em.catmaid.virtualflybrain.org/) |

In the table, "male CNS" is the Janelia and Google "flylab malecns" connectome, which covers the whole central nervous system of one male fly (about 166,700 neurons). FlyWire's Codex portal lists it as MCNS.

## Whole adult fly brain, female: FlyWire FAFB

The FlyWire consortium's whole-brain connectome (version 783, 139,255 neurons, about 3.7 million proofread connections) is the dataset most people mean by "the fruit fly brain connectome".

**Fastest bulk route: Zenodo.** The static v783 release is about 10.6 GB, licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), DOI [10.5281/zenodo.10676866](https://doi.org/10.5281/zenodo.10676866). It contains:

| File | Size | Contents |
|---|---|---|
| `proofread_connections_783.feather` | 852 MB | Neuron-to-neuron connections with synapse counts and neurotransmitter probabilities |
| `proofread_root_ids_783.npy` | 1.1 MB | IDs of all proofread neurons |
| `per_neuron_neuropil_count_pre_783.feather` | 16.9 MB | Presynapse counts per neuron and neuropil |
| `per_neuron_neuropil_count_post_783.feather` | 233.8 MB | Postsynapse counts per neuron and neuropil |
| `flywire_synapses_783.feather` | 9.5 GB | About 130 million synapses, with positions |

```bash
# connections and neuron IDs only (about 0.85 GB)
wget -O proofread_connections_783.feather 'https://zenodo.org/records/10676866/files/proofread_connections_783.feather?download=1'
wget -O proofread_root_ids_783.npy 'https://zenodo.org/records/10676866/files/proofread_root_ids_783.npy?download=1'
```

```python
import pandas as pd
conn = pd.read_feather("proofread_connections_783.feather")
```

**Live data: Codex.** [FlyWire Codex](https://codex.flywire.ai/) offers a [download portal](https://codex.flywire.ai/api/download) for FAFB and BANC. It needs a Google sign-in and an API token from your Codex account page. Codex files track the current data and can differ from the Zenodo snapshot, and Codex states that it provides no general live-query API for bulk access, so use the files rather than scraping pages. See the [Codex FAQ](https://codex.flywire.ai/faq) and its Colab notebook for the token workflow. Skeletons (SWC) are available from cell pages; full meshes come through the [MeshParty](https://github.com/CAVEconnectome/MeshParty) package.

**Images, segmentation and meshes.** The EM and segmentation volumes are read remotely with [fafbseg](https://fafbseg-py.readthedocs.io/en/dev/api.html) (Python) or [CloudVolume](https://navis-org.github.io/navis/generated/gallery/4_remote/tutorial_remote_01_cloudvolume), which fetch just the region you ask for.

## Whole central nervous system, male: male CNS v1.0

The [male CNS download page](https://male-cns.janelia.org/download/) (dataset `male-cns:v1.0`, released 8 June 2026, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); [release notes](https://male-cns.janelia.org/release/)) is the most complete official bulk offer. Everything sits in public Google Cloud Storage buckets.

| What | Where (`gs://`) | Size / format |
|---|---|---|
| Neuron-to-neuron weights | `flyem-male-cns/v1.0/connectome-data/flat-connectome/connectome-weights-male-cns-v1.0-minconf-0.5.feather` | 1.1 GB, Feather |
| Neuron annotations | `.../flat-connectome/body-annotations-male-cns-v1.0-minconf-0.5.feather` | 13 MB |
| Neurotransmitter predictions | `.../flat-connectome/body-neurotransmitters-male-cns-v1.0.feather` | 42 MB |
| Synapse locations | `.../flat-connectome/syn-points-male-cns-v1.0-minconf-0.5.feather` | 12.7 GB |
| Skeletons | `flyem-male-cns/v1.0/segmentation/skeletons-malecns/` | SWC and precomputed |
| Neo4j database | `flyem-male-cns/v1.0/database/neo4j` | built for Neo4j 4.4.16 |
| EM, segmentation, ROIs | `flyem_cns_z0720_07m_dvidcoords_n5`, `flyem-male-cns/v1.0/segmentation`, `flyem-male-cns/rois/` | N5 and precomputed volumes |

```bash
# the connection table, via the public HTTPS mirror
wget https://storage.googleapis.com/flyem-male-cns/v1.0/connectome-data/flat-connectome/connectome-weights-male-cns-v1.0-minconf-0.5.feather

# a whole folder, using the Google Cloud CLI
gsutil -m cp -r gs://flyem-male-cns/v1.0/connectome-data/flat-connectome/ ./male-cns-flat/
```

The page lists the paths but gives no `gsutil` commands; the commands above are the standard way to read those paths. The HTTPS mirror is stated for the flat-connectome folder only, so use `gsutil` for the rest. For queries instead of files, use [neuPrint](https://neuprint.janelia.org/) (free account) with `pip install neuprint-python` and `Client("https://neuprint.janelia.org", dataset="male-cns:v1.0", token=...)`.

## Whole brain and nerve cord, female: BANC

The Brain And Nerve Cord connectome (BANC v888, 158,262 neurons) has a citable static release on [Harvard Dataverse](https://doi.org/10.7910/DVN/7WTH1N) (CC BY 4.0). It holds per-neuron metadata, edge lists, per-synapse tables, neurotransmitter predictions, meshes, SWC skeletons and registration templates. The [BANC project repository](https://github.com/htem/BANC-project) lists each data product with its Dataverse and Google Cloud path in `manuscript/print/banc_data_locations.md`. The current, still-changing version is on [Codex](https://codex.flywire.ai/banc). Programmatic access uses [bancr](https://github.com/natverse/bancr) (R) or the `banc` Python package, which sit on top of CAVEclient.

## Hemibrain (central brain)

The [hemibrain v1.2 release](https://dvid.io/blog/release-v1.2) gives:

- A compact flat-file set (neuron table and connection tables, 44 MB): `exported-traced-adjacencies-v1.2.tar.gz` from the `hemibrain` bucket, linked on the release page.
- The neuPrint input CSVs (`hemibrain_v1.2_neo4j_inputs.zip`), which contain everything in the neuPrint database except 3D data and skeletons.
- Bulk image and segmentation data in `gs://neuroglancer-janelia-flyem-hemibrain` (raw EM, CLAHE EM and `v1.2/segmentation`). The page suggests `gsutil -m cp -r gs://bucket mydir`.

A full DVID replica is not a simple download; the release page asks you to contact the team. Query access is through neuPrint with the `hemibrain:v1.2.1` dataset.

## Nerve cord, optic lobe and larva

- **MANC (male nerve cord).** The [MANC page](https://www.janelia.org/manc-connectome) states that the complete connectome is available as flat files in the public bucket `flyem-manc-exports` ([browse it](https://console.cloud.google.com/storage/browser/flyem-manc-exports)). The page does not say which version the flat files hold; check the bucket's file names. Query it as `manc:v1.2.1` in neuPrint, or use the [malevnc](https://natverse.org/malevnc/) R package. CC BY 4.0.
- **Male optic lobe.** The [optic lobe page](https://www.janelia.org/project-team/flyem/optic-lobe) gives v1.1 (March 2025) as flat files in the public bucket `flyem-optic-lobe` ([browse it](https://console.cloud.google.com/storage/browser/flyem-optic-lobe)), with EM and segmentation as precomputed volumes readable by TensorStore or CloudVolume. CC BY 4.0.
- **FANC (female nerve cord).** Automated reconstructions are mostly in the bucket `gs://lee-lab_female-adult-nerve-cord`; the wiki does not say which files hold synapses or neuron tables and does not state a licence. Manual skeletons are in [CATMAID on VFB](https://catmaid.virtualflybrain.org/). Tools: [fanc-fly](https://pypi.org/project/fanc-fly) and the [FANC_auto_recon](https://github.com/htem/FANC_auto_recon) repository.
- **Larva (L1EM).** The first-instar larval brain from [Winding et al. 2023](https://doi.org/10.1126/science.add9330) is served by VFB's [L1EM CATMAID](https://l1em.catmaid.virtualflybrain.org/). Export neurons and connectivity through the [CATMAID API](https://catmaid.readthedocs.io/en/stable/api.html) at `https://l1em.catmaid.virtualflybrain.org/apis/` (for example with `pymaid`).

## Use VFB IDs as a stable reference for neurons

Every dataset above numbers its neurons in its own way: FlyWire root IDs, neuPrint body IDs, CATMAID skeleton IDs. Those numbers belong to one dataset and one version, and they can change when a dataset is proofread and re-released. The same neuron therefore has different identifiers in different places, and the same number can mean different things in different datasets.

Each neuron that VFB serves has a VFB ID (for example `VFB_jrcv0gef`). It is a persistent identifier that VFB does not reuse for another neuron. VFB records the source ID and the dataset version it came from as a cross-reference on that neuron's page, and links out to the source. For `VFB_jrcv0gef`, VFB shows it as MANC body 21255 in `manc:v1.2.1` and links to neuPrint. That gives you one fixed handle that you can cite, share in a paper, bookmark and put in a script, and always trace back to the exact source record.

When a dataset is re-released, VFB curators check the neurons by hand against the previous version. If the same neuron is still there, its VFB ID follows it and gains a cross-reference to the new version as well as the old. If a neuron has been split, absorbed into others, or removed because the earlier reconstruction was a mistake that proofreading has corrected, its VFB ID is deprecated rather than reassigned to a different cell. A deprecated ID is not deleted: it still resolves, and it stays linked to the last dataset version in which the neuron existed, with the source ID it had in that version. A VFB ID therefore never silently points at a different neuron: it keeps pointing at the same cell, or it is retired with its history intact. Deprecated neurons are left out of connectivity results. The full policy is on the [Dataset Versions and Deprecation](/docs/data/em/versioning/) page.

VFB also links neurons across connectomes by type. Each neuron is annotated with a cell type from the [Drosophila anatomy ontology](https://github.com/FlyBase/drosophila-anatomy-developmental-ontology) (FBbt), so you can ask for all neurons of a type across FlyWire, hemibrain, MANC and male CNS together. A VFB ID identifies one reconstructed neuron in one dataset, while the FBbt type is what ties equivalent neurons in different animals together. VFB does not claim two IDs are the same cell unless the source says so.

In practice:

- Cite the VFB ID, the source ID and the dataset version together, for example "VFB_jrcv0gef (MANC 21255, manc:v1.2.1)".
- Look a neuron up by VFB ID in [VFB_connect](/docs/tools/vfb-connect/) or the [VFB MCP server](https://github.com/VirtualFlyBrain/VFB3-MCP) to get its source ID, type, connectivity and images without knowing which dataset it came from.
- For one neuron's shape, each VFB term page offers downloads (NRRD image, OBJ mesh, SWC skeleton) registered to a standard template brain, so neurons from different connectomes sit in the same coordinate space.
- Use the bulk files above when you need every neuron or synapse, then map to VFB IDs afterwards to carry your results forward between versions. If a VFB ID you saved has been deprecated, the neuron was split, absorbed or corrected in a later release; its page still shows the last version it appeared in, so check the current records before reusing old results. See [Dataset Versions and Deprecation](/docs/data/em/versioning/).

## Get the data through VFB

If you want specific neurons or regions rather than whole files, VFB gives programmatic access to all of the above through one ontology: [VFB_connect](/docs/tools/vfb-connect/) (Python), the [VFB MCP server](https://github.com/VirtualFlyBrain/VFB3-MCP) for AI assistants, and the downloads on each term page ([Term Info](/docs/website-features/terminfo/#data)). Template brains and domain meshes are described in [Templates](/docs/data/templates/). VFB is a map to the data, so use the sources above when you need every synapse.

## Simulate the fly brain after downloading it

A connectome is not a simulator, but the following run on the files above:

- **Whole-brain simulation:** [Drosophila_brain_model](https://github.com/philshiu/Drosophila_brain_model) (Shiu et al. 2024, MIT licence) is a leaky integrate-and-fire model of the FlyWire connectome in Python with Brian 2. It runs in Colab with no install. The code is set to FlyWire version 630 and needs its config paths changed to use v783.
- **Embodied simulation:** [FlyGym / NeuroMechFly v2](https://pypi.org/project/flygym/2.0.1/) (`pip install flygym`, Apache-2.0) is a physics model of the fly body. It does not include a connectome-derived controller.

## Tips

- Check the licence. All sources above that state one use CC BY 4.0, and you must cite the paper and dataset version. FANC's wiki states none.
- State the version you used (for example "FlyWire v783" or "male-cns:v1.0"). Source neuron IDs and connections change between versions.
- Record the VFB ID alongside the source ID. Source IDs belong to one dataset version; the VFB ID is the reference to keep (see the next section).
- Budget disk: the flat connection tables are about 1 GB each, synapse tables 10 GB or more, and EM volumes are terabytes.

## Other ways people search for this

"Fly brain", "flybrain", "fly's brain", "flys brain", "fruitfly brain", "digital fly brain", "virtual fruit fly brain", "downloadable fly brain", "open source fly brain", "fly brain dataset", "fly brain data", "fly brain files", "fly brain zip", "fly brain python", "fly brain api", "fly brain github", "fly brain atlas", "fly brain 3D model", "drosophila brain map" and "drosophila brain atlas" all lead to the datasets above. The 3D "scan" or "scanned fly brain" is the EM volume; the "fly neural network" or "fly connectome" is the connection table. "Cerebro de mosca descargar" (Spanish), "мозг мухи скачать" (Russian), "Fruchtfliege Gehirn Download" (German), "cérebro de mosca mapeado download" (Portuguese) and "초파리 시뮬레이션" (Korean) mean the same thing.

To browse the fly brain in your web browser without downloading anything, use [Virtual Fly Brain](https://www.virtualflybrain.org/) itself.
