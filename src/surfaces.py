#!/usr/bin/env python
import os
import sys
from py_utils import *
from globals import *


def main():
    dem_tin_file = f"{DEMPATH}/{BASENAME}.tif"
    dsm_tin_file = f"{DSMPATH}/{BASENAME}.tif"

    metadata = get_pc_metadata(IN_FILE)    

    print("Creating DEM TIN...")    
    make_dem_tin(pipelines.DEM, IN_FILE, dem_tin_file, metadata)

    print("Creating DSM TIN...")    
    make_dem_tin(pipelines.DSM, IN_FILE, dsm_tin_file, metadata)

    
if __name__ == "__main__":

    IN_FILE = sys.argv[1]
    BASENAME = os.path.basename(IN_FILE).split('.')[0]
    DEMPATH = os.path.join(constants.DATA_DIR, constants.WORKUNIT, constants.QG_DEM)
    DSMPATH = os.path.join(constants.DATA_DIR, constants.WORKUNIT, constants.QG_DSM)
    
    for d in [DEMPATH, DSMPATH]:
        os.makedirs(d, exist_ok=True)
    
    main()