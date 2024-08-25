---
title: "Guide to adding new query properties to the VFBTerm object in the VFBConnect Library"
linkTitle: "Adding new query in VFBconnect"
date: 2024-08-25
description: >
    An exploration of how an example query is added to the VFBTerm object under VFBconnect which provides a template for any future queries you may want to add add to vfb.term
---

Most of the queries in VFBTerm are built on previous older implementation queries so can be spread across multiple functions but as I just added a new query I thought this was a good example of a complex query (multiple steps combined) that is all in one function:

https://github.com/VirtualFlyBrain/VFB_connect/blob/master/src/vfb_connect/schema/vfb_term.py#L1709C5-L1735C78

```python
def add_anatomy_type_properties(self):
        @property
        def transgene_expression(self):
            """
            Get the transgene expression data associated with this anatomy type term.
            """
            if self._transgene_expression is None:
                print("Loading transgene expression for the first time...") if self.debug else None
                subclasses = self.vfb.oc.get_subclasses(query=f"'{self.id}'", verbose=self.debug)
                print("Subclasses: ", subclasses) if self.debug else None
                overlapping_cells = self.vfb.oc.get_subclasses(query=f"'cell' that 'overlaps' some '{self.id}'", verbose=self.debug)
                print("Overlapping cells: ", overlapping_cells) if self.debug else None
                part_of = self.vfb.oc.get_subclasses(query=f"'is part of' some '{self.id}'", verbose=self.debug)
                print("Part of: ", part_of) if self.debug else None
                all_anatomy = subclasses + overlapping_cells + part_of + [self.id]
                print("All anatomy: ", all_anatomy) if self.debug else None
                result = dict_cursor(self.vfb.nc.commit_list([f"MATCH (ep:Class:Expression_pattern)<-[ar:overlaps|part_of]-(:Individual)-[:INSTANCEOF]->(anat:Class) WHERE anat.short_form in {all_anatomy} WITH DISTINCT collect(DISTINCT ar.pub[0]) as pubs, anat, ep OPTIONAL MATCH (pub:pub) WHERE pub.short_form IN pubs RETURN distinct ep.short_form as term, coalesce(ep.symbol, ep.label) as term_name, anat.short_form as type, coalesce(anat.symbol, anat.label) as type_name, collect(pub) as pubs"]))
                print("Result: ", result) if self.debug else None
                if result:
                    self._transgene_expression = ExpressionList([Expression(term=exp['term'], term_name=exp['term_name'], term_type='transgene', type=exp['type'], type_name=exp['type_name'], reference=[Publication(FlyBase=pub.get('FlyBase',''), PubMed=pub.get('PMID',''), DOI=pub.get('DOI', ''), core=MinimalEntityInfo(short_form=pub['short_form'], label=pub['label'], iri=pub['iri'], types=pub['label'], symbol=','.join(pub['miniref'][0].split(',')[:2])), description=pub['title']) for pub in exp['pubs']]) for exp in result])
                else:
                    self._transgene_expression = ExpressionList([])
                print(f"Transgene expression: {repr(self._transgene_expression)}") if self.debug else None
            return self._transgene_expression

        # Dynamically add the property to the instance
        setattr(self.__class__, 'transgene_expression', transgene_expression)
```

This is based on the VFB site query https://github.com/VirtualFlyBrain/geppetto-vfb/tree/development/model#transgeneexpressionhere-reports-of-transgene-expression-in-name 

To find any potential Transgenes in X it need to find all types that are subclasses (subtypes) + any overlapping cells + any parts of X plus the term X itself. These are all collected using [OWLery](https://github.com/phenoscape/owlery?tab=readme-ov-file) query for the id's of all these types using MANCHESTER syntax queries:

```python
subclasses: '{self.id}' 

subclasses: 'cell' that 'overlaps' some '{self.id}'

subclasses: 'is part of' some '{self.id}'
```

This is added to the ```self.id``` to include the term itself and passed (as all_anatomy) to a neo4j cypher query running against the VFB PDB (Production DB):

```cypher
MATCH (ep:Class:Expression_pattern)<-[ar:overlaps|part_of]-(:Individual)-[:INSTANCEOF]->(anat:Class) WHERE anat.short_form in {all_anatomy} WITH DISTINCT collect(DISTINCT ar.pub[0]) as pubs, anat, ep OPTIONAL MATCH (pub:pub) WHERE pub.short_form IN pubs RETURN distinct ep.short_form as term, coalesce(ep.symbol, ep.label) as term_name, anat.short_form as type, coalesce(anat.symbol, anat.label) as type_name, collect(pub) as pubs
```

the output of this is put through the dict_cursor to turn them into an easily accessible dictionary and then constructed as an Expression object into an ExpressionList:
```python
ExpressionList(
    [Expression(
        term=exp['term'], 
        term_name=exp['term_name'], 
        term_type='transgene', type=exp['type'], 
        type_name=exp['type_name'], 
        reference=[
            Publication(
                FlyBase=pub.get('FlyBase',''), 
                PubMed=pub.get('PMID',''), 
                DOI=pub.get('DOI', ''), 
                core=MinimalEntityInfo(
                    short_form=pub['short_form'], 
                    label=pub['label'], 
                    iri=pub['iri'], 
                    types=pub['label'], 
                    symbol=','.join(pub['miniref'][0].split(',')[:2])), 
                description=pub['title']
            ) for pub in exp['pubs']
        ]
    ) for exp in result]
)
```

Note: the ```for X in Y``` simply iterates a list and as it's inside ```[]``` it returns as a list

Note: the reason the name as well as the id is often passed is that these terms are themselves Lasy loaded and so passing the name prevents full loading needing to be done for just summary display.

Speaking of Lazy loading this is the reason for the ```@propery``` and the ```setattr(self.__class__, 'transgene_expression', transgene_expression)``` which (if ```add_anatomy_type_properties()``` is run) add transgene_expression to the term to be called as ```X.transgene_expression``` and the first time will run the query, cashing the results in ```self._transgene_expression``` for future calls.

The code here up in the ```VFBTerm __init__ ``` adds this option only if the term ```is_type``` and has the tag for `Anatomy`:

```python
if self.has_tag('Anatomy') and self.is_type:
                self._transgene_expression = None
                self.add_anatomy_type_properties()
                self._lineage_clones = None
                self._lineage_clone_types = None
                self.add_lineage_clone_properties() 
```
https://github.com/VirtualFlyBrain/VFB_connect/blob/master/src/vfb_connect/schema/vfb_term.py#L1681C1-L1682C51

Initialising the cache: ```self._transgene_expression = None```
and calling the relevant properties: ```self.add_anatomy_type_properties()```

Copying this procedure will allow you to add any query based on checked against tags or other checks.

Note: Tags are Neo4j 'labels' (```labels(n)``` as apposed to n.label) for the term and can be checked against using ```self.has_tag('X')```.


VFBconnect Docs: [VFBConnect library](https://vfb-connect.readthedocs.io/).
