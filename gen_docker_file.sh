#!/bin/sh -eux
CANDY_TAG=$1 gomplate -f ./Dockerfile.tmpl -o ./Dockerfile
