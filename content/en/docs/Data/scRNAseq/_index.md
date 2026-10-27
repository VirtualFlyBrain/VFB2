---
title: "Single Cell RNA Sequencing Data"
linkTitle: "scRNAseq Data"
weight: 510
date: 2026-08-15
description: >
    scRNAseq Data available on Virtual Fly Brain.

---

VFB integrates single-cell and single-nucleus RNA sequencing data by connecting it to
anatomy: each cluster from a published study is annotated with the Drosophila Anatomy
Ontology term for the cell type it corresponds to, so that a query for a cell type
returns its transcriptomic clusters alongside its images and connectivity. The
sequencing itself is not VFB's; the anatomical annotation and the cross-linking are.

{{< vfb-figures set="scrnaseq" >}}

VFB curates these datasets itself, in
[vfb-scRNAseq](https://github.com/VirtualFlyBrain/vfb-scRNAseq). For each study, the
clusters are the authors' own, taken with their cell-type annotations from GEO,
ArrayExpress, the paper or the authors' published analysis, and each cluster is mapped
to the Drosophila Anatomy Ontology term for the cell type it is composed primarily of. Clusters
that no anatomy term describes well enough are held back rather than given a vague
term, so every cluster VFB shows has a cell type. Expression is summarised per cluster
from the authors' count data. The studies include the
[Fly Cell Atlas](https://flycellatlas.org/) and the
[Aging Fly Cell Atlas](https://hongjielilab.org/afca/).

## Finding clusters and genes

Clusters for a cell type are reached through the `Single cell transcriptomics data for…`
query on that cell type's Term Info pane. Datasets themselves are found by searching for
`scRNAseq` and filtering to `Dataset`.

![transcriptomics_query](https://www.virtualflybrain.org/images/scRNAseq/cluster_query.png)

Genes in a cluster can be filtered by function and sorted by expression level and by
extent — the proportion of cells in the cluster expressing the gene. As with other VFB
result tables, the list exports as CSV.

_Only genes with extent > 0.2 in a cluster are included._

![cluster_genes](https://www.virtualflybrain.org/images/scRNAseq/gene_expression.png)

The same queries are available through
[VFB_connect](https://vfb-connect.readthedocs.io/en/stable/API_reference.html#transcriptomics-queries).

## Datasets

Gene counts are after the extent filter above, so they are lower than the gene count
reported by the original study. Ordered by cluster count. Datasets that span several
stages are listed once on [Datasets by stage](/docs/data/stages/), at their earliest.

| Dataset | Stage | Study | Clusters | Genes |
|---|---|---|---|---|
| [scRNAseq data from Özel (2021)](https://virtualflybrain.org/reports/VFBseq_00001758) | Pupa, adult | Neuronal diversity and convergence in a visual system developmental atlas | 522 | 8,138 |
| [scRNAseq data from Li (2022), 10x](https://virtualflybrain.org/reports/VFBseq_00000538) | Adult | Fly Cell Atlas: A single-nucleus transcriptomic atlas of the adult fruit fly | 335 | 12,747 |
| [scRNAseq data from Kurmangaliyev (2020)](https://virtualflybrain.org/reports/VFBseq_00000001) | Pupa | Transcriptional Programs of Circuit Assembly in the Drosophila Visual System | 232 | 7,473 |
| [scRNAseq data from Calderon (2022)](https://virtualflybrain.org/reports/VFBseq_00002863) | Embryo | The continuum of Drosophila embryonic development at single-cell resolution | 223 | 4,539 |
| [scRNAseq data from Li (2022), Smart-seq2](https://virtualflybrain.org/reports/VFBseq_00000777) | Adult | Fly Cell Atlas: A single-nucleus transcriptomic atlas of the adult fruit fly | 211 | 15,011 |
| [scRNAseq data from Lu (2023)](https://virtualflybrain.org/reports/VFBseq_00001468) | Adult | Aging Fly Cell Atlas identifies exhaustive aging features at cellular resolution | 143 | 5,399 |
| [scRNAseq data from Allen (2020)](https://virtualflybrain.org/reports/VFBseq_00002728) | Adult | A single-cell transcriptomic atlas of the adult Drosophila ventral nerve cord | 106 | 6,264 |
| [scRNAseq data from Xie (2021)](https://virtualflybrain.org/reports/VFBseq_00002581) | Prepupa, pupa, adult | Temporal evolution of single-cell transcriptomes of Drosophila olfactory projection neurons | 92 | 8,317 |
| [scRNAseq data from Davie (2018)](https://virtualflybrain.org/reports/VFBseq_00000243) | Adult | A Single-Cell Transcriptome Atlas of the Aging Drosophila Brain | 82 | 6,704 |
| [scRNAseq data from Konstantinides (2022)](https://virtualflybrain.org/reports/VFBseq_00002364) | L3 larva | A complete temporal transcription factor series in the fly visual system | 75 | 7,154 |
| [scRNAseq data from Hörmann (2020)](https://virtualflybrain.org/reports/VFBseq_00002461) | Pupa | A combinatorial code of transcription factors specifies subtypes of visual motion-sensing neurons in Drosophila | 40 | 3,874 |
| [scRNAseq data from Brunet Avalos (2019)](https://virtualflybrain.org/reports/VFBseq_00003150) | L1 larva | Single cell transcriptome atlas of the Drosophila larval brain | 28 | 6,772 |
| [scRNAseq data from Mokashi (2021)](https://virtualflybrain.org/reports/VFBseq_00003188) | Adult | Developmental Alcohol Exposure in Drosophila: Effects on Adult Phenotypes and Gene Expression in the Brain | 26 | 3,664 |
| [scRNAseq data from Baker (2021)](https://virtualflybrain.org/reports/VFBseq_00003265) | Adult | The Drosophila brain on cocaine at single-cell resolution | 22 | 3,634 |
| [scRNAseq data from Li (2017)](https://virtualflybrain.org/reports/VFBseq_00002527) | Pupa, adult | Classifying Drosophila Olfactory Projection Neuron Subtypes by Single-Cell RNA Sequencing | 22 | 7,562 |
| [scRNAseq data from Saavedra (2023)](https://virtualflybrain.org/reports/VFBseq_00003198) | Adult | REPTOR and CREBRF encode key regulators of muscle energy metabolism | 14 | 1,402 |
| [scRNAseq data from Ing-Simmons (2021)](https://virtualflybrain.org/reports/VFBseq_00002844) | Embryo | Independence of chromatin conformation and gene regulation during Drosophila dorsoventral patterning | 13 | 6,763 |

Clusters a study left untyped, or typed only as a generic cell or neuron, are not
loaded, so these counts can be lower than the study's own. Counts here are of what VFB
holds, and are regenerated with the [content report](/blog/2022/01/01/vfb-content-report/)
after each data release; the machine-readable version is
[scRNAseq_DataSets.tsv](https://github.com/VirtualFlyBrain/VFB_reporting_results/blob/master/scRNAseq_DataSets.tsv).
