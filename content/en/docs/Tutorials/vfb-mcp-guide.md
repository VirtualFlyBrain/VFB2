---
title: "VFB Model Context Protocol (MCP) Tool Guide"
weight: 402
date: 2026-02-07
series: ["Tutorials"]
description: >
  Learn how to use the VFB MCP tool to explore Virtual Fly Brain data through Large Language Models
---

## Overview

The Virtual Fly Brain **Model Context Protocol (MCP) Tool** enables you to query VFB data through Large Language Models like Claude using natural language. This guide shows you how to get started and provides examples of common queries.

## What is MCP?

The Model Context Protocol is a standard that allows LLMs to interact with external data sources and tools. The VFB MCP tool follows this standard, providing your LLM with access to VFB's neuroanatomical databases, NBLAST similarity scores, and term information.

## Accessing the Tool

The VFB MCP tool is available at: **[vfb3-mcp.virtualflybrain.org](https://vfb3-mcp.virtualflybrain.org/)**

That page always states the currently deployed version and the
full client setup instructions, including GitHub Copilot, VS Code and Gemini, so check it there
rather than here if the two disagree.

### Quick Start

#### Use the Live Service (Recommended)

The easiest way to use VFB3-MCP is through our hosted service. This requires no installation or setup on your machine.

The server speaks MCP over **streamable HTTP** at
`https://vfb3-mcp.virtualflybrain.org`. There is no API key and no account to create. Every client
below needs the same two facts — that URL and the HTTP transport — so if your client is not listed,
those are what to give it.

Client menus and config formats change faster than this page can track. Where a client offers a
first-class command or UI for adding a remote MCP server, use that in preference to hand-editing
configuration, and follow the client's own current documentation if the steps below have drifted.

##### Claude Desktop

Add it as a custom connector: **Settings → Connectors → Add custom connector**, then give the name
`virtual-fly-brain` and the URL `https://vfb3-mcp.virtualflybrain.org`. Remote MCP servers are added
through Connectors; `claude_desktop_config.json` is for locally-run servers and is not the route for
this one.

##### Claude Code

One command, from any directory:

```bash
claude mcp add --transport http virtual-fly-brain https://vfb3-mcp.virtualflybrain.org
```

Add `--scope user` to make it available in every project rather than the current one. Check it
registered with `claude mcp list`. Editing `~/.claude.json` by hand also works but is easy to get
wrong and is not needed.

##### VS Code and GitHub Copilot

Run **MCP: Add Server** from the Command Palette, choose the HTTP option, and give the same name and
URL. This writes an `mcp.json` for you:

```json
{
  "servers": {
    "virtual-fly-brain": {
      "type": "http",
      "url": "https://vfb3-mcp.virtualflybrain.org"
    }
  }
}
```

##### Other MCP clients

Most clients take a block of this shape. Consult your client's documentation for the exact key names
— `type`, `transport` and `url` are spelled differently across implementations.

```json
{
  "mcpServers": {
    "virtual-fly-brain": {
      "type": "http",
      "url": "https://vfb3-mcp.virtualflybrain.org"
    }
  }
}
```

##### Gemini and other models without built-in MCP support

There is no MCP support in the Gemini web interface, so you connect from your own code: use the
`mcp` Python package to open a streamable-HTTP session against the VFB URL, call `list_tools()`, and
pass the returned schemas to the model as function declarations. The same pattern works for any
model with function calling — the MCP client does the transport, and the model only ever sees tool
schemas.

```bash
pip install google-genai mcp
```

#### Testing the Connection

Once configured, you can test that VFB3-MCP is working by asking your AI assistant questions like:

Basic Queries:

- "Get information about the neuron VFB_jrcv0i43"
- "Search for terms related to medulla in the fly brain"
- "What neurons are in the antennal lobe?"

Advanced Queries:

- "Find all neurons that connect to the mushroom body"
- "Show me expression patterns for gene repo"
- "What brain regions are involved in olfactory processing?"
- "Run a connectivity analysis for neuron VFB_00101567"

Search Examples:

- "Search for adult neurons in the visual system"
- "Find genes expressed in the central complex"
- "Show me all templates available in VFB"

If you see responses with VirtualFlyBrain data, including neuron names, brain regions, gene expressions, or connectivity information, the setup is successful!

For more detailed usage examples and API calls, see [examples.md](https://github.com/VirtualFlyBrain/VFB3-MCP/blob/main/examples.md).

### Local Installation

If you prefer to run the MCP server locally, see the [VFB3-MCP repository README](https://github.com/VirtualFlyBrain/VFB3-MCP/blob/main/README.md) for detailed installation instructions.

## Core Features

The server exposes a set of tools covering search, term lookup, hierarchy, connectivity, name
resolution and the precomputed queries behind the VFB website. The tools below are those documented here at the
time of writing; the server's own
page at [vfb3-mcp.virtualflybrain.org](https://vfb3-mcp.virtualflybrain.org/) lists the full set as
deployed, which is the authoritative source if this page has fallen behind.

Connectivity is worth calling out because the examples further down rely on it: `query_connectivity`
answers "what connects to this neuron" directly, and `list_connectome_datasets` gives the dataset
symbols you need to include or exclude a connectome from that query. Ask your assistant in plain
language and it will pick the tool; you do not need to name them.

### 1. **Term Information Queries** (`get_term_info`)

Retrieve detailed information about any VFB term using its VFB ID.

**Example Query:**
```text
"What is the medulla? Please get the full definition and structure."
```

**Returns:**
- Term definition and synonyms
- Classification and type information
- Anatomical relationships (part of, develops from, innervates, etc.)
- Associated neurons and expression patterns
- Related images and connectivity data

### 2. **Term Search** (`search_terms`)

Search for VFB terms using keywords and filters.

**Example Query:**
```text
"Find neurons in the medulla"
```

**Advanced Filtering Options:**
- **Filter by entity type:** neuron, muscle, glia, anatomical region
- **Filter by nervous system component:** visual system, olfactory system, sensory neuron, motor neuron, etc.
- **Filter by nervous system property:** cholinergic, GABAergic, glutamatergic, dopaminergic, peptidergic, etc.
- **Filter by dataset:** FAFB, FlyCircuit, hemibrain, neuprint, flycircuit, etc.

### 3. **Query Execution** (`run_query`)

Execute specific queries on VFB terms, including NBLAST similarity analysis.

**Example Query:**
```text
"What neurons are morphologically similar to IN02A049?"
```

### 4. **Hierarchy Trees** (`get_hierarchy`)

Walk the ontology up or down from a term. Use `part_of` for how a region is built from its parts,
and `subclass_of` for cell type taxonomies. Start one level deep and go further only if you need to.

**Example Query:**
```text
"What are the parts of the mushroom body?"
"What types of Kenyon cell are there?"
```

Asking for the parts of the mushroom body (FBbt_00005801) one level down returns 17 children,
including the calyx, pedunculus, spur and lobe system, each for adult and larval stages.

### 5. **Search Facets** (`list_search_facets`)

List the type names that searches can filter, exclude, boost or demote by, with the number of terms
carrying each. There are 233 of them and they come from the index's own annotations rather than a
curated list, so they change as data is added. Worth listing rather than guessing.

**Example Query:**
```text
"What connectivity filters can I search by?"
```

That returns `has_neuron_connectivity` (488,110 terms) and `has_region_connectivity` (22,587).

### 6. **Name Resolution** (`resolve_entity`)

Turn a name as written in a paper into FlyBase and VFB IDs — gene symbols, driver lines, construct
names. It tries an exact match first, then synonyms, then a broad pattern match, and tells you which
of the three it used.

**Example Query:**
```text
"What is Hb9-GAL4?"
"Tell me about P{VT054895-GAL4.DBD}"
```

⚠️ When the match came from a synonym or a broad pattern rather than an exact name, check the
result is the entity you meant before building on it. Your assistant should say which it was.

### 7. **Split-GAL4 Combinations** (`resolve_combination`)

Resolve a split-GAL4 combination name to its FBco ID and the component hemidrivers that make it up.

**Example Query:**
```text
"What are the components of SS04495?"
"What is MB002B?"
```

## Example Use Cases

### Case 1: Exploring a Transgenic Construct

**User Question:**
"What is P{E(spl)m8-HLH-2.61} and where is it used?"

**Tool Actions:**
1. Search for the construct in VFB
2. Retrieve full term information
3. Return detailed description including:
   - FlyBase ID (FBtp0004163)
   - Gene involved: E(spl)m8
   - Type: Transgenic construct (reporter for gene expression)
   - Expression patterns and research use
   - Related constructs and variants

**Result:** You get comprehensive information about the transgenic reporter, its purpose, and research applications.

### Case 2: Understanding a Neuroblast Population

**User Question:**
"What is the Medulla Forming Neuroblast and what role does it play?"

**Tool Actions:**
1. Search for "medulla forming neuroblast"
2. Get term info for FBbt_00001938
3. Return:
   - Cell type classification (neuroblast)
   - Location in the larval optic anlage
   - Developmental fate (produces medulla neurons)
   - Marker genes (dpn, ase)
   - Number of neurons produced (~54,000 secondary neurons)
   - Available scRNAseq and expression data

**Result:** Understand the neuroblast's role in developing the adult medulla's neural circuitry.

### Case 3: Discovering Neuron Types

**User Question:**
"What types of neurons are in the medulla?"

**Tool Actions:**
1. Search for "neuron" with filter for medulla
2. Return 472 neuron types with parts in the medulla, organized by category:
   - **Medulla intrinsic neurons (Mi):** columnar neurons with confined processes
   - **Central medulla intrinsic neurons (Cm):** arborizing in central/serpentine layer
   - **Medulla tangential neurons (Mt):** wide-field spanning neurons
   - **Medulla visual projection neurons (MeVP):** tangential projection neurons
   - **Medulla columnar neurons (MC):** connecting medulla to tubercle
   - Plus many more specialized types

**Result:** Get a comprehensive overview of medulla neuron diversity and organization.

### Case 4: Morphological Similarity Queries

**User Question:**
"Show me what the IN02A049 neuron looks like and find similar neurons."

**Tool Actions:**
1. Get term info for IN02A049 (specific instance from MANC connectome)
2. Execute NBLAST query for morphologically similar neurons
3. Return:
   - 3D visualization of the neuron
   - Classification and properties
   - Synaptic inputs (neurotransmitter types and counts)
   - Morphologically similar neurons with NBLAST scores
   - Cross-connectome comparisons

**Result:** Discover morphologically similar neurons for comparative analysis.

### Case 5: Understanding NBLAST Scores

**User Question:**
"How are NBLAST scores calculated?"

**Tool Actions:**
1. Search for "NBLAST"
2. Return detailed explanation including:
   - Algorithm basis (Costa et al. 2016)
   - How neurons are represented (point skeletons with direction vectors)
   - Scoring mechanism (Euclidean distance + direction similarity)
   - Normalization approach (comparison to self-match)
   - Asymmetry property and symmetrical variants
   - Available datasets (FAFB-FlyWire, Male-CNS optic lobe, FlyCircuit, Hemibrain, FAFB-CATMAID)

**Result:** Understand the methodology behind VFB's morphological similarity analysis.

## Tips for Effective Queries

### 1. **Use VFB IDs When Known**

If you know the VFB ID of a term, use it directly:
```text
"Get me detailed information about FBbt_00003748 (the medulla)"
```

### 2. **Combine Search and Query**

Use search first to find relevant terms, then query them:
```text
"Find all cholinergic neurons in the visual system, 
then tell me about the top 5"
```

### 3. **Filter Strategically**

Use filters to narrow results:
```text
"Show me motor neurons from the male-CNS optic lobe dataset"
```

### 4. **Explore Relationships**

Ask about anatomical and functional relationships:
```text
"What neurons innervate the medulla? 
What brain regions do they come from?"
```

### 5. **Cross-Dataset Comparisons**

Compare neurons across different connectome datasets:
```text
"Find the equivalent of this FAFB neuron in the hemibrain dataset"
```

## Available Datasets

The VFB MCP tool provides access to neurons and data from:

- **FAFB-FlyWire** (v783) - Large-scale adult brain connectome
- **Male-CNS optic lobe** (v1.0.1) - Focused optic lobe connectome
- **FlyCircuit** (1.0) - Single-neuron morphology database
- **Hemibrain** (1.2.1) - Subset of adult brain connectome
- **FAFB-CATMAID** - Manually traced EM data
- **FlyLight Split-GAL4** - Driver line expression images
- **scRNAseq data** - Transcriptomic information

## Understanding VFB IDs

VFB terms use standardized identifiers:

- **FBbt_** - Drosophila anatomy terms (e.g., FBbt_00003748 = medulla)
- **FBgn_** - FlyBase genes (e.g., FBgn0000137 = ase gene)
- **FBtp_** - FlyBase transgenic constructs (e.g., FBtp0004163 = P{E(spl)m8-HLH-2.61})
- **VFB_** - VirtualFlyBrain-specific IDs for individuals and images

## Next Steps

- **Explore the tool:** Visit [vfb3-mcp.virtualflybrain.org](https://vfb3-mcp.virtualflybrain.org/)
- **Endpoint reference:** See the [MCP Server API page](/docs/apis/mcp/) for the endpoint, transport and source repository at a glance
- **Read more about NBLAST:** See our [NBLAST concepts page](/docs/concepts/nblast)
- **Learn about VFB APIs:** Check our [API overview](/docs/tutorials/apis/vfb_api_overview)
- **Browse VFB directly:** Visit the main [Virtual Fly Brain site](https://virtualflybrain.org/)

## Common Questions

**Q: Do I need to install anything?**
A: No, if you're using Claude or another MCP-compatible LLM with the integration already set up, just start asking questions.

**Q: Can I download the data I find?**
A: Yes, many results include links to download images, neuron skeletons, and connectivity data. Check the [API documentation](/docs/tutorials/apis/vfb_api_overview) for programmatic access.

**Q: What if I don't know the VFB ID?**
A: The search tool can find terms by name or keyword. The LLM will help you locate the right term.

**Q: Can I combine VFB queries with other analyses?**
A: Absolutely! You can ask your LLM to retrieve VFB data and then perform additional analyses, create visualizations, or integrate with other tools.

---

**Happy exploring!** If you have questions or suggestions about the VFB MCP tool, please reach out to the [VFB team](/about/contactus).
