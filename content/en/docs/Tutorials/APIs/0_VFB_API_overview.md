---
title: "VFB connect API overview"
weight: 100
series: ["APIs"]
alias: ["/docs/tutorials/0_vfb_api_overview/"]
date: 2021-12-27
description: >
  The VFB connect API provides programmatic access to the databases underlying VFB
---


### VFB connect API overview

The VFB connect API provides programmatic access to the databases underlying [Virtual Fly Brain](http://virtualflybrain.org). 

At the core of Virtual Fly Brain is a set of curated terms for Drosophila neuro-anatomy organised into a queryable classification, including terms for brain regions, e.g. [nodulus](http://virtualflybrain.org/reports/FBbt_00003680) and neurons e.g. [MBON01](http://virtualflybrain.org/reports/FBbt_00100234). These terms are used to annotate and classify individual brain regions and neurons in images and connectomics data. For example the term MBON01 is used to classify individual [neurons from sources including the CATMAID-FAFB and Neuprint-HemiBrain databases](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?q=FBbt_00100234,ListAllAvailableImages). VFB stores both [registered 3D images](http://virtualflybrain.org/reports/VFB_00101382) and [connectomics data](https://v2-dev.virtualflybrain.org/org.geppetto.frontend/geppetto?q=VFB_00101382,ref_neuron_neuron_connectivity_query) (where available) for all of these neurons.

A single VfbConnect object wraps connections and canned queries against all open VFB databases. It includes methods for retreiving metadata about anatomy, individual brain regions and neurons including IDs for these that can be used for queries against other databases (e.g. CATMAID & neuprint).  It provides methods for downloading images and connectomics data. It provides access to sophisticated queries for anatomical classes and individual neurons accoring to their classification & properties. 

### Locations for methods under a `VfbConnect` object.

1. Under `vc.neo_query_wrapper` are 
   1. A set of methods that take lists of IDs as a primary argument and return metadata. 
   2. A set of methods for mapping between VFB IDs and external IDs
2. Directly under `vc` are:
    1. A set of methods that take the names of classes in VFB e.g. 'nodulus' or 'Kenyon cell', or simple query expressions using the names of classes and return metadata about the classes.
    2. A set methods for querying connectivity and similarity
3. Direct access to API queries is provided under the 'nc' and 'oc' attributes for Neo4J and OWL queries respectively. We will not cover details of how to use these here.

Note: available methods and their documentation are easy to explore in DeepNote. Tab completion and type adhead can be used to help find methods. Float your cursor over a method to see its signature and docstring. 

### 1. `vc.neo_query_wrapper` methods overview

**1.1** `vc.neo_query_wrapper` TermInfo queries return the results of a VFB Term Information window as JSON, following the [VFB_JSON standard](), or a summary that can easily be converted into a DataFrame.


```python
# A query for full TermInfo.  This probably produces more information than you will need for most purposes.

vc.neo_query_wrapper.get_type_TermInfo(['FBbt_00003686'])
```




    [{'term': {'core': {'iri': 'http://purl.obolibrary.org/obo/FBbt_00003686',
        'symbol': '',
        'types': ['Entity',
         'Anatomy',
         'Nervous_system',
         'Cell',
         'Neuron',
         'Class'],
        'label': 'Kenyon cell',
        'short_form': 'FBbt_00003686'},
       'description': ['Intrinsic neuron of the mushroom body. They have tightly-packed cell bodies, situated in the rind above the calyx of the mushroom body (Ito et al., 1997). Four short fascicles, one per lineage, extend from the cell bodies of the Kenyon cells into the calyx (Ito et al., 1997). These 4 smaller fascicles converge in the calyx where they arborize and form pre- and post-synaptic terminals (Christiansen et al., 2011), with different Kenyon cells receiving input in different calyx regions/accessory calyces (Tanaka et al., 2008). They emerge from the calyx as a thick axon bundle referred to as the peduncle that bifurcates to innervate the dorsal and medial lobes of the mushroom body (Tanaka et al., 2008).'],
       'comment': ['Pre-synaptic terminals were identified using two presynaptic markers (Brp and Dsyd-1) and post-synaptic terminals by labelling a subunit of the acetylcholine receptor (Dalpha7) in genetically labelled Kenyon cells (Christiansen et al., 2011).']},
      'query': 'Get JSON for Class',
      'version': '44725ae',
      'parents': [{'iri': 'http://purl.obolibrary.org/obo/FBbt_00001366',
        'symbol': '',
        'types': ['Entity',
         'Anatomy',
         'Nervous_system',
         'Cell',
         'Neuron',
         'Class'],
        'label': 'supraesophageal ganglion neuron',
        'short_form': 'FBbt_00001366'},
       {'iri': 'http://purl.obolibrary.org/obo/FBbt_00007484',
        'symbol': '',
        'types': ['Entity',
         'Anatomy',
         'Nervous_system',
         'Cell',
         'Neuron',
         'Class'],
        'label': 'mushroom body intrinsic neuron',
        'short_form': 'FBbt_00007484'}],
      'relationships': [{'relation': {'type': 'develops_from',
         'iri': 'http://purl.obolibrary.org/obo/RO_0002202',
         'label': 'develops from'},
        'object': {'iri': 'http://purl.obolibrary.org/obo/FBbt_00007113',
         'symbol': '',
         'types': ['Entity',
          'Anatomy',
          'Nervous_system',
          'Cell',
          'Neuroblast',
          'Class'],
         'label': 'mushroom body neuroblast',
         'short_form': 'FBbt_00007113'}},
       {'relation': {'type': 'overlaps',
         'iri': 'http://purl.obolibrary.org/obo/RO_0002131',
         'label': 'overlaps'},
        'object': {'iri': 'http://purl.obolibrary.org/obo/FBbt_00003687',
         'symbol': '',
         'types': ['Entity',
          'Synaptic_neuropil',
          'Anatomy',
          'Nervous_system',
          'Synaptic_neuropil_domain',
          'Class'],
         'label': 'mushroom body pedunculus',
         'short_form': 'FBbt_00003687'}},
       {'relation': {'type': 'part_of',
         'iri': 'http://purl.obolibrary.org/obo/BFO_0000050',
         'label': 'is part of'},
        'object': {'iri': 'http://purl.obolibrary.org/obo/FBbt_00005801',
         'symbol': '',
         'types': ['Entity',
          'Synaptic_neuropil',
          'Anatomy',
          'Nervous_system',
          'Synaptic_neuropil_block',
          'Class'],
         'label': 'mushroom body',
         'short_form': 'FBbt_00005801'}},
       {'relation': {'type': 'receives_synaptic_input_in',
         'iri': 'http://purl.obolibrary.org/obo/RO_0013002',
         'label': 'receives synaptic input in'},
        'object': {'iri': 'http://purl.obolibrary.org/obo/FBbt_00003685',
         'symbol': '',
         'types': ['Entity',
          'Synaptic_neuropil',
          'Anatomy',
          'Nervous_system',
          'Synaptic_neuropil_domain',
          'Class'],
         'label': 'mushroom body calyx',
         'short_form': 'FBbt_00003685'}}],
      'xrefs': [],
      'anatomy_channel_image': [{'channel_image': {'channel': {'iri': 'http://virtualflybrain.org/reports/VFBc_jrchjwig',
          'symbol': '',
          'types': ['Entity', 'Individual'],
          'label': 'KCg-t_R - 5812981989_c',
          'short_form': 'VFBc_jrchjwig'},
         'image': {'template_channel': {'iri': 'http://virtualflybrain.org/reports/VFBc_00101567',
           'symbol': '',
           'types': ['Entity', 'Individual', 'Template'],
           'label': 'JRC2018Unisex_c',
           'short_form': 'VFBc_00101567'},
          'index': [],
          'template_anatomy': {'iri': 'http://virtualflybrain.org/reports/VFB_00101567',
           'symbol': '',
           'types': ['Entity',
            'has_image',
            'Adult',
            'Anatomy',
            'Nervous_system',
            'Individual',
            'Template'],
           'label': 'JRC2018Unisex',
           'short_form': 'VFB_00101567'},
          'image_folder': 'http://www.virtualflybrain.org/data/VFB/i/jrch/jwig/VFB_00101567/'},
         'imaging_technique': {'iri': 'http://purl.obolibrary.org/obo/FBbi_00050000',
          'symbol': 'FIB-SEM',
          'types': ['Entity', 'Class'],
          'label': 'focussed ion beam scanning electron microscopy (FIB-SEM)',
          'short_form': 'FBbi_00050000'}},
        'anatomy': {'iri': 'http://virtualflybrain.org/reports/VFB_jrchjwig',
         'symbol': '',
         'types': ['Entity',
          'has_image',
          'Adult',
          'Anatomy',
          'has_neuron_connectivity',
          'Cell',
          'Individual',
          'has_region_connectivity',
          'NBLAST',
          'Nervous_system',
          'Neuron'],
         'label': 'KCg-t_R - 5812981989',
         'short_form': 'VFB_jrchjwig'}},
       {'channel_image': {'channel': {'iri': 'http://virtualflybrain.org/reports/VFBc_jrchjwig',
          'symbol': '',
          'types': ['Entity', 'Individual'],
          'label': 'KCg-t_R - 5812981989_c',
          'short_form': 'VFBc_jrchjwig'},
         'image': {'template_channel': {'iri': 'http://virtualflybrain.org/reports/VFBc_00101384',
           'symbol': '',
           'types': ['Entity', 'Individual', 'Template'],
           'label': 'JRC_FlyEM_Hemibrain_c',
           'short_form': 'VFBc_00101384'},
          'index': [],
          'template_anatomy': {'iri': 'http://virtualflybrain.org/reports/VFB_00101384',
           'symbol': '',
           'types': ['Entity',
            'has_image',
            'Adult',
            'Anatomy',
            'Nervous_system',
            'Individual',
            'Template'],
           'label': 'JRC_FlyEM_Hemibrain',
           'short_form': 'VFB_00101384'},
          'image_folder': 'http://www.virtualflybrain.org/data/VFB/i/jrch/jwig/VFB_00101384/'},
         'imaging_technique': {'iri': 'http://purl.obolibrary.org/obo/FBbi_00050000',
          'symbol': 'FIB-SEM',
          'types': ['Entity', 'Class'],
          'label': 'focussed ion beam scanning electron microscopy (FIB-SEM)',
          'short_form': 'FBbi_00050000'}},
        'anatomy': {'iri': 'http://virtualflybrain.org/reports/VFB_jrchjwig',
         'symbol': '',
         'types': ['Entity',
          'has_image',
          'Adult',
          'Anatomy',
          'has_neuron_connectivity',
          'Cell',
          'Individual',
          'has_region_connectivity',
          'NBLAST',
          'Nervous_system',
          'Neuron'],
         'label': 'KCg-t_R - 5812981989',
         'short_form': 'VFB_jrchjwig'}},
       {'channel_image': {'channel': {'iri': 'http://virtualflybrain.org/reports/VFBc_jrchjwih',
          'symbol': '',
          'types': ['Entity', 'Individual'],
          'label': 'KCg-t_R - 1392655948_c',
          'short_form': 'VFBc_jrchjwih'},
         'image': {'template_channel': {'iri': 'http://virtualflybrain.org/reports/VFBc_00101567',
           'symbol': '',
           'types': ['Entity', 'Individual', 'Template'],
           'label': 'JRC2018Unisex_c',
           'short_form': 'VFBc_00101567'},
          'index': [],
          'template_anatomy': {'iri': 'http://virtualflybrain.org/reports/VFB_00101567',
           'symbol': '',
           'types': ['Entity',
            'has_image',
            'Adult',
            'Anatomy',
            'Nervous_system',
            'Individual',
            'Template'],
           'label': 'JRC2018Unisex',
           'short_form': 'VFB_00101567'},
          'image_folder': 'http://www.virtualflybrain.org/data/VFB/i/jrch/jwih/VFB_00101567/'},
         'imaging_technique': {'iri': 'http://purl.obolibrary.org/obo/FBbi_00050000',
          'symbol': 'FIB-SEM',
          'types': ['Entity', 'Class'],
          'label': 'focussed ion beam scanning electron microscopy (FIB-SEM)',
          'short_form': 'FBbi_00050000'}},
        'anatomy': {'iri': 'http://virtualflybrain.org/reports/VFB_jrchjwih',
         'symbol': '',
         'types': ['Entity',
          'has_image',
          'Adult',
          'Anatomy',
          'has_neuron_connectivity',
          'Cell',
          'Individual',
          'has_region_connectivity',
          'NBLAST',
          'Nervous_system',
          'Neuron'],
         'label': 'KCg-t_R - 1392655948',
         'short_form': 'VFB_jrchjwih'}},
       {'channel_image': {'channel': {'iri': 'http://virtualflybrain.org/reports/VFBc_jrchjwih',
          'symbol': '',
          'types': ['Entity', 'Individual'],
          'label': 'KCg-t_R - 1392655948_c',
          'short_form': 'VFBc_jrchjwih'},
         'image': {'template_channel': {'iri': 'http://virtualflybrain.org/reports/VFBc_00101384',
           'symbol': '',
           'types': ['Entity', 'Individual', 'Template'],
           'label': 'JRC_FlyEM_Hemibrain_c',
           'short_form': 'VFBc_00101384'},
          'index': [],
          'template_anatomy': {'iri': 'http://virtualflybrain.org/reports/VFB_00101384',
           'symbol': '',
           'types': ['Entity',
            'has_image',
            'Adult',
            'Anatomy',
            'Nervous_system',
            'Individual',
            'Template'],
           'label': 'JRC_FlyEM_Hemibrain',
           'short_form': 'VFB_00101384'},
          'image_folder': 'http://www.virtualflybrain.org/data/VFB/i/jrch/jwih/VFB_00101384/'},
         'imaging_technique': {'iri': 'http://purl.obolibrary.org/obo/FBbi_00050000',
          'symbol': 'FIB-SEM',
          'types': ['Entity', 'Class'],
          'label': 'focussed ion beam scanning electron microscopy (FIB-SEM)',
          'short_form': 'FBbi_00050000'}},
        'anatomy': {'iri': 'http://virtualflybrain.org/reports/VFB_jrchjwih',
         'symbol': '',
         'types': ['Entity',
          'has_image',
          'Adult',
          'Anatomy',
          'has_neuron_connectivity',
          'Cell',
          'Individual',
          'has_region_connectivity',
          'NBLAST',
          'Nervous_system',
          'Neuron'],
         'label': 'KCg-t_R - 1392655948',
         'short_form': 'VFB_jrchjwih'}},
       {'channel_image': {'channel': {'iri': 'http://virtualflybrain.org/reports/VFBc_jrchjwii',
          'symbol': '',
          'types': ['Entity', 'Individual'],
          'label': 'KCg-t_R - 785918963_c',
          'short_form': 'VFBc_jrchjwii'},
         'image': {'template_channel': {'iri': 'http://virtualflybrain.org/reports/VFBc_00101567',
           'symbol': '',
           'types': ['Entity', 'Individual', 'Template'],
           'label': 'JRC2018Unisex_c',
           'short_form': 'VFBc_00101567'},
          'index': [],
          'template_anatomy': {'iri': 'http://virtualflybrain.org/reports/VFB_00101567',
           'symbol': '',
           'types': ['Entity',
            'has_image',
            'Adult',
            'Anatomy',
            'Nervous_system',
            'Individual',
            'Template'],
           'label': 'JRC2018Unisex',
           'short_form': 'VFB_00101567'},
          'image_folder': 'http://www.virtualflybrain.org/data/VFB/i/jrch/jwii/VFB_00101567/'},
         'imaging_technique': {'iri': 'http://purl.obolibrary.org/obo/FBbi_00050000',
          'symbol': 'FIB-SEM',
          'types': ['Entity', 'Class'],
          'label': 'focussed ion beam scanning electron microscopy (FIB-SEM)',
          'short_form': 'FBbi_00050000'}},
        'anatomy': {'iri': 'http://virtualflybrain.org/reports/VFB_jrchjwii',
         'symbol': '',
         'types': ['Entity',
          'has_image',
          'Adult',
          'Anatomy',
          'has_neuron_connectivity',
          'Cell',
          'Individual',
          'has_region_connectivity',
          'NBLAST',
          'Nervous_system',
          'Neuron'],
         'label': 'KCg-t_R - 785918963',
         'short_form': 'VFB_jrchjwii'}}],
      'pub_syn': [{'pub': {'core': {'iri': 'http://flybase.org/reports/Unattributed',
          'symbol': '',
          'types': ['Entity', 'Individual', 'pub'],
          'label': '',
          'short_form': 'Unattributed'},
         'FlyBase': '',
         'PubMed': '',
         'DOI': ''},
        'synonym': {'type': '', 'label': 'KC', 'scope': 'has_exact_synonym'}},
       {'pub': {'core': {'iri': 'http://flybase.org/reports/FBrf0236359',
          'symbol': '',
          'types': ['Entity', 'Individual', 'pub'],
          'label': 'Eichler et al., 2017, Nature 548(7666): 175--182',
          'short_form': 'FBrf0236359'},
         'FlyBase': 'FBrf0236359',
         'PubMed': '28796202',
         'DOI': '10.1038/nature23455'},
        'synonym': {'type': '',
         'label': 'mature Kenyon cell',
         'scope': 'has_exact_synonym'}},
       {'pub': {'core': {'iri': 'http://flybase.org/reports/FBrf0111409',
          'symbol': '',
          'types': ['Entity', 'Individual', 'pub'],
          'label': 'Lee et al., 1999, Development 126(18): 4065--4076',
          'short_form': 'FBrf0111409'},
         'FlyBase': '',
         'PubMed': '10457015',
         'DOI': ''},
        'synonym': {'type': '',
         'label': 'MB neuron',
         'scope': 'has_narrow_synonym'}}],
      'def_pubs': [{'core': {'iri': 'http://flybase.org/reports/FBrf0214059',
         'symbol': '',
         'types': ['Entity', 'Individual', 'pub'],
         'label': 'Christiansen et al., 2011, J. Neurosci. 31(26): 9696--9707',
         'short_form': 'FBrf0214059'},
        'FlyBase': '',
        'PubMed': '21715635',
        'DOI': '10.1523/JNEUROSCI.6542-10.2011'},
       {'core': {'iri': 'http://flybase.org/reports/FBrf0092568',
         'symbol': '',
         'types': ['Entity', 'Individual', 'pub'],
         'label': 'Ito et al., 1997, Development 124(4): 761--771',
         'short_form': 'FBrf0092568'},
        'FlyBase': '',
        'PubMed': '9043058',
        'DOI': ''},
       {'core': {'iri': 'http://flybase.org/reports/FBrf0205263',
         'symbol': '',
         'types': ['Entity', 'Individual', 'pub'],
         'label': 'Tanaka et al., 2008, J. Comp. Neurol. 508(5): 711--755',
         'short_form': 'FBrf0205263'},
        'FlyBase': '',
        'PubMed': '18395827',
        'DOI': '10.1002/cne.21692'}]}]




```python
# A query for summary info
import pandas as pd

summary = vc.neo_query_wrapper.get_type_TermInfo(['FBbt_00003686'], summary=True)
summary_tab = pd.DataFrame.from_records(summary)
summary_tab
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kenyon cell</td>
      <td></td>
      <td>FBbt_00003686</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>supraesophageal ganglion neuron|mushroom body ...</td>
      <td>FBbt_00001366|FBbt_00007484</td>
    </tr>
  </tbody>
</table>
</div>




```python
# A different method is needed to get info about individual neurons

summary = vc.neo_query_wrapper.get_anatomical_individual_TermInfo(['VFB_jrchjrch'], summary=True)
summary_tab = pd.DataFrame.from_records(summary)
summary_tab

```python




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
      <td>5-HTPLP01_R - 1324365879</td>
      <td></td>
      <td>VFB_jrchjrch</td>
      <td>Entity|has_image|Adult|Anatomy|has_neuron_conn...</td>
      <td>adult serotonergic PLP neuron</td>
      <td>FBbt_00110945</td>
      <td>neuprint_JRC_Hemibrain_1point1</td>
      <td>1324365879</td>
      <td>JRC_FlyEM_Hemibrain|JRC2018Unisex</td>
      <td>Xu2020NeuronsV1point1</td>
      <td>https://creativecommons.org/licenses/by/4.0/le...</td>
    </tr>
  </tbody>
</table>
</div>



**1.2** The `neo_query_wrapper` also includes methods for mapping between IDs from different sources. 


```python
# Some bodyIDs of HemiBrain neurons from the neuprint DataBase:
bodyIDs = [1068958652, 571424748, 1141631198]
vc.neo_query_wrapper.xref_2_vfb_id(map(str, bodyIDs)) # Note IDs must be strings
```




    {'1068958652': [{'db': 'neuronbridge', 'vfb_id': 'VFB_jrchjwda'},
      {'db': 'neuronbridge', 'vfb_id': 'VFB_jrch06r9'},
      {'db': 'neuprint_JRC_Hemibrain_1point0point1', 'vfb_id': 'VFB_jrch06r9'},
      {'db': 'neuprint_JRC_Hemibrain_1point1', 'vfb_id': 'VFB_jrchjwda'}],
     '571424748': [{'db': 'neuronbridge', 'vfb_id': 'VFB_jrch06r6'},
      {'db': 'neuronbridge', 'vfb_id': 'VFB_jrchjwct'},
      {'db': 'neuprint_JRC_Hemibrain_1point0point1', 'vfb_id': 'VFB_jrch06r6'},
      {'db': 'neuprint_JRC_Hemibrain_1point1', 'vfb_id': 'VFB_jrchjwct'}],
     '1141631198': [{'db': 'neuronbridge', 'vfb_id': 'VFB_jrch05uz'},
      {'db': 'neuronbridge', 'vfb_id': 'VFB_jrchjw8r'},
      {'db': 'neuprint_JRC_Hemibrain_1point0point1', 'vfb_id': 'VFB_jrch05uz'},
      {'db': 'neuprint_JRC_Hemibrain_1point1', 'vfb_id': 'VFB_jrchjw8r'}]}




```python
# xref queries can be constrained by DB. Results can optionally be reversed

vc.neo_query_wrapper.xref_2_vfb_id(map(str, bodyIDs), db = 'neuprint_JRC_Hemibrain_1point1' , reverse_return=True)
```




    {'VFB_jrchjw8r': [{'acc': '1141631198',
       'db': 'neuprint_JRC_Hemibrain_1point1'}],
     'VFB_jrchjwct': [{'acc': '571424748',
       'db': 'neuprint_JRC_Hemibrain_1point1'}],
     'VFB_jrchjwda': [{'acc': '1068958652',
       'db': 'neuprint_JRC_Hemibrain_1point1'}]}



### 2. `vc` direct methods overview

**2.1** Methods that take the names of classes in VFB e.g. 'nodulus' or 'Kenyon cell', or simple query expressions using the names of classes and return metadata about the classes or individual neurons


```python
KC_types = vc.get_subclasses("Kenyon cell", summary=True)
pd.DataFrame.from_records(KC_types)
```

    Running query: FBbt:00003686
    Query URL: http://owl.virtualflybrain.org/kbs/vfb/subclasses?object=FBbt%3A00003686&prefixes=%7B%22FBbt%22%3A+%22http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFBbt_%22%2C+%22RO%22%3A+%22http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FRO_%22%2C+%22BFO%22%3A+%22http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FBFO_%22%7D&direct=False
    Query results: 37





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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>adult alpha'/beta' Kenyon cell</td>
      <td></td>
      <td>FBbt_00049834</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>alpha'/beta' Kenyon cell|adult Kenyon cell</td>
      <td>FBbt_00100249|FBbt_00049825</td>
    </tr>
    <tr>
      <th>1</th>
      <td>immature Kenyon cell</td>
      <td></td>
      <td>FBbt_00047995</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>Kenyon cell</td>
      <td>FBbt_00003686</td>
    </tr>
    <tr>
      <th>2</th>
      <td>gamma Kenyon cell</td>
      <td></td>
      <td>FBbt_00100247</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>Kenyon cell</td>
      <td>FBbt_00003686</td>
    </tr>
    <tr>
      <th>3</th>
      <td>adult Kenyon cell</td>
      <td></td>
      <td>FBbt_00049825</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>adult MBp lineage neuron|Kenyon cell</td>
      <td>FBbt_00110577|FBbt_00003686</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gamma main Kenyon cell</td>
      <td>KCg-m</td>
      <td>FBbt_00111061</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>Kenyon cell of main calyx|adult gamma Kenyon cell</td>
      <td>FBbt_00047926|FBbt_00049828</td>
    </tr>
    <tr>
      <th>5</th>
      <td>alpha'/beta' anterior-posterior type 1 Kenyon ...</td>
      <td></td>
      <td>FBbt_00049859</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>alpha'/beta' anterior-posterior type 1 Kenyon ...</td>
      <td>FBbt_00049836</td>
    </tr>
    <tr>
      <th>6</th>
      <td>alpha/beta Kenyon cell</td>
      <td></td>
      <td>FBbt_00100248</td>
      <td>Entity|Neuron|Adult|Anatomy|Nervous_system|Cel...</td>
      <td>cholinergic neuron|adult Kenyon cell</td>
      <td>FBbt_00007173|FBbt_00049825</td>
    </tr>
    <tr>
      <th>7</th>
      <td>gamma-s4 Kenyon cell</td>
      <td>KCg-s4</td>
      <td>FBbt_00049832</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>gamma-s Kenyon cell</td>
      <td>FBbt_00049830</td>
    </tr>
    <tr>
      <th>8</th>
      <td>two-claw Kenyon cell</td>
      <td></td>
      <td>FBbt_00047997</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>multi-claw Kenyon cell</td>
      <td>FBbt_00047994</td>
    </tr>
    <tr>
      <th>9</th>
      <td>single-claw Kenyon cell</td>
      <td></td>
      <td>FBbt_00047993</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>Kenyon cell</td>
      <td>FBbt_00003686</td>
    </tr>
    <tr>
      <th>10</th>
      <td>alpha/beta posterior Kenyon cell</td>
      <td>KCab-p</td>
      <td>FBbt_00110931</td>
      <td>Entity|Neuron|Adult|Anatomy|Nervous_system|Cel...</td>
      <td>alpha/beta Kenyon cell</td>
      <td>FBbt_00100248</td>
    </tr>
    <tr>
      <th>11</th>
      <td>alpha'/beta' middle Kenyon cell</td>
      <td>KCa'b'-m</td>
      <td>FBbt_00100253</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>Kenyon cell of main calyx|adult alpha'/beta' K...</td>
      <td>FBbt_00047926|FBbt_00049834</td>
    </tr>
    <tr>
      <th>12</th>
      <td>alpha/beta surface Kenyon cell</td>
      <td>KCab-s</td>
      <td>FBbt_00110930</td>
      <td>Entity|Neuron|Adult|Anatomy|Nervous_system|Cel...</td>
      <td>alpha/beta surface/core Kenyon cell</td>
      <td>FBbt_00049838</td>
    </tr>
    <tr>
      <th>13</th>
      <td>alpha'/beta' anterior-posterior type 1 Kenyon ...</td>
      <td>KCa'b'-ap1</td>
      <td>FBbt_00049836</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>alpha'/beta' anterior-posterior Kenyon cell</td>
      <td>FBbt_00100250</td>
    </tr>
    <tr>
      <th>14</th>
      <td>larval alpha'/beta' Kenyon cell</td>
      <td></td>
      <td>FBbt_00049835</td>
      <td>Entity|Neuron|Anatomy|Nervous_system|Cell|Larv...</td>
      <td>larval Kenyon cell|alpha'/beta' Kenyon cell</td>
      <td>FBbt_00049826|FBbt_00100249</td>
    </tr>
    <tr>
      <th>15</th>
      <td>gamma-s1 Kenyon cell</td>
      <td>KCg-s1</td>
      <td>FBbt_00049787</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>gamma-s Kenyon cell</td>
      <td>FBbt_00049830</td>
    </tr>
    <tr>
      <th>16</th>
      <td>gamma-t Kenyon cell</td>
      <td>KCg-t</td>
      <td>FBbt_00049833</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>adult gamma Kenyon cell</td>
      <td>FBbt_00049828</td>
    </tr>
    <tr>
      <th>17</th>
      <td>four-claw Kenyon cell</td>
      <td></td>
      <td>FBbt_00047999</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>multi-claw Kenyon cell</td>
      <td>FBbt_00047994</td>
    </tr>
    <tr>
      <th>18</th>
      <td>alpha'/beta' Kenyon cell</td>
      <td></td>
      <td>FBbt_00100249</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>Kenyon cell</td>
      <td>FBbt_00003686</td>
    </tr>
    <tr>
      <th>19</th>
      <td>alpha/beta surface/core Kenyon cell</td>
      <td></td>
      <td>FBbt_00049838</td>
      <td>Entity|Neuron|Adult|Anatomy|Nervous_system|Cel...</td>
      <td>Kenyon cell of main calyx|alpha/beta Kenyon cell</td>
      <td>FBbt_00047926|FBbt_00100248</td>
    </tr>
    <tr>
      <th>20</th>
      <td>larval Kenyon cell</td>
      <td></td>
      <td>FBbt_00049826</td>
      <td>Entity|Neuron|Anatomy|Nervous_system|Cell|Larv...</td>
      <td>Kenyon cell|embryonic/larval neuron</td>
      <td>FBbt_00003686|FBbt_00001446</td>
    </tr>
    <tr>
      <th>21</th>
      <td>alpha'/beta' anterior-posterior Kenyon cell</td>
      <td></td>
      <td>FBbt_00100250</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>adult alpha'/beta' Kenyon cell</td>
      <td>FBbt_00049834</td>
    </tr>
    <tr>
      <th>22</th>
      <td>six-claw Kenyon cell</td>
      <td></td>
      <td>FBbt_00048001</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>multi-claw Kenyon cell</td>
      <td>FBbt_00047994</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Kenyon cell of main calyx</td>
      <td></td>
      <td>FBbt_00047926</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>adult Kenyon cell</td>
      <td>FBbt_00049825</td>
    </tr>
    <tr>
      <th>24</th>
      <td>alpha'/beta' anterior-posterior type 2 Kenyon ...</td>
      <td>KCa'b'-ap2</td>
      <td>FBbt_00049837</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>alpha'/beta' anterior-posterior Kenyon cell|Ke...</td>
      <td>FBbt_00100250|FBbt_00047926</td>
    </tr>
    <tr>
      <th>25</th>
      <td>gamma-s3 Kenyon cell</td>
      <td>KCg-s3</td>
      <td>FBbt_00049831</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>gamma-s Kenyon cell</td>
      <td>FBbt_00049830</td>
    </tr>
    <tr>
      <th>26</th>
      <td>alpha/beta inner-core Kenyon cell</td>
      <td></td>
      <td>FBbt_00049111</td>
      <td>Entity|Neuron|Adult|Anatomy|Nervous_system|Cel...</td>
      <td>alpha/beta core Kenyon cell</td>
      <td>FBbt_00110929</td>
    </tr>
    <tr>
      <th>27</th>
      <td>gamma dorsal Kenyon cell</td>
      <td>KCg-d</td>
      <td>FBbt_00110932</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>adult gamma Kenyon cell</td>
      <td>FBbt_00049828</td>
    </tr>
    <tr>
      <th>28</th>
      <td>alpha/beta outer-core Kenyon cell</td>
      <td></td>
      <td>FBbt_00049112</td>
      <td>Entity|Neuron|Adult|Anatomy|Nervous_system|Cel...</td>
      <td>alpha/beta core Kenyon cell</td>
      <td>FBbt_00110929</td>
    </tr>
    <tr>
      <th>29</th>
      <td>five-claw Kenyon cell</td>
      <td></td>
      <td>FBbt_00048000</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>multi-claw Kenyon cell</td>
      <td>FBbt_00047994</td>
    </tr>
    <tr>
      <th>30</th>
      <td>alpha/beta core Kenyon cell</td>
      <td>KCab-c</td>
      <td>FBbt_00110929</td>
      <td>Entity|Neuron|Adult|Anatomy|Nervous_system|Cel...</td>
      <td>alpha/beta surface/core Kenyon cell</td>
      <td>FBbt_00049838</td>
    </tr>
    <tr>
      <th>31</th>
      <td>multi-claw Kenyon cell</td>
      <td></td>
      <td>FBbt_00047994</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>Kenyon cell</td>
      <td>FBbt_00003686</td>
    </tr>
    <tr>
      <th>32</th>
      <td>adult gamma Kenyon cell</td>
      <td></td>
      <td>FBbt_00049828</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>gamma Kenyon cell|adult Kenyon cell</td>
      <td>FBbt_00100247|FBbt_00049825</td>
    </tr>
    <tr>
      <th>33</th>
      <td>three-claw Kenyon cell</td>
      <td></td>
      <td>FBbt_00047998</td>
      <td>Entity|Anatomy|Nervous_system|Cell|Neuron|Class</td>
      <td>multi-claw Kenyon cell</td>
      <td>FBbt_00047994</td>
    </tr>
    <tr>
      <th>34</th>
      <td>larval gamma Kenyon cell</td>
      <td></td>
      <td>FBbt_00049827</td>
      <td>Entity|Neuron|Anatomy|Nervous_system|Cell|Larv...</td>
      <td>larval Kenyon cell|gamma Kenyon cell</td>
      <td>FBbt_00049826|FBbt_00100247</td>
    </tr>
    <tr>
      <th>35</th>
      <td>gamma-s2 Kenyon cell</td>
      <td>KCg-s2</td>
      <td>FBbt_00049788</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>gamma-s Kenyon cell</td>
      <td>FBbt_00049830</td>
    </tr>
    <tr>
      <th>36</th>
      <td>gamma-s Kenyon cell</td>
      <td></td>
      <td>FBbt_00049830</td>
      <td>Entity|Adult|Anatomy|Nervous_system|Cell|Neuro...</td>
      <td>adult gamma Kenyon cell</td>
      <td>FBbt_00049828</td>
    </tr>
  </tbody>
</table>
</div>



**2.2** Methods for querying connectivity

Please see Connectivity Notebook for examples


