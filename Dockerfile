# Build image for the static site.
#
#   docker build -t vfb-static-builder .
#   docker run --rm -v "$PWD:/src" -v vfb_cache:/tmp vfb-static-builder
#
# v0.164.0 is the newest stable Hugo (released 2026-07-06) and the site builds
# clean on it: 186 pages, no WARN, no ERROR. Pinned rather than :latest so
# rebuilding this image cannot silently change the site.
#
# The theme's declared minimum is 0.128.0 (`[pagination] pagerSize`). It does
# also build on 0.122.0, which is what rcourt/docsy-builder:Feb2023 carries, but
# that image has no rsync and warns about the declared minimum.
#
# Base is Alpine 3.22, so apk is correct. The upstream image already carries
# git, Node, npm and Dart Sass. This site needs none of them — the theme ships
# plain CSS concatenated by Hugo, so even the extended edition is optional — but
# they come with the official image and are not worth stripping out.
#
# bash and rsync are for deploy.sh, which stages the build and syncs it into the
# served directory rather than writing there directly. findutils replaces
# busybox find so the page-count gate behaves predictably.
FROM ghcr.io/gohugoio/hugo:v0.164.0

# Deliberately root, unlike the upstream image's hugo:hugo. The published tree
# on the NFS volume is owned by root from the klakegg-era builds, so an
# unprivileged rsync could not overwrite it.
USER root
RUN apk add --no-cache bash rsync findutils

# The upstream image sets HUGO_CACHEDIR=/cache and WORKDIR /project. Both are
# wrong here and neither can be left to deploy.sh's defaults: the script uses
# ${HUGO_CACHEDIR:-/tmp/hugo_cache}, which never fires while the image has the
# variable set, so the cache would land in the container's writable layer
# instead of the volume mounted at /tmp — discarded every run, and growing host
# disk in between. Rancher mounts the workspace at /src and the cache at /tmp.
ENV HUGO_CACHEDIR=/tmp/hugo_cache
WORKDIR /src

ENTRYPOINT []
CMD ["/bin/bash", "/src/deploy.sh"]
