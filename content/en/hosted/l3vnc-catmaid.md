---
title: L3VNC CATMAID Data Viewer
description: "This CATMAID (Collaborative Annotation Toolkit for Massive Amounts of Image Data) instance hosts neuroanatomical data from the Drosophila third instar larva ventral nerve cord (L3 VNC) electron microscopy dataset."
---

## Access

The L3VNC CATMAID instance is hosted and maintained by Virtual Fly Brain (VFB) as part of their mission to integrate and preserve key Drosophila neuroscience datasets. The instance is accessible at:
[https://l3vnc.catmaid.virtualflybrain.org/](https://l3vnc.catmaid.virtualflybrain.org/?pid=2&zp=0&yp=53578.49999999999&xp=71242.5&tool=tracingtool&sid0=2&s0=6&help=true&layout=h(XY,%20%7B%20type:%20%22neuron-search%22,%20id:%20%22neuron-search-1%22,%20options:%20%7B%22annotation-name%22:%20%22papers%22%7D%7D,%200.6))

This resource provides access to the L3 VNC dataset and its associated neural reconstructions. Virtual Fly Brain ensures its long-term availability to the research community.

## Source Publication

### Contributing Publications
- Gerhard S, Andrade I, Fetter RD, Cardona A, Schneider-Mizell CM (2017) Conserved neural circuit structure across Drosophila larval development revealed by comparative connectomics. eLife, 6:e29089. https://doi.org/10.7554/eLife.29089

## Dataset Contents

The viewer provides access to:
- Serial section electron microscopy volume of a Drosophila third instar larva ventral nerve cord
- Manually traced neuron reconstructions
- Synaptic connectivity information
- Associated metadata and annotations

### Image stack

Scale levels 0 and 1 of the image stack are incomplete, missing roughly 72% and 30% of
slices respectively. This is a property of the source export rather than a fault in the
viewer. Because the original imaging is at very high resolution, browsing and
reconstruction at scale level 2 (or an upscaling of it) is unaffected, and scale level 2
is the recommended working resolution for this volume.

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
- API access for programmatic data retrieval (documentation: https://catmaid.readthedocs.io/en/stable/api.html): https://l3vnc.catmaid.virtualflybrain.org/apis/

### Public API token

Read-only access to this instance is open to everyone, but most of CATMAID's query
endpoints are POST rather than GET, and POST requests are subject to a CSRF check.
Command-line and server-side clients (pymaid, curl, scripts) can satisfy that check by
requesting a page first and replaying the cookie they are given. Code running in a
browser cannot: it can neither read a cookie belonging to another site nor set a
`Referer` header. Browser-based tools should therefore authenticate as the anonymous
user, using this token:

```
ce6984c9d4d00a40d3173a9aad3924afe6612c43
```

**This token is published deliberately and is not a secret.** It authenticates as
`AnonymousUser`, whose only permission on this project is `can_browse`, so it grants
exactly the read access this page already offers to everyone and nothing further.
Write requests made with it are refused by the server.

Send it in either the `X-Authorization` or the `Authorization` header:

```bash
curl -X POST https://l3vnc.catmaid.virtualflybrain.org/2/skeleton/neuronnames \
  -H "X-Authorization: Token ce6984c9d4d00a40d3173a9aad3924afe6612c43" \
  --data "skids[0]=16"
```


## Citation Guidelines

When using this data, please cite:

1. The L3VNC dataset:
   Gerhard S, Andrade I, Fetter RD, Cardona A, Schneider-Mizell CM (2017) Conserved neural circuit structure across Drosophila larval development revealed by comparative connectomics. eLife, 6:e29089. https://doi.org/10.7554/eLife.29089

2. The CATMAID platform:
   Saalfeld S, Cardona A, Hartenstein V, Tomancak P (2009) CATMAID: collaborative annotation toolkit for massive amounts of image data. Bioinformatics 25(15): 1984-1986. https://doi.org/10.1093/bioinformatics/btp266

3. The specific publication(s) associated with any neurons you analyze or reference

## Maintenance & Support

This resource is archived, hosted, and maintained by Virtual Fly Brain (VFB - https://virtualflybrain.org) as part of their commitment to preserving and making accessible critical Drosophila neuroscience data resources.
