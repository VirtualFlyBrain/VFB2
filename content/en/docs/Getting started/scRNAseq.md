---
categories: ["overview","help"]
tags: ["scRNAseq","tools"]
title: "Single cell RNAseq data"
linkTitle: "scRNAseq data"
description: >
   Single cell RNAseq data on VFB. 
weight: 9000
---

## Finding gene expression data on VFB

### Finding cell type clusters
Cell types with available scRNAseq data can be identified using the 'Has scRNAseq data filter' when searching.

<p align="center">
  <img src="https://www.virtualflybrain.org/images/scRNAseq/scRNAseq_search.png" alt="scRNAseq filtered search" style="max-width=50%" />
</p>

Clusters for a cell type of interest can be found via the 'Single cell transcriptomics data for...' query.

<p align="center">
  <img src="https://www.virtualflybrain.org/images/scRNAseq/cluster_query.png" alt="scRNAseq cluster query" style="max-width=50%" />
</p>

### Gene expression data
After selecting a cluster, gene expression can be retrieved via the 'Genes expressed in...' query.

<p align="center">
  <img src="https://www.virtualflybrain.org/images/scRNAseq/gene_expression.png" alt="gene expression filtered to GPCRs" style="max-width=50%" />
</p>

Expression level is the mean counts per million reads of all cells in the cell type cluster that express the given gene. Expression extent is the proportion of cells within the cluster that express the given gene. VFB only shows genes that are expressed in at least 20% of cells in the cluster (Extent > 0.2).

### Gene semantic tags
We add semantic tags to genes to allow quick searching and filtering of results ('Function' column of gene expression data). These tags are based on FlyBase Gene Group membership and GO annotations, which are all sourced from FlyBase. A full list of gene tags with their associated Gene group and GO terms can be found [here](https://github.com/VirtualFlyBrain/vfb-scRNAseq-gene-annotations/blob/main/src/ontology/gene_functions.tsv).

### API
Data can also be retrieved using [VFB_connect](https://pypi.org/project/vfb-connect/).

[Tutorial](https://vfb-connect.readthedocs.io/en/stable/tutorials/discovery.html#Finding-single-cell-transcriptomics-data-for-a-given-cell-type)

[Documentation](https://vfb-connect.readthedocs.io/en/stable/API_reference.html#transcriptomics-queries)


## Data sources and processing
1. Raw scRNAseq data is ingested by the EBI Single Cell Expression Atlas (SCEA). Where possible, cells are linked to cell types from the [Drosophila Anatomy Ontology](https://www.ebi.ac.uk/ols4/ontologies/fbbt) based on author annotations. Data is reprocessed, filtered and reclustered.
2. FlyBase takes data from EBI, keeping only cells that are linked to ontology terms and generating summary expression data for each cell type (cluster).
3. VFB takes control/wild type expression data from FlyBase for datasets where at least one nervous system cell type is present and filter out any genes expressed in less than 20% of cells per cluster.


## Database schema
A simplified schema showing how scRNAseq data is stored in the VFB Neo4j database is shown below:

<p align="center">
  <img src="https://www.virtualflybrain.org/images/scRNAseq/scRNAseq_schema.png" alt="scRNAseq schema" style="max-width=50%" />
</p>

Cell types are classes from the Drosophila Anatomy Ontology and are also linked to several other types of data in VFB, such as images, connectomics and driver expression information.

