import numpy as np 

def getSplittingNb(grid, entryCoords):
    if grid.shape[0] == 1: 
        return 0
    
    nextCoords = [] 
    nb_splits = 0 
    for j in entryCoords: 
        if grid[0,j] == 1: 
            if j-1 >= 0: 
                nextCoords.append(j-1)
            if j+1 < grid.shape[1]: 
                nextCoords.append(j+1)
            nb_splits += 1 
        else: 
            nextCoords.append(j)
    nextCoords = list(set(nextCoords))

    return nb_splits + getSplittingNb(grid[1:,:], nextCoords)        

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()
    
    grid = np.zeros((len(lines), len(lines[0])), dtype=int)

    Sidx = 0, 0 
    for i in range(grid.shape[0]): 
        for j in range(grid.shape[1]): 
            if lines[i][j] == 'S': 
                Sidx = i, j 
            elif lines[i][j] == '^': 
                grid[i][j] = 1 
    
    retval = getSplittingNb(grid, [Sidx[1]])
    
    return retval

# Part 1: 
# Part 2: 
