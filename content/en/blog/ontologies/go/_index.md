---
title: "Gene Ontology (GO)"
linkTitle: "Gene Ontology"
tags: [ontologies,annotation,GO]
categories: [ontologies,annotations]
weight: 60
date: 2022-01-05
Description: >
  The Gene Ontology (GO) provides a framework and set of concepts for describing the functions of gene products from all organisms.
ontology: "go"
cascade:
- type: "docs"
  _target:
    path: "/**"
---

[//]: # (feel free to add extra details here or include a readme file)

<a href="https://www.ebi.ac.uk/ols/ontologies/{{< param "ontology" >}}" target="_blank"><img src="https://www.ebi.ac.uk/ols/img/OLS_logo_2017.png" style="max-width: 20%; background: #000000; padding: 5px;" alt="Open in the Ontology Lookup Service (OLS)" ></a>

<div id="result">
<script>  $( "#result" ).load( "https://www.ebi.ac.uk/ols/ontologies/{{< param "ontology" >}}  #ontology_info_box", function(){$("a[href^='../']").each(function(){$(this).attr('target','_blank');$(this).attr('href',$(this).attr('href').replace('../','https://www.ebi.ac.uk/ols/'));})})</script>


</script>
</div>
