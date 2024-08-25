---
title: "Contribution Guidelines"
linkTitle: "Contribution Guidelines"
weight: 10
categories: ["help"]
description: >
  Contribute or update Virtual Fly Brain data/sites
---

Submitting new data to VFB
--------------------------

We integrate information from published papers and image data. See below for what to do if you have new data that could be incorporated into VFB.  
The provenance of information, textual or image, is always acknowledged.

### Tell us about your paper

**Have you just had a paper published which describes new anatomical or expression information?**  
The best way to make us aware of your paper, and to put it on our curation list is to act on an email you will receive from FlyBase after your paper has been published. The link on the email points to the [Fast-Track Your Paper Tool](http://flybase.org/submission/publication/).  
Using this tool you can provide information on what types of data your paper contains. If it has new anatomical or expression information you'll need to fill the sections, _Anatomical data_ or _Expression_, respectively, in addition to any other suitable ones.  
You can also use this tool for any other, previously published paper.

### Do you have image data that could be incorporated into VFB?

[Email us](mailto:data@virtualflybrain.org?subject=Submitting%20Image%20data), and we will be able to give you advice on image requirements.  
Ideally, you should contact us when you are still in the planning stages. But if you already generated a dataset, we'll still be able to provide advice.

How to register your image data
-------------------------------

It is essential for successful registrations that the images are of good quality.

Follow [this protocol](http://www.dx.doi.org/10.1101/pdb.prot071720) to acquire stacks that can be used for registration.

Once you have the images, follow [this protocol](http://www.dx.doi.org/10.1101/pdb.prot071738) to register your images.

Information on publicly available template brains and bridging data is available [here](http://jefferislab.org/si/bridging).


How to contribute to these docs
-------------------------------

We use [Hugo](https://gohugo.io/) to format and generate these support pages, the
[Docsy](https://github.com/google/docsy) theme for styling and site structure. 
Hugo is an open-source static site generator that provides us with templates, 
content organisation in a standard directory structure, and a website generation 
engine. You write the pages in Markdown (or HTML if you want), and Hugo wraps them up into a website.

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.

## Updating a single page

If you've just spotted something you'd like to change while using the docs, Docsy has a shortcut for you:

1. Click **Edit this page** in the top right hand corner of the page.
1. If you don't already have an up to date fork of the project repo, you are prompted to get one - click **Fork this repository and propose changes** or **Update your Fork** to get an up to date version of the project to edit. The appropriate page in your fork is displayed in edit mode.

## Creating an issue

If you've found a problem in the docs, but you're not sure how to fix it yourself, please create an issue in the [VirtualFlyBrain/VFB2 repo](https://github.com/VirtualFlyBrain/VFB2/issues). You can also create an issue about a specific page by clicking the **Create Issue** button in the top right hand corner of the page.

## Useful resources

* [Docsy user guide](https://www.docsy.dev/docs/): All about Docsy, including how it manages navigation, look and feel, and multi-language support.
* [Hugo documentation](https://gohugo.io/documentation/): Comprehensive reference for Hugo.
* [Github Hello World!](https://guides.github.com/activities/hello-world/): A basic introduction to GitHub concepts and workflow.
* [nbcovert](https://github.com/jupyter/nbconvert): A tool to convert jupyter notebooks into markdown (md) format.
* [HTML to Markdown Converter](https://codebeautify.org/html-to-markdown): It helps to convert your HTML to MD. This tool is super fast and processes conversion in the browser.
* [How to add new query properties to VFBConnect library](https://virtualflybrain.org/docs/contribution-guidelines/expanding_vfbconnect_queries/)


