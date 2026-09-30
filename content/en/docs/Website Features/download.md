---
categories: ["overview","help"]
tags: ["download","OBJ","SWC","NRRD","tools"]
title: "Downloading images"
linkTitle: "Download"
description: >
   Download the meshes, skeletons, image volumes and references for everything you have loaded, as one zip file.
weight: 216
---

**Tools → Download Contents** opens the download dialog for the images currently loaded in the viewers.

Choose one or more file types (OBJ, SWC or NRRD), then the items to include (all loaded instances, or a selection), and click **Download**. VFB packages the files into a single zip, `VFB Files.zip`.

- **OBJ** – surface meshes, as shown in the 3D Viewer.
- **SWC** – neuron skeletons, where the image has one.
- **NRRD** – the aligned image volume, in the coordinate space of its template.

Not every item has every file type; items without the selected type are left out, and the dialog tells you if nothing matched. For a step-by-step walkthrough, see the [Bulk Image Download](/docs/tutorials/website/bulkdownloads/) tutorial; to fetch files from code instead, see [downloading images through the API](/docs/tutorials/apis/apiimagedownload/).
