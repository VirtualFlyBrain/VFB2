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


```python
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


```python
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


```python
# Current root node of this neuron
n.root
```




    array([1], dtype=int32)



Some of the properties such as `.root` or `.ends` are computed on-the-fly from the underlying raw data. For `TreeNeurons` that's the node table (and it's graph representation). The node table is a pandas DataFrame that looks effectively like a SWC:


```python
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


```python
# Reroot neuron to another node
n2 = n.reroot(new_root=2)
# Print the new root -> expect "2"
n2.root
```




    array([2])




```python
# Instead of calling the shorthand method, we can also do this
n3 = navis.reroot_neuron(n, new_root=2)
n3.root
```




    array([2])



## NeuronLists
In practice you will likely work with multiple neurons at a time. For that, `navis` has a convenient container: `NeuronLists`


```python
# Get more than one example neuron
nl = navis.example_neurons(5)

# `nl` is a NeuronList 
type(nl)
```




    navis.core.neuronlist.NeuronList




```python
# You can also create neuron lists yourself
my_nl = navis.NeuronList(n)
```

In many ways `NeuronLists` work like Python-lists with a couple of extras: 


```python
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




```python
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


```python
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




```python
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


```python
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


```python
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




```python
# Access properties across neurons -> returns numpy arrays
nl.n_nodes 
```




    array([4465, 4845, 4336, 4702, 4890])




```python

```


```python
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






Further reading: [https://navis.readthedocs.io/en/latest/source/tutorials/neurons_intro.html](https://navis.readthedocs.io/en/latest/source/tutorials/neurons_intro.html)

