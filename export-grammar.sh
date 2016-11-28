#!/bin/sh -eux
# Part of the awpa package: https://github.com/habnabit/awpa
# See LICENSE for copyright.

export GIT_DIR="$1/.git"
shift
for v in "$@"; do
    vn=$(echo "$v" | tr -d .)
    git show origin/"$v":Grammar/Grammar > awpa/pgen2/py"$vn"/Grammar.txt
    git show origin/"$v":Lib/token.py | sed '/^def .*main/,$d' > awpa/pgen2/py"$vn"/token.py
done
