---
title: L1EM CATMAID Data Viewer
description: "This CATMAID (Collaborative Annotation Toolkit for Massive Amounts of Image Data) instance hosts neuroanatomical data from the Drosophila first instar larva (L1) electron microscopy dataset, featuring manually traced neurons from numerous research publications."
---

![Drosopila Larval CNS 70% traced back in 2017](https://www.virtualflybrain.org/images/l1em_70percent.jpeg)

## Access

The L1EM CATMAID instance is hosted and maintained by Virtual Fly Brain (VFB) as part of their mission to integrate and preserve key Drosophila neuroscience datasets. The instance is accessible at:
[https://l1em.catmaid.virtualflybrain.org/](https://l1em.catmaid.virtualflybrain.org/?pid=1&zp=108250&yp=82961.59999999999&xp=54210.799999999996&tool=tracingtool&sid0=1&s0=2.4999999999999996&help=true&layout=h(XY,%20%7B%20type:%20%22neuron-search%22,%20id:%20%22neuron-search-1%22,%20options:%20%7B%22annotation-name%22:%20%22papers%22%7D%7D,%200.6))

This resource provides access to the L1EM dataset and its associated neural reconstructions. Virtual Fly Brain ensures its long-term availability to the research community.

## Source Publication

### Primary Resource
- L1EM Dataset: Winding M, et al. (2023) The connectome of an insect brain. Science, 379(6636):eadd9330. https://doi.org/10.1126/science.add9330

### Contributing Publications
The database includes neurons traced and published in numerous studies. Each neuron is annotated with its source publication. Major contributing publications include:

- Andrade et al. (2019)
- Barnes et al. (2022)
- Berck, Khandelwal et al. (2016)
- Burgos et al. (2018)
- Carreira-Rosario, Arzan Zarin, Clark et al. (2018)
- Eichler, Li, Litwin-Kumar et al. (2017)
- Eschbach, Fushiki et al. (2020, 2020b)
- Fushiki et al. (2016)
- Gerhard et al. (2017)
- Heckscher et al. (2015)
- Hueckesfeld et al. (2020)
- Imambocus et al.
- Jovanic et al. (2019)
- Jovanic, Schneider-Mizell et al. (2016)
- Larderet, Fritsch et al. (2017)
- Mark et al. (2019)
- Miroschnikow et al. (2018)
- Ohyama, Schneider-Mizell et al. (2015)
- Schlegel et al. (2016)
- Takagi et al. (2017)
- Tastekin et al. (2018)
- Valdes-Aleman et al. (2021)
- Winding, Pedigo et al. (2023)
- Zarin, Mark et al. (2019)
- Zwart et al. (2016)

Full references for specific neurons can be found on Virtual Fly Brain by searching for their skeleton ID (skid).

## Dataset Contents

The viewer provides access to:
- Complete electron microscopy volume of a Drosophila first instar larva brain
- Manually traced neuron reconstructions from multiple research groups
- Synaptic connectivity information
- Associated metadata and annotations

## Features

This CATMAID instance enables:
- Browser-based visualization of the serial section electron microscopy data
- Navigation through image stacks
- Viewing of neuron reconstructions
- Analysis of synaptic connectivity
- Data export functionality

### Available Tools
- Tracing tool for examining reconstructions
- Neuron search interface with paper-based filtering
- Connectivity analysis tools
- Skeleton visualization options
- API access for programmatic data retrieval (documentation: https://catmaid.readthedocs.io/en/stable/api.html): https://l1em.catmaid.virtualflybrain.org/apis/

### Recommended: VFB pass-through API

For most uses, the fastest and simplest way to pull data out of this instance is VFB's
CATMAID pass-through, `v3-cached.virtualflybrain.org` — it takes VFB ids as well as native
skeleton ids (skids), needs no token or CSRF cookie, and is documented interactively at
[v3-cached.virtualflybrain.org](https://v3-cached.virtualflybrain.org/):

```bash
curl "https://v3-cached.virtualflybrain.org/catmaid/l1em/annotations_for_skeletons?ids=16"
```

See the [CATMAID API](/docs/apis/catmaid/) page for the full command list, VFB-id/skid
resolution, and response format. The direct, native CATMAID API below remains available for
anything the pass-through's command list doesn't cover.

### Public API token

Read-only access to this instance is open to everyone, but most of CATMAID's query
endpoints are POST rather than GET, and POST requests are subject to a CSRF check.
Command-line and server-side clients (pymaid, curl, scripts) can satisfy that check by
requesting a page first and replaying the cookie they are given. Code running in a
browser cannot: it can neither read a cookie belonging to another site nor set a
`Referer` header. Browser-based tools should therefore authenticate as the anonymous
user, using this token:

```
4c1c9c60d4864c41ebc79f42ba99014a9e912f49
```

**This token is published deliberately and is not a secret.** It authenticates as
`AnonymousUser`, whose only permission on this project is `can_browse`, so it grants
exactly the read access this page already offers to everyone and nothing further.
Write requests made with it are refused by the server.

Send it in either the `X-Authorization` or the `Authorization` header:

```bash
curl -X POST https://l1em.catmaid.virtualflybrain.org/1/skeleton/neuronnames \
  -H "X-Authorization: Token 4c1c9c60d4864c41ebc79f42ba99014a9e912f49" \
  --data "skids[0]=16"
```


## Citation Guidelines

When using this data, please cite:

1. The L1EM dataset:
   Winding M, et al. (2023) The connectome of an insect brain. Science, 379(6636):eadd9330. https://doi.org/10.1126/science.add9330

2. The CATMAID platform:
   Saalfeld S, Cardona A, Hartenstein V, Tomančák P (2009) CATMAID: collaborative annotation toolkit for massive amounts of image data. Bioinformatics 25(15): 1984-1986. https://doi.org/10.1093/bioinformatics/btp266

3. The specific publication(s) associated with any neurons you analyze or reference (see Contributing Publications section)

## Maintenance & Support

This resource is archived, hosted, and maintained by Virtual Fly Brain (VFB - https://virtualflybrain.org) as part of their commitment to preserving and making accessible critical Drosophila neuroscience data resources.
