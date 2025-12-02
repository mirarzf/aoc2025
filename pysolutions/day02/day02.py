import numpy as np 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    line = lines[0].split(',')
    for range_of_ids in line: 
        ids = range_of_ids.split('-')[0]
        print(ids)

    if puzzlepart == 1: 
        return 0
    else: 
        return 0
