---
title: "Owlery API"
linkTitle: "Owlery API"
weight: 3
date: 2024-01-13
description: >
  The Owlery API provides OWL reasoning services for VFB's ontologies, enabling complex queries over class hierarchies and relationships.
---

The Owlery API is VFB's OWL (Web Ontology Language) reasoning service, providing advanced query capabilities over the ontologies used in VFB. It enables Description Logic (DL) queries, SPARQL queries with OWL reasoning, and access to multiple knowledgebases.

## API Endpoint

Base URL: `https://owl.virtualflybrain.org/`

**Note**: VFB provides a single knowledgebase (`vfb`) containing all VFB ontologies and reasoning data. All examples in this documentation use the `vfb` knowledgebase.

## Knowledgebase Operations

**Note**: VFB provides access to a single knowledgebase (`vfb`) containing all VFB ontologies and reasoning data. The general `/kbs` endpoint is not accessible - all operations must use `/kbs/vfb/`.

### Get Knowledgebase Information
```http
GET /kbs/vfb
```

Display information and status for the VFB knowledgebase.

**Response**: JSON object with KB information

## DL Queries (Description Logic)

Owlery provides standard OWL DL query operations for reasoning over class hierarchies and relationships using Manchester syntax.

### Subclasses
```http
GET /kbs/vfb/subclasses
```

Get subclasses of a named class or class expression.

**Parameters:**
- `object` (query): Manchester-syntax OWL class expression
- `prefixes` (query): JSON format prefix map for expanding prefixes
- `direct` (query): `true` for direct subclasses only (default: `true`)
- `includeEquivalent` (query): Include equivalent classes (default: `false`)
- `includeNothing` (query): Include owl:Nothing (default: `false`)
- `includeDeprecated` (query): Include deprecated terms (default: `true`)

### Superclasses
```http
GET /kbs/vfb/superclasses
```

Get superclasses of a named class or class expression.

**Parameters:**
- `object` (query): Manchester-syntax OWL class expression
- `prefixes` (query): JSON format prefix map
- `direct` (query): `true` for direct superclasses only (default: `true`)
- `includeEquivalent` (query): Include equivalent classes (default: `false`)
- `includeThing` (query): Include owl:Thing (default: `false`)
- `includeDeprecated` (query): Include deprecated terms (default: `true`)

### Equivalent Classes
```http
GET /kbs/vfb/equivalent
```

Get equivalent classes of a named class or class expression.

**Parameters:**
- `object` (query): Manchester-syntax OWL class expression
- `prefixes` (query): JSON format prefix map
- `direct` (query): `true` for direct equivalents only (default: `true`)
- `includeDeprecated` (query): Include deprecated terms (default: `true`)

### Satisfiability
```http
GET /kbs/vfb/satisfiable
```

Check if a class expression is satisfiable.

**Parameters:**
- `object` (query): Manchester-syntax OWL class expression
- `prefixes` (query): JSON format prefix map

**Response**: Boolean indicating satisfiability

### Instances
```http
GET /kbs/vfb/instances
```

Get instances of a named class or class expression.

**Parameters:**
- `object` (query): Manchester-syntax OWL class expression
- `prefixes` (query): JSON format prefix map
- `direct` (query): `true` for direct instances only (default: `true`)
- `includeDeprecated` (query): Include deprecated terms (default: `true`)

### Types
```http
GET /kbs/vfb/types
```

Get types (classes) of a named individual.

**Parameters:**
- `object` (query): Individual IRI
- `prefixes` (query): JSON format prefix map
- `direct` (query): `true` for direct types only (default: `true`)
- `includeThing` (query): Include owl:Thing (default: `false`)
- `includeDeprecated` (query): Include deprecated terms (default: `true`)

## SPARQL Services

Owlery provides SPARQL query capabilities with OWL reasoning support using Owlet-style embedded class expressions.

### SPARQL Query (GET)
```http
GET /kbs/vfb/sparql
```

Perform SPARQL query encoded in URL parameter.

**Parameters:**
- `query` (query): SPARQL query string

**Response**: SPARQL results in XML format (`application/sparql-results+xml`)

### SPARQL Query (POST)
```http
POST /kbs/vfb/sparql
```

Perform SPARQL query contained in request body.

**Request Body:**
- Content-Type: `application/sparql-query`
- Body: SPARQL query text

**Response**: SPARQL results

### SPARQL Query Expansion (GET)
```http
GET /kbs/vfb/expand
```

Expand a SPARQL query by transforming Owlet-style embedded class expressions into FILTERs.

**Parameters:**
- `query` (query): SPARQL query string

**Response**: Expanded SPARQL query (`application/sparql-query`)

### SPARQL Query Expansion (POST)
```http
POST /kbs/vfb/expand
```

Expand a SPARQL query contained in request body.

**Request Body:**
- Content-Type: `application/sparql-query`
- Body: SPARQL query text

**Response**: Expanded SPARQL query

## VFB Query Integration

VFB extensively uses Owlery for its high-level query operations. The following table shows how VFB's named query operations map to Owlery API endpoints, focusing on the `vfb` knowledgebase:

| VFB Query Operation | Owlery API Call | Description |
|---------------------|-----------------|-------------|
| `Owlery Subclasses of` | `GET /kbs/vfb/subclasses?object={IRI}&direct=false&includeDeprecated=false&includeEquivalent=true` | Get all subclasses of a class |
| `Owlery Part of` | `GET /kbs/vfb/superclasses?object={IRI}&direct=false&includeDeprecated=false&includeEquivalent=true` | Get all superclasses/parts containing a class |
| `Owlery Neuron class with part here` | `GET /kbs/vfb/subclasses?object=<http://purl.obolibrary.org/obo/FBbt_00005106> and <http://purl.obolibrary.org/obo/RO_0002131> some {IRI}&direct=false&includeDeprecated=false&includeEquivalent=true` | Find neuron classes with anatomical parts in a region |
| `Owlery Neurons Synaptic` | `GET /kbs/vfb/subclasses?object=<http://purl.obolibrary.org/obo/FBbt_00005106> and <http://purl.obolibrary.org/obo/RO_0002130> some {IRI}&direct=false&includeDeprecated=false&includeEquivalent=true` | Find neurons with synaptic terminals in a region |
| `Owlery Neurons Presynaptic` | `GET /kbs/vfb/subclasses?object=<http://purl.obolibrary.org/obo/FBbt_00005106> and <http://purl.obolibrary.org/obo/RO_0002113> some {IRI}&direct=false&includeDeprecated=false&includeEquivalent=true` | Find neurons with presynaptic terminals in a region |
| `Owlery Neurons Postsynaptic` | `GET /kbs/vfb/subclasses?object=<http://purl.obolibrary.org/obo/FBbt_00005106> and <http://purl.obolibrary.org/obo/RO_0002110> some {IRI}&direct=false&includeDeprecated=false&includeEquivalent=true` | Find neurons with postsynaptic terminals in a region |
| `Owlery Neuron classes fasciculating here` | `GET /kbs/vfb/subclasses?object=<http://purl.obolibrary.org/obo/FBbt_00005106> and <http://purl.obolibrary.org/obo/RO_0002101> some {IRI}&direct=false&includeDeprecated=false&includeEquivalent=true` | Find neurons that fasciculate together in a region |
| `Owlery tracts in` | `GET /kbs/vfb/subclasses?object=<http://purl.obolibrary.org/obo/FBbt_00005099> and <http://purl.obolibrary.org/obo/RO_0002134> some {IRI}&direct=false&includeDeprecated=false&includeEquivalent=true` | Find tracts/nerves innervating a region |
| `Owlery Lineage Clones` | `GET /kbs/vfb/subclasses?object=<http://purl.obolibrary.org/obo/FBbt_00007683> and <http://purl.obolibrary.org/obo/RO_0002131> some {IRI}&direct=false&includeDeprecated=false&includeEquivalent=true` | Find lineage clones in a region |
| `Owlery Transgenes expressed in` | `GET /kbs/vfb/subclasses?object=<http://purl.obolibrary.org/obo/SO_0001059> and <http://purl.obolibrary.org/obo/RO_0002292> some {IRI}&direct=false&includeDeprecated=false&includeEquivalent=true` | Find transgenes expressed in a region |
| `Owlery Images of neurons with some part here` | `GET /kbs/vfb/instances?object=<http://purl.obolibrary.org/obo/FBbt_00005106> and <http://purl.obolibrary.org/obo/RO_0002131> some {IRI}&direct=false&includeDeprecated=false` | Find individual neurons with anatomical parts in a region |
| `Owlery individual parts` | `GET /kbs/vfb/instances?object=<http://purl.obolibrary.org/obo/BFO_0000050> some {IRI}&direct=false&includeDeprecated=false` | Find individuals that are part of some anatomical entity |
| `Images of neurons that develops from this` | `GET /kbs/vfb/instances?object=<http://purl.obolibrary.org/obo/FBbt_00005106> and <http://purl.obolibrary.org/obo/RO_0002202> some {IRI}&direct=false&includeDeprecated=false` | Find individual neurons that develop from a particular anatomical entity |

### Common VFB Query Patterns

#### Find all anatomical subclasses of the adult brain
```http
GET /kbs/vfb/subclasses?object=FBbt_00003624&direct=false&includeDeprecated=false&includeEquivalent=true
```
*Used in: PartsOf, SubclassesOf queries*

#### Find all neurons with some part in the antennal lobe
```http
GET /kbs/vfb/subclasses?object=<http://purl.obolibrary.org/obo/FBbt_00005106> and <http://purl.obolibrary.org/obo/RO_0002131> some FBbt_00007484&direct=false&includeDeprecated=false&includeEquivalent=true
```
*Used in: NeuronsPartHere, neuron classification queries*

#### Find all synaptic neuropils in the brain
```http
GET /kbs/vfb/subclasses?object=FBbt_00005106&direct=false&includeDeprecated=false&includeEquivalent=true
```
*Used in: NeuronsSynaptic, connectivity queries*

#### Check if a class expression is valid
```http
GET /kbs/vfb/satisfiable?object=FBbt_00003624
```
*Used in: Query validation and reasoning checks*

### Complex Query Examples

Many VFB queries combine Owlery with other services. For example, the "Neurons with presynaptic terminals in antennal lobe" query typically involves:

1. **Owlery reasoning**: Find anatomical subclasses of the antennal lobe
2. **Neo4j lookup**: Find neurons with presynaptic terminals in those regions
3. **SOLR search**: Retrieve associated images and metadata

While these complex queries are handled by VFB's query orchestration system, the individual Owlery components can be called directly for custom analyses.

## Usage Examples

**Note**: VFB supports both full IRIs (e.g., `http://purl.obolibrary.org/obo/FBbt_00003624`) and short forms (e.g., `FBbt_00003624`) for class identifiers.

### Basic Ontology Queries

#### Find all parts of the adult brain
```http
GET /kbs/vfb/subclasses?object=FBbt_00003624
# or using full IRI:
GET /kbs/vfb/subclasses?object=http://purl.obolibrary.org/obo/FBbt_00003624
```

#### Find all neurons in the antennal lobe
```http
GET /kbs/vfb/instances?object=FBbt_00007484
```

#### Find all synaptic neuropil subclasses
```http
GET /kbs/vfb/subclasses?object=FBbt_00005106
```

### SPARQL Reasoning Examples

#### Find GABAergic neurons using OWL reasoning
```sparql
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?neuron ?label
WHERE {
  ?neuron rdfs:subClassOf <http://purl.obolibrary.org/obo/FBbt_00005106> .
  ?neuron rdfs:label ?label .
  FILTER(CONTAINS(?label, "GABA"))
}
```

#### Find anatomical parts with expression data
```sparql
PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT ?part ?expression
WHERE {
  ?part rdfs:subClassOf <http://purl.obolibrary.org/obo/FBbt_00003624> .
  ?expression <http://purl.obolibrary.org/obo/RO_0002292> ?part .
}
```

## Response Formats

Owlery returns results in JSON format by default. Available formats include:

- `application/json` (default)
- `text/plain`
- `application/rdf+xml`
- `text/turtle`

Specify format using the `Accept` header or `format` query parameter.

## Error Handling

Owlery returns standard HTTP status codes:
- `200`: Success
- `400`: Bad request (invalid query/parameters)
- `404`: Knowledgebase or resource not found
- `500`: Server error

Error responses include JSON with error details:
```json
{
  "error": "Error message",
  "details": "Additional information"
}
```

## Integration with VFB

Owlery is a core component of VFB's query system, providing the reasoning capabilities that power complex anatomical and connectivity queries. It's used in combination with the PDB (Neo4j) and SOLR search services to deliver comprehensive results to users.