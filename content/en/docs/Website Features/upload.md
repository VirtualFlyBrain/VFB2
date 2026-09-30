---
categories: ["overview","help"]
tags: ["NBLAST","upload","tools"]
title: "NBLAST against your own data"
linkTitle: "Upload for NBLAST"
description: >
   Upload a neuron of your own and get back a link to the VFB neurons most similar to it in shape.
weight: 217
---

**Tools → NBLAST → NBLAST against your own data** opens the upload dialog. It runs an [NBLAST](/docs/concepts/nblast/) comparison between a neuron you supply and the neurons on VFB aligned to the same template.

1. **Select a template** – the template brain your file is aligned to: JRC2018Unisex (adult brain), JRC2018UnisexVNC (adult VNC), L1EM or L3CNS (larva). Your file must already be in that template's coordinate space.
2. **Add your file** – one `.swc` skeleton or `.nrrd` image volume, up to 5 MB.
3. **Optionally, allow the cookie** – tick the box and VFB stores the link to your query in a browser [cookie](/about/cookies/#functional-cookies) so you can find it again. Leave it unticked and nothing is stored; just copy the link.
4. **Generate a NBLAST query link** – the file uploads and you get a link to copy.

The comparison can take over an hour, so keep the link. When it is ready, opening the link runs the [Neurons with similar morphology to your upload](/docs/website-features/queries/#SimilarMorphologyToUserData) query, with matches sorted by score.
