---
title: "SOLR search example"
linkTitle: "SOLR API"
weight: 100
description: >-
     How to programatically search for a term.
---

## SOLR python example

an example using pysolr:

install:
```bash
pip install vfb-connect pysolr
```

example looking for label/name match:

```python
import pysolr

solr = pysolr.Solr('https://solr.virtualflybrain.org/solr/ontology/')

term = 'medulla'

results = solr.search('label:"' + term + '"')

print(results.docs[0])
```

```json
{'iri': ['http://purl.obolibrary.org/obo/FBbt_00003748'],
 'obo_id_autosuggest': ['FBbt_00003748', 'FBbt:00003748', 'FBbt 00003748'],
 'label_autosuggest': ['medulla', 'medulla', 'medulla'],
 'synonym_autosuggest': ['ME', 'Med', 'optic medulla', 'm'],
 'label': 'medulla',
 'synonym': ['ME', 'Med', 'optic medulla', 'm'],
 'short_form': 'FBbt_00003748',
 'autosuggest': ['medulla', 'ME', 'Med', 'optic medulla', 'm'],
 'facets_annotation': ['Entity',
  'Adult',
  'Anatomy',
  'Class',
  'Nervous_system',
  'Synaptic_neuropil',
  'Synaptic_neuropil_domain'],
 'unique_facets': ['Nervous_system', 'Adult', 'Synaptic_neuropil_domain'],
 'id': 'http://purl.obolibrary.org/obo/FBbt_00003748',
 'shortform_autosuggest': ['FBbt_00003748', 'FBbt:00003748', 'FBbt 00003748'],
 'obo_id': ['FBbt:00003748'],
 '_version_': 1734360220689235970}
```
 
Note: any of the above fields can be searched (autosuggest being a combination of both label and synonyms)

 
