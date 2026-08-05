# Build image for the static site.
#
#   docker build -t vfb-static-builder .
#   docker run --rm -v "$PWD:/src" vfb-static-builder
#
# Standard (non-extended) Hugo is deliberate: the theme ships plain CSS
# concatenated by Hugo rather than Sass, so it needs neither the extended
# edition nor a Dart Sass binary, and no Node toolchain.
#
# Replaces klakegg/hugo, which is unmaintained and predates the minimum this
# site needs (Hugo 0.128.0).
FROM ghcr.io/gohugoio/hugo:v0.164.0

WORKDIR /src
CMD ["--gc", "--minify"]
