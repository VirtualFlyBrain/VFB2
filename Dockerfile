# Build image for the static site.
#
#   docker build -t vfb-static-builder .
#   docker run --rm -v "$PWD:/src" -v vfb_cache:/tmp vfb-static-builder
#
# Standard Hugo is deliberate: the theme ships plain CSS concatenated by Hugo
# rather than Sass, so it needs neither the extended edition nor Dart Sass, and
# no Node toolchain. bash and rsync are added for deploy.sh, which stages the
# build and syncs it into the served directory rather than writing there
# directly.
#
# Replaces klakegg/hugo, which is unmaintained and predates the minimum this
# site needs (Hugo 0.128.0).
FROM ghcr.io/gohugoio/hugo:v0.164.0

USER root
RUN apk add --no-cache bash rsync findutils

ENTRYPOINT []
CMD ["/bin/bash", "/src/deploy.sh"]
