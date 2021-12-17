+++
title = "About"
date = "2021-12-17"
aliases = ["about-us","about-vfb","contact"]
[ author ]
  name = "Robert Court"
+++

What is Virtual Fly Brain?
--------------------------

Welcome to **Virtual Fly Brain (VFB)** - an interactive tool for neurobiologists to explore the detailed neuroanatomy, neuron connectivity and gene expression of _Drosophila melanogaster_. Our goal is to make it easier for researchers to find relevant anatomical information and reagents.

We integrate the neuroanatomical and expression data from the published literature, as well as image datasets onto the same brain template, making it possible to run cross searches, find similar neurons and compare image data on our [3D Viewer](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto).

The 3D Brain Viewer
-------------------

Using our [Viewer](/org.geppetto.frontend/geppetto), one can explore the anatomy, as well as view image stacks from datasets integrated by VFB. Any number of images can be displayed at the same time.

See [here]({{< ref "posts/content_report.md" >}} "Content Report") which image datasets are available on VFB.

The Viewer page is divided into 3 areas: the Stack Viewer and its navigation tools are on left; on the right hand side corresponds to the term info window, where information about a term will be shown and where further queries can be done from. The viewer menu with different tabs and functionalities is shown below the viewer.

![Main page](/images/vfb/project/viewer_intro.png)

The template brain (JFRC2) and painted domains stack we currently use are kindly provided by Arnim Jenett of [HHMI Janelia Research Campus](https://www.janelia.org/), and Kei Ito and Kazunori Shinomiya of [University of Tokyo](http://www.u-tokyo.ac.jp/en/index.html). The painted domain boundaries comply with the new BrainName's standard nomenclature [(Ito et al., 2014)](https://doi.org/10.1016/j.neuron.2013.12.017). It is available to download from [here](template_files_downloads.htm).

You can overlay any number of images stacks in our [Viewer](/org.geppetto.frontend/geppetto). And each display is associated to a URL which you can share with others

Below, is an example of an overlay of 3 image stacks and 2 neuropils. In green, a single neuron from the FlyCircuit dataset (Cha-F-500059); in dark blue the lineage clone LALv1 and in magenta the lineage clone DL1, both from Tzumin Lee's dataset. In addition to the image stacks, two neuropils are also selected: noduli (in yellow) and ellipsoid body (in light blue).

![Composite view](/images/vfb/project/composite.png)

What can I search for
---------------------

#### Simple queries

Searches for anatomical terms can be done from any page, using the search box in the header. The query options allow searches for neuron classes, or single neurons by location or connectivity, tracts, lineage, expression of transgenes and genes or phenotypes associated to a neuropil domain or neuron.  
Searches for similar neurons, individually or as a group, are also possible. These type of searches rely on [NBLAST](http://jefferislab.org/si/nblast/), a neuron similarity tool developed by Gregory Jefferis (Division of Neurobiology, MRC Laboratory of Molecular Biology) and described [here](https://doi.org/10.1016/j.neuron.2016.06.012).

The menu is context dependent, with the query options being different depending if the search starts from a neuron, brain region or single neuron image. The queries available are shown below.

![Query Menu](/images/vfb/project/bothmenus.png)

Searches for individual neuron images is also possible, with result lists displaying relevant neurons divided into precomputed groups of morphologically similar neurons (NBLAST tool developed by Gregory Jefferis, Division of Neurobiology, MRC Laboratory of Molecular Biology). This approach makes it easier to find a specific neuron, as well as all of the neurons of similar shape.

NBLAST searches can also be done on the fly, from single neuron images. Options available include searches for similar neurons and for GAL4 lines that might include the neuron of choice.

#### Advanced queries

The interactive [Query Builder](../tools/query_builder/index.htm) allows the building and execution of more complex queries. For example, to find neurons that innervate two different anatomical regions specifying the directionality of these connections.
