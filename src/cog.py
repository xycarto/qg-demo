#!/usr/bin/env python
import os
import boto3
import sys
import subprocess as sub
from osgeo import gdal
from py_utils import *
from globals import *


def main():

    tifs = [f"{os.path.join(IN_DIR, tif)}" for tif in os.listdir(IN_DIR) if not os.path.isdir(tif) and tif.endswith('.tif')]

    vrt = f"{IN_DIR}/{os.path.basename(IN_DIR)}.vrt"
    gdal.BuildVRT(
        vrt,
        tifs,
    ) 

    creation_options = [
    "COMPRESS=DEFLATE",
    "BIGTIFF=YES",
    "NUM_THREADS=10",
    "OVERVIEW_RESAMPLING=LANCZOS",
    "WARP_RESAMPLING=BILINEAR",
    "OVERVIEW_COMPRESS=DEFLATE",
    ]

    gdal.Translate(    
        f"{COGPATH}/{os.path.basename(IN_DIR)}-cog.tif",
        vrt,
        format = "COG",
        callback=gdal.TermProgress_nocb,
        creationOptions = creation_options
    )

if __name__ == "__main__":

    IN_DIR = sys.argv[1]
    COGPATH = os.path.join(constants.DATA_DIR, constants.WORKUNIT, constants.QG_COG)

    for d in [COGPATH]:
        os.makedirs(d, exist_ok=True)

    main()