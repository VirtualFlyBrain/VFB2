---
title: "Virtual Fly Brain Images (VFB)"
linkTitle: "VFB Image Ontology"
tags: [ontologies,annotation,VFB,VFBexp]
categories: [ontologies,annotations]
weight: 20
ontology: "vfb"
Description: >
  The VFB query system relies on representation of data/knowledge in OWL. Central to this a representation of Drosophila neuro-anatomy in the [Drosophila anatomy ontology]({{< ref "../fbbt/_index.md" >}}). The anatomical structures depicted in images displayed on VFB are represented as a [KnowledgeBase of OWL individuals](https://github.com/VirtualFlyBrain/VFB_owl/blob/master/doc/vfb_owl_ind_schema.md), which are classified (typed) using OWL class expressions referencing the anatomy ontology.  When this KnowledgeBase of individuals is combined with the ontology, a reasoner can be used to classify and query for anatomical structures depicted in the images on VFB.
---

[//]: # (feel free to add extra details here or include a readme file)

You can run queries against the VFB OWL server using the python package [vfb-connect](https://vfb-connect.readthedocs.io/en/stable/) or directly via our owlery server endpoint [http://owl.virtualflybrain.org/kbs/vfb](http://owl.virtualflybrain.org/kbs/vfb). Details of the [Owlery rest API](https://github.com/phenoscape/owlery) can be found [here](https://owlery.phenoscape.org/api/).

The latest live version of the vfb.owl file can be accessed at [http://virtualflybrain.org/data/VFB/OWL/owlery-live.owl](http://virtualflybrain.org/data/VFB/OWL/owlery-live.owl)
