---
title: "Knowledge Base (KB) API"
linkTitle: "KB API"
weight: 2
date: 2024-01-13
description: >
  The VFB Knowledge Base (KB) provides specialized storage and query capabilities for VFB-specific data and annotations.
---

The VFB Knowledge Base (KB) is a specialized Neo4j database that complements the Production Database (PDB). While the PDB handles integrated ontology data, expression patterns, and image annotations, the KB serves specific VFB requirements and workflows.

## Browser Access

Explore the KB using the Neo4j browser:

[https://kb.virtualflybrain.org/browser/](https://kb.virtualflybrain.org/browser/)

## Purpose and Scope

The KB serves as:

1. **VFB-Specific Data Repository**: Storage for VFB-specific annotations, metadata, and derived data
2. **Workflow Support**: Specialized storage supporting VFB curation and integration workflows

**Note**: Ontology data, expression patterns, image annotations, and connectivity data are stored in the Production Database (PDB).

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

- **KB**: Specialized storage for VFB-specific annotations, metadata, and derived data
- **PDB**: Integrated storage for ontology data, expression patterns, image annotations, connectivity data, and cross-referenced information
- **Data Flow**: VFB-specific data from KB supports curation and integration workflows alongside PDB data


**Note**: For queries involving ontology data, expression patterns, or image annotations, use the Production Database (PDB).

## Maintenance and Updates

The KB is maintained through:
- Manual curation workflows
- Automated data loading pipelines
- Integration with external data sources
- Quality control and validation processes

For more details on the underlying schema, see the [VFB Neo4j documentation](https://github.com/VirtualFlyBrain/VFB_neo4j/tree/master/doc).