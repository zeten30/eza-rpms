#!/bin/bash

cargo install --git https://github.com/ogham/exa --force

cp ~/.cargo/bin/exa src/exa/

cd src/

tar cfz exa.tar.gz exa/

cd ..

