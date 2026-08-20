# Build image for the static site.
#
#   docker build -t vfb-static-builder .
#   docker run --rm -v "$PWD:/src" -v vfb_cache:/tmp vfb-static-builder
#
# Pinned to Hugo 0.122.0 rather than the newest release. That is a deliberate
# step backwards and the reason is measured, not suspected.
#
# The content tree is ~763k generated term pages, ~650k of them in a single
# directory (content/en/blog/ontologies/vfb), reached over NFSv3 from a Synology
# volume whose btrfs metadata sits on RAID5 spinning disks. Measured on that
# volume: plain readdir runs at 5-29k entries/s, but readdir+stat runs at
# 253/s — ~4ms per inode, a disk seek, nothing cached. NFSv3 uses READDIRPLUS,
# so the server stats every entry it enumerates. Per-page filesystem cost is
# therefore the dominant term in this build, far above template or render cost.
#
# Hugo's per-page filesystem cost rose at v0.123.0, which rewrote page assembly.
# Counted with strace over an identical 25k-page corpus on local disk:
#
#     0.122.0    75,658 openat    76,997 newfstatat   3.06 stat/page
#     0.128.0   100,788 openat   101,527 newfstatat   4.04 stat/page
#     0.140.2   100,813 openat   101,485 newfstatat   4.03 stat/page
#     0.164.0   100,844 openat   101,488 newfstatat   4.03 stat/page
#
# Flat from 0.128 onward, so this is one regression at 0.123, not a drift. At
# 763k pages and 253 stat/s that extra stat per page is ~49 min on top of a
# build already costing ~2.6h of pure metadata I/O.
#
# 0.122.0 is the last version known to complete this build: the live term pages
# carry `generator: Hugo 0.122.0` and were written 2026-08-05 17:59. No 0.16x
# build has ever finished — each ran 17h+ with one thread in uninterruptible
# sleep on the vfb/ directory and not a single page written.
#
# This pin is a workaround. The fix is to stop holding 650k files in one
# directory (shard vfbterms.py's output) and to pin the volume's btrfs metadata
# to its SSD cache. When either lands, raise HUGO_VERSION — it is an ARG so that
# is a one-line change.
#
# Debian rather than Alpine, and the tarball rather than ghcr.io/gohugoio/hugo:
# that registry has no v0.122.0 tag (it begins around v0.140), and the extended
# release binary is glibc-linked — `ldd` gives /lib64/ld-linux-x86-64.so.2 plus
# libstdc++.so.6 — so musl with gcompat is not a safe host for it.
#
# Extended edition, matching the rcourt/docsy-builder:Feb2023 that produced the
# last good site. The theme ships plain CSS and needs no Sass, so the standard
# edition would also serve and is statically linked; keeping extended here
# changes one variable at a time relative to the last build known to work.
#
# The theme declares min_version 0.128.0 for `[pagination] pagerSize`, so 0.122
# emits one WARN and falls back to 10 items per page. Nothing on the site
# paginates today, so that is latent rather than active.
FROM debian:bookworm-slim

ARG HUGO_VERSION=0.122.0

# bash and find are already in the base image. rsync is for deploy.sh, which
# stages the build and syncs it into the served directory rather than writing
# there directly. libstdc++6 is what the extended Hugo binary links against.
RUN apt-get update \
 && apt-get install -y --no-install-recommends rsync ca-certificates libstdc++6 \
 && rm -rf /var/lib/apt/lists/*

ADD https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz /tmp/hugo.tgz
RUN tar xzf /tmp/hugo.tgz -C /usr/local/bin hugo \
 && rm -f /tmp/hugo.tgz \
 && hugo version

# Deliberately root. The published tree on the NFS volume is owned by root from
# the klakegg-era builds, so an unprivileged rsync could not overwrite it.
USER root

# deploy.sh uses ${HUGO_CACHEDIR:-/tmp/hugo_cache}, so this must be set
# explicitly: Rancher mounts the workspace at /src and the cache volume at /tmp.
ENV HUGO_CACHEDIR=/tmp/hugo_cache
WORKDIR /src

ENTRYPOINT []
CMD ["/bin/bash", "/src/deploy.sh"]
