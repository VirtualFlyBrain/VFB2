---
title: "Data types"
weight: 110
---


# Overview
`navis` is a Python package for analysing, manipulating and visualizing neurons.

`pymaid` lets you interface with a CATMAID server such as those hosted by VFB. 

Both packages have extensive documentation ([navis](https://navis.readthedocs.io/en/latest/) | [pymaid](https://pymaid.readthedocs.io/en/latest/)) with introductory tutorials, examples and a list of all available functions.

## Basic datatypes: neurons and neuron lists 
`navis` knows three types of neurons:

1. `TreeNeurons` = skeletons, e.g. from CATMAID
2. `MeshNeurons` = meshes, e.g. from the hemibrain segmentation
3. `Dotprops` = points + tangent vectors (typically only used for NBLAST)

Collections of neurons are typically held in a specialized container: a`NeuronList`.

## Neurons

In this notebook we will focus on skeletons - a.k.a. `TreeNeurons` - since this is what you get out of CATMAID. Let's kick things off by having a look at what neurons look like once it's loaded: 


```
import navis

# Load one of the example neurons shipped with navis
# (these are olfactory projection neurons from the hemibrain data set)
n = navis.example_neurons(1, kind='skeleton')

# Print some basic info
n
```

    WARNING: Could not load OpenGL library.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>type</th>
      <td>navis.TreeNeuron</td>
    </tr>
    <tr>
      <th>name</th>
      <td>1734350788</td>
    </tr>
    <tr>
      <th>id</th>
      <td>1734350788</td>
    </tr>
    <tr>
      <th>n_nodes</th>
      <td>4465</td>
    </tr>
    <tr>
      <th>n_connectors</th>
      <td>None</td>
    </tr>
    <tr>
      <th>n_branches</th>
      <td>603</td>
    </tr>
    <tr>
      <th>n_leafs</th>
      <td>619</td>
    </tr>
    <tr>
      <th>cable_length</th>
      <td>266457.994591</td>
    </tr>
    <tr>
      <th>soma</th>
      <td>[4176]</td>
    </tr>
    <tr>
      <th>units</th>
      <td>8 nanometer</td>
    </tr>
  </tbody>
</table>
</div>



Above summary lists a couple of (computed) properties of the neuron. Each of those can also be accessed directly like so:


```
n.id
```




    1734350788



There are many more properties that you might find interesting! In theory, you can use type `n.` and TAB to get auto-complete suggestions of available properties and methods.

Deepnote appears to have problems with that sometimes - you can fall back to good 'ole `dir()` in that case.

Here is an (incomplete) list of some of the more relevant properties:
- `bbox`: bounding box of the neuron
- `cable_length`: cable length
- `id`: every neuron has an ID
- `nodes`: the SWC node table underlying the neuron

And a couple of class methods:
- `reroot`: reroot neuron
- `plot2d`/`plot3d`: plot the neuron (see also subsequent lessons)
- `copy`: make and return a copy
- `prune_twigs`: remove small terminal twigs

At this point I encourage you to just explore and play around with what TreeNeuron has to offer. Also check out the [docs](https://navis.readthedocs.io/en/latest/source/tutorials/generated/navis.TreeNeuron.html#navis.TreeNeuron)!

As an example: this is how you get the ID of this neuron's root node.


```
# Current root node of this neuron
n.root
```




    array([1], dtype=int32)



Some of the properties such as `.root` or `.ends` are computed on-the-fly from the underlying raw data. For `TreeNeurons` that's the node table (and it's graph representation). The node table is a pandas DataFrame that looks effectively like a SWC:


```
# `.head()` gives us the first couple rows
n.nodes.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>node_id</th>
      <th>label</th>
      <th>x</th>
      <th>y</th>
      <th>z</th>
      <th>radius</th>
      <th>parent_id</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>15784.0</td>
      <td>37250.0</td>
      <td>28102.0</td>
      <td>10.000000</td>
      <td>-1</td>
      <td>root</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0</td>
      <td>15764.0</td>
      <td>37230.0</td>
      <td>28102.0</td>
      <td>18.284300</td>
      <td>1</td>
      <td>slab</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0</td>
      <td>15744.0</td>
      <td>37190.0</td>
      <td>28142.0</td>
      <td>34.721401</td>
      <td>2</td>
      <td>slab</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0</td>
      <td>15744.0</td>
      <td>37150.0</td>
      <td>28182.0</td>
      <td>34.721401</td>
      <td>3</td>
      <td>slab</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>15704.0</td>
      <td>37130.0</td>
      <td>28242.0</td>
      <td>34.721401</td>
      <td>4</td>
      <td>slab</td>
    </tr>
  </tbody>
</table>
</div>



The methods (such as `.reroot`) are short-hands for main navis functions:


```
# Reroot neuron to another node
n2 = n.reroot(new_root=2)
# Print the new root -> expect "2"
n2.root
```




    array([2])




```
# Instead of calling the shorthand method, we can also do this
n3 = navis.reroot_neuron(n, new_root=2)
n3.root
```




    array([2])



## NeuronLists
In practice you will likely work with multiple neurons at a time. For that, `navis` has a convenient container: `NeuronLists`


```
# Get more than one example neuron
nl = navis.example_neurons(5)

# `nl` is a NeuronList 
type(nl)
```




    navis.core.neuronlist.NeuronList




```
# You can also create neuron lists yourself
my_nl = navis.NeuronList(n)
```

In many ways `NeuronLists` work like Python-lists with a couple of extras: 


```
# Calling just the neuronlist produces a summary 
nl
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>name</th>
      <th>id</th>
      <th>n_nodes</th>
      <th>n_connectors</th>
      <th>n_branches</th>
      <th>n_leafs</th>
      <th>cable_length</th>
      <th>soma</th>
      <th>units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>navis.TreeNeuron</td>
      <td>1734350788</td>
      <td>1734350788</td>
      <td>4465</td>
      <td>None</td>
      <td>603</td>
      <td>619</td>
      <td>266457.994591</td>
      <td>[4176]</td>
      <td>8 nanometer</td>
    </tr>
    <tr>
      <th>1</th>
      <td>navis.TreeNeuron</td>
      <td>1734350908</td>
      <td>1734350908</td>
      <td>4845</td>
      <td>None</td>
      <td>733</td>
      <td>760</td>
      <td>304277.007958</td>
      <td>[6]</td>
      <td>8 nanometer</td>
    </tr>
    <tr>
      <th>2</th>
      <td>navis.TreeNeuron</td>
      <td>722817260</td>
      <td>722817260</td>
      <td>4336</td>
      <td>None</td>
      <td>635</td>
      <td>658</td>
      <td>274910.568784</td>
      <td>None</td>
      <td>8 nanometer</td>
    </tr>
    <tr>
      <th>3</th>
      <td>navis.TreeNeuron</td>
      <td>754534424</td>
      <td>754534424</td>
      <td>4702</td>
      <td>None</td>
      <td>697</td>
      <td>727</td>
      <td>286742.998887</td>
      <td>[4]</td>
      <td>8 nanometer</td>
    </tr>
    <tr>
      <th>4</th>
      <td>navis.TreeNeuron</td>
      <td>754538881</td>
      <td>754538881</td>
      <td>4890</td>
      <td>None</td>
      <td>626</td>
      <td>642</td>
      <td>291434.992623</td>
      <td>[703]</td>
      <td>8 nanometer</td>
    </tr>
  </tbody>
</table>
</div>




```
# Get a single neuron from the neuronlist
nl[1]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>type</th>
      <td>navis.TreeNeuron</td>
    </tr>
    <tr>
      <th>name</th>
      <td>1734350908</td>
    </tr>
    <tr>
      <th>id</th>
      <td>1734350908</td>
    </tr>
    <tr>
      <th>n_nodes</th>
      <td>4845</td>
    </tr>
    <tr>
      <th>n_connectors</th>
      <td>None</td>
    </tr>
    <tr>
      <th>n_branches</th>
      <td>733</td>
    </tr>
    <tr>
      <th>n_leafs</th>
      <td>760</td>
    </tr>
    <tr>
      <th>cable_length</th>
      <td>304277.007958</td>
    </tr>
    <tr>
      <th>soma</th>
      <td>[6]</td>
    </tr>
    <tr>
      <th>units</th>
      <td>8 nanometer</td>
    </tr>
  </tbody>
</table>
</div>



`neuronlists` also support fancy indexing similar to `numpy` arrays:


```
# Get multiple neurons from the neuronlist
nl[[1, 2]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>name</th>
      <th>id</th>
      <th>n_nodes</th>
      <th>n_connectors</th>
      <th>n_branches</th>
      <th>n_leafs</th>
      <th>cable_length</th>
      <th>soma</th>
      <th>units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>navis.TreeNeuron</td>
      <td>1734350908</td>
      <td>1734350908</td>
      <td>4845</td>
      <td>None</td>
      <td>733</td>
      <td>760</td>
      <td>304277.007958</td>
      <td>[6]</td>
      <td>8 nanometer</td>
    </tr>
    <tr>
      <th>1</th>
      <td>navis.TreeNeuron</td>
      <td>722817260</td>
      <td>722817260</td>
      <td>4336</td>
      <td>None</td>
      <td>635</td>
      <td>658</td>
      <td>274910.568784</td>
      <td>None</td>
      <td>8 nanometer</td>
    </tr>
  </tbody>
</table>
</div>




```
# Slicing is also supported
nl[1:3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>name</th>
      <th>id</th>
      <th>n_nodes</th>
      <th>n_connectors</th>
      <th>n_branches</th>
      <th>n_leafs</th>
      <th>cable_length</th>
      <th>soma</th>
      <th>units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>navis.TreeNeuron</td>
      <td>1734350908</td>
      <td>1734350908</td>
      <td>4845</td>
      <td>None</td>
      <td>733</td>
      <td>760</td>
      <td>304277.007958</td>
      <td>[6]</td>
      <td>8 nanometer</td>
    </tr>
    <tr>
      <th>1</th>
      <td>navis.TreeNeuron</td>
      <td>722817260</td>
      <td>722817260</td>
      <td>4336</td>
      <td>None</td>
      <td>635</td>
      <td>658</td>
      <td>274910.568784</td>
      <td>None</td>
      <td>8 nanometer</td>
    </tr>
  </tbody>
</table>
</div>



Strings will be matched against the neurons' names.


```
# Get neuron(s) by their name
nl['754534424']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>name</th>
      <th>id</th>
      <th>n_nodes</th>
      <th>n_connectors</th>
      <th>n_branches</th>
      <th>n_leafs</th>
      <th>cable_length</th>
      <th>soma</th>
      <th>units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>navis.TreeNeuron</td>
      <td>754534424</td>
      <td>754534424</td>
      <td>4702</td>
      <td>None</td>
      <td>697</td>
      <td>727</td>
      <td>286742.998887</td>
      <td>[4]</td>
      <td>8 nanometer</td>
    </tr>
  </tbody>
</table>
</div>



`neuronlists` have a special `.idx` indexer that let's you select neurons by their ID


```
# Get neuron(s) by their ID 
# -> note that for example neurons name == id 
nl.idx[[754534424, 722817260]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>name</th>
      <th>id</th>
      <th>n_nodes</th>
      <th>n_connectors</th>
      <th>n_branches</th>
      <th>n_leafs</th>
      <th>cable_length</th>
      <th>soma</th>
      <th>units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>navis.TreeNeuron</td>
      <td>754534424</td>
      <td>754534424</td>
      <td>4702</td>
      <td>None</td>
      <td>697</td>
      <td>727</td>
      <td>286742.998887</td>
      <td>[4]</td>
      <td>8 nanometer</td>
    </tr>
    <tr>
      <th>1</th>
      <td>navis.TreeNeuron</td>
      <td>722817260</td>
      <td>722817260</td>
      <td>4336</td>
      <td>None</td>
      <td>635</td>
      <td>658</td>
      <td>274910.568784</td>
      <td>None</td>
      <td>8 nanometer</td>
    </tr>
  </tbody>
</table>
</div>




```
# Access properties across neurons -> returns numpy arrays
nl.n_nodes 
```




    array([4465, 4845, 4336, 4702, 4890])




```

```


```
# Select neurons by given property
# -> this works with any boolean array 
nl[nl.n_nodes >= 4500]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>name</th>
      <th>id</th>
      <th>n_nodes</th>
      <th>n_connectors</th>
      <th>n_branches</th>
      <th>n_leafs</th>
      <th>cable_length</th>
      <th>soma</th>
      <th>units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>navis.TreeNeuron</td>
      <td>1734350908</td>
      <td>1734350908</td>
      <td>4845</td>
      <td>None</td>
      <td>733</td>
      <td>760</td>
      <td>304277.007958</td>
      <td>[6]</td>
      <td>8 nanometer</td>
    </tr>
    <tr>
      <th>1</th>
      <td>navis.TreeNeuron</td>
      <td>754534424</td>
      <td>754534424</td>
      <td>4702</td>
      <td>None</td>
      <td>697</td>
      <td>727</td>
      <td>286742.998887</td>
      <td>[4]</td>
      <td>8 nanometer</td>
    </tr>
    <tr>
      <th>2</th>
      <td>navis.TreeNeuron</td>
      <td>754538881</td>
      <td>754538881</td>
      <td>4890</td>
      <td>None</td>
      <td>626</td>
      <td>642</td>
      <td>291434.992623</td>
      <td>[703]</td>
      <td>8 nanometer</td>
    </tr>
  </tbody>
</table>
</div>



**Exercises**: 

1. Select the first and the last neuron in the neuronlist
2. Select all neurons with a soma 
3. Select all neurons with a soma and less than 300,000 cable length



```

```



Further reading: https://navis.readthedocs.io/en/latest/source/tutorials/neurons_intro.html

<a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=8708b017-8976-4124-8c35-604b1bd5dba6' target="_blank">
<img style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
