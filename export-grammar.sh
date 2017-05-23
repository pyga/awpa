#!/bin/sh -eux
# Part of the awpa package: https://github.com/habnabit/awpa
# See LICENSE for copyright.

export GIT_DIR="$1/.git"
git fetch

LICENSE='# Part of the awpa package: https://github.com/habnabit/awpa
# See LICENSE for copyright.
'

shift
for v in "$@"; do
    vn=$(echo "$v" | tr -d .)
    gramdir="awpa/gram_py$vn"
    mkdir -p "$gramdir"
    touch "$gramdir/__init__.py"
    echo "$LICENSE" > "$gramdir/Grammar.txt"
    git show origin/"$v":Grammar/Grammar >> "$gramdir/Grammar.txt"
    echo "$LICENSE" > "$gramdir/token.py"
    git show origin/"$v":Lib/token.py | sed '/^def .*main/,$d' >> "$gramdir/token.py"
done
