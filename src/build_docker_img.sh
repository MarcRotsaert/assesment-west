#!/usr/bin/env bash

name="westassesment"
version="0.1"

target_img="${name}:${version}"

printf "Build image %s\n" "${target_image}"

docker build --no-cache -f Dockerfile -t ${target_img} --build-arg BASE_CONTAINER=${target_img} .
# docker tag "${target_img}" "${name}:latest"

# printf "Tag %s as latest\n" "${repo}/${name}:latest"
# docker tag ${target_img} "${repo}/${name}:latest"

docker images | grep ${name}
