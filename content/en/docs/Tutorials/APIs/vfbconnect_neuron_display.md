---
title: "Guide to Working with Images from Virtual Fly Brain (VFB) Using the VFBConnect Library"
linkTitle: "Neuron display in VFBconnect"
date: 2024-08-25
weight: 5
description: >
    This guide will help you use the VFBConnect library to interact with Virtual Fly Brain (VFB) data, specifically focusing on working with neuron images and their representations. The examples provided cover retrieving neuron data, accessing different types of data representations (skeleton, mesh, volume), and visualizing this data.
---

## Prerequisites

Before starting, ensure you have the VFBConnect library installed. The recommended Python version is 3.10.14, as this version is tested against the library.

```bash
pip install vfb-connect
```

## Importing the VFBConnect Library

Start by importing the VFBConnect library. This library provides a simple interface to interact with neuron data from the Virtual Fly Brain.

```python
from vfb_connect import vfb
```

## Retrieving Neuron Data

To work with specific neurons, you can use the `vfb.term()` function. This function takes a unique identifier (e.g., ID, label, synonym) for the neuron.

### Example: Retrieving a Single Neuron

```python
neuron = vfb.term('5th s-LNv (FlyEM-HB:511051477)')
```

The `neuron` variable now holds data about the neuron identified by the given term.

### Working with Neuron Data

The retrieved neuron object can provide different representations of neuron data, such as its skeleton, mesh, and volume. These representations can be visualized using various plotting methods.

```python
# Access the skeleton representation
neuron_skeleton = neuron.skeleton

# Check the type of the skeleton representation
print(type(neuron_skeleton))  # Output: <class 'navis.neuron.Neuron'>

# Plot the skeleton in 2D
neuron_skeleton.plot2d()

# Access the mesh representation
neuron_mesh = neuron.mesh

# Access the volume representation
neuron_volume = neuron.volume
```

## Retrieving Multiple Neurons

You can retrieve multiple neurons using the `vfb.terms()` function, which accepts a list of neuron identifiers.

### Example: Retrieving Multiple Neurons

```python
neurons = vfb.terms(['5th s-LNv', 'fru-M-300008', 'catmaid_fafb:8876600'])
```

This command retrieves multiple neurons, which can then be visualized or manipulated collectively.

## Flexible Matching Capabilities

One of the key features of the VFBConnect library is its flexible matching capability. The `vfb.terms()` function can accept a variety of identifiers, such as:

- **IDs**: Unique identifiers assigned to each neuron.
- **Xref (Cross-references)**: External references that relate to other datasets.
- **Labels**: Human-readable names for neurons.
- **Symbols**: Abbreviated names or symbols used to represent neurons.
- **Synonyms**: Alternative names by which a neuron might be known.
- **Partial Matching**: You can provide a partial name, and VFBConnect will attempt to find the best match.
- **Case Insensitive Matching**: Matching is case insensitive, so if an exact match isn't found, '5th s-LNv' and '5TH S-LNV' are treated the same. This allows for more flexible querying without worrying about exact case matching.

### Example: Using Flexible Matching

```python
neurons = vfb.terms('5th s-LN')
```

If an exact match isn't found, VFBConnect will provide potential matches. This feature ensures that even with partial or approximate information, you can still retrieve the relevant neuron data.

**Output Example:**

```
Notice: No exact match found, but potential matches starting with '5th s-LN': 
'5th s-LNv (FlyEM-HB:511051477)': 'VFB_jrchk8e0', 
'5th s-LNv': 'VFB_jrchk8e0'
```

This notice will help you identify the correct neuron based on the closest matches.

## Visualizing Neurons

VFBConnect provides various methods to visualize neuron data, both individually and collectively.

### 3D Visualization

To plot neurons in 3D, use the `plot3d()` method. This is useful for visualizing the spatial structure of neurons.

```python
neurons.plot3d()
```

### 2D Visualization

For 2D visualization, use the `plot2d()` method.

```python
neurons.plot2d()
```

### Viewing Merged Templates

VFBConnect also allows viewing merged templates of neurons, combining multiple neuron structures into a single view.

```python
neurons.show()
```

### Opening Neurons in VFB

To open the neurons directly in Virtual Fly Brain, use the `open()` method. This will launch a browser window displaying the neurons in the VFB interface.

```python
neurons.open()
```

## Summary

- Use `vfb.term()` to retrieve single neuron data.
- Use `vfb.terms()` to retrieve multiple neurons with support for partial, case-insensitive, and flexible matching (IDs, labels, symbols, synonyms, etc.).
- Access different data representations (skeleton, mesh, volume) via neuron objects.
- Visualize neuron data in 2D and 3D.
- Use the `show()` method to view merged neuron templates.
- Open neuron data directly in Virtual Fly Brain with the `open()` method.

These examples provide a foundation for working with neuron data from Virtual Fly Brain using the [VFBConnect library](https://vfb-connect.readthedocs.io/). By exploring different neuron representations and visualization methods, you can analyze and understand neuron structures more effectively.
