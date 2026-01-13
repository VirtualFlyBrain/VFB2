
---
title: "VFB APIs"
linkTitle: "VFB APIs"
weight: 3
date: 2017-01-05
description: >
  All available VFB APIs and underlying schemas.
---

VFB provides access to its data through several APIs and databases. The core data infrastructure consists of Neo4j graph databases that store integrated neuroanatomical data, complemented by OWL reasoning services for advanced ontological queries and SOLR search for fast text-based queries.

## User Access Options

**For Regular Users (GUI Access):**
- **VFB Web Interface**: [https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto) - User-friendly web interface for browsing and querying VFB data

**For Programmatic Access:**
- **VFBconnect Library**: [https://vfb-connect.readthedocs.io/](https://vfb-connect.readthedocs.io/) - Python library that provides high-level access to VFB data and queries. See also: [VFB API Tutorial](Tutorials/APIs/0_VFB_API_overview.md)

**For Advanced Data Access:**
- **Direct APIs** (documented below): Low-level access to underlying databases and reasoning services

## Important Notes

These API documentations describe the schemas used for data storage and basic interfaces. **Most VFB queries are constructed from combined query chains** that integrate multiple services (Neo4j, OWL reasoning, SOLR search) rather than single API calls. For details on how queries are orchestrated, see the [VFB query chains documentation](https://github.com/VirtualFlyBrain/geppetto-vfb/blob/master/model/README.md).

The APIs documented here are intended for:
- Advanced users needing direct database access
- Developers building custom tools or integrations
- Researchers requiring low-level data access for specialized analyses

For most use cases, we recommend starting with the [VFBconnect library](https://vfb-connect.readthedocs.io/) or the [web interface](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto).

## Core Databases

### [Production Database (PDB)](PDB.md)
The main VFB database containing integrated ontology data, expression patterns, image annotations, and connectivity information from multiple sources, optimized for comprehensive queries across the entire knowledge graph.

- **Technology**: Neo4j graph database
- **Content**: Complete integrated neuroanatomical knowledge base
- **Browser**: [https://pdb.virtualflybrain.org/browser/](https://pdb.virtualflybrain.org/browser/)

### [Knowledge Base (KB)](KB.md)
Specialized database focused on large-scale synaptic connectivity data and related annotations, separated from the main PDB due to the size and complexity of modern connectomes.

- **Technology**: Neo4j graph database
- **Content**: Detailed synaptic connectivity and connectome data
- **Browser**: [https://kb.virtualflybrain.org/browser/](https://kb.virtualflybrain.org/browser/)

### [Owlery API](Owlery.md)
OWL reasoning service providing advanced queries over VFB ontologies using Description Logic and SPARQL.

- **Technology**: OWL API-based reasoner
- **Capabilities**: Class hierarchies, instance queries, SPARQL with reasoning
- **Endpoint**: [https://owl.virtualflybrain.org/kbs/vfb/](https://owl.virtualflybrain.org/kbs/vfb/)

### [SOLR Search API](SOLR.md)
Fast text search and autocomplete service for VFB entities, datasets, and publications.

- **Technology**: Apache SOLR search engine
- **Capabilities**: Full-text search, faceted search, result boosting
- **Endpoint**: [https://solr.virtualflybrain.org/solr/vfb_olympiad/select](https://solr.virtualflybrain.org/solr/vfb_olympiad/select)

## Additional APIs

VFB also provides other services for specialized functionality. See the [Owlery API](Owlery.md) documentation for OWL reasoning capabilities. Additional REST APIs and services may be documented in future updates.
