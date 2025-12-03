import numpy as np 

def getMaximumVoltage(line): 
    return 0 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    retval = 0

    for line in lines: 
        retval += getMaximumVoltage(line)

    if puzzlepart == 1: 
        return retval #  
    else: 
        return retval #  
