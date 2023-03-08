---
title: "How to Interpret VFB Thumbnails"
linkTitle: "Thumbnails"
tags: ["thumbnails","CD-MIP","MIP"]
weight: 100
description: >-
     VFB (Virtual Fly Brain) thumbnails are color depth maximum projection images that allow users to visualize the distribution of intensity values across different depths in a 3D image stack. 
---

## How to Interpret VFB Thumbnails

Here is a guide on how to interpret VFB thumbnails:

- Each pixel in a VFB thumbnail corresponds to a specific depth in the image stack.
- Brighter or more intense colors indicate higher intensity values at that depth.
- The color bar on the right side of the image provides additional context about the mapping between color and depth.
- Each color in the color bar corresponds to a specific depth in the image stack, and the intensity of the color represents the maximum intensity value at that depth.
- Users can use the color bar to identify the depth of the signal and gain insights into the distribution of intensity values across different depths in the image stack.

![Example VFB template thumbnail](https://www.virtualflybrain.org/data/VFB/i/0010/1567/VFB_00101567/thumbnail.png)
* Note the colour bar and hence the signal in the image uses nealy the whole of the available (Z) stack space.

![Example VFB neuron thumbnail](http://www.virtualflybrain.org/data/VFB/i/0000/0001/VFB_00101567/thumbnail.png)
* Note the colour bar and hence the signal in the image uses less of the available (Z) stack space.

![Example VFB flat neuron thumbnail](http://virtualflybrain.org/data/VFB/i/0000/0123/VFB_00101567/thumbnail.png)
* Note the colour bar and hence the signal in the image uses much less of the available (Z) stack space.

In summary, VFB thumbnails provide a simplified way to visualize complex 3D image data. Each pixel's color and intensity represent the maximum intensity value at a specific depth, and the color bar provides additional context about the mapping between color and depth. By interpreting the colors and using the color bar, users can gain insights into the distribution of intensity values across the image stack.
