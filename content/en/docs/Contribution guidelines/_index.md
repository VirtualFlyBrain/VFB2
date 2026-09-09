---
title: "Contribution Guidelines"
linkTitle: "Contribution Guidelines"
weight: 700
categories: ["help"]
description: >
  How to tell us about a paper, get your image data into VFB, and improve these docs.
---

We integrate information from published papers and image data produced by other groups. The
provenance of that information, textual or image, is always acknowledged.

There are three ways to contribute, covered below and on the pages linked from here.

Submitting new data to VFB
--------------------------

### Tell us about your paper

**Have you just had a paper published which describes new anatomical or expression information?**  
The best way to make us aware of your paper, and to put it on our curation list is to act on an email you will receive from FlyBase after your paper has been published. The link on the email points to the [Fast-Track Your Paper Tool](https://flybase.org/submission/publication/).  
Using this tool you can provide information on what types of data your paper contains. If it has new anatomical or expression information you'll need to fill the sections, _Anatomical data_ or _Expression_, respectively, in addition to any other suitable ones.  
You can also use this tool for any other, previously published paper.

### Do you have image data that could be incorporated into VFB?

[Email us](mailto:data@virtualflybrain.org?subject=Submitting%20Image%20data) at
`data@virtualflybrain.org` and we will advise on image requirements and arrange a way to get
the files to us. Ideally, contact us when you are still in the planning stages, but if you
have already generated a dataset we can still help.

Two pages cover the detail:

* [Submitting image data](/docs/contribution-guidelines/image-upload/): what we can take, what
  to say in that first email, and what happens next.
* [Registering your images](/docs/contribution-guidelines/image-registration/): how to align
  your stacks to a standard template, starting with the easiest route.

Please use `data@virtualflybrain.org` rather than our support address. `support@` goes to a
[publicly archived forum](https://groups.google.com/g/vfb-suport), which is not a good place
for unpublished or embargoed data.

How to contribute to these docs
-------------------------------

We use [Hugo](https://gohugo.io/) to format and generate these support pages. Hugo is an
open-source static site generator that provides us with templates, content organisation in a
standard directory structure, and a website generation engine. You write the pages in Markdown
(or HTML if you want), and Hugo wraps them up into a website.

All submissions, including submissions by project members, require review. We use GitHub pull
requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more information on
using pull requests.

### Updating a single page

If you've just spotted something you'd like to change while using the docs, there's a shortcut:

1. Click **Edit this page** in the sidebar on the right of the page.
1. If you don't already have an up to date fork of the project repo, you are prompted to get one. Click **Fork this repository and propose changes** or **Update your Fork** to get an up to date version of the project to edit. The appropriate page in your fork is displayed in edit mode.
1. Make your change and open a pull request.

### Reporting a problem

If you've found a problem in the docs, but you're not sure how to fix it yourself, click
**Report an issue** in the same sidebar to raise one about that specific page. You can also
create an issue directly in the
[VirtualFlyBrain/VFB2 repo](https://github.com/VirtualFlyBrain/VFB2/issues).

### Useful resources

* [Hugo documentation](https://gohugo.io/documentation/): Comprehensive reference for Hugo.
* [Github Hello World!](https://guides.github.com/activities/hello-world/): A basic introduction to GitHub concepts and workflow.
* [nbconvert](https://github.com/jupyter/nbconvert): A tool to convert jupyter notebooks into markdown (md) format.
* [HTML to Markdown Converter](https://codebeautify.org/html-to-markdown): It helps to convert your HTML to MD. This tool is super fast and processes conversion in the browser.
* [How to add new query properties to VFBConnect library](/docs/contribution-guidelines/expanding_vfbconnect_queries/)
