import os
import sys
from ..globals import *

def main():

    # print(contants.DATA_DIR)
    for d in reversed([x[0] for x in os.walk(contants.DATA_DIR)]):
         if d != 'data':
             enddir = d.split("/")[-1].lower().replace(" ", "-")
             oldpath = '/'.join(d.split("/")[:-1])
             newpath = os.path.join(oldpath, enddir)
             os.rename(d, newpath)

if __name__ == "__main__":

    main()