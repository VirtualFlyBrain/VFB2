---
categories: ["overview","help"]
tags: ["term","classification","location","tools"]
title: "The Term Context tab"
linkTitle: "Term Context"
description: >
   Term Context displays graphical information on the currently selected term's location or classification.
weight: 212
---
<link rel="stylesheet" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto/node_modules/@geppettoengine/geppetto-client/geppetto-client/style/css/gpt-icons.css">

Select a graph from the **Graphs for** section of the [Term Info](/docs/website-features/terminfo/#ontology-terms-and-graphs) pane to display it in the Term Context pane. Click on any term in the graph to select it and view its Term Info.

## Show location of *[term]* {#location}

The `location` graph shows where the selected term sits in the nervous system: the structures it is `part of` or `overlaps`, and, for neurons, the regions it has synaptic terminals in, followed up through the anatomy hierarchy.

## Show classification of *[term]* {#classification}

The `classification` graph shows what kind of thing the selected term is: its parent classes (`is a`) up through the anatomy ontology, restricted to anatomical, cell, neuropil, ganglion and tract classes.

## Controls {#controls}

<p align="center">
  <img src="/images/term-context.png" alt="Term Context tab showing classification of MBON01." style="max-width=50%" />
</p>

<i class="fa fa-home"></i>   Home resets your view

<i class="fa fa-search-plus"></i>   Use the zoom icons or scroll with the mouse to zoom in/out
    
<i class="fas fa-sync-alt"></i>   Click to refresh to the current focus term
    
<i class="fa fa-bars"></i>   Select either the location or the classification for the current term
