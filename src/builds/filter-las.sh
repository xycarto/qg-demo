#!/bin/bash

LASDIR=$1

# Filter Las
find $LASDIR -name "*.laz" | xargs -P 10 -t -I % make filter pc=%