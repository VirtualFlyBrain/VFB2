---
title: "Similarity Score Queries Guide"
linkTitle: "Similarity Score Queries Guide"
weight: 4000
description: >
  This guide provides step-by-step instructions on how to use the similarity score queries on VirtualFlyBrain.org. These queries allow users to find neurons or expression patterns that are morphologically similar to a selected neuron or expression pattern.
---

# Similarity Score Queries Guide

The similarity scores are calculated using [NBLAST](https://www.virtualflybrain.org/docs/tutorials/apis/connectome/5_nblast/) or other third-party scores (e.g. [NeuronBridge](https://neuronbridge.janelia.org/)). Only queries with above-threshold scores will appear in the 'Find similar...' menu. 

## Step 1: Select a Neuron or Expression Pattern

Navigate to the [VFB browser](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto) and select a neuron or expression pattern of interest so it's information is shown in the [Term Info](https://www.virtualflybrain.org/docs/getting-started/terminfo/) panel

## Step 2: Open the 'Find similar...' Menu under the 'Query For' section

Under the 'Query For' section, locate the 'Find similar...' expandable menu. This menu will only appear if an above-threshold score is available for the selected neuron or expression pattern.

## Step 3: Run a Similarity Score Query

Inside the 'Find similar...' menu, you will find queries to find morphologically similar neurons or expression patterns. Select a query to run it. The results will display neurons or expression patterns that are similar to your selected neuron or expression pattern.

**Note:** We recalculate these scores shortly after new data is added, so new matches may appear if you check back a few months later. 
