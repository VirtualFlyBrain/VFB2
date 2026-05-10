---
title: "SOLR Search API"
linkTitle: "SOLR API"
weight: 4
date: 2024-01-13
description: >
  The SOLR Search API provides fast text search and autocomplete functionality for VFB entities, datasets, and publications.
---

The SOLR Search API powers VFB's search and autocomplete functionality, providing fast text-based queries across all VFB entities including anatomical terms, neurons, datasets, publications, and more.

**Note**: Search and autocomplete functionality is also built into [VFBconnect](https://vfb-connect.readthedocs.io/en/stable/) by default. The `vfb.term()` method will automatically attempt to match partial terms and provide autocomplete suggestions. See the [VFBconnect documentation](https://vfb-connect.readthedocs.io/en/stable/tutorials/vfb_terms.html#Creating-and-Exploring-VFBTerm-Objects) for programmatic access.

## API Endpoint

Base URL: `https://solr.virtualflybrain.org/solr/ontology/select`

**Note**: VFB uses JSON-formatted parameter requests for complex queries.

## Search Parameters

### Core Search Parameters

| Parameter | Description | VFB Default | Example |
|-----------|-------------|-------------|---------|
| `q` | Main search query (supports SOLR query syntax) | Complex expansion | `(medulla OR medulla* OR *medulla OR *medulla*)` |
| `defType` | Query parser type | `edismax` | `edismax` |
| `mm` | Minimum match percentage for multi-term queries | `45%` | `45%` |
| `qf` | Query fields with boost values | `label^110 synonym^100 label_autosuggest synonym_autosuggest shortform_autosuggest` | `label^110 synonym^100...` |
| `fl` | Fields to return | `short_form,label,synonym,id,facets_annotation,unique_facets` | `short_form,label,synonym,id,facets_annotation,unique_facets` |
| `rows` | Number of results to return | `150` | `50` |
| `start` | Starting offset for pagination | `0` | `0` |
| `wt` | Response format | `json` | `json` |
| `indent` | Pretty-print JSON response | `true` | `true` |

### Query Field Boosting (qf)

VFB uses sophisticated field boosting for optimal search results:

- `label^110` - Primary labels get highest boost
- `synonym^100` - Synonyms get high boost  
- `label_autosuggest` - Autosuggest-optimized labels
- `synonym_autosuggest` - Autosuggest-optimized synonyms
- `shortform_autosuggest` - Autosuggest-optimized short forms

### Query Expansion

VFB automatically expands search terms for better matching:
- Original term: `medulla`
- Expanded to: `(medulla OR medulla* OR *medulla OR *medulla*)`

This catches prefix, suffix, and infix matches.

### Filter Queries (fq)

VFB applies specific filter queries to focus results on relevant entities:

```http
fq=(short_form:VFB* OR short_form:FB* OR facets_annotation:DataSet OR facets_annotation:pub) AND NOT short_form:VFBc_*
```

This filter includes:
- VFB entities (`VFB*`) including anatomical individuals (`VFB_*`), expression patterns (`VFBexp*`), and extension ontology terms (`VFBext*`)
- FlyBase entities (`FB*`)
- Datasets (`facets_annotation:DataSet`)
- Publications (`facets_annotation:pub`)

And excludes:
- VFB image channel node entries (`VFBc_*`) - as opposed to anatomical individuals (`VFB_*`)

### Boost Parameters (bq)

VFB uses boost queries to prioritize certain types of results:

```http
bq=short_form:VFBexp*^10.0 short_form:VFB*^100.0 short_form:FBbt*^100.0 short_form:FBbt_00003982^2 facets_annotation:Deprecated^0.001 facets_annotation:DataSet^500.0 facets_annotation:pub^100.0
```

**Boost Priorities:**
- Expression patterns (`VFBexp*`): 10x boost
- VFB entities (`VFB*`): 100x boost
- Anatomy terms (`FBbt*`): 100x boost
- Adult brain (`FBbt_00003982`): 2x boost
- Datasets: 500x boost
- Publications: 100x boost
- Deprecated items: 0.001x (demoted)

### Additional Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `pf` | Phrase fields for exact phrase boosting | `true` |
| `indent` | Pretty-print JSON response | `true` |

## Response Format

### JSON Response Structure

```json
{
  "responseHeader": {
    "status": 0,
    "QTime": 15,
    "params": {...}
  },
  "response": {
    "numFound": 1234,
    "start": 0,
    "docs": [
      {
        "short_form": "FBbt_00007484",
        "label": "antennal lobe",
        "synonym": ["antennal lobe"],
        "id": "http://purl.obolibrary.org/obo/FBbt_00007484",
        "facets_annotation": ["Adult", "Nervous_system"],
        "unique_facets": ["adult antennal lobe", "nervous system"]
      }
    ]
  }
}
```

### Field Descriptions

| Field | Description |
|-------|-------------|
| `short_form` | VFB/FlyBase short identifier |
| `label` | Primary display name |
| `synonym` | Alternative names and synonyms |
| `id` | Full IRI/URI identifier |
| `facets_annotation` | Categorization facets (e.g., "Adult", "Nervous_system") |
| `unique_facets` | Processed facet combinations for display |

## Search Examples

### JSON Parameter Format (VFB Standard)

VFB uses JSON-formatted parameter requests for complex queries:

```http
GET /solr/ontology/select?json={"params":{"q":"(medulla OR medulla* OR *medulla OR *medulla*)","q.op":"OR","defType":"edismax","mm":"45%","qf":"label^110 synonym^100 label_autosuggest synonym_autosuggest shortform_autosuggest","indent":"true","fl":"short_form,label,synonym,id,facets_annotation,unique_facets","start":"0","pf":"true","fq":["(short_form:VFB* OR short_form:FB* OR facets_annotation:DataSet OR facets_annotation:pub) AND NOT short_form:VFBc_*"],"rows":"150","wt":"json","bq":"short_form:VFBexp*^10.0 short_form:VFB*^100.0 short_form:FBbt*^100.0 short_form:FBbt_00003982^2 facets_annotation:Deprecated^0.001 facets_annotation:DataSet^500.0 facets_annotation:pub^100.0"}}
```

### URL-Encoded Parameters (Alternative)

For simpler queries, you can use traditional URL parameters:

```http
GET /solr/ontology/select?q=medulla&fl=short_form,label,synonym,id&rows=10&wt=json
```

### Autocomplete Query Example

The medulla autocomplete query expands to match various forms:

**Query Breakdown:**
- `q`: `(medulla OR medulla* OR *medulla OR *medulla*)` - Matches medulla at start, middle, or end
- `defType`: `edismax` - Extended dismax query parser for complex queries
- `mm`: `45%` - At least 45% of query terms must match
- `qf`: Field boosting for optimal relevance
- `fq`: Filters to include relevant entities only
- `bq`: Boosts for prioritizing certain result types

### Simple Search Examples

#### Basic term search
```http
GET /solr/ontology/select?q=antennal&rows=10&wt=json&fl=short_form,label
```

#### Dataset search
```http
GET /solr/ontology/select?q=dataset&fq=facets_annotation:DataSet&rows=20&wt=json
```

#### Publication search
```http
GET /solr/ontology/select?q=connectome&fq=facets_annotation:pub&rows=10&wt=json
```

## Autocomplete Usage

VFB's autocomplete functionality uses this SOLR API with specific parameters optimized for fast, relevant suggestions:

### Autocomplete Query
```http
GET /solr/vfb_olympiad/select?q=antennal&fl=short_form,label,synonym,id,facets_annotation,unique_facets&start=0&rows=150&wt=json&pf=true&fq=(short_form:VFB*%20OR%20short_form:FB*%20OR%20facets_annotation:DataSet%20OR%20facets_annotation:pub)%20AND%20NOT%20short_form:VFBc_*&bq=short_form:VFBexp*^10.0%20short_form:VFB*^100.0%20short_form:FBbt*^100.0%20short_form:FBbt_00003982^2%20facets_annotation:Deprecated^0.001%20facets_annotation:DataSet^500.0%20facets_annotation:pub^100.0
```

## Integration with VFB

The SOLR API is a core component of VFB's search infrastructure:

1. **Web Interface**: Powers the main search box and autocomplete
2. **Query Chains**: Used in combination with PDB and Owlery queries
3. **Result Ranking**: Complex sorting logic prioritizes relevant results
4. **Facet Filtering**: Enables filtering by categories like "Adult", "Larva", etc.

### Result Processing

VFB applies additional client-side processing to SOLR results:
- **Sorting**: Custom ranking based on match quality and entity type
- **Deduplication**: Removes duplicate entries
- **Facet Processing**: Converts facet annotations to user-friendly labels

## Performance Notes

- **Caching**: VFB implements caching for frequently searched terms
- **Pagination**: Use `start` and `rows` for large result sets
- **Query Optimization**: Complex queries may benefit from the `pf` (phrase fields) parameter
- **Rate Limiting**: Consider implementing delays between rapid autocomplete requests

## Error Handling

SOLR returns standard HTTP status codes:
- `200`: Success
- `400`: Bad request (malformed query)
- `500`: Server error

Error responses include details in the response header.