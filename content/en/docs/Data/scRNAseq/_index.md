---
title: "Single Cell RNA Sequencing Data"
linkTitle: "scRNAseq Data"
weight: 15
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

Data comes from [FlyBase](https://flybase.org/), which takes it from the
[Single Cell Expression Atlas](https://www.ebi.ac.uk/gxa/sc/home). The studies include
the [Fly Cell Atlas](https://flycellatlas.org/) and the
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
reported by the original study. Ordered by cluster count.

| Dataset | Study | Clusters | Genes |
|---|---|---|---|
| [scRNAseq_2022_FCA_MIXED](https://flybase.org/reports/FBlc0004785) | Single-nucleus RNA-seq on cells from 5-days old female and male flies | 497 | 11,079 |
| [scRNAseq_2022_FCA_MALE](https://flybase.org/reports/FBlc0004307) | Single-nucleus RNA-seq on cells from 5-days old male flies | 422 | 10,978 |
| [scRNAseq_2022_FCA_FEMALE](https://flybase.org/reports/FBlc0003846) | Single-nucleus RNA-seq on cells from 5-days old female flies | 411 | 8,169 |
| [scRNAseq_2022_Calderon](https://flybase.org/reports/FBlc0007797) | The continuum of Drosophila embryonic development at single-cell resolution | 274 | 2,166 |
| [scRNAseq_2023_AFCA_D30_FEMALE](https://flybase.org/reports/FBlc0006424) | Single-nucleus RNA-seq on cells from 30-days old female flies | 179 | 4,987 |
| [scRNAseq_2023_AFCA_D70_FEMALE](https://flybase.org/reports/FBlc0007348) | Single-nucleus RNA-seq on cells from 70-days old female flies | 176 | 5,458 |
| [scRNAseq_2023_AFCA_D50_FEMALE](https://flybase.org/reports/FBlc0006888) | Single-nucleus RNA-seq on cells from 50-days old female flies | 175 | 4,595 |
| [scRNAseq_2023_AFCA_D50_MALE](https://flybase.org/reports/FBlc0007071) | Single-nucleus RNA-seq on cells from 50-days old male flies | 172 | 4,878 |
| [scRNAseq_2023_AFCA_D30_MALE](https://flybase.org/reports/FBlc0006611) | Single-nucleus RNA-seq on cells from 30-days old male flies | 168 | 4,857 |
| [scRNAseq_2023_AFCA_D70_MALE](https://flybase.org/reports/FBlc0007532) | Single-nucleus RNA-seq on cells from 70-days old male flies | 161 | 4,835 |
| [scRNAseq_2023_AFCA_D30](https://flybase.org/reports/FBlc0006423) | Single-nucleus RNA-seq on cells from 30-days old flies | 99 | 5,312 |
| [scRNAseq_2023_AFCA_D70](https://flybase.org/reports/FBlc0007347) | Single-nucleus RNA-seq on cells from 70-days old flies | 95 | 5,592 |
| [scRNAseq_2023_AFCA_D50](https://flybase.org/reports/FBlc0006887) | Single-nucleus RNA-seq on cells from 50-days old flies | 95 | 5,015 |
| [scRNAseq_2021_Ozel](https://flybase.org/reports/FBlc0005659) | Single-cell RNA-seq study of pupal and adult optic lobes | 66 | 4,770 |
| [scRNAseq_2020_Kurmangaliyev](https://flybase.org/reports/FBlc0006237) | Single-cell RNA-seq study of the pupal optic lobe | 62 | 5,975 |
| [scRNAseq_2018_Davie](https://flybase.org/reports/FBlc0006090) | Single-cell RNA-seq study of the aging brain | 59 | 6,111 |
| [scRNAseq_2020_Hormann](https://flybase.org/reports/FBlc0006305) | Single-cell RNA-seq study of visual motion-sensing neurons | 40 | 4,014 |
| [scRNAseq_2021_Mokashi_CTRL](https://flybase.org/reports/FBlc0005420) | Single-cell RNA-seq study of adult brain without alcohol exposure | 39 | 3,097 |
| [scRNAseq_2021_Baker_CTRL](https://flybase.org/reports/FBlc0005515) | Single-cell RNA-seq study of adult brain without cocaine exposure | 36 | 3,329 |
| [scRNAseq_2020_Allen](https://flybase.org/reports/FBlc0005603) | Single-cell RNA-seq study of adult ventral nerve cords | 20 | 3,085 |
| [scRNAseq_2022_Konstantinides](https://flybase.org/reports/FBlc0006404) | Single-cell RNA-seq study of larval optic lobes | 14 | 5,530 |
| [scRNAseq_2023_Saavedra](https://flybase.org/reports/FBlc0006361) | Single-cell RNA-seq study of the adult thorax | 11 | 1,726 |
| [scRNAseq_2019_Avalos](https://flybase.org/reports/FBlc0005362) | Single-cell RNA-seq study of first instar larval brains upon starvation | 10 | 6,463 |
| [scRNAseq_2021_IngSimmons](https://flybase.org/reports/FBlc0006191) | Single-cell RNA-seq study of gastrulating embryos | 9 | 6,423 |

Not every cluster carries an anatomical annotation: many are non-neural or were not
resolved to a cell type in the source study. Counts here are of what VFB holds, and are
regenerated with the [content report](/blog/2022/01/01/vfb-content-report/) after each
data release; the machine-readable version is
[scRNAseq_DataSets.tsv](https://github.com/VirtualFlyBrain/VFB_reporting_results/blob/master/scRNAseq_DataSets.tsv).
