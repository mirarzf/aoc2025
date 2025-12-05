import numpy as np 

def isFresh(fresh_ranges, id): 
    for rangeids in fresh_ranges: 
        if id >= rangeids[0] and id <= rangeids[1]: 
            return True 
    return False 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    i = 0 
    line = lines[0]
    fresh_ranges = []
    while line != '\n': 
        ids_ranges = [int(e) for e in line.split('-')] 
        fresh_ranges.append(ids_ranges)
        i += 1 
        line = lines[i]
    
    i += 1 
    ids_to_check = []
    while i < len(lines) and lines[i] != '\n': 
        ids_to_check.append(int(lines[i]))
        i += 1 

    print(fresh_ranges, ids_to_check)

    counter = 0 
    for id in ids_to_check: 
        if isFresh(fresh_ranges, id): 
            counter += 1 

    return counter 
# Part 1: 
# Part 2: 
