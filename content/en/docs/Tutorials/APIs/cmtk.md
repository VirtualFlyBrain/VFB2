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

## macOS (Apple Silicon)

Paste this into a terminal. It installs CMTK under your home directory, so it needs no
administrator rights and touches nothing outside its own folder — which matters on managed
or institutional Macs, where you may have no admin rights at all.

```sh
#!/usr/bin/env bash
set -euo pipefail

PREFIX="${CMTK_PREFIX:-$HOME/.local/opt/cmtk}"
ARCHIVE="cmtk-3.4.0-dev-macos-arm64-gcd.tar.gz"
URL="https://github.com/jefferis/cmtk/releases/download/natdev-latest/${ARCHIVE}"
SHA256="4160852416b6cba9a55c7e7d0497e4d7153262a3a5265cafb39d1bb850649d6c"

if [ "$(uname -s)" != "Darwin" ] || [ "$(uname -m)" != "arm64" ]; then
  echo "This installs the Apple Silicon build; you are on $(uname -s)/$(uname -m)." >&2
  exit 1
fi

case "$PREFIX" in
  *" "*) echo "CMTK's launcher cannot handle a space in its path; pick another." >&2; exit 1 ;;
esac

if [ -e "$PREFIX" ] && [ ! -x "$PREFIX/bin/cmtk" ]; then
  echo "$PREFIX exists and is not a CMTK install; set CMTK_PREFIX elsewhere." >&2
  exit 1
fi

tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT

echo "Downloading ${ARCHIVE} (about 50 MB)..."
curl -fSL --progress-bar -o "$tmp/$ARCHIVE" "$URL"

echo "Verifying checksum..."
echo "${SHA256}  ${tmp}/${ARCHIVE}" | shasum -a 256 -c - >/dev/null

mkdir -p "$tmp/stage"
tar -xzf "$tmp/$ARCHIVE" -C "$tmp/stage" --strip-components=2
rm -rf "$PREFIX"; mkdir -p "$(dirname "$PREFIX")"; mv "$tmp/stage" "$PREFIX"

echo "CMTK $("$PREFIX/lib/cmtk/bin/registration" --version) installed in $PREFIX"
echo "Add it to your PATH with:"
echo "  echo 'export PATH=\"${PREFIX}/lib/cmtk/bin:${PREFIX}/bin:\$PATH\"' >> ~/.zshrc"
```

Then run the `export PATH` line it prints, open a new terminal, and check with
`registration --version`.

Two things the script is guarding against. It verifies the download against a published
SHA-256 before unpacking anything, and it refuses to install to a path containing a space:
CMTK's own launcher expands its tool path unquoted, so it cannot dispatch a tool from, say,
`~/Library/Application Support/...`. If the checksum check fails, upstream has most likely
reissued the build — the tag it comes from is a rolling one — so check this page for an
updated hash rather than skipping the verification.

Intel Macs are not covered by that build. Use the contributed
[`CMTK-3.4.0-contrib-MacOSX.zip`](https://www.nitrc.org/frs/?group_id=212) from NITRC instead,
or build from source.

## Linux

CMTK is packaged for Ubuntu/Debian directly:

```sh
sudo apt update && sudo apt install -y cmtk
```

If you have no `sudo` on the machine, the macOS approach works in spirit here too: the
[jefferis/cmtk](https://github.com/jefferis/cmtk/releases/tag/natdev-latest) release also
publishes an x86_64 Linux tarball you can unpack into your home directory.

## Windows

We recommend [**MADI3D**](https://madi3d.org)
([GitHub](https://github.com/sandorbx/MADI3D)), which installs CMTK for you rather than asking
you to do it by hand. In its CMTK setup dialog, choose **Automatic setup**: it enables WSL if
needed, creates its own isolated `MADI3D-CMTK` Ubuntu distribution — your existing WSL
distributions are left untouched — and installs the `cmtk` package inside it.

To do it by hand instead: install [WSL](https://learn.microsoft.com/windows/wsl/install)
(`wsl --install`, from an administrator PowerShell), then inside the Ubuntu shell it opens run
the `apt` command from the Linux section above.

## A note on MADI3D

MADI3D manages its own copy of CMTK rather than using one already on your `PATH`, so installing
it there does not give you CMTK for navis-flybrains or the natverse, and vice versa. Its
automatic setup currently covers Windows and native Ubuntu/Debian; macOS support is
[proposed in PR #38](https://github.com/sandorbx/MADI3D/pull/38). Until that is released, the
script above is the route on macOS. MADI3D also offers "use an existing CMTK installation",
which will happily point at the install the script creates.

## Verifying

Any of the above should leave the individual tools (`registration`, `warp`, `mat2dof`,
`dof2mat`, `reformatx`, `describe`, ...) on your `PATH`:

```sh
registration --version
```

navis-flybrains and the natverse look for those tools rather than the `cmtk` launcher, so it is
the `lib/cmtk/bin` directory that has to be on `PATH` — which is what the script sets up.
