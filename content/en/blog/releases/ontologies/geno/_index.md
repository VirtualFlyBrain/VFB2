---
title: "GENO ontology"
linkTitle: "GENO ontology"
tags: [ontologies,annotation,GENO]
categories: [ontologies,annotations]
weight: 70
date: 2022-01-05
Description: >
  GENO is an OWL model of genotypes, their more fundamental sequence components, and links to related biological and experimental entities. 
ontology: "geno"
cascade:
- type: "docs"
  _target:
    path: "/**"
---

At present many parts of the model are exploratory and set to undergo refactoring. In addition, many classes and properties have GENO URIs but are place holders for classes that will be imported from an external ontology (e.g. SO, ChEBI, OBI, etc). Furthermore, ongoing work will implement a model of genotype-to-phenotype associations. This will support description of asserted and inferred relationships between a genotypes, phenotypes, and environments, and the evidence/provenance behind these associations. Documentation is under development as well, and for now a slidedeck is available at http://www.slideshare.net/mhb120/brush-icbo-2013

<a href="https://www.ebi.ac.uk/ols/ontologies/{{< param "ontology" >}}" target="_blank"><img src="https://www.ebi.ac.uk/ols/img/OLS_logo_2017.png" style="max-width: 20%; background: #000000; padding: 5px;" alt="Open in the Ontology Lookup Service (OLS)" ></a>

<div id="result">
<script>  $( "#result" ).load( "https://www.ebi.ac.uk/ols/ontologies/{{< param "ontology" >}}  #ontology_info_box", function(){$("a[href^='../']").each(function(){$(this).attr('target','_blank');$(this).attr('href',$(this).attr('href').replace('../','https://www.ebi.ac.uk/ols/'));})})</script>


</script>
</div>
