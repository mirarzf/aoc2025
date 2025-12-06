import numpy as np 

def hasNoOverlap(range1, range2):
    return range2[1] < range1[0] or range2[0] > range1[1]     

def isInRanges(fresh_ranges, id): 
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

    if puzzlepart == 1: 
        counter = 0 
        for id in ids_to_check: 
            if isInRanges(fresh_ranges, id): 
                counter += 1 

        return counter 

    # Sort fresh_ranges per minimum 
    fresh_ranges_sort = np.sort(np.array(fresh_ranges), axis=0)

    left = fresh_ranges_sort[0][0]
    right = fresh_ranges_sort[0][1]
    new_fresh_ranges = []
    for i in range(len(fresh_ranges_sort)): 
        rangei = fresh_ranges_sort[i]
        if rangei[0] <= right: 
            if rangei[1] > right: 
                right = rangei[1]
        else: # rangei[0] > right
            new_fresh_ranges.append([left, right])
            left = rangei[0]
            right = rangei[1]
    new_fresh_ranges.append([left, right])

    # Start counting all the ids 
    somme = 0 
    for range_ids in new_fresh_ranges: 
        somme += range_ids[1]-range_ids[0]+1
    
    return somme 
            
# Part 1: 615
# Part 2: 353716783056994 
