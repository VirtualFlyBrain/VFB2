---
title: "ON and OFF motion detection circuit"
tag: [optic lobe, T4, T5, motion detection, ON-edge, OFF-edge, medulla]
categories: [circuit diagram]
description: >
  Schematic wiring of the ON-edge (T4) and OFF-edge (T5) motion-detection circuits, from Figure 6 of Shinomiya et al. (2019). Panels A and B show the columnar inputs that converge on T4 and T5 dendrites — Mi1, Mi4, Mi9, Tm3, TmY15, C3 (and CT1 feedback) for T4; Tm1, Tm2, Tm4, Tm9, TmY15 (and CT1) for T5 — with arrow weights indicating relative synapse counts. Panel C is the canonical summary cartoon: photoreceptors R1-6 → lamina monopolar cells L1/L2/L3 → medulla cells (Mi1/Mi4/Mi9/Tm3 driving T4 ON-edge; Tm1/Tm2/Tm4/Tm9 driving T5 OFF-edge) → T4/T5 → lobula plate. Click a labelled neuron type or neuropil to open the corresponding term in Virtual Fly Brain.
---
<div style="border:1px solid grey;width:100%;height:fit-content;overflow:auto;zoom: 0.6;">
<img src="https://www.virtualflybrain.org/images/elife-40025-fig6-v2.jpg" style="max-width:2362px;max-height:948px;width:2362px;height:948px;" usemap="#Shinomiya_Figure_6" border="0">
<map name="Shinomiya_Figure_6">
    <area shape="rect" coords="60,30,150,90" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003721" title="L3 — lamina monopolar neuron L3">
    <area shape="rect" coords="200,30,290,90" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003719" title="L1 — lamina monopolar neuron L1">
    <area shape="rect" coords="60,140,150,200" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003784" title="Mi9 — medulla intrinsic neuron Mi9">
    <area shape="rect" coords="155,140,250,200" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003776" title="Mi1 — medulla intrinsic neuron Mi1">
    <area shape="rect" coords="155,205,250,265" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003791" title="Tm3 — transmedullary neuron Tm3">
    <area shape="rect" coords="255,140,365,200" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048246" title="TmY15 — transmedullary Y neuron TmY15">
    <area shape="rect" coords="290,205,395,265" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003744" title="C3 — centrifugal neuron C3">
    <area shape="rect" coords="380,140,460,200" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003779" title="Mi4 — medulla intrinsic neuron Mi4">
    <area shape="rect" coords="40,400,160,470" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003731" title="T4 neuron">
    <area shape="rect" coords="540,290,640,360" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048245" title="CT1 — tangential neuron CT1">
    <area shape="rect" coords="540,140,640,210" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003776" title="Mi1">
    <area shape="rect" coords="540,210,640,275" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003784" title="Mi9">
    <area shape="rect" coords="320,650,460,720" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003885" title="LOP — lobula plate">
    <area shape="rect" coords="800,30,890,90" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003721" title="L3 — lamina monopolar neuron L3">
    <area shape="rect" coords="950,30,1040,90" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003720" title="L2 — lamina monopolar neuron L2">
    <area shape="rect" coords="800,140,890,200" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003797" title="Tm9 — transmedullary neuron Tm9">
    <area shape="rect" coords="900,140,990,200" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003792" title="Tm4">
    <area shape="rect" coords="990,140,1080,200" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003789" title="Tm1">
    <area shape="rect" coords="990,205,1080,265" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003790" title="Tm2">
    <area shape="rect" coords="900,205,985,265" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048246" title="TmY15 — transmedullary Y neuron TmY15">
    <area shape="rect" coords="900,475,1100,540" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00049516" title="LT33 — lobula tangential neuron LT33">
    <area shape="rect" coords="900,540,1100,600" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003811" title="Tm23 — transmedullary neuron Tm23">
    <area shape="rect" coords="780,400,900,470" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003736" title="T5 neuron">
    <area shape="rect" coords="1280,290,1380,360" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048245" title="CT1">
    <area shape="rect" coords="1280,140,1380,210" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003789" title="Tm1">
    <area shape="rect" coords="1280,210,1380,275" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003797" title="Tm9">
    <area shape="rect" coords="1060,650,1200,720" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003885" title="LOP — lobula plate">
    <area shape="rect" coords="1620,80,1740,160" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00006007" title="R1-6 — outer photoreceptor cells">
    <area shape="rect" coords="1830,80,1950,160" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00006007" title="R1-6 — outer photoreceptor cells">
    <area shape="rect" coords="2070,80,2190,160" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00006007" title="R1-6 — outer photoreceptor cells">
    <area shape="rect" coords="1610,170,1670,230" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003719" title="L1">
    <area shape="rect" coords="1670,170,1730,230" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003721" title="L3">
    <area shape="rect" coords="1730,170,1790,230" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003720" title="L2">
    <area shape="rect" coords="1820,170,1880,230" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003719" title="L1">
    <area shape="rect" coords="1880,170,1940,230" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003720" title="L2">
    <area shape="rect" coords="2070,170,2130,230" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003719" title="L1">
    <area shape="rect" coords="2130,170,2190,230" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003720" title="L2">
    <area shape="rect" coords="1530,310,1620,370" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003784" title="Mi9">
    <area shape="rect" coords="1640,310,1730,370" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003776" title="Mi1">
    <area shape="rect" coords="1640,370,1730,430" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003791" title="Tm3">
    <area shape="rect" coords="1740,310,1830,370" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048245" title="CT1">
    <area shape="rect" coords="1740,370,1830,430" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003779" title="Mi4">
    <area shape="rect" coords="1900,310,1990,370" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003797" title="Tm9">
    <area shape="rect" coords="2000,310,2090,370" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003789" title="Tm1">
    <area shape="rect" coords="2000,370,2090,430" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003792" title="Tm4">
    <area shape="rect" coords="2100,310,2190,370" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003790" title="Tm2">
    <area shape="rect" coords="2200,310,2300,370" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048245" title="CT1">
    <area shape="rect" coords="1580,610,1730,690" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003731" title="T4 neuron — ON-edge">
    <area shape="rect" coords="1990,610,2150,690" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003736" title="T5 neuron — OFF-edge">
</map>
</div>

<a href="https://doi.org/10.7554/eLife.40025" target="_blank">https://doi.org/10.7554/eLife.40025</a>

Figure reproduced under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) from Shinomiya K, Huang G, Lu Z, Parag T, Xu CS, Aniceto R, Ansari N, Cheatham N, Lauchie S, Neace E, Ogundeyi O, Ordish C, Peel D, Shinomiya A, Smith C, Takemura S, Talebi I, Rivlin PK, Nern A, Scheffer LK, Plaza SM, Meinertzhagen IA (2019). *Comparisons between the ON- and OFF-edge motion pathways in the Drosophila brain.* eLife 8:e40025.
