---
title: "Production Database (PDB) API"
linkTitle: "PDB API"
weight: 1
date: 2024-01-13
description: >
  The VFB Production Database (PDB) is a Neo4j graph database containing integrated neuroanatomical data from multiple sources.
---

The VFB Production Database (PDB) is the main Neo4j graph database containing integrated neuroanatomical data from multiple sources, including ontology data, expression patterns, image annotations, and connectivity information. It serves as the primary data store for comprehensive queries across VFB's knowledge graph.

## Browser Access

You can explore the PDB interactively using the Neo4j browser:

[https://pdb.virtualflybrain.org/browser/](https://pdb.virtualflybrain.org/browser/)

## Data Structure Overview

The PDB contains over 1.1 million nodes and 43 million relationships, representing a comprehensive knowledge graph of Drosophila neuroanatomy. Below is an overview of the available node labels, relationship types, and property keys.

### Node Labels (Gross Classifications)

The PDB uses hierarchical node labels to classify different types of entities:

**Core Ontology Nodes:**
- `Class`, `Individual` - OWL ontology elements
- `Property` - Relationships and attributes

**Anatomical Classifications:**
- `Anatomy`, `Neuron`, `Glial_cell`, `Muscle`, `Sense_organ`
- `Nervous_system`, `Synaptic_neuropil`, `Ganglion`, `Neuromere`
- `Neuron_projection_bundle`, `Template`

**Cell Types and Lineages:**
- `Motor_neuron`, `Sensory_neuron`, `Neuroblast`
- `lineage_*` (200+ lineage classifications for neural development)

**Molecular and Functional:**
- `Gene`, `Expression_pattern`, `Clone`, `Feature`
- `Receptor`, `Channel`, `Transporter`, `Enzyme`
- `Neurotransmitter_receptor` (Cholinergic, GABAergic, Glutamatergic, etc.)

**Data and Metadata:**
- `DataSet`, `Sample`, `License`, `Person`
- `pub` (Publications), `Site`, `Template`
- `VFB`, `Deprecated`, `Individual`

**Dataset-Specific:**
- `FAFB`, `FlyCircuit`, `L1EM`, `FANC` (Different connectome datasets)
- `has_image`, `has_neuron_connectivity`, `has_region_connectivity`

### Relationship Types

The PDB defines 200+ relationship types for connecting entities:

**Core Ontology Relationships:**
- `INSTANCEOF`, `SUBCLASSOF` - Class hierarchies
- `has_part`, `part_of` - Anatomical composition
- `located_in`, `overlaps` - Spatial relationships

**Connectivity Relationships:**
- `synapsed_to` - Basic synaptic connections
- `has_presynaptic_terminals_in`, `has_postsynaptic_terminal_in` - Detailed synapse locations
- `sends_synaptic_output_to_region`, `receives_synaptic_input_in_region` - Functional connectivity
- `synapsed_via_type_*_bouton_to` - Specific bouton types

**Developmental and Temporal:**
- `develops_from`, `develops_into` - Developmental progression
- `happens_during`, `existence_starts_during` - Temporal relationships
- `has_member` - Group memberships

**Functional and Molecular:**
- `expresses` - Gene expression relationships
- `has_role`, `capable_of` - Functional classifications
- `regulates`, `positively_regulates`, `negatively_regulates` - Regulatory interactions

**Metadata and Attribution:**
- `has_reference`, `created_by`, `has_license` - Provenance
- `database_cross_reference` - External identifiers
- `depicts` - Image relationships

### Property Keys

Properties provide additional metadata and attributes for nodes and relationships:

**Identifiers and Labels:**
- `id`, `short_form`, `label`, `symbol`, `name`
- `iri`, `curie`, `unique_id`

**Descriptions and Definitions:**
- `definition`, `description`, `comment`
- `example_of_usage`, `elucidation`

**References and Attribution:**
- `PMID`, `PMCID`, `DOI`, `FlyBase`
- `created_by`, `creation_date`, `creator`
- `has_reference`, `miniref`, `pub`

**Spatial and Quantitative:**
- `center`, `orientation`, `volume`, `voxel`
- `Tbars`, `cell_count`, `cubic_micrometer_overlap`
- `NBLAST_score`, `neuronbridge_score`

**Quality and Status:**
- `confidence_value`, `curation_status`
- `is_obsolete`, `deprecated`, `hide_in_terminfo`
- `has_curation_status`, `obsolescence_reason`

**Technical Metadata:**
- `filename`, `link_base`, `thumbnail`, `nrrd`, `swc`
- `dataset_link`, `license_url`, `homepage`

### Query Examples

**Note**: These are direct Cypher queries for programmatic access to the PDB. The VFB web application typically uses higher-level query chains that combine multiple data sources and reasoning services. For user-friendly querying, use the VFB web interface.

#### Find all expression patterns for a gene
```cypher
MATCH (ep:Expression_pattern)-[:expresses]->(gene:Gene {symbol: 'gene_name'})
RETURN ep
```

#### Find neurons with presynaptic terminals in a brain region
```cypher
MATCH (neuron:Neuron)-[:has_presynaptic_terminals_in]->(region:Synaptic_neuropil {label: 'antennal lobe'})
RETURN neuron, region
```

#### Find neurons with specific neurotransmitter types
```cypher
MATCH (neuron:Neuron)-[:INSTANCEOF]->(type:Class)
WHERE type.label CONTAINS 'GABAergic'
RETURN neuron, type
```

#### Find neurons in a specific lineage
```cypher
MATCH (neuron:Neuron)-[:INSTANCEOF]->(type:Class)-[:has_member]->(lineage)
WHERE lineage:lineage_DL1
RETURN neuron, type, lineage
```

#### Find synaptic connections between neurons
```cypher
MATCH (n1:Neuron)-[syn:synapsed_to]->(n2:Neuron)
WHERE n1:FAFB AND n2:FAFB
RETURN n1, syn, n2
LIMIT 10
```

#### Find neurons by morphology similarity (NBLAST)
```cypher
MATCH (n1:Neuron)-[sim:has_similar_morphology_to]->(n2:Neuron)
WHERE sim.NBLAST_score[0] > 0.8
RETURN n1, n2, sim.NBLAST_score[0] AS score
ORDER BY score DESC
LIMIT 10
```

#### Find anatomical parts of a brain region
```cypher
MATCH (part:Anatomy)-[:part_of]->(region:Anatomy {label: 'adult brain'})
RETURN part
```

#### Find genes expressed in a specific cell type
```cypher
MATCH (gene:Gene)<-[:expresses]-(ep:Expression_pattern)-[:overlaps]->(cell:Neuron)
WHERE cell.label CONTAINS ' Kenyon cell '
RETURN DISTINCT gene, ep
```

## Schema Details

### OLS OWL Representation

The core schema follows OLS conventions for representing OWL in Neo4j:

- Classes are represented as nodes with label `Class`
- Individuals as nodes with label `Individual`
- Properties as nodes with label `Property`
- Relationships use `Related` edges with property labels

### Denormalizations

For query performance, the schema includes denormalized named relationships alongside the generic `Related` edges. This allows efficient pattern matching without attribute filtering.

### Expression Data Model

Expression patterns are modeled as:
```cypher
(ep:Class:Expression_pattern)-[:SUBCLASSOF]->(:Class {label: 'expression pattern'})
(ep)-[:expresses]->(gene:Class)
(ep)<-[:INSTANCEOF]-(individual:Individual)
(ep)-[:overlaps]->(anatomy:Class)
```

### Connectivity Data

Synaptic connections are represented as:
```cypher
(neuron1:Individual)-[:synapsed_to {count: N}]->(neuron2:Individual)
```

Or with detailed synapse partonomy using GO terms.

## Data Sources

The PDB integrates data from:
- FlyBase (ontology terms, features, annotations)
- VFB Knowledge Base (connectivity data)
- External ontologies (FBbt, GO, etc.)
- Image datasets and annotations
- Third-party connectivity datasets
- Expression pattern data

## Updates and Maintenance

The PDB is updated regularly to incorporate new data releases and maintain consistency with upstream sources.