import os
import sys
from ..globals import *
import zipfile 

def main():

    zlist = zipfile.ZipFile(zfile)
    with zlist.open(zlist.namelist()[0]) as zf:
        with open(os.path.join(laspath,zlist.namelist()[0]), 'wb') as f:
            f.write(zf.read())

if __name__ == "__main__":

    zfile = sys.argv[1]
    laspath = os.path.join(contants.DATA_DIR, contants.QG_LAS, '/'.join(zfile.split("/")[1:-1]))
    os.makedirs(laspath, exist_ok=True)

    main()