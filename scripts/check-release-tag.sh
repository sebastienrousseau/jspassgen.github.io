#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0 OR MIT
#
# Check a release tag before the release workflow builds from it:
#
#   scripts/check-release-tag.sh <tag> <project> <commit>
#
# The tag must be `v` + the version in VERSION, an annotated tag whose
# first message line is `<project> v<version>`, carry a signature, and
# point at <commit> (the commit the workflow checked out). It cannot
# verify the signature (CI has no maintainer keys): run
# `git verify-tag <tag>` locally before pushing the tag.
set -euo pipefail

fail() {
  echo "::error::$1" >&2
  exit 1
}

[ "$#" -eq 3 ] || fail "usage: $0 <tag> <project> <commit>"
tag=$1
project=$2
commit=$3

cd "$(git rev-parse --show-toplevel)"
version=$(tr -d '[:space:]' <VERSION)

[ "$tag" = "v${version}" ] || fail "tag ${tag} does not match VERSION ${version}"
[ "$(git cat-file -t "refs/tags/${tag}")" = "tag" ] || fail "${tag} is not an annotated tag"
subject=$(git tag -l --format='%(contents:subject)' "$tag")
[ "$subject" = "${project} v${version}" ] ||
  fail "tag message is '${subject}', expected '${project} v${version}'"
[ -n "$(git tag -l --format='%(contents:signature)' "$tag")" ] || fail "${tag} is not signed"
[ "$(git rev-parse "${tag}^{commit}")" = "$commit" ] ||
  fail "${tag} does not point at ${commit}"

echo "version=${version}"
