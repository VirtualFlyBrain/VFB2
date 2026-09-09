---
title: "VFB_connect"
linkTitle: "VFB_connect"
weight: 651
description: >
  VFB's own Python client — query VFB's terms, images, connectivity and cross-references
  from code.
---

`VFB_connect` is the Python client for the databases behind Virtual Fly Brain. A single object
wraps connections and canned queries across all of VFB's open databases, so you can look up
anatomy terms, resolve IDs between VFB and external resources such as CATMAID and neuPrint,
retrieve connectivity, and download images without writing queries against each service
yourself.

If you are working with VFB data from Python, start here: most of the other tools on these
pages consume data that `VFB_connect` can hand them.

## Install

```sh
pip install vfb_connect
```

## Quick start

```python
from vfb_connect import vfb

# Metadata for a class -- here, Kenyon cell
vfb.term('FBbt_00003686')

# Everything VFB knows in a named region
vfb.get_terms_by_region('fan-shaped body')
```

Terms are addressed by their identifiers in CURIE form — `FBbt_00003686` above is a
[Drosophila Anatomy Ontology](https://www.ebi.ac.uk/ols4/ontologies/fbbt) class, and VFB's own
individuals use `VFB_` identifiers. Any report page on the website shows the identifier for
what you are looking at, so the website is a convenient way to find the term you want before
querying it from code.

## Where next

The [VFB connect API overview](/docs/tutorials/apis/vfb_api_overview/) tutorial covers the
query surface in depth — term info, mapping between VFB and external IDs, connectivity and
similarity queries. For the endpoints underneath it, see [VFB APIs](/docs/apis/).

Full documentation: [vfb_connect.readthedocs.io](https://vfb_connect.readthedocs.io/en/stable/).
Source: [VirtualFlyBrain/VFB_connect](https://github.com/VirtualFlyBrain/VFB_connect).
