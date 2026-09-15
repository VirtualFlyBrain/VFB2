---
title: "elastix"
linkTitle: "elastix"
weight: 659
description: >
  The registration toolbox behind the FANC and BANC transforms — what to install, and the
  detail that catches people out.
---

Most of the bridging transforms VFB and the Jefferis lab publish are
[CMTK](/docs/tools/cmtk/) registrations. The FANC and BANC transforms are not: they are
elastix, so moving data into or out of those spaces needs elastix installed as well.

If you are not working with FANC or BANC, you do not need this.

## What to install

navis looks for a **`transformix` executable** on your `PATH` and uses the elastix `lib`
directory that sits beside it. It is therefore the precompiled command-line binaries you want,
from the [elastix releases](https://github.com/SuperElastix/elastix/releases), unpacked
somewhere on your `PATH`.

The Python package `itk-elastix` and the SimpleElastix bindings are a different interface to
the same algorithms. They are useful in their own right, but installing them does not give
navis the `transformix` binary it looks for.

## The library-path catch

elastix needs its own `lib` directory on the dynamic library search path — `LD_LIBRARY_PATH`
on Linux, `DYLD_LIBRARY_PATH` on macOS — or the binaries fail to start. navis sets this up
itself when it imports, so transforms run from inside a Python session generally work once the
binaries are unpacked. Running `transformix` directly from a shell may need the variable set by
hand; the release archives ship a script for this.

Note that macOS strips `DYLD_*` variables from protected processes under SIP, which is a
recurring source of confusion when the same setup works in one context and not another.

## Where next

Which spaces need elastix, and how a route between two spaces is chosen, is covered on the
[bridging registrations](/docs/concepts/bridging/) page.
[flybrains](/docs/tools/navis-flybrains/) is what actually invokes it from Python.

Documentation and manual: [elastix.dev](https://elastix.dev/) and the
[project wiki](https://github.com/SuperElastix/elastix/wiki).
Source: [SuperElastix/elastix](https://github.com/SuperElastix/elastix).
