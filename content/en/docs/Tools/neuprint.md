---
title: "neuPrint clients"
linkTitle: "neuPrint clients"
weight: 656
description: >
  neuprint-python and neuprintr — query the hemibrain, MANC and other connectomes hosted
  at neuPrint.
---

[neuPrint](https://neuprint.janelia.org) is Janelia's connectome database, hosting the
hemibrain, MANC, optic-lobe and male-CNS datasets. Both language ecosystems have a client for
it: `neuprint-python` and, on the R side, `neuprintr`.

Either needs an authentication token, which you get by logging in to neuPrint and copying it
from your account page. The datasets themselves are public; the token identifies you to the
server.

## neuprint-python

```sh
pip3 install neuprint-python
```

```python
import neuprint as neu

client = neu.Client('https://neuprint.janelia.org',
                    dataset='hemibrain:v1.1',
                    token={your_token})
```

Most functions accept `neu.NeuronCriteria`, a filter over body IDs, types, instance names and
regions of interest, which is how you select the neurons a query applies to.

## neuprintr

`neuprintr` is part of the [natverse](/docs/tools/natverse/) and is installed with it:

```r
install.packages('natmanager')
natmanager::install('natverse')
```

## Which neurons am I looking at

Body IDs are local to a neuPrint dataset. VFB assigns its own persistent identifiers to the
same neurons and records the cross-references, so [VFB_connect](/docs/tools/vfb-connect/) can
map between a neuPrint body ID and everything else VFB holds for that neuron — including
imagery and its classification in the anatomy ontology.

## Where next

The [neuPrint tutorial](/docs/tutorials/apis/neuprint/) covers fetching neurons, synaptic
partners and paths through the connectome, and plotting the resulting graphs. VFB's own
connectivity data is described under [Data](/docs/data/).

Full documentation:
[neuprint-python](https://connectome-neuprint.github.io/neuprint-python/docs/) and
[neuprintr](https://natverse.org/neuprintr/).
