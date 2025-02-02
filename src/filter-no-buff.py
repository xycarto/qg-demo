#!/usr/bin/env python
import os
import geopandas as gp
import sys
from globals import *
import subprocess as sub


def filter_laz(in_file):
    print("Filtering...")   
    bcm_file =  f"{OUTPATH}/{os.path.basename(in_file)}"
    sub.call(
        f"pdal -v 1 pipeline --nostream '{pipelines.FILTER}' \
            --readers.las.filename='{in_file}' \
            --readers.las.spatialreference='EPSG:{constants.CRS}' \
            --writers.las.filename='{bcm_file}'",
        shell=True,
    )

def main():

    filter_laz(IN_FILE)    

if __name__ == "__main__":

    IN_FILE = sys.argv[1]
    OUTPATH = os.path.join(constants.DATA_DIR, constants.WORKUNIT, constants.QG_FILTERED)

    for d in [OUTPATH]:
        os.makedirs(d, exist_ok=True)
        
    main()