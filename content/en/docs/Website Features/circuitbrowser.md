---
categories: ["overview","help"]
tags: ["connectome","tools"]
title: "The Circuit Browser tab"
linkTitle: "Circuit Browser"
description: >
   The Circuit Browser finds the strongest synaptic paths from one neuron or neuron type to another, in each connectome.
weight: 214
---
<link rel="stylesheet" href="https://v3.virtualflybrain.org/org.geppetto.frontend/geppetto/node_modules/@geppettoengine/geppetto-client/geppetto-client/style/css/gpt-icons.css">

The Circuit Browser finds the strongest multi-step routes from a source to a target. Each end can be a neuron type (a [class](/docs/concepts/classes-and-individuals/), such as *lobula columnar neuron LC12*) or a single neuron from a connectome (an individual). Each connectome is searched separately, so you can compare the routes found in different datasets.

## Running a search {#running-a-search}

<i class="fas fa-dot-circle"></i>   **From:** search for the neuron or neuron type to start from. The search is directional.

<i class="fa fa-map-marker"></i>   **To:** search for the neuron or neuron type to end at. The arrows beside the fields swap From and To.

**# Paths:** how many paths to return for each connectome, strongest first.

**Min Weight:** the minimum number of synapses for each connection on a path (default 5). Lower it if nothing is found.

Each search result is tagged **Class** (a neuron type) or **Individual** (one neuron). Neuron types with no neurons in any connectome are listed last, greyed out and marked *no connectome neurons*, as a search from them cannot find anything. Once you have chosen a neuron in one field, the other field only offers neurons from the same connectome, as paths between neurons stay within one dataset. Neuron types are always offered.

## How paths are found {#how-paths-are-found}

Each connection is weighted by the share of the target's synaptic input that comes from the source. A path's score is the product of these shares along it, so a path is strong when every step is a large part of the next neuron's input. The best-scoring paths are returned for each connectome.

**Searching between neuron types.** When both ends are neuron types, the search runs on a graph of neuron types built for each connectome. Each neuron is counted under its single most specific type in that connectome, so broad types do not act as shortcuts. A broad type such as *Kenyon cell* stands for all the specific types beneath it. A connection between two types adds up the synapses between all their neurons. Hemibrain and FAFB (CATMAID) are not searched between neuron types.

**Searching from or to a neuron.** When either end is a single neuron, the search runs on that neuron's connectome at the level of individual neurons. A neuron type at the other end stands for all of its neurons in that connectome.

The graphs are rebuilt with each VFB data release.

## Reading the graph {#reading-the-graph}

<img src="/images/circuitbrowser/class_paths.png" alt="Circuit Browser showing the three strongest FlyWire paths from LC12 to the giant fiber neuron (DNp01) via PVLP097, PVLP100, CB0813 and CB3513, with the legend at the top right." style="max-width:100%">

*Paths from LC12 to the giant fiber neuron (DNp01) in FlyWire, searched between neuron types.*

Paths read from left to right, from source to target. Each box is a neuron type or a neuron:

- The title is the type's symbol, or its name if it has no symbol.
- For a neuron, its own name is shown under the title.
- The coloured bar shows what kind of neuron it is, such as its transmitter, as listed in the legend.
- Hovering over a box shows its full name and ID.

Each link is labelled with the number of synapses and the share of the target's input, e.g. *98 · 13%*. Hovering over a link shows the details: synapses, the number of connected neuron pairs (between neuron types), the share of the target's input and the share of the source's output.

The legend at the top right controls what is shown:

- **Dataset:** choose which connectome's paths to show, with the number of paths found in each. The connectome with the strongest path is shown first.
- **Show example neurons (slower):** for a search between neuron types, shows the strongest chains of individual neurons along each path. This can take tens of seconds on the larger connectomes.
- When paths between neuron types are also found in other connectomes, the legend says which. These paths are the most robust.
- The legend also says how many neurons in the dataset are not included in a search between neuron types, because they have no single specific type (see below).

<img src="/images/circuitbrowser/example_neurons.png" alt="The same search with Show example neurons ticked: chains of individual FlyWire neurons, each box titled with its type and showing the neuron's own name." style="max-width:100%">

*The same search with **Show example neurons** ticked: each box is one FlyWire neuron, titled with its type.*

### Neurons without a single type {#neurons-without-a-single-type}

Paths between individual neurons can pass through neurons that are not counted under one specific type in their connectome, so are left out of searches between neuron types. Their boxes show the types they do have, separated by "/" where there is more than one, and hovering shows the types' full names. This happens when a neuron:

- is typed only as a broad class, such as *adult ascending neuron*, while other neurons in that connectome have more specific types beneath it;
- has more than one most specific type in that connectome;
- has no type at all, shown as *untyped*.

## Navigating the graph {#navigating-the-graph}

- Click a box to open that neuron or neuron type in [Term Info](/docs/website-features/terminfo/); a neuron is also added to the 3D viewer.
- Right-click a box to zoom in on it.
- Use the home and zoom icons at the top left to reset or zoom the view, or scroll to zoom.

## Add a neuron or neuron type from Term Info {#add-a-neuron-from-term-info}

Neurons with connectivity data, and neuron types, show an **Add *[term]* to Circuit Browser Query** link in their [Term Info](/docs/website-features/terminfo/) pane. Clicking it opens the Circuit Browser with that term filled into the first empty field (if both fields are already set, it replaces the last one), so you can build a path search from the term you are looking at without searching for it again.

## From code or an AI assistant {#from-code-or-an-ai-assistant}

The same searches are available from the [VFBquery API](/docs/apis/vfbquery/#connectivity) (`/circuit_paths`) and, for AI assistants, from the [VFB MCP server](/docs/tutorials/vfb-mcp-guide/) (`find_circuit_paths`).
