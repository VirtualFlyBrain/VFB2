---
categories: ["overview","help"]
tags: ["scRNAseq","tools"]
title: "Browsing single cell RNAseq data"
linkTitle: "scRNAseq data"
description: >
   How to navigate single cell RNAseq data on VFB. 
weight: 418
---

## Finding transcriptomics data on VFB

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
1. VFB curates each dataset in [vfb-scRNAseq](https://github.com/VirtualFlyBrain/vfb-scRNAseq). The clusters are the authors' own, with their cell-type annotations, taken from GEO, ArrayExpress, the paper or the authors' published analysis. Samples record the stage, sex, tissue and genotype or stock. Where a study compares treatments or mutants, VFB uses the control samples.
2. Each cluster is mapped to the [Drosophila Anatomy Ontology](https://www.ebi.ac.uk/ols4/ontologies/fbbt) term for the cell type it is composed primarily of. A cluster with no adequate term is held back rather than given a vague one, and is not shown in VFB.
3. Summary expression is calculated per cluster from the authors' count data (counts per million), and genes expressed in less than 20% of a cluster's cells are left out. Gene ids are kept current with FlyBase.


## Database schema
A simplified schema showing how scRNAseq data is stored in the VFB Neo4j database is shown below:

<p align="center">
  <img src="https://www.virtualflybrain.org/images/scRNAseq/scRNAseq_schema.png" alt="scRNAseq schema" style="max-width=50%" />
</p>

Cell types are classes from the Drosophila Anatomy Ontology and are also linked to several other types of data in VFB, such as images, connectomics and driver expression information.

