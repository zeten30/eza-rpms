#!/bin/bash

rm -rf src/github-exa 2>/dev/null

git clone https://github.com/ogham/exa src/github-exa

cargo install --git https://github.com/ogham/exa --force

cp ~/.cargo/bin/exa src/exa/

cp -r src/github-exa/contrib/man/exa.1 src/exa/exa-man
cp -r src/github-exa/contrib/completions* src/exa/
cp -r src/github-exa/LICENCE src/exa/

cd src/

tar cfz exa.tar.gz exa/

cd ..
