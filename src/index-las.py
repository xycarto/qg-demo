import os
import sys
from .globals import *
from .py_utils import *
import subprocess as sub
import geopandas as gp

def main():

    df = []
    pclist = os.listdir(PC_DIR)
    for laz in pclist:
        lazpath = os.path.join(PC_DIR, laz)
        metadata = get_pc_metadata(lazpath)
        poly = bbox(metadata.header)
        write_df(df, constants.CRS, laz, constants.WORKUNIT, lazpath, "unknown", metadata.header, poly)


    gpkg_out = os.path.join(constants.DATA_DIR, constants.WORKUNIT, f'{constants.WORKUNIT}-index.gpkg')
    gp.GeoDataFrame(df, crs=constants.CRS).to_file(gpkg_out, driver='GPKG')

if __name__ == "__main__":

    PC_DIR = sys.argv[1]

    main()