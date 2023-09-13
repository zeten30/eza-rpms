#!/bin/bash

PKG_NAME="eza"
GIT_REPO="https://github.com/eza-community/eza"
SRC_PATH="src/github-eza"

rm -rf "${SRC_PATH:?}/" 2>/dev/null

git clone "${GIT_REPO}" "${SRC_PATH}"

cargo install --git "${GIT_REPO}" --force

cp ~/.cargo/bin/${PKG_NAME} "src/${PKG_NAME}/"

mkdir -p "src/${PKG_NAME}/completions"

cp -r "${SRC_PATH}/completions/" "src/${PKG_NAME}/"
cp -r "${SRC_PATH}/LICENCE" "src/${PKG_NAME}/LICENSE"

cd src/ || exit

tar cfz "${PKG_NAME}.tar.gz" "${PKG_NAME}/"

cd ..
