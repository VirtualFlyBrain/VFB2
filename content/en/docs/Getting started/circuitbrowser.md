---
categories: ["overview","help"]
tags: ["connectome","tools"]
title: "This is the Circuit Browser tab"
linkTitle: "Circuit Browser"
description: >
   The Circuit Browser allows you to find the strongest paths from one neuron (the source neuron) to another (the target neuron). 
weight: 70
---
<link rel="stylesheet" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto/node_modules/@geppettoengine/geppetto-client/geppetto-client/style/css/gpt-icons.css">

The 'strongest' paths are the shortest/highest weighted paths. Paths are arranged from the 'strongest' at the bottom to the 'weakest' at the top. A detailed explanation for the algorithm used to determine path strengths can be found [here](https://github.com/VirtualFlyBrain/graph_queries/blob/main/weighted_path.md).

<i class="fas fa-dot-circle"></i>   Search for the source neuron to start from (Note: query is directional)
    
<i class="fa fa-map-marker"></i>   Search for the target neuron
    
<i class="fas fa-arrows-alt-h"></i>   Maximum number of paths to return (only the 'strongest' paths will be returned)
    
<i class="fa fa-balance-scale"></i>   A minimum weight for the synapse count of each connection can be applied, paths containing individual connections below this minimum will not be returned


<p align="center">
  <img src="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto/build/circuit1.png" alt="Virtual Fly Brain (VFB) 3D Viewer" style="max-width=50%" />
</p>
