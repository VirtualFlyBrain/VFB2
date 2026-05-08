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
    <area shape="rect" coords="130,15,250,90" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003721" title="L3 — lamina monopolar neuron L3">
    <area shape="rect" coords="320,15,440,90" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003719" title="L1 — lamina monopolar neuron L1">
    <area shape="rect" coords="100,125,210,205" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003784" title="Mi9 — medulla intrinsic neuron Mi9">
    <area shape="rect" coords="220,125,345,205" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048246" title="TmY15 — transmedullary Y neuron TmY15">
    <area shape="rect" coords="355,125,460,205" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003776" title="Mi1 — medulla intrinsic neuron Mi1">
    <area shape="rect" coords="355,210,460,290" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003791" title="Tm3 — transmedullary neuron Tm3">
    <area shape="rect" coords="520,125,590,205" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003744" title="C3 — centrifugal neuron C3">
    <area shape="rect" coords="600,125,720,205" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003779" title="Mi4 — medulla intrinsic neuron Mi4">
    <area shape="rect" coords="30,395,150,470" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003731" title="T4 neuron">
    <area shape="rect" coords="720,225,830,300" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003776" title="Mi1">
    <area shape="rect" coords="720,305,830,380" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003784" title="Mi9">
    <area shape="rect" coords="720,580,830,650" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048245" title="CT1 — tangential neuron CT1">
    <area shape="rect" coords="480,650,590,740" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003885" title="LOP — lobula plate">
    <area shape="rect" coords="880,15,1000,90" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003721" title="L3 — lamina monopolar neuron L3">
    <area shape="rect" coords="1050,15,1170,90" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003720" title="L2 — lamina monopolar neuron L2">
    <area shape="rect" coords="880,125,1000,205" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003797" title="Tm9 — transmedullary neuron Tm9">
    <area shape="rect" coords="1015,210,1100,290" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048246" title="TmY15 — transmedullary Y neuron TmY15">
    <area shape="rect" coords="1090,125,1180,205" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003792" title="Tm4">
    <area shape="rect" coords="1190,125,1280,205" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003789" title="Tm1">
    <area shape="rect" coords="1190,210,1280,290" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003790" title="Tm2">
    <area shape="rect" coords="800,395,910,470" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003736" title="T5 neuron">
    <area shape="rect" coords="945,580,1085,640" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00049516" title="LT33 — lobula tangential neuron LT33">
    <area shape="rect" coords="945,645,1085,705" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003811" title="Tm23 — transmedullary neuron Tm23">
    <area shape="rect" coords="1395,225,1495,300" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003789" title="Tm1">
    <area shape="rect" coords="1395,305,1495,380" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003797" title="Tm9">
    <area shape="rect" coords="1395,580,1495,650" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048245" title="CT1">
    <area shape="rect" coords="1180,720,1290,800" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003885" title="LOP — lobula plate">
    <area shape="rect" coords="1620,15,2200,75" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003731" title="PD — preferred direction (T4 ON-edge)">
    <area shape="rect" coords="1620,100,1740,170" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00006007" title="R1-6 — outer photoreceptor cells">
    <area shape="rect" coords="1820,100,1940,170" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00006007" title="R1-6 — outer photoreceptor cells">
    <area shape="rect" coords="2065,100,2200,170" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00006007" title="R1-6 — outer photoreceptor cells">
    <area shape="rect" coords="1610,200,1670,260" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003719" title="L1">
    <area shape="rect" coords="1671,200,1730,260" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003721" title="L3">
    <area shape="rect" coords="1731,200,1795,260" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003720" title="L2">
    <area shape="rect" coords="1820,200,1880,260" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003719" title="L1">
    <area shape="rect" coords="1881,200,1940,260" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003720" title="L2">
    <area shape="rect" coords="2065,200,2125,260" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003719" title="L1">
    <area shape="rect" coords="2126,200,2185,260" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003721" title="L3">
    <area shape="rect" coords="2186,200,2245,260" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003720" title="L2">
    <area shape="rect" coords="1530,330,1620,395" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003784" title="Mi9">
    <area shape="rect" coords="1640,325,1730,375" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003776" title="Mi1">
    <area shape="rect" coords="1640,376,1730,425" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003791" title="Tm3">
    <area shape="rect" coords="1740,325,1830,375" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048245" title="CT1">
    <area shape="rect" coords="1740,376,1830,425" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003779" title="Mi4">
    <area shape="rect" coords="1900,330,1990,395" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003797" title="Tm9">
    <area shape="rect" coords="2000,325,2080,375" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003789" title="Tm1">
    <area shape="rect" coords="2000,376,2080,425" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003792" title="Tm4">
    <area shape="rect" coords="2090,325,2170,395" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003790" title="Tm2">
    <area shape="rect" coords="2200,325,2300,395" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00048245" title="CT1">
    <area shape="rect" coords="1620,600,1740,680" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003731" title="T4 neuron — ON-edge">
    <area shape="rect" coords="2030,600,2150,680" target="_blank" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=VFB_00101567&id=FBbt_00003736" title="T5 neuron — OFF-edge">
</map>
</div>

<a href="https://doi.org/10.7554/eLife.40025" target="_blank">https://doi.org/10.7554/eLife.40025</a>

Figure reproduced under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) from Shinomiya K, Huang G, Lu Z, Parag T, Xu CS, Aniceto R, Ansari N, Cheatham N, Lauchie S, Neace E, Ogundeyi O, Ordish C, Peel D, Shinomiya A, Smith C, Takemura S, Talebi I, Rivlin PK, Nern A, Scheffer LK, Plaza SM, Meinertzhagen IA (2019). *Comparisons between the ON- and OFF-edge motion pathways in the Drosophila brain.* eLife 8:e40025.
