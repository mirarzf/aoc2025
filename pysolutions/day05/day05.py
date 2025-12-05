import numpy as np 

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

    # new_fresh_ranges = []
    # for fresh_range in fresh_ranges: 
    #     new_range = []
    #     first_id, sec_id = fresh_range[0], fresh_range[1]
    #     isInRangeFID = isInRanges(new_fresh_ranges, first_id)
    #     isInRangeSID = isInRanges(new_fresh_ranges, sec_id)
    #     if isInRangeFID[0] and not isInRangeSID[0]: 
    #         new_range = [first_id, isInRangeSID[1][0]-1] 
    #     if not isInRangeFID[0] and isInRangeSID[0]: 
    #         new_range = [isInRangeSID[1][1]+1, sec_id] 
    #     if not isInRangeFID[0] and not isInRangeSID[0]: 
    #         new_range = [first_id, sec_id] 
    #     if len(new_range) != 0: 
    #         new_fresh_ranges.append(new_range)
        
    # Start counting all the ids 
    somme = 0 
    for range_ids in new_fresh_ranges: 
        somme += range_ids[1]-range_ids[0]+1
    
    return somme 

            
# Part 1: 615
# Part 2: 
