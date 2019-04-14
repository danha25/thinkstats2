"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def readFemaleResponses(dictionaryFile='./data/2002FemResp.dct', dataFile='./data/2002FemResp.dat.gz', nrows=None):
    dictionary = thinkstats2.ReadStataDct(dictionaryFile);
    femResp = dictionary.ReadFixedWidth(dataFile, compression='gzip', nrows=nrows)
    return femResp

def ValidatePregnum(femResp):
    # Get female pregnancy dataFrame
    femPreg = nsfg.ReadFemPreg()
    pregMap = nsfg.MakePregMap(femPreg)
    
    for index, pregnum in femResp.pregnum.items():
        caseid = femResp.caseid[index]
        indices = pregMap[caseid]
        
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    femResp = readFemaleResponses();
    
    assert(len(femResp) == 7643)
    assert(femResp.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(femResp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
