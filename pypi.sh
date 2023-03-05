#!/bin/bash

G_SYNOPSIS="

 NAME

	pypi.sh

 SYNOPSIS

	pypi.sh <ver>

 ARGS

	<ver>
	A version string to upload. Typically something like '0.20.22'.

 DESCRIPTION

	pypi.sh is a simple helper script to tag and upload a new version of pypi.sh 


"

if (( $# != 1 )) ; then
    echo "$G_SYNOPSIS"
    exit 1
fi

VER=$1

pandoc README.md --from markdown --to rst -s -o README.rst
git commit -am "v${VER}"
git push origin master
git tag $VER
git push origin --tags

rstcheck README.rst
python3 -m build
twine check dist/*
twine upload dist/$(basename $(pwd)|tr '-' '_')-${VER}.tar.gz

