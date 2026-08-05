#!/bin/bash
# Build the static site into public/.
#
# Run by the Rancher `hugo` service (start_once), which mounts the Jenkins
# workspace jenkins_home/workspace/update_vfb_static_site at /src. The output
# directory is then served read-only by vfb-services-live/vfb-static-site.
#
# Deliberately does NOT pass --enableGitInfo: hugo.toml sets enableGitInfo=false
# and the flag would override it. Collecting git metadata across the generated
# term corpus costs a great deal and nothing in the theme uses it.
#
# The npm/yarn/postcss install and the `hugo mod` calls this script used to
# carry were Docsy's requirements. vfb-nova has no modules, no node
# dependencies and no Sass, so a single Hugo invocation is the whole build.
set -euo pipefail
set -x

cd /src

hugo --gc --minify
