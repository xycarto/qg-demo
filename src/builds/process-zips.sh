#!/bin/bash

ZIPDIR=$1

# List zips
ziplist=$( find $ZIPDIR -name "*.zip" )

# Process Zips
for z in ${ziplist[@]}; do
    make unzip zip=$z
done