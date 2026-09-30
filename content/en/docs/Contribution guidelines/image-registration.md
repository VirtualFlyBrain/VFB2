---
title: "How to register your image data"
linkTitle: "Image Registration"
weight: 702
date: 2026-09-09
categories: ["help"]
tags: ["Registration","CMTK","MADI3D","Template","Alignment"]
description: >
  Aligning your confocal stacks to a standard template, starting with MADI3D, a free GUI.
---

Registration warps your images onto a standard [template brain](/docs/data/templates/) so that
they share a coordinate space with everything else on VFB. Once that is done your images can
be overlaid on other people's data, scored for overlap, and searched against.

This page covers how to do it. For background on what registration is and how accurate it can
be expected to be, see [Image Registration](/docs/concepts/registration/) under Concepts.

## Before you start: image quality

It is essential for successful registrations that the images are of good quality. Registration
works from a reference channel rather than from the signal you are interested in. That is
usually an anti-Bruchpilot (nc82) neuropil counterstain, which looks broadly similar in every
animal and so gives the algorithm something stable to match on. The transform computed from
that channel is then applied to your signal channel.

So you want a clean, even counterstain, the whole structure inside the frame, undamaged
tissue, and a voxel size fine enough to resolve neuropil boundaries. None of this can be
corrected afterwards, so if you are still planning the experiment it is worth
[talking to us first](/docs/contribution-guidelines/image-upload/).

Follow [this protocol](https://doi.org/10.1101/pdb.prot071720) to acquire stacks that can be
used for registration.

## Recommended: MADI3D

If you have not registered images before, start with [MADI3D](https://madi3d.org). It is a
free, cross-platform desktop application that wraps CMTK registration in a graphical
interface, so you can align a stack to a template without using the command line, and inspect
the result against the reference in the same 3D scene.

For registration it offers:

* Rigid, affine (9-DOF and 12-DOF) and non-linear B-spline deformable registration
* Microscopy-oriented presets, with configurable similarity metrics and optimisation parameters
* Landmark-assisted registration, where you place corresponding anatomical landmark pairs in
  the 3D scene to guide or supplement the intensity-based fit. This is useful when an automated
  registration will not converge
* Reformatting of registered data, and saving transforms so they can be reapplied to other
  channels

It reads TIFF/TIF, Zeiss LSM, Olympus OIF/OIB, NRRD, NIfTI/NII and H5J volumes, as well as OBJ
meshes and SWC reconstructions, so you can load raw microscopy alongside a template and check
the alignment directly.

Pre-built packages for Windows x64, Linux x64, macOS Apple Silicon and macOS Intel are on the
[MADI3D releases page](https://github.com/sandorbx/MADI3D/releases). They are self-contained
and do not need a separate Python environment: download the package for your platform, extract
it once and run it. The [project README](https://github.com/sandorbx/MADI3D#readme) has
per-platform steps and describes the registration panel.

{{< alert title="It is a public beta" color="warning" >}}
MADI3D is under active development and the released packages are not code-signed or notarized,
so Windows SmartScreen or macOS Gatekeeper may warn on first run. Check your download against
the `SHA256SUMS.txt` published with the release before overriding the warning, and validate
any quantitative conclusions for your own workflow.
{{< /alert >}}

MADI3D is developed by Sandor Bx, with support from the University of Cologne, Prof. Dr. Kei
Ito and Dr. Thomas Riemensperger. It is not a VFB product, so problems with it are best raised
on its [issue tracker](https://github.com/sandorbx/MADI3D/issues).

## The established protocol

Most published fly registrations have used CMTK driven from the command line. Once you have
suitable stacks, follow [this protocol](https://doi.org/10.1101/pdb.prot071738) to register
your images.

This route gives you full control over the registration parameters and scripts cleanly over a
large dataset, so it is still the better choice for a batch of hundreds of images. MADI3D
drives the same underlying toolkit, so results from the two are comparable
([Rohlfing and Maurer, 2003](https://doi.org/10.1109/TITB.2003.808506)).

## Which template to register to

Information on publicly available template brains is on the
[Templates](/docs/data/templates/) page, and the registrations that map between them are
described under [Bridging registrations](/docs/concepts/bridging/). Those bridging transforms
are what allow data registered to one template to be compared against data in another, so
registering to a well-bridged standard matters more than the choice of any particular one.

If you are unsure which template suits your data, ask us before you start.

## When your images are registered

[Get in touch](/docs/contribution-guidelines/image-upload/) and we will arrange to take the
data in. Let us know which template you registered to and which tool you used, as it helps us
check the alignment before curation.
