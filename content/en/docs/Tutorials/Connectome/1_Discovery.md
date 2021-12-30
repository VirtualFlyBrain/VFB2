---
title: "Discovery"
weight: 110
---


Required packages: vfb-connect and python-catmaid (pymaid & navis)


```python
!pip install vfb-connect --upgrade
!pip install python-catmaid --upgrade
```


### A note on using these notebooks
This is designed as an interactive tutorial. Feel free to add code cells below each example to try out variations of your own.

### How to find neurons across datasets

VirtualFlyBrain integrates images and connectomics profiles of neurons from many sources.  It classifies and records their properties using a standard, queryable classification ([The Drosophila Anatomy Ontology](https://www.ebi.ac.uk/ols/ontologies/fbbt)). This standardises the names of neuron types across sources, so you don't need to worry about differences in nomenclature uses and supports queries for neurons by their classification. 


```python
# Import libs and initialise API objects
from vfb_connect.cross_server_tools import VfbConnect
import pandas as pd
vc = VfbConnect()

import pymaid
import navis

navis.set_pbars(jupyter=False)
pymaid.set_pbars(jupyter=False)

# Connect to the VFB CATMAID server hosting the FAFB data
rm = pymaid.connect_catmaid(server="https://fafb.catmaid.virtualflybrain.org/", api_token=None, max_threads=10)

# Test call to see if connection works 
print(f'Server is running CATMAID version {rm.catmaid_version}')

```

    WARNING: Could not load OpenGL library.
    INFO  : Global CATMAID instance set. Caching is ON. (pymaid)
    Server is running CATMAID version 2020.02.15-905-g93a969b37


### Finds neurons by type (classification) across datasets

We can use the `vc.get_instances` method in combination with the name of a neuron type on VFB to find individual neurons from multiple sources.

Use the search tool on [VFB](http://virtualflybrain.org) to find neuron types by name or synonym:

<img src="https://user-images.githubusercontent.com/112839/109564687-535c9380-7ad9-11eb-80e9-5a5bc21cd915.png" width=30% height=30%>
<img src="https://user-images.githubusercontent.com/112839/109565128-eac1e680-7ad9-11eb-9649-1ec55a298a1b.png" width=30% height=30%>

Use either the full name or the Symbol to query for neurons:


```python
DA3adPN = vc.get_instances("adult Drosulfakinin neuron", summary=True)
pd.DataFrame.from_records(DA3adPN)
```




<div style="border: 1px solid grey; width: 100%; height: fit-content; overflow: auto;" >
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
      <th>label</th>
      <th>symbol</th>
      <th>id</th>
      <th>tags</th>
      <th>parents_label</th>
      <th>parents_id</th>
      <th>data_source</th>
      <th>accession</th>
      <th>templates</th>
      <th>dataset</th>
      <th>license</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DSKMP3_R - 327937328</td>
      <td></td>
      <td>VFB_jrchjti6</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult Drosulfakinin neuron</td>
      <td>FBbt_00048999</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>327937328</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DSKMP1A(PVM02)_L - 1260833150</td>
      <td></td>
      <td>VFB_jrchjti3</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult Drosulfakinin neuron</td>
      <td>FBbt_00048999</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1260833150</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>DSKMP3_R - 328559607</td>
      <td></td>
      <td>VFB_jrchjti7</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult Drosulfakinin neuron</td>
      <td>FBbt_00048999</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>328559607</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>DSKMP1B_R - 1352077058</td>
      <td></td>
      <td>VFB_jrchjti4</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult Drosulfakinin neuron</td>
      <td>FBbt_00048999</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1352077058</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DSKMP1B(PVM02)_L - 1011184205</td>
      <td></td>
      <td>VFB_jrchjti5</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult Drosulfakinin neuron</td>
      <td>FBbt_00048999</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1011184205</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>DSKMP1A_R - 1135837629</td>
      <td></td>
      <td>VFB_jrchjti2</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult Drosulfakinin neuron</td>
      <td>FBbt_00048999</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1135837629</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
  </tbody>
</table>
</div>



### Find neurons by location

We can use the same method to search for neurons by location, using simple queries.


```python
# Find neurons by location. The following query works across multiple data sources and both sides of the brain.  
# Results may be incomplete & may include minor overlap inferred from low synapse counts

neurons_in_DA3 = vc.get_instances("'neuron' that 'overlaps' some 'antennal lobe glomerulus DA3'", summary=True)
neurons_in_DA3_tab = pd.DataFrame.from_records(neurons_in_DA3)
neurons_in_DA3_tab[0:5]

```

    Running query: FBbt:00005106 that RO:0002131 some FBbt:00003934
    Query URL: http://owl.virtualflybrain.org/kbs/vfb/instances?object=FBbt%3A00005106+that+RO%3A0002131+some+FBbt%3A00003934&prefixes=%7B%22FBbt%22%3A+%22http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFBbt_%22%2C+%22RO%22%3A+%22http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FRO_%22%2C+%22BFO%22%3A+%22http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FBFO_%22%7D&direct=False
    Query results: 158





<div style="border: 1px solid grey; width: 100%; height: fit-content; overflow: auto;" >
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
      <th>label</th>
      <th>symbol</th>
      <th>id</th>
      <th>tags</th>
      <th>parents_label</th>
      <th>parents_id</th>
      <th>data_source</th>
      <th>accession</th>
      <th>templates</th>
      <th>dataset</th>
      <th>license</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>lLN2T_a(Tortuous)_R - 5813056598</td>
      <td></td>
      <td>VFB_jrchk8bi</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813056598</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ORN_DL3_R - 1671625186</td>
      <td></td>
      <td>VFB_jrchk1hj</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult olfactory receptor neuron Or65</td>
      <td>FBbt_00067011</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1671625186</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>DA4m_adPN_R - 574037266</td>
      <td></td>
      <td>VFB_jrchjtdq</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe projection neuron DA4m adPN</td>
      <td>FBbt_00047714</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>574037266</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Uniglomerular mALT DA3 adPN#L1 (FAFB:2449792)</td>
      <td></td>
      <td>VFB_0010123h</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe projection neuron DA3 adPN</td>
      <td>FBbt_00100384</td>
      <td>catmaid_fafb</td>
      <td>2449792</td>
      <td>JRC2018Unisex</td>
      <td>BatesSchlegel2020</td>
      <td>https://creativecommons.org/licenses/by-sa/4.0...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>lLN2T_e(Tortuous)_R - 1699974843</td>
      <td></td>
      <td>VFB_jrchk8br</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1699974843</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Find local interneurons (intrinsic neurons) of the AL, overlapping DA3:

local_in_DA3 = vc.get_instances("'local interneuron of adult antennal lobe' that 'overlaps' some 'antennal lobe glomerulus DA3'",
                                summary=True)
local_in_DA3_tab = pd.DataFrame.from_records(local_in_DA3)
local_in_DA3_tab
```

    Running query: FBbt:00007390 that RO:0002131 some FBbt:00003934
    Query URL: http://owl.virtualflybrain.org/kbs/vfb/instances?object=FBbt%3A00007390+that+RO%3A0002131+some+FBbt%3A00003934&prefixes=%7B%22FBbt%22%3A+%22http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFBbt_%22%2C+%22RO%22%3A+%22http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FRO_%22%2C+%22BFO%22%3A+%22http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FBFO_%22%7D&direct=False
    Query results: 53





<div style="border: 1px solid grey; width: 100%; height: fit-content; overflow: auto;" >
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
      <th>label</th>
      <th>symbol</th>
      <th>id</th>
      <th>tags</th>
      <th>parents_label</th>
      <th>parents_id</th>
      <th>data_source</th>
      <th>accession</th>
      <th>templates</th>
      <th>dataset</th>
      <th>license</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>lLN16b_R - 1887168462</td>
      <td></td>
      <td>VFB_jrchk89w</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1887168462</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>lLN1_c_R - 5813047691</td>
      <td></td>
      <td>VFB_jrchk8ae</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813047691</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>lLN2S(Star)_R - 1670627928</td>
      <td></td>
      <td>VFB_jrchk8bb</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2S</td>
      <td>FBbt_00049815</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1670627928</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lLN2F_b(Full)_R - 5813024698</td>
      <td></td>
      <td>VFB_jrchk8an</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2F</td>
      <td>FBbt_00049812</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813024698</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>lLN2T_c(Tortuous)_R - 1671292719</td>
      <td></td>
      <td>VFB_jrchk8bo</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1671292719</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>lLN1_c_R - 5813062199</td>
      <td></td>
      <td>VFB_jrchk8af</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813062199</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>lLN1_a_R - 5813130064</td>
      <td></td>
      <td>VFB_jrchk8a4</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813130064</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>lLN1_c_R - 1702651358</td>
      <td></td>
      <td>VFB_jrchk8aj</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1702651358</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>lLN2T_e(Tortuous)_R - 1640922516</td>
      <td></td>
      <td>VFB_jrchk8bs</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1640922516</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>lLN11_R - 1670278227</td>
      <td></td>
      <td>VFB_jrchk89e</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1670278227</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>lLN2P_c(Patchy)_R - 2105086391</td>
      <td></td>
      <td>VFB_jrchk8b0</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2P</td>
      <td>FBbt_00049813</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>2105086391</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>lLN2T_b(Tortuous)_R - 1640572741</td>
      <td></td>
      <td>VFB_jrchk8bl</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1640572741</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>lLN1_c_R - 1578826464</td>
      <td></td>
      <td>VFB_jrchk8ah</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1578826464</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>lLN2P_a(Patchy)_R - 2041621893</td>
      <td></td>
      <td>VFB_jrchk8ao</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2P</td>
      <td>FBbt_00049813</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>2041621893</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>lLN2S(Star)_R - 1762359683</td>
      <td></td>
      <td>VFB_jrchk8bc</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2S</td>
      <td>FBbt_00049815</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1762359683</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>lLN1_b_R - 5813054622</td>
      <td></td>
      <td>VFB_jrchk8a8</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813054622</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>lLN2F_a(Full)_R - 1670287030</td>
      <td></td>
      <td>VFB_jrchk8al</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2F</td>
      <td>FBbt_00049812</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1670287030</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>lLN12a_R - 1826445251</td>
      <td></td>
      <td>VFB_jrchk89g</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1826445251</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>lLN11_R - 2040301572</td>
      <td></td>
      <td>VFB_jrchk89d</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>2040301572</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>il3LN6_R - 5813018460</td>
      <td></td>
      <td>VFB_jrchk88v</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>local interneuron of adult antennal lobe</td>
      <td>FBbt_00007390</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813018460</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>lLN2R_b(Regional)_R - 5813076969</td>
      <td></td>
      <td>VFB_jrchk8b6</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2R</td>
      <td>FBbt_00049814</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813076969</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>lLN16a_R - 1702318692</td>
      <td></td>
      <td>VFB_jrchk89t</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1702318692</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>lLN2T_d(Tortuous)_R - 1667251683</td>
      <td></td>
      <td>VFB_jrchk8bp</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1667251683</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>lLN2R_b(Regional)_R - 1702305987</td>
      <td></td>
      <td>VFB_jrchk8b5</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2R</td>
      <td>FBbt_00049814</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1702305987</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>v2LN35_R - 1733056086</td>
      <td></td>
      <td>VFB_jrchk8ew</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>local interneuron of adult antennal lobe</td>
      <td>FBbt_00007390</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1733056086</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>lLN1_b_R - 1610530558</td>
      <td></td>
      <td>VFB_jrchk8ac</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1610530558</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>lLN2S(Star)_R - 1640922754</td>
      <td></td>
      <td>VFB_jrchk8b8</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2S</td>
      <td>FBbt_00049815</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1640922754</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>lLN1_c_R - 1824101645</td>
      <td></td>
      <td>VFB_jrchk8ag</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1824101645</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>lLN1_c_R - 1547454812</td>
      <td></td>
      <td>VFB_jrchk8ai</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1547454812</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>lLN1_b_R - 5813069055</td>
      <td></td>
      <td>VFB_jrchk8aa</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069055</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>lLN1_b_R - 1642623277</td>
      <td></td>
      <td>VFB_jrchk8ad</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1642623277</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>lLN2T_a(Tortuous)_R - 5813054726</td>
      <td></td>
      <td>VFB_jrchk8bh</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813054726</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>lLN2F_b(Full)_R - 1640909284</td>
      <td></td>
      <td>VFB_jrchk8am</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2F</td>
      <td>FBbt_00049812</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1640909284</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>lLN2F_a(Full)_R - 5901218894</td>
      <td></td>
      <td>VFB_jrchk8ak</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2F</td>
      <td>FBbt_00049812</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5901218894</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>lLN2T_e(Tortuous)_R - 1699974843</td>
      <td></td>
      <td>VFB_jrchk8br</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1699974843</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>lLN10_R - 1825789179</td>
      <td></td>
      <td>VFB_jrchk89b</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1825789179</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>lLN2S(Star)_R - 1702306037</td>
      <td></td>
      <td>VFB_jrchk8b7</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2S</td>
      <td>FBbt_00049815</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1702306037</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>37</th>
      <td>lLN2S(Star)_R - 1732995501</td>
      <td></td>
      <td>VFB_jrchk8ba</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2S</td>
      <td>FBbt_00049815</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1732995501</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>38</th>
      <td>lLN2S(Star)_R - 5813069085</td>
      <td></td>
      <td>VFB_jrchk8b9</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2S</td>
      <td>FBbt_00049815</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069085</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>v2LN3b_R - 1888199872</td>
      <td></td>
      <td>VFB_jrchk8fg</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>local interneuron of adult antennal lobe</td>
      <td>FBbt_00007390</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1888199872</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>40</th>
      <td>lLN1_b_R - 1640887603</td>
      <td></td>
      <td>VFB_jrchk8a6</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1640887603</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>lLN1_b_R - 5813078440</td>
      <td></td>
      <td>VFB_jrchk8a7</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813078440</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>42</th>
      <td>lLN2T_b(Tortuous)_R - 5813034493</td>
      <td></td>
      <td>VFB_jrchk8bm</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813034493</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>lLN1_b_R - 5813054777</td>
      <td></td>
      <td>VFB_jrchk8a9</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813054777</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>44</th>
      <td>v2LN30_R - 1671620613</td>
      <td></td>
      <td>VFB_jrchk8e8</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>local interneuron of adult antennal lobe</td>
      <td>FBbt_00007390</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1671620613</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>45</th>
      <td>v2LN3b_R - 5813034455</td>
      <td></td>
      <td>VFB_jrchk8ff</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>local interneuron of adult antennal lobe</td>
      <td>FBbt_00007390</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813034455</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>46</th>
      <td>lLN2T_a(Tortuous)_R - 5813032595</td>
      <td></td>
      <td>VFB_jrchk8bd</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813032595</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>47</th>
      <td>lLN2T_a(Tortuous)_R - 5813056598</td>
      <td></td>
      <td>VFB_jrchk8bi</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813056598</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>48</th>
      <td>lLN1_b_R - 5813054725</td>
      <td></td>
      <td>VFB_jrchk8ab</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult local interneuron of the lateral ALl1 ne...</td>
      <td>FBbt_00007394</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813054725</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>49</th>
      <td>lLN2P_b(Patchy)_R - 1946178096</td>
      <td></td>
      <td>VFB_jrchk8au</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2P</td>
      <td>FBbt_00049813</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1946178096</td>
      <td>JRC2018Unisex|JRC_FlyEM_Hemibrain</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>50</th>
      <td>lLN2T_a(Tortuous)_R - 5813055277</td>
      <td></td>
      <td>VFB_jrchk8bf</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813055277</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>51</th>
      <td>l2LN18_R - 5813054773</td>
      <td></td>
      <td>VFB_jrchk891</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>local interneuron of adult antennal lobe</td>
      <td>FBbt_00007390</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813054773</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
    <tr>
      <th>52</th>
      <td>lLN2T_a(Tortuous)_R - 1762354941</td>
      <td></td>
      <td>VFB_jrchk8bg</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult antennal lobe lateral local neuron 2T</td>
      <td>FBbt_00049816</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1762354941</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Find neurons by dataset/paper - on CATMAID

bates = pymaid.find_neurons(annotations='Paper: Bates and Schlegel et al 2020')
bates
```

    INFO  : Found 583 neurons matching the search parameters (pymaid)





<div style="border: 1px solid grey; width: 100%; height: fit-content; overflow: auto;" >
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
      <th>skeleton_id</th>
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
      <td>CatmaidNeuron</td>
      <td>Uniglomerular mALT DA1 lPN 57316 2863105 ML</td>
      <td>2863104</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>1 nanometer</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CatmaidNeuron</td>
      <td>Uniglomerular mALT DA3 adPN 57350 HG</td>
      <td>57349</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>1 nanometer</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>581</th>
      <td>CatmaidNeuron</td>
      <td>Multiglomerular mlALT vPN VM7d+VM5d+DC4+6 LTS ...</td>
      <td>4624378</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>1 nanometer</td>
    </tr>
    <tr>
      <th>582</th>
      <td>CatmaidNeuron</td>
      <td>Uniglomerular mALT DL2d adPN 57342 ML</td>
      <td>57341</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>1 nanometer</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Inspect what datasets are available on VFB

ds = vc.neo_query_wrapper.get_datasets(summary=True)
ds_tab = pd.DataFrame.from_records(ds)
ds_tab.sort_values(by=['id'])
```




<div style="border: 1px solid grey; width: 100%; height: fit-content; overflow: auto;" >
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
      <th>label</th>
      <th>symbol</th>
      <th>id</th>
      <th>tags</th>
      <th>description</th>
      <th>miniref</th>
      <th>FlyBase</th>
      <th>PMID</th>
      <th>DOI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>81</th>
      <td>EM L1 Andrade et al. 2019</td>
      <td></td>
      <td>Andrade2019</td>
      <td>Entity|Individual|DataSet</td>
      <td>[L1 EM reconstructed neurons from Andrade et a...</td>
      <td>Andrade et al., 2019, Curr. Biol. 29(3): 412--...</td>
      <td>FBrf0241389</td>
      <td>30661802</td>
      <td>10.1016/j.cub.2018.12.012</td>
    </tr>
    <tr>
      <th>16</th>
      <td>MBONs and split-GAL4 lines that target them (A...</td>
      <td></td>
      <td>Aso2014</td>
      <td>Entity|Individual|DataSet</td>
      <td>[]</td>
      <td>Aso et al., 2014, eLife 3: e04577</td>
      <td>FBrf0227179</td>
      <td>25535793</td>
      <td>10.7554/eLife.04577</td>
    </tr>
    <tr>
      <th>19</th>
      <td>split-GAL4 lines for dopaminergic neurons (Aso...</td>
      <td></td>
      <td>AsoRubin2016</td>
      <td>Entity|Individual|DataSet</td>
      <td>[For comparison of the properties of memories ...</td>
      <td>Aso and Rubin, 2016, eLife 5: e16135</td>
      <td>FBrf0233230</td>
      <td>27441388</td>
      <td>10.7554/eLife.16135</td>
    </tr>
    <tr>
      <th>52</th>
      <td>EM FAFB Bates and Schlegel et al 2020</td>
      <td></td>
      <td>BatesSchlegel2020</td>
      <td>Entity|Individual|DataSet</td>
      <td>[FAFB EM reconstructed neurons from Bates and ...</td>
      <td>Bates and Schlegel et al., 2020</td>
      <td></td>
      <td></td>
      <td>10.1016/j.cub.2020.06.042</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Larval olfactory system neurons - EM (Berk2016)</td>
      <td></td>
      <td>Berck2016</td>
      <td>Entity|Individual|DataSet</td>
      <td>[Berck, Khandelwal et al. 2016]</td>
      <td>Berck et al., 2016, eLife 5: e14859</td>
      <td>FBrf0232785</td>
      <td>27177418</td>
      <td>10.7554/eLife.14859</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Lee lab adult brain lineage clone image set</td>
      <td></td>
      <td>Yu2013</td>
      <td>Entity|Individual|DataSet</td>
      <td>[An exhaustive set of lineage clones covering ...</td>
      <td>Yu et al., 2013, Curr. Biol. 23(8): 633--643</td>
      <td>FBrf0221412</td>
      <td>23541733</td>
      <td>10.1016/j.cub.2013.02.057</td>
    </tr>
    <tr>
      <th>15</th>
      <td>EM L1 Zarin, Mark et al. 2019</td>
      <td></td>
      <td>Zarin2019</td>
      <td>Entity|Individual|DataSet</td>
      <td>[L1 EM reconstructed neurons from Zarin, Mark ...</td>
      <td>Zarin, Mark et al., 2019</td>
      <td></td>
      <td></td>
      <td>10.1101/617977</td>
    </tr>
    <tr>
      <th>48</th>
      <td>EM FAFB Zheng et al 2018</td>
      <td></td>
      <td>Zheng2018</td>
      <td>Entity|Individual|DataSet</td>
      <td>[FAFB EM reconstructed neurons from Zheng et a...</td>
      <td>Zheng et al., 2018, Cell 174(3): 730--743.e22</td>
      <td>FBrf0239557</td>
      <td>30033368</td>
      <td>10.1016/j.cell.2018.06.019</td>
    </tr>
    <tr>
      <th>34</th>
      <td>EM FAFB Zheng et al 2020</td>
      <td></td>
      <td>Zheng2020</td>
      <td>Entity|Individual|DataSet</td>
      <td>[FAFB EM reconstructed neurons from Zheng et a...</td>
      <td>Zheng et al. 2020</td>
      <td></td>
      <td></td>
      <td>10.1101/2020.04.17.047167</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Larval motor circuit neurons (Zwart2016)</td>
      <td></td>
      <td>Zwart2016</td>
      <td>Entity|Individual|DataSet</td>
      <td>[Zwart et al. 2016]</td>
      <td>Zwart et al., 2016, Neuron 91(3): 615--628</td>
      <td>FBrf0233076</td>
      <td>27427461</td>
      <td>10.1016/j.neuron.2016.06.031</td>
    </tr>
  </tbody>
</table>
<p>83 rows × 9 columns</p>
</div>




```python
sayin_tab = pd.DataFrame.from_records(vc.get_instances_by_dataset('Sayin2019', summary=True))
sayin_tab
```




<div style="border: 1px solid grey; width: 100%; height: fit-content; overflow: auto;" >
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
      <th>label</th>
      <th>symbol</th>
      <th>id</th>
      <th>tags</th>
      <th>parents_label</th>
      <th>parents_id</th>
      <th>data_source</th>
      <th>accession</th>
      <th>templates</th>
      <th>dataset</th>
      <th>license</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OA-VPM3 (FAFB:1329078)</td>
      <td></td>
      <td>VFB_001001dr</td>
      <td>Entity|Octopaminergic|Adult|Anatomy|has_image|...</td>
      <td>octopaminergic VPM3 neuron</td>
      <td>FBbt_00110151</td>
      <td>catmaid_fafb</td>
      <td>1329078</td>
      <td>JRC2018Unisex</td>
      <td>Sayin2019</td>
      <td>https://creativecommons.org/licenses/by-sa/4.0...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>OA-VPM4 (FAFB:1191261)</td>
      <td></td>
      <td>VFB_001001dq</td>
      <td>Entity|Octopaminergic|Adult|Anatomy|has_image|...</td>
      <td>octopaminergic VPM4 neuron</td>
      <td>FBbt_00110152</td>
      <td>catmaid_fafb</td>
      <td>1191261</td>
      <td>JRC2018Unisex</td>
      <td>Sayin2019</td>
      <td>https://creativecommons.org/licenses/by-sa/4.0...</td>
    </tr>
  </tbody>
</table>
</div>




```python
vc.get_connected_neurons_by_type(upstream_type='LNd', downstream_type='adult descending neuron', weight=20)
```




<div style="border: 1px solid grey; width: 100%; height: fit-content; overflow: auto;" >
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
      <th>upstream_neuron_id</th>
      <th>upstream_neuron_name</th>
      <th>weight</th>
      <th>downstream_neuron_id</th>
      <th>downstream_neuron_name</th>
      <th>upstream_class</th>
      <th>downstream_class</th>
      <th>up_data_source</th>
      <th>up_accession</th>
      <th>down_source</th>
      <th>down_accession</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>VFB_jrchjzxx</td>
      <td>LNd_R - 5813021192</td>
      <td>25</td>
      <td>VFB_jrchjthm</td>
      <td>DNp27_R - 1072063538</td>
      <td>LNd neuron</td>
      <td>descending neuron of the posterior brain DNp27</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813021192</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1072063538</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Intra pacemaker neuron neuron connections

vc.get_connected_neurons_by_type(upstream_type='pacemaker neuron', downstream_type='pacemaker neuron', weight=20)
```




<div style="border: 1px solid grey; width: 100%; height: fit-content; overflow: auto;" >
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
      <th>upstream_neuron_id</th>
      <th>upstream_neuron_name</th>
      <th>weight</th>
      <th>downstream_neuron_id</th>
      <th>downstream_neuron_name</th>
      <th>upstream_class</th>
      <th>downstream_class</th>
      <th>up_data_source</th>
      <th>up_accession</th>
      <th>down_source</th>
      <th>down_accession</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>VFB_jrchjzxy</td>
      <td>LNd_R - 5813069648</td>
      <td>37</td>
      <td>VFB_jrchk8e0</td>
      <td>5th s-LNv - 511051477</td>
      <td>LNd neuron</td>
      <td>s-LNv neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069648</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>511051477</td>
    </tr>
    <tr>
      <th>1</th>
      <td>VFB_jrchk089</td>
      <td>LPN_R - 480029788</td>
      <td>43</td>
      <td>VFB_jrchk08a</td>
      <td>LPN_R - 450034902</td>
      <td>LP neuron</td>
      <td>LP neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>480029788</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>450034902</td>
    </tr>
    <tr>
      <th>2</th>
      <td>VFB_jrchjtf0</td>
      <td>DN1pA_R - 324846570</td>
      <td>25</td>
      <td>VFB_jrchk8e0</td>
      <td>5th s-LNv - 511051477</td>
      <td>DN1p neuron</td>
      <td>s-LNv neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>324846570</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>511051477</td>
    </tr>
    <tr>
      <th>3</th>
      <td>VFB_jrchjtf0</td>
      <td>DN1pA_R - 324846570</td>
      <td>37</td>
      <td>VFB_jrchjzxy</td>
      <td>LNd_R - 5813069648</td>
      <td>DN1p neuron</td>
      <td>LNd neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>324846570</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069648</td>
    </tr>
    <tr>
      <th>4</th>
      <td>VFB_jrchk8e0</td>
      <td>5th s-LNv - 511051477</td>
      <td>40</td>
      <td>VFB_jrchjzxy</td>
      <td>LNd_R - 5813069648</td>
      <td>s-LNv neuron</td>
      <td>LNd neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>511051477</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069648</td>
    </tr>
    <tr>
      <th>5</th>
      <td>VFB_jrchjtf3</td>
      <td>DN1pA_R - 387166379</td>
      <td>25</td>
      <td>VFB_jrchk8e0</td>
      <td>5th s-LNv - 511051477</td>
      <td>DN1p neuron</td>
      <td>s-LNv neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>387166379</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>511051477</td>
    </tr>
    <tr>
      <th>6</th>
      <td>VFB_jrchjtf1</td>
      <td>DN1pA_R - 325529237</td>
      <td>30</td>
      <td>VFB_jrchjzxy</td>
      <td>LNd_R - 5813069648</td>
      <td>DN1p neuron</td>
      <td>LNd neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>325529237</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069648</td>
    </tr>
    <tr>
      <th>7</th>
      <td>VFB_jrchk8e0</td>
      <td>5th s-LNv - 511051477</td>
      <td>25</td>
      <td>VFB_jrchjzxx</td>
      <td>LNd_R - 5813021192</td>
      <td>s-LNv neuron</td>
      <td>LNd neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>511051477</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813021192</td>
    </tr>
    <tr>
      <th>8</th>
      <td>VFB_jrchjtez</td>
      <td>DN1pA_R - 5813010153</td>
      <td>25</td>
      <td>VFB_jrchk8e0</td>
      <td>5th s-LNv - 511051477</td>
      <td>DN1p neuron</td>
      <td>s-LNv neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813010153</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>511051477</td>
    </tr>
    <tr>
      <th>9</th>
      <td>VFB_jrchjzxy</td>
      <td>LNd_R - 5813069648</td>
      <td>29</td>
      <td>VFB_jrchjzxw</td>
      <td>LNd_R - 5813056917</td>
      <td>LNd neuron</td>
      <td>LNd neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069648</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813056917</td>
    </tr>
    <tr>
      <th>10</th>
      <td>VFB_jrchjtf2</td>
      <td>DN1pA_R - 387944118</td>
      <td>22</td>
      <td>VFB_jrchk8e0</td>
      <td>5th s-LNv - 511051477</td>
      <td>DN1p neuron</td>
      <td>s-LNv neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>387944118</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>511051477</td>
    </tr>
    <tr>
      <th>11</th>
      <td>VFB_jrchjtf2</td>
      <td>DN1pA_R - 387944118</td>
      <td>34</td>
      <td>VFB_jrchjzxy</td>
      <td>LNd_R - 5813069648</td>
      <td>DN1p neuron</td>
      <td>LNd neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>387944118</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069648</td>
    </tr>
    <tr>
      <th>12</th>
      <td>VFB_jrchjtf1</td>
      <td>DN1pA_R - 325529237</td>
      <td>33</td>
      <td>VFB_jrchk8e0</td>
      <td>5th s-LNv - 511051477</td>
      <td>DN1p neuron</td>
      <td>s-LNv neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>325529237</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>511051477</td>
    </tr>
    <tr>
      <th>13</th>
      <td>VFB_jrchk08a</td>
      <td>LPN_R - 450034902</td>
      <td>30</td>
      <td>VFB_jrchk089</td>
      <td>LPN_R - 480029788</td>
      <td>LP neuron</td>
      <td>LP neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>450034902</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>480029788</td>
    </tr>
    <tr>
      <th>14</th>
      <td>VFB_jrchjtey</td>
      <td>DN1a_R - 5813022274</td>
      <td>63</td>
      <td>VFB_jrchk8e0</td>
      <td>5th s-LNv - 511051477</td>
      <td>DN1a neuron</td>
      <td>s-LNv neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813022274</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>511051477</td>
    </tr>
    <tr>
      <th>15</th>
      <td>VFB_jrchjtex</td>
      <td>DN1a_R - 264083994</td>
      <td>55</td>
      <td>VFB_jrchk8e0</td>
      <td>5th s-LNv - 511051477</td>
      <td>DN1a neuron</td>
      <td>s-LNv neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>264083994</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>511051477</td>
    </tr>
    <tr>
      <th>16</th>
      <td>VFB_jrchjtey</td>
      <td>DN1a_R - 5813022274</td>
      <td>75</td>
      <td>VFB_jrchjzxy</td>
      <td>LNd_R - 5813069648</td>
      <td>DN1a neuron</td>
      <td>LNd neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813022274</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069648</td>
    </tr>
    <tr>
      <th>17</th>
      <td>VFB_jrchjtex</td>
      <td>DN1a_R - 264083994</td>
      <td>79</td>
      <td>VFB_jrchjzxy</td>
      <td>LNd_R - 5813069648</td>
      <td>DN1a neuron</td>
      <td>LNd neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>264083994</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069648</td>
    </tr>
    <tr>
      <th>18</th>
      <td>VFB_jrchjtf3</td>
      <td>DN1pA_R - 387166379</td>
      <td>30</td>
      <td>VFB_jrchjzxy</td>
      <td>LNd_R - 5813069648</td>
      <td>DN1p neuron</td>
      <td>LNd neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>387166379</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069648</td>
    </tr>
    <tr>
      <th>19</th>
      <td>VFB_jrchjzxy</td>
      <td>LNd_R - 5813069648</td>
      <td>21</td>
      <td>VFB_jrchjzxx</td>
      <td>LNd_R - 5813021192</td>
      <td>LNd neuron</td>
      <td>LNd neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813069648</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813021192</td>
    </tr>
  </tbody>
</table>
</div>




```python

vc.get_connected_neurons_by_type(upstream_type='adult neuron', downstream_type='adult Drosulfakinin neuron', weight=20)
```




<div style="border: 1px solid grey; width: 100%; height: fit-content; overflow: auto;" >
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
      <th>upstream_neuron_id</th>
      <th>upstream_neuron_name</th>
      <th>weight</th>
      <th>downstream_neuron_id</th>
      <th>downstream_neuron_name</th>
      <th>upstream_class</th>
      <th>downstream_class</th>
      <th>up_data_source</th>
      <th>up_accession</th>
      <th>down_source</th>
      <th>down_accession</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>VFB_jrchjsj3</td>
      <td>AstA1_L - 362473525</td>
      <td>28</td>
      <td>VFB_jrchjti4</td>
      <td>DSKMP1B_R - 1352077058</td>
      <td>adult neuron</td>
      <td>adult Drosulfakinin neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>362473525</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1352077058</td>
    </tr>
    <tr>
      <th>1</th>
      <td>VFB_jrchk5zh</td>
      <td>SLP384_R - 482702027</td>
      <td>20</td>
      <td>VFB_jrchjti6</td>
      <td>DSKMP3_R - 327937328</td>
      <td>adult superior lateral protocerebrum neuron 384</td>
      <td>adult Drosulfakinin neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>482702027</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>327937328</td>
    </tr>
    <tr>
      <th>2</th>
      <td>VFB_jrchjrjn</td>
      <td>AVLP001_R - 1321564092</td>
      <td>26</td>
      <td>VFB_jrchjti2</td>
      <td>DSKMP1A_R - 1135837629</td>
      <td>adult anterior ventrolateral protocerebrum neu...</td>
      <td>adult Drosulfakinin neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1321564092</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1135837629</td>
    </tr>
    <tr>
      <th>3</th>
      <td>VFB_jrchk5eo</td>
      <td>SLP066_R - 327843160</td>
      <td>42</td>
      <td>VFB_jrchjti4</td>
      <td>DSKMP1B_R - 1352077058</td>
      <td>adult superior lateral protocerebrum neuron 066</td>
      <td>adult Drosulfakinin neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>327843160</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1352077058</td>
    </tr>
    <tr>
      <th>4</th>
      <td>VFB_jrchk5qf</td>
      <td>SLP244_R - 298214577</td>
      <td>27</td>
      <td>VFB_jrchjti6</td>
      <td>DSKMP3_R - 327937328</td>
      <td>adult superior lateral protocerebrum neuron 244</td>
      <td>adult Drosulfakinin neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>298214577</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>327937328</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>56</th>
      <td>VFB_jrchk6zu</td>
      <td>SMP449_R - 5813026592</td>
      <td>25</td>
      <td>VFB_jrchjti4</td>
      <td>DSKMP1B_R - 1352077058</td>
      <td>adult superior medial protocerebrum neuron 449</td>
      <td>adult Drosulfakinin neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>5813026592</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1352077058</td>
    </tr>
    <tr>
      <th>57</th>
      <td>VFB_jrchk5jv</td>
      <td>SLP152_R - 487812620</td>
      <td>28</td>
      <td>VFB_jrchjti4</td>
      <td>DSKMP1B_R - 1352077058</td>
      <td>adult superior lateral protocerebrum neuron 152</td>
      <td>adult Drosulfakinin neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>487812620</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1352077058</td>
    </tr>
    <tr>
      <th>58</th>
      <td>VFB_jrchjrxe</td>
      <td>AVLP223_R - 1356743512</td>
      <td>27</td>
      <td>VFB_jrchjti2</td>
      <td>DSKMP1A_R - 1135837629</td>
      <td>adult anterior ventrolateral protocerebrum neu...</td>
      <td>adult Drosulfakinin neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1356743512</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1135837629</td>
    </tr>
    <tr>
      <th>59</th>
      <td>VFB_jrchk5qg</td>
      <td>SLP244_R - 297533212</td>
      <td>33</td>
      <td>VFB_jrchjti6</td>
      <td>DSKMP3_R - 327937328</td>
      <td>adult superior lateral protocerebrum neuron 244</td>
      <td>adult Drosulfakinin neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>297533212</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>327937328</td>
    </tr>
    <tr>
      <th>60</th>
      <td>VFB_jrchk6g5</td>
      <td>SMP157_R - 421041565</td>
      <td>32</td>
      <td>VFB_jrchjti4</td>
      <td>DSKMP1B_R - 1352077058</td>
      <td>adult superior medial protocerebrum neuron 157</td>
      <td>adult Drosulfakinin neuron</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>421041565</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1352077058</td>
    </tr>
  </tbody>
</table>
<p>61 rows × 11 columns</p>
</div>





