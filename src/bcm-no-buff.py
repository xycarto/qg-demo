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
        f"pdal -v 0 pipeline '{pipelines.FILTER}' \
            --readers.las.filename='{in_file}' \
            --writers.las.filename='{bcm_file}'",
        shell=True,
    )

def main():
    # s3 = get_creds()
    # get_grid_index(s3, WESM_GRID_BUCKET, GRID_INDEX_FILE, INDEX_FILE)

    # index_file = gp.read_file(INDEX_FILE)
    # index_row = index_file[index_file['file_name'] == os.path.basename(IN_FILE)]

    # get_usgs_file(s3, index_row.usgs_loc.values[0], IN_FILE, USGS_BUCKET)

    filter_laz(IN_FILE)    

if __name__ == "__main__":

    IN_FILE = sys.argv[1]
    OUTPATH = os.path.join(contants.DATA_DIR, contants.QG_FILTERED, '/'.join(IN_FILE.split("/")[1:-1]))

    for d in [OUTPATH]:
        os.makedirs(d, exist_ok=True)
        
    main()