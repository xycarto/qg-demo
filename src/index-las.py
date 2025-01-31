import os
import sys
from .globals import *
import subprocess as sub
import json

def main():

    pclist = os.listdir(PC_DIR)
    for laz in pclist:
        lazpath = os.path.join(PC_DIR, laz)
        header = sub.check_output(
            f"pdal info --all {lazpath}",
        shell=True,
        )

        jhead = json.loads(header)
        print(json.dumps(jhead))

if __name__ == "__main__":

    PC_DIR = sys.argv[1]

    main()