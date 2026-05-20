---
title: "Accessibility Statement"
linkTitle: "Accessibility"
weight: 22
---

## Accessibility statement for Virtual Fly Brain

Website accessibility statement in line with the Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018.

This statement applies to the public Virtual Fly Brain (VFB) services hosted at [www.virtualflybrain.org](https://www.virtualflybrain.org) and its sub-domains. VFB is run by the [University of Edinburgh's School of Informatics](https://www.inf.ed.ac.uk/) as a research data integration platform for *Drosophila melanogaster* neurobiology.

We want as many people as possible to be able to use this website. Where the underlying content is inherently visual (3D image stacks, neuron skeletons and connectivity diagrams) we recognise that some features cannot be made fully accessible without losing scientific meaning, and we have documented those limitations below.

### Using this website

Across the site you should be able to:

- Change colours, contrast levels and font size using your browser settings on the documentation pages
- Use the documentation pages without encountering flashing, scrolling or moving content
- Listen to most of the documentation pages with a screen reader (JAWS, NVDA, VoiceOver)
- Navigate the documentation pages by keyboard alone
- Resize text up to 200% on the documentation pages without loss of content

The 3D web client (Geppetto-based) and the embedded CATMAID connectome viewers have known accessibility limitations — see below.

### Customising the website

[AbilityNet — My Computer My Way](https://mcmw.abilitynet.org.uk/) has advice on making your device easier to use if you have a disability.

University of Edinburgh staff and students can use the free [SensusAccess document conversion service](https://www.ed.ac.uk/information-services/computing/computing-infrastructure/disability-information/sensusaccess) for converting accessible PDFs, captions and large print.

### How accessible this website is

We know parts of the website are not fully accessible:

- The Geppetto 3D web client (`v2.virtualflybrain.org` and variants) is built around WebGL and a 3D scene-graph. Keyboard navigation of the scene is limited; screen-reader access to the neuron meshes is not currently meaningful.
- The CATMAID connectome viewers (`*.catmaid.virtualflybrain.org`) are embedded third-party software whose interface is optimised for mouse and keyboard interaction at high zoom levels. We do not control its accessibility behaviour.
- Some neuroanatomical diagrams use colour to encode region or cell-type identity. We are progressively adding `aria-label` and image-map fallbacks; some legacy diagrams still rely on colour alone.
- Some embedded scientific figures from external publications retain their original styling, including small text size and low colour contrast.
- Not all image alternative text fully describes the underlying scientific content.

### Feedback and contact information

If you need information from this site in a different format, or you encounter an accessibility problem we have not listed:

- Email: [support@virtualflybrain.org](mailto:support@virtualflybrain.org)
- GitHub: file an issue at [github.com/VirtualFlyBrain/VFB2/issues](https://github.com/VirtualFlyBrain/VFB2/issues)

We will respond within five working days.

### Enforcement procedure

The Equality and Human Rights Commission (EHRC) is responsible for enforcing the Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018. If you are not satisfied with how we respond to your complaint, you can contact the [Equality Advisory and Support Service (EASS)](https://www.equalityadvisoryservice.com/).

### Technical information about this website's accessibility

The University of Edinburgh is committed to making its websites and applications accessible in line with the regulations. This website is partially compliant with the [Web Content Accessibility Guidelines (WCAG) 2.2 AA standard](https://www.w3.org/TR/WCAG22/), with the non-compliances listed below.

#### Non-compliance with the accessibility regulations

The following items do not currently comply with WCAG 2.2 AA success criteria:

- **1.1.1 Non-text content.** Not all neuron images and anatomical diagrams have meaningful alternative text. We are adding alt text and image-map labels on an ongoing basis.
- **1.3.1 Info and relationships, 1.3.2 Meaningful sequence.** Some legacy figure pages do not present content in a programmatically determined reading order.
- **1.4.1 Use of colour.** Some neuroanatomical schematics use colour as the sole means of distinguishing regions or cell types.
- **1.4.3 Contrast (minimum).** Some embedded figures from external publications use low-contrast labels we cannot modify.
- **2.1.1 Keyboard.** The Geppetto 3D viewer cannot be navigated by keyboard alone for full feature parity with mouse interaction.
- **4.1.2 Name, role, value.** The 3D viewer's scene-graph elements (neurons, brain regions) are not exposed to assistive technology as named, role-tagged elements.

#### Content that is not within the scope of the accessibility regulations

- **Third-party scientific content.** PDFs and figures imported from peer-reviewed publications retain their original formatting and are republished under their original licences. We do not modify them.
- **Older content (pre-September 2018).** Some legacy pages and PDFs pre-date the regulations and are kept for reference; we will replace them with accessible HTML where reasonable.

### What we are doing to improve accessibility

- Adding `aria-label` and image-map fallbacks to anatomical schematics — ongoing through 2026.
- Documenting alternative routes to the same information (text search, the [VFB_connect Python API](https://github.com/VirtualFlyBrain/VFB_connect), and the [VFB MCP server](https://virtualflybrain.org/blog/2026/02/07/introducing-the-vfb-model-context-protocol-mcp-tool/)) so users who cannot use the 3D viewer can still access the underlying data programmatically.
- Reviewing and improving alternative text for image content.
- Following the [University of Edinburgh accessibility guidance](https://www.ed.ac.uk/about/website/accessibility) for the documentation site framework (Hugo + Docsy).

### Preparation of this statement

This statement was prepared in May 2026. It has not yet been independently audited; an internal review will be carried out before the firewall-hole review cycle.

This article was published on 2026-05-19.
