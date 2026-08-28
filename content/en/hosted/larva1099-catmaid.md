---
title: L1 CNS (Larva1099) eFIB-SEM CATMAID Data Viewer
description: "This CATMAID (Collaborative Annotation Toolkit for Massive Amounts of Image Data) instance hosts the enhanced focused-ion-beam SEM (eFIB-SEM) volume of a Drosophila first instar larva central nervous system (sample 1099), together with a curated set of identified, named neuron reconstructions."
---

![Cross-section of the Larva1099 eFIB-SEM volume of the first instar larval CNS](https://virtualflybrain.org/data/EM/drosophila/l1/Larva1099/Larva1099_preview.png)

## Access

The Larva1099 CATMAID instance is hosted and maintained by Virtual Fly Brain (VFB) as part of its mission to integrate and preserve key *Drosophila* neuroscience datasets. The instance is accessible at:
[https://larva1099.catmaid.virtualflybrain.org/](https://larva1099.catmaid.virtualflybrain.org/?pid=1&sid0=1&tool=tracingtool&s0=3)

This is a distinct volume from the L1EM serial-section TEM dataset also hosted by VFB: it is a separate first instar larva (sample 1099) imaged by enhanced focused-ion-beam scanning electron microscopy (eFIB-SEM) at 12 × 12 × 12 nm/voxel isotropic resolution.

## Source Publication

The volume and reconstructions are from:

- Randel N, Wang C, Clayton MS, Wang K, Pang S, Xu CS, Champion A, Hess HF, Cardona A, Keller PJ, Zlatic M (2026) *Combining brain-wide activity imaging with electron microscopy reveals a distributed nociceptive network in the brain.* bioRxiv 2025.09.25.678485. https://doi.org/10.1101/2025.09.25.678485 *(preprint, in revision)*

## Dataset Contents

The viewer provides access to:

- The complete eFIB-SEM image volume of a *Drosophila* first instar larva CNS (sample 1099), 12 × 12 × 12 nm/voxel, served as N5
- A curated set of identified, named neuron reconstructions exported from the source project for hosting on VFB
- The associated neuron and annotation metadata

The hosted set is the curated, named-neuron export rather than the complete connectome; each skeleton carries its neuron-name annotations.

## Features

This CATMAID instance enables:

- Browser-based visualisation of the eFIB-SEM image volume
- Navigation through the image stack
- Viewing of neuron reconstructions
- Neuron-name search
- API access for programmatic data retrieval (documentation: https://catmaid.readthedocs.io/en/stable/api.html): https://larva1099.catmaid.virtualflybrain.org/apis/

### Public API token

Read-only access to this instance is open to everyone, but most of CATMAID's query
endpoints are POST rather than GET, and POST requests are subject to a CSRF check.
Command-line and server-side clients (pymaid, curl, scripts) can satisfy that check by
requesting a page first and replaying the cookie they are given. Code running in a
browser cannot: it can neither read a cookie belonging to another site nor set a
`Referer` header. Browser-based tools should therefore authenticate as the anonymous
user, using this token:

```
b0cbcf16d84f2b820673471445e3d64d04797d06
```

**This token is published deliberately and is not a secret.** It authenticates as
`AnonymousUser`, whose only permission on this project is `can_browse`, so it grants
exactly the read access this page already offers to everyone and nothing further.
Write requests made with it are refused by the server.

Send it in either the `X-Authorization` or the `Authorization` header:

```bash
curl -X POST https://larva1099.catmaid.virtualflybrain.org/1/skeleton/neuronnames \
  -H "X-Authorization: Token b0cbcf16d84f2b820673471445e3d64d04797d06" \
  --data "skids[0]=16"
```


## Citation Guidelines

When using this data, please cite:

1. The source dataset:
   Randel N, et al. (2026) Combining brain-wide activity imaging with electron microscopy reveals a distributed nociceptive network in the brain. bioRxiv 2025.09.25.678485. https://doi.org/10.1101/2025.09.25.678485

2. The CATMAID platform:
   Saalfeld S, Cardona A, Hartenstein V, Tomančák P (2009) CATMAID: collaborative annotation toolkit for massive amounts of image data. Bioinformatics 25(15): 1984-1986. https://doi.org/10.1093/bioinformatics/btp266

## Maintenance & Support

This resource is archived, hosted, and maintained by Virtual Fly Brain (VFB - https://virtualflybrain.org) as part of its commitment to preserving and making accessible critical *Drosophila* neuroscience data resources.
