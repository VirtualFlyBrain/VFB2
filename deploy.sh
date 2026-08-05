#!/bin/bash
# Build the static site and publish it into the served directory.
#
# Run by the Rancher `hugo` service (start_once), which mounts the Jenkins
# workspace at /src and a cache volume at /tmp. /src/public is the NFS volume
# that vfb-services-live/vfb-static-site serves read-only, so it is live traffic.
#
# The build therefore goes to a staging directory first and is rsynced into
# place afterwards. Building straight into /src/public would leave the site
# half-updated for the length of a full run — roughly a quarter of an hour once
# the generated term corpus is included — and every page changes when the theme
# changes, so visitors would be served a mixture of old and new markup with
# fingerprinted asset URLs that may not exist yet.
#
# rsync updates the live tree file by file and defers removals to the end
# (--delete-after), so no page is ever missing mid-run. A directory swap is not
# an option: /src/public is bind-mounted into the nginx container, which holds
# the old inode and would not follow a rename.
#
# Deliberately does NOT pass --enableGitInfo. hugo.toml sets
# enableGitInfo = false and the flag would override it; collecting git metadata
# across the term corpus is expensive and nothing in the theme uses it.
set -euo pipefail
set -x

SRC="${SRC_DIR:-/src}"
LIVE="$SRC/public"
STAGE="${STAGE_DIR:-/tmp/build}"
# Keep Hugo's own cache on the same volume as the staging tree.
export HUGO_CACHEDIR="${HUGO_CACHEDIR:-/tmp/hugo_cache}"
# --checksum avoids rewriting pages whose content has not changed, at the cost
# of reading both trees. Worth trying once the corpus is large and most nightly
# term pages are identical.
RSYNC_OPTS="${RSYNC_OPTS:--a --delete-after --omit-dir-times}"

cd "$SRC"

# ---------------------------------------------------------------- build ------
rm -rf "$STAGE"

# --noBuildLock, and a stale lock cleared first.
#
# Hugo takes an flock on .hugo_build.lock at startup and waits for it forever if
# it cannot get one — no message, no error, no timeout. The symptom is a build
# that copies the static files, then hangs: on 2026-08-05 that was ~66 files and
# 16 MB in the staging tree, a sleeping process at near-zero CPU, and nothing
# else for as long as anyone cared to wait.
#
# The workspace is on NFS, where a lock left behind by an uncleanly killed build
# survives the process that took it. And the lock guards against a second
# concurrent build, which cannot happen here: this container is the only builder
# and Rancher runs it start_once. So it protects nothing and its failure mode is
# an invisible hang.
rm -f "$SRC/.hugo_build.lock"
hugo --noBuildLock --gc --minify --destination "$STAGE"

# ---------------------------------------------------------------- gates ------
# Never publish an obviously broken build. The term corpus comes from an API
# that can fail partially, so a run that produced far fewer pages than the live
# site is far more likely to be a bad vfbterms run than a real deletion.
test -s "$STAGE/index.html"
test -s "$STAGE/sitemap.xml"

new=$(find "$STAGE" -name '*.html' | wc -l)
old=$(find "$LIVE" -name '*.html' 2>/dev/null | wc -l || echo 0)
echo "pages: live=$old new=$new"

if [ "$old" -gt 100 ] && [ "$new" -lt $(( old * 90 / 100 )) ]; then
  echo "ERROR: build has $new pages against $old live, a drop of more than 10%." >&2
  echo "Refusing to publish. Set ALLOW_SHRINK=1 to override." >&2
  [ "${ALLOW_SHRINK:-0}" = "1" ] || exit 1
fi

# ---------------------------------------------------------------- publish ----
rsync $RSYNC_OPTS "$STAGE/" "$LIVE/"

echo "published $new pages to $LIVE"
