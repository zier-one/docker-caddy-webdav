#!/bin/sh -eux
docker run -e CANDY_TAG=$1 -v $(pwd):/pwd hairyhenderson/gomplate -f /pwd/Dockerfile.tmpl -o /pwd/Dockerfile

