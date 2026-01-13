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

Base URL: `https://owl.virtualflybrain.org/kbs/vfb/`

**Note**: VFB provides a single knowledgebase (`vfb`) containing all VFB ontologies and reasoning data.

## DL Queries (Description Logic)

Owlery provides standard OWL DL query operations for reasoning over class hierarchies and relationships.

### Subclasses
```http
GET /kbs/vfb/subclasses/{class}
```

Get all subclasses of a named class or class expression.

**Parameters:**
- `class`: Class IRI or expression

**Query Parameters:**
- `direct`: `true` for direct subclasses only (default: `false`)

### Superclasses
```http
GET /kbs/vfb/superclasses/{class}
```

Get all superclasses of a named class or class expression.

### Equivalent Classes
```http
GET /kbs/vfb/equivalent/{class}
```

Get classes equivalent to the specified class.

### Instances
```http
GET /kbs/vfb/instances/{class}
```

Get all instances (individuals) of a class.

### Types
```http
GET /kbs/vfb/types/{individual}
```

Get all types (classes) of a named individual.

### Satisfiability
```http
GET /kbs/vfb/satisfiable/{class}
```

Check if a class expression is satisfiable (consistent).

## SPARQL Services

Owlery provides SPARQL query capabilities with OWL reasoning support.

### SPARQL Endpoint
```http
GET /kbs/vfb/sparql?query={sparql_query}
POST /kbs/vfb/sparql
```

Execute SPARQL queries with OWL reasoning. Supports Owlet-style embedded class expressions.

**Query Parameters (GET):**
- `query`: URL-encoded SPARQL query

**Request Body (POST):**
- Content-Type: `application/sparql-query`
- Body: SPARQL query text

### SPARQL Query Expander
```http
GET /kbs/vfb/expand?query={sparql_query}
POST /kbs/vfb/expand
```

Expand a SPARQL query by transforming Owlet-style embedded class expressions into FILTER clauses.

## VFB Query Integration

Owlery is extensively used in VFB's high-level query chains. The following table shows how VFB's named query operations map to Owlery API endpoints:

| VFB Query Operation | Owlery API Endpoint | Description |
|---------------------|-------------------|-------------|
| `Owlery Subclasses of` | `GET /kbs/vfb/subclasses/{class}` | Get all subclasses of a class |
| `Owlery Part of` | `GET /kbs/vfb/superclasses/{class}` | Get all superclasses/parts containing a class |
| `Owlery Instances` | `GET /kbs/vfb/instances/{class}` | Get all individuals of a class |
| `Owlery Neuron classes fasciculating here` | Complex query combining multiple endpoints | Find neurons that fasciculate together in a region |
| `Owlery Neuron class with part here` | Complex query with spatial reasoning | Find neuron classes with anatomical parts in a region |

### Common VFB Query Patterns

#### Find all anatomical subclasses of the adult brain
```http
GET /kbs/vfb/subclasses/FBbt_00003624
```
*Used in: PartsOf, SubclassesOf queries*

#### Find all neurons that are part of a specific type
```http
GET /kbs/vfb/instances/FBbt_00005106
```
*Used in: NeuronsPartHere, neuron classification queries*

#### Find all synaptic neuropils in the brain
```http
GET /kbs/vfb/subclasses/FBbt_00005106?direct=true
```
*Used in: NeuronsSynaptic, connectivity queries*

#### Check if a class expression is valid
```http
GET /kbs/vfb/satisfiable/FBbt_00003624
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
GET /kbs/vfb/subclasses/FBbt_00003624
# or using full IRI:
GET /kbs/vfb/subclasses/http://purl.obolibrary.org/obo/FBbt_00003624
```

#### Find all neurons in the antennal lobe
```http
GET /kbs/vfb/instances/FBbt_00007484
```

#### Find all synaptic neuropil subclasses
```http
GET /kbs/vfb/subclasses/FBbt_00005106
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