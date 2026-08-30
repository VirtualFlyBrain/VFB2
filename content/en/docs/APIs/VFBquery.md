---
title: "VFBquery API"
linkTitle: "VFBquery API"
weight: 6
date: 2026-08-30
description: >
  VFB's general-purpose query API — term information, search, connectivity, cross-references, FlyBase stocks and combinations, and the CATMAID pass-through — all as simple read-only JSON calls.
---

VFBquery is the query service behind most of what the VFB website itself does — the term information panel, the search box, the hierarchy browser, connectivity queries, stock lookups — exposed as a plain JSON HTTP API anyone can call directly. It's the same recommended entry point as the [CATMAID pass-through](/docs/apis/catmaid/), which is one part of this service:

```
https://v3-cached.virtualflybrain.org/
```

Every endpoint is a read-only GET (the CATMAID pass-through also accepts POST — see its own page) returning JSON, with no API key or account needed.

## Interactive docs and the full spec

As with the CATMAID pass-through, the endpoint list changes over time, so it isn't duplicated in full here. The authoritative, always-current reference is the service itself:

- **[https://v3-cached.virtualflybrain.org/](https://v3-cached.virtualflybrain.org/)** — browsable docs for every endpoint, with a "Run" button to try a call directly.
- **`https://v3-cached.virtualflybrain.org/docs.json`** — the same catalogue as machine-readable JSON.

What follows is a guided tour of the main groups of endpoints, to help you find the right one.

## Term information

- **`/get_term_info?id=FBbt_00003748`** — the full report behind the website's term information panel for one VFB or FBbt id: metadata, synonyms, relationships, aligned images, cross-references, and the list of named queries that can be run from the term.
- **`/run_query?id=FBbt_00003748&query_type=ListAllAvailableImages`** — runs one of the named query types listed in a term's `/get_term_info` response (e.g. `ListAllAvailableImages`), in the website's own row format. Supports `offset`/`limit` paging.
- **`/get_hierarchy?id=FBbt_00005801&max_depth=1`** — the hierarchy browser's tree: follows one relationship (`part_of` or `subclass_of`) from a term, upward, downward, or both.

## Search and identifiers

- **`/search?query=medulla&limit=10`** — the same ranked free-text search the website uses. `filter_types`/`exclude_types`/`boost_types`/`demote_types` narrow or re-rank by type.
- **`/facets`** — the vocabulary of type names `/search`'s type parameters accept.
- **`/xref?id=VFB_001011rj`** — cross-reference lookup in either direction: `id=` for VFB id → external accessions, or `accession=` (optionally with `db=`) for external id → VFB.
- **`/combine?expr=calyx AND lh&calyx=...&lh=...`** — set algebra (AND/OR/NOT/XOR and friends) over two or more named query results, compared on term id, with every step traced in the response.

## Connectivity

- **`/list_connectome_datasets`** — the connectome datasets `/query_connectivity` can draw on.
- **`/query_connectivity?upstream_type=LPLC2&downstream_type=giant fiber neuron`** — synaptic connectivity from one neuron type (or any subclass) to another, summed across the connectomes. Types can be given as labels, synonyms or FBbt ids.

## FlyBase stocks and combinations

- **`/resolve_entity?query=dpp`** — free-text resolver for a gene, allele or transgene name, returning candidate FlyBase feature ids.
- **`/find_stocks?id=FBgn0000490`** — stock-centre holdings for a resolved feature id.
- **`/resolve_combination?query=GMR37H08-ZpGAL4DBD in attP2`** — resolver for split-GAL4 hemidriver combinations, returning FBco ids.
- **`/find_combo_publications?id=FBco0000052`** — publications using a resolved combination.

## CATMAID pass-through

`/catmaid`, `/catmaid/{instance}` and `/catmaid/{instance}/{command}` proxy VFB's hosted CATMAID instances, converting between VFB ids and native skeleton ids (skids) along the way. This is documented in full, with worked examples, on its own page: **[CATMAID API](/docs/apis/catmaid/)**.

## Service

- **`/health`** — a plain `OK` liveness check.
- **`/status`** — queue depth, cache hit/miss counts and worker utilisation.

## force_refresh and caching

`v3-cached.virtualflybrain.org` caches responses for speed. Most endpoints that reflect fast-changing data accept `force_refresh=true` to bypass the cache for that one call — see the individual endpoint's parameters on the [interactive docs page](https://v3-cached.virtualflybrain.org/).
