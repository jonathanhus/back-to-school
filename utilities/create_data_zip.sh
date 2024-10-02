#!/bin/sh

# Creates a zip file for the resources and splits directories
# Also adds password protection so that language data won't be
# leaked on the web.

# run this script using:
#    bash create_data_zip.sh

# The zip file is included in the GitHub repo, which can then be
# unzipped on the target system

cd ..
zip -r -e -P password language.zip splits resources  -x "**/.DS_Store"
# zip -r -e -P password splits.zip splits  -x "**/.DS_Store"
# zip -r -e -P password resources.zip resources  -x "**/.DS_Store"
