---
title: "Knowledge Base (KB) API"
linkTitle: "KB API"
weight: 2
date: 2024-01-13
description: >
  The VFB Knowledge Base (KB) stores large-scale synaptic connectivity data and related annotations.
---

The VFB Knowledge Base (KB) is a specialized Neo4j database focused on storing large-scale connectivity data. Due to the size and complexity of modern connectomes, most ontology data, expression patterns, and other integrated content has been moved to the Production Database (PDB). The KB now serves as a dedicated repository for synaptic connectivity information and related annotations.

## Browser Access

Explore the KB using the Neo4j browser:

[https://kb.virtualflybrain.org/browser/](https://kb.virtualflybrain.org/browser/)

## Purpose and Scope

The KB serves as:

1. **Connectivity Data Repository**: Primary storage for synaptic connectivity information from large-scale connectomes
2. **VFB-Specific Annotations**: Annotations and metadata related to connectivity data

**Note**: Ontology data, expression patterns, image annotations, and other integrated content are now stored in the Production Database (PDB) to handle the growing size and complexity of modern connectomes.

## Data Types

### Connectivity Data

VFB stores connectivity data at multiple levels:

1. **Neo4j Graph Storage**: Detailed synaptic connectivity in the KB graph database
2. **OWL Ontology Files**: Connectomic data exported as OWL files for semantic interoperability

**OWL Connectivity Files**: Available at [https://virtualflybrain.org/data/VFB/OWL/raw/](https://virtualflybrain.org/data/VFB/OWL/raw/) (connectome_*.owl files)

Two levels of representation in Neo4j:

1. **Crude Connectivity**: Simple triples `A synapsed_to B` with synapse counts
2. **Detailed Synapses**: Individual synapse partonomy using GO terms (3 individuals per synapse)

**Note**: Image annotations, ontology data, and expression patterns are now stored in the Production Database (PDB).

## Schema Requirements

The KB schema is designed with specific requirements:

- **Updateability**: Ontology terms and FlyBase features must be updateable via CI
- **ID Stability**: Derived class IDs (e.g., expression patterns) must be preserved during updates
- **OWL Compatibility**: Subset of content convertible to OWL using standard patterns
- **Dataset Isolation**: Ability to generate OWL files for individual datasets

## Expression Patterns

Expression patterns in the KB follow the general semantic specification:

- **Definition**: Mereological sum of all cells in an anatomical structure expressing a gene/transgene
- **Classification**: Hierarchical organization via OWL reasoning
- **Stability**: IDs must remain stable across updates

### Pattern Types

- **Complete Expression Pattern**: All cells in an organism expressing a gene
- **Regional Expression Pattern**: Subset of expression in specific anatomical regions

## Integration with PDB

The KB and PDB work together in VFB's data architecture:

- **KB**: Specialized storage for large-scale connectivity data and related annotations
- **PDB**: Integrated storage for ontology data, expression patterns, image annotations, and cross-referenced information
- **Data Flow**: Connectivity data from KB is integrated with other data types in PDB for comprehensive queries

## Query Patterns

### Connectivity Queries
```cypher
MATCH (neuron1:Individual)-[syn:synapsed_to]->(neuron2:Individual)
RETURN neuron1, syn, neuron2
```

### Synapse Detail Queries
```cypher
MATCH (neuron:Individual)-[:has_presynaptic_terminal_in]->(region:Class)
RETURN neuron, region
```

**Note**: For queries involving ontology data, expression patterns, or image annotations, use the Production Database (PDB).

## Maintenance and Updates

The KB is maintained through:
- Manual curation workflows
- Automated data loading pipelines
- Integration with external data sources
- Quality control and validation processes

For more details on the underlying schema, see the [VFB Neo4j documentation](https://github.com/VirtualFlyBrain/VFB_neo4j/tree/master/doc).