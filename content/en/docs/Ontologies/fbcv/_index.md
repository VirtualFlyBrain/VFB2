---
title: "FlyBase Controlled Vocabulary (FBcv)"
linkTitle: "FlyBase Controlled Vocabulary (FBcv)"
tags: [ontologies,annotation,FBcv]
content: [ontologies,annotations]
weight: 20
ontology: "fbcv"
Description: >
  A miscellaneous ontology of terms used for curation in FlyBase, including the DPO.
---

#feel free to add extra details here or include a readme file

{{< param "ontology" >}}

<a href="https://www.ebi.ac.uk/ols/ontologies/fbcv" target="_blank"><img src="https://www.ebi.ac.uk/ols/img/OLS_logo_2017.png" style="max-width: 20%; background: #000000; padding: 5px;" alt="Open in the Ontology Lookup Service (OLS)" ></a>

<div id="result">
<script>  $( "#result" ).load( {{ printf "https://www.ebi.ac.uk/ols/ontologies/%s  #ontology_info_box" $.Params.ontology }}, function(){$("a[href^='../']").each(function(){$(this).attr('target','_blank');$(this).attr('href',$(this).attr('href').replace('../','https://www.ebi.ac.uk/ols/'));})})</script>


</script>
</div>
