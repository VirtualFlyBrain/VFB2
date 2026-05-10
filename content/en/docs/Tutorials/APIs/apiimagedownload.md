---
title: "Downloading Images from VFB Using VFBconnect"
linkTitle: "Downloading Images via API"
weight: 20
description: >
  This guide will show you how to use VFBconnect to download images from the Virtual Fly Brain (VFB) based on a dataset.
---

## Introduction

VFBconnect is a Python package that provides an interface to the Virtual Fly Brain (VFB) API. It allows users to query the VFB database and download data, including images.

## Installation

Before you can use VFBconnect, you need to install it. You can do this using pip:

```bash
pip install vfb-connect
```

## Downloading Images

To download images from VFB using VFBconnect, you need to first import the package and create a client:

```python
from vfb_connect.cross_server_tools import VfbConnect
vc = VfbConnect()
```

Next, you can use the `get_images` method to download images. This method requires the dataset ID as an argument:

```python
dataset_id = 'your_dataset_id'
images = vc.get_images(dataset_id)
```

This will return a list of images from the specified dataset. Each image is represented as a dictionary with information such as the image ID, title, and URL.

To download the images, you can loop through the list and use the `urlretrieve` function from the `urllib.request` module:

```python
import urllib.request

for image in images:
    url = image['image_url']
    filename = image['image_id'] + '.jpg'
    urllib.request.urlretrieve(url, filename)
```

This will download each image and save it as a JPEG file in the current directory. The filename is the image ID.

## Conclusion

This guide showed you how to use VFBconnect to download images from the Virtual Fly Brain based on a dataset. With VFBconnect, you can easily access and download data from VFB for your research.
