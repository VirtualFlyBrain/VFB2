---
title: "pymaid"
linkTitle: "pymaid"
weight: 655
description: >
  Python client for CATMAID, including the FAFB and other EM datasets VFB hosts.
---

`pymaid` talks to CATMAID servers and returns neurons as `navis` objects, so skeletons you pull
from CATMAID drop straight into the rest of the Python toolchain. VFB hosts the public CATMAID
instances for several connectomics datasets — see [what is
available](https://catmaid.virtualflybrain.org/) — and those are open for read-only access
without a token.

## Install

```sh
pip3 install python-catmaid
```

Note the package name. There is an unrelated `pymaid` package on PyPI; installing that one will
not give you this library.

## Quick start

VFB's CATMAID servers are public, so connecting needs no API token:

```python
import pymaid
import navis

# Connect to the VFB CATMAID server hosting the FAFB data
rm = pymaid.connect_catmaid(server="https://fafb.catmaid.virtualflybrain.org/",
                            api_token=None, max_threads=10)

print(f'Server is running CATMAID version {rm.catmaid_version}')
```

With a connection established, `pymaid.get_neuron(16)` fetches a skeleton by its ID, returning
a `CatmaidNeuron` that `navis` can plot, prune and compare like any other neuron.

Skeleton IDs are local to each CATMAID instance and are not unique between them, which is why
VFB gives every image its own persistent identifier. [VFB_connect](/docs/tools/vfb-connect/)
can map between the two.

## Where next

The [pymaid tutorial](/docs/tutorials/apis/pymaid/) works through retrieving neurons, filtering
them by name and lineage, and plotting the results.

Full documentation: [pymaid.readthedocs.io](https://pymaid.readthedocs.io/).
Source: [navis-org/pymaid](https://github.com/navis-org/pymaid).
CATMAID itself: [catmaid.readthedocs.io](https://catmaid.readthedocs.io/en/stable/).
