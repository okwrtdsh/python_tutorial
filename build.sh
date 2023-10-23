#!/bin/bash
set -eux
npx honkit build
rm -rf ./docs
mv ./_book ./docs
