#!/bin/bash
# Build the static site directly into the served directory.
#
# Run by the Rancher `hugo-builder` service (start_once), which mounts the
# Jenkins workspace at /src and a cache volume at /tmp. /src/public is the NFS
# volume that vfb-services-live/vfb-static-site serves read-only.
#
# ---------------------------------------------------------------------------
# Why this builds in place again
#
# The previous version staged to /tmp/build and rsynced into /src/public, so
# that no visitor ever saw a half-updated site. Sound in principle; on this
# storage it does not finish.
#
# Both /src and /tmp are NFS mounts of the same Synology volume, so staging
# turns one write pass into: write 763k files to NFS, enumerate 763k in the
# staging tree, enumerate ~763k in the live tree, then read 763k and write 763k
# back -- roughly four times the metadata work, all of it against the one
# resource that is already the bottleneck. Measured on the volume: readdir+stat
# runs at 253/s, because 187 GiB of btrfs metadata is backed by 128 MiB of page
# cache on a 6 GB appliance.
#
# Measured on the 2026-08-14 run: Hugo 4h41m, then 1h15m for the staging
# find alone, with the live-tree find and the copy still to come. The staged
# path has never once completed. The in-place build published every version of
# this site up to 2026-08-05.
#
# The trade-off is real and accepted: during the build the site serves a mix of
# old and new pages. It is survivable because nothing is deleted -- old
# fingerprinted assets stay on disk, so old pages keep resolving until they are
# overwritten. Restore the staged version from git history once the corpus is
# sharded and the volume's metadata is cached; the cost model is what makes it
# unworkable, not the design.
#
# Corollary: pages that are no longer generated are never removed from
# /src/public. That was true of every build before 2026-08-05 too. Removing
# them needs an occasional deliberate sweep, not --cleanDestinationDir, which
# would empty the live tree at the start of a four-hour build.
#
# Deliberately does NOT pass --enableGitInfo. hugo.toml sets
# enableGitInfo = false and the flag would override it; collecting git metadata
# across the term corpus is expensive and nothing in the theme uses it.
# ---------------------------------------------------------------------------
set -euo pipefail
set -x

SRC="${SRC_DIR:-/src}"
LIVE="$SRC/public"
export HUGO_CACHEDIR="${HUGO_CACHEDIR:-/tmp/hugo_cache}"
LOG="${BUILD_LOG:-/tmp/hugo-build.out}"

cd "$SRC"

# ---------------------------------------------------------------- build ------
# --noBuildLock, and a stale lock cleared first.
#
# Hugo takes an flock on .hugo_build.lock at startup and waits for it forever if
# it cannot get one -- no message, no error, no timeout. The lock guards against
# a second concurrent build, which cannot happen here: this container is the
# only builder and Rancher runs it start_once. So it protects nothing.
rm -f "$SRC/.hugo_build.lock"

hugo --noBuildLock --gc --minify --destination "$LIVE" 2>&1 | tee "$LOG"

# ---------------------------------------------------------------- gates ------
# Cheap checks only. An in-place build has already published by the time these
# run, so they are an alarm rather than a gate -- but two stats cost nothing and
# a missing index.html is worth shouting about. The old page-count gate is gone
# with the staging tree: counting 763k files with find took 75 minutes.
test -s "$LIVE/index.html"
test -s "$LIVE/sitemap.xml"

# Hugo's own summary table, rather than a find over the live tree.
#   Pages            | 763455
pages=$(awk -F'|' '/^[[:space:]]*Pages[[:space:]]*\|/ {gsub(/[^0-9]/,"",$2); print $2; exit}' "$LOG")

if [ -z "${pages:-}" ]; then
  echo "ERROR: could not read a page count from Hugo's output." >&2
  exit 1
fi
if [ "$pages" -lt 100 ]; then
  echo "ERROR: Hugo reported only $pages pages." >&2
  exit 1
fi

echo "published $pages pages to $LIVE"
