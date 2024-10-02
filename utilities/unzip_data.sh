#!/bin/sh

# Creates a zip file for the resources and splits directories
# Also adds password protection so that language data won't be
# leaked on the web.

# run this script using:
#    bash unzip_data.sh

# The zip file is included in the GitHub repo, which can then be
# unzipped on the target system

cd ..
unzip language.zip
