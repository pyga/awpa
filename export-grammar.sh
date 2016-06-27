#!/bin/sh -eux
export GIT_DIR="$1/.git"
shift
for v in "$@"; do
    vn=$(echo "$v" | tr -d .)
    git show origin/"$v":Grammar/Grammar > awpa/pgen2/py"$vn"/Grammar.txt
    git show origin/"$v":Lib/token.py | sed '/^def .*main/,$d' > awpa/pgen2/py"$vn"/token.py
done
