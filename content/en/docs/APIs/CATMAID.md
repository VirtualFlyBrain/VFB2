---
title: "CATMAID API (VFB Pass-through)"
linkTitle: "CATMAID API"
weight: 10
date: 2026-08-30
description: >
  The fastest and simplest way to pull data out of VFB's hosted CATMAID instances — accepts VFB ids as well as native skeleton ids (skids), needs no token or CSRF handshake, and is cached for speed.
---

VFB hosts several [CATMAID](https://catmaid.readthedocs.io/) instances (FAFB, FANC, L1EM, Larva1099, and others — see [Hosted Sites](/hosted/)). Each one has its own native CATMAID API, but for most uses **the recommended way to pull data out of any of them is VFB's CATMAID pass-through**, served at:

```
https://v3-cached.virtualflybrain.org/catmaid/{instance}/{command}
```

It sits in front of the same instances and forwards to their native API, but resolves two problems that come up as soon as you try to use CATMAID data alongside the rest of VFB: it takes VFB ids directly, and it needs no CSRF cookie, referrer or per-instance token to read data. If you already have a `VFB_...` id from a term-info page or a VFBconnect query, you can hand it straight to the pass-through — no separate lookup step to find the matching skeleton id first.

## Why use it instead of calling CATMAID directly

- **VFB ids and skids, mixed freely.** Pass a list containing both forms — e.g. `VFB_001011rj` alongside a native skid such as `16` — or a comma-separated string of either, and the pass-through resolves VFB ids to skids internally via VFB's knowledge base before forwarding the call.
- **No token, no CSRF cookie.** CATMAID's own read API is open, but most of its query endpoints are POST and subject to a CSRF check that a plain `curl`/`requests` call has to work around (see the per-instance "Public API token" sections under [Hosted Sites](/hosted/)). The pass-through is a plain JSON GET/POST API with none of that to handle.
- **GET or POST.** Every command works as `GET .../catmaid/{instance}/{command}?param=value`; the same parameters can go in a POST body instead (JSON object, or form-encoded) — the only way to send an id list too long for a URL.
- **Cached.** Responses are served from a cache tuned for repeat queries, so the same query is fast on every call after the first.
- **VFB-registered SWC.** The `swc` command accepts `aligned={template}` to fetch the skeleton already transformed into one of VFB's registered template spaces — something the native CATMAID API doesn't offer, since template registration is VFB's own addition.
- **One consistent response envelope** across every hosted instance and command, so client code doesn't need per-instance branching.

## Interactive docs and the full command list

The command catalogue changes as commands are added, so it isn't duplicated here. The authoritative, always-current reference is the interactive docs page itself:

- **[https://v3-cached.virtualflybrain.org/](https://v3-cached.virtualflybrain.org/)** — browsable docs for every command, with a "Run" button to try a call directly.
- **`https://v3-cached.virtualflybrain.org/docs.json`** — the same catalogue as machine-readable JSON, for generating clients or checking parameters programmatically.

## Basic usage

```bash
# Native skid
curl "https://v3-cached.virtualflybrain.org/catmaid/fafb/annotations_for_skeletons?ids=16"

# VFB id instead — resolved to a skid internally before the call is forwarded
curl "https://v3-cached.virtualflybrain.org/catmaid/fafb/annotations_for_skeletons?ids=VFB_001011rj"

# A long id list, or a mix of VFB ids and skids, goes in the POST body instead of the query string
curl -X POST "https://v3-cached.virtualflybrain.org/catmaid/fafb/annotations_for_skeletons" \
  -H "Content-Type: application/json" \
  -d '{"ids": ["VFB_001011rj", 16]}'
```

`{instance}` is one of the ids from the [Hosted Sites](/hosted/) list (`fafb`, `fanc`, `l1em`, `larva1099`, `abd1.5`, `iav-robo`, `iav-tnt`, `l3vnc`) — the same machine-readable list is published at [`/data/EM/catmaid.json`](https://virtualflybrain.org/data/EM/catmaid.json). `{command}` is any command shown on the docs page, e.g. `annotations_for_skeletons`, `connectivity`, `skeleton_ids`, `swc`. Where an instance hosts more than one CATMAID project (FANC does), pass `project` as a query parameter to pick a project other than the default.

## Response format

Every call returns a JSON object wrapping CATMAID's own response alongside the id resolution VFB did on your behalf:

```json
{
  "instance": "fafb",
  "project_id": 1,
  "command": "annotations_for_skeletons",
  "xref_db": "catmaid_fafb",
  "id_map": {"VFB_001011rj": "2856545"},
  "unmatched": [],
  "result": { }
}
```

- `id_map` — `{vfb_id: skid}` for every VFB id in your request that resolved to a skeleton on this instance.
- `unmatched` — VFB ids in your request that had no skeleton on this instance (not every VFB anatomy term has a CATMAID reconstruction).
- `result` — CATMAID's own response for `command`, unchanged.
- `reverse_map` — included on commands that return skids as keys or values, mapping them back to VFB ids where one exists.

## Direct access to the underlying CATMAID instance

The pass-through covers read access; for tracing, editing, or anything the pass-through's command list doesn't cover, use the instance's own native CATMAID API directly. Each hosted instance documents this under its own page, with the base API URL, a link to [CATMAID's own API documentation](https://catmaid.readthedocs.io/en/stable/api.html), and the public read-only token needed for browser-based tools:

- [Hosted Sites](/hosted/) — one page per instance (FAFB, FANC, L1EM, Larva1099, and others), each with its "Public API token" section.

Tools that already speak CATMAID's native API directly — [pymaid](/docs/tutorials/apis/pymaid/), [navis](/docs/tutorials/apis/navis/) — continue to work unchanged against those native endpoints; the pass-through is an additional, simpler option for scripts and services that just need data by id, not a replacement for them.
