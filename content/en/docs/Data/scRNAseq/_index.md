---
title: "Single Cell RNA Sequencing Data"
linkTitle: "scRNAseq Data"
weight: 15
description: >
    scRNAseq Data available on Virtual Fly Brain.

---

Virtual Fly Brain incorporates scRNAseq data from multiple studies, including the [Fly Cell Atlas](https://flycellatlas.org/), [Aging Fly Cell Atlas](https://hongjielilab.org/afca/) and other datasets that identify nervous system cell types - full list [here](https://github.com/VirtualFlyBrain/VFB_reporting_results/blob/master/scRNAseq_DataSets.tsv). These datasets can be found by searching for 'scRNAseq' and filtering to 'Dataset'.

Clusters can be found for particular cell types via the `Single cell transcriptomics data for..` query on the cell type Term Info pane.

![transcriptomics_query](https://www.virtualflybrain.org/images/scRNAseq/cluster_query.png)

Genes for a particular cluster can be filtered by function and sorted by expression level and extent (proportion of cells in cluster expressing the gene). As with other VFB search results, these can be exported as a csv.

_Note that we currently only include genes that have extent > 0.2 in a cluster._

![cluster_genes](https://www.virtualflybrain.org/images/scRNAseq/gene_expression.png)

Data can also be retrieved using [VFB_connect](https://vfb-connect.readthedocs.io/en/stable/API_reference.html#transcriptomics-queries).

We pull scRNAseq data from [FlyBase](https://flybase.org/), which takes it from the [Single Cell Expression Atlas](https://www.ebi.ac.uk/gxa/sc/home).
