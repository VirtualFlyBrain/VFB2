---
title: "Installing CMTK"
weight: 432
series: ["API"]
date: 2026-09-09
description: >
  The simplest way to get a local copy of CMTK, for using navis-flybrains / nat.flybrains
  bridging transforms outside VFB, or for registering your own data.
---

VFB's [registration](/docs/concepts/registration/) and [bridging](/docs/concepts/bridging/)
pages describe how [**CMTK**](https://www.nitrc.org/projects/cmtk/) is used to align data to
common template spaces. You do not need a local copy to use VFB itself — registration already
happened before data was loaded. You need one if you want to run
[navis-flybrains](https://github.com/navis-org/navis-flybrains) or
[nat.flybrains](https://natverse.org/nat.flybrains/index.html) transforms yourself, or register
your own images.

This page covers the least-effort route to a working CMTK for each platform.

## macOS

Download and run the Apple Silicon installer package from the actively-maintained
[jefferis/cmtk](https://github.com/jefferis/cmtk) mirror (the same one the natverse project
builds against):

[**cmtk-3.4.0-dev-macos-arm64-gcd.pkg**](https://github.com/jefferis/cmtk/releases/download/natdev-latest/cmtk-3.4.0-dev-macos-arm64-gcd.pkg)

Double-click it and step through the installer. It places the `cmtk` launcher at
`/usr/local/bin/cmtk` and the individual tools under `/usr/local/lib/cmtk/bin`.
`/usr/local/bin` is on the default macOS `PATH`, so no further setup is needed — open a new
Terminal and confirm with:

```sh
cmtk --version
```

Intel Macs are not covered by that build. Use the older, contributed
[`CMTK-3.4.0-contrib-MacOSX.zip`](https://www.nitrc.org/frs/?group_id=212) from NITRC instead,
or build from source.

## Windows

We recommend [**MADI3D**](https://madi3d.org) ([GitHub](https://github.com/sandorbx/MADI3D)),
which installs CMTK for you rather than asking you to do it by hand. From its CMTK setup dialog,
choose **Automatic setup**: it enables WSL if needed, creates its own isolated
`MADI3D-CMTK` Ubuntu distribution (your existing WSL distributions, if any, are left untouched),
and installs the `cmtk` package inside it. The same automatic route also works if you are on
native Ubuntu/Debian Linux.

If you would rather do it by hand: install [WSL](https://learn.microsoft.com/windows/wsl/install)
(`wsl --install`, from an administrator PowerShell), then inside the Ubuntu shell it opens:

```sh
sudo apt update && sudo apt install -y cmtk
```

## Linux

CMTK is packaged for Ubuntu/Debian directly:

```sh
sudo apt update && sudo apt install -y cmtk
```

## Verifying the install

Any of the above should leave `cmtk` and the individual tools (`registration`, `warp`, `mat2dof`,
`dof2mat`, `reformatx`, `describe`, ...) on your `PATH`:

```sh
cmtk --version
registration --version
```
