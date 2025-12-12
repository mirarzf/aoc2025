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

def getNbTimelines(grid, dist): 
    if grid.shape[0] == 1: 
        return np.sum(dist)
    
    next_dist = np.zeros(grid.shape[1], dtype=int)
    for j in range(grid.shape[1]): 
        if dist[j] > 0: 
            if grid[0,j] == 1: 
                if j-1 >= 0: 
                    next_dist[j-1] += dist[j]
                if j+1 < grid.shape[1]: 
                    next_dist[j+1] += dist[j]
            else: 
                next_dist[j] += dist[j]
    
    return getNbTimelines(grid[1:], next_dist)


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
    
    if puzzlepart == 1: 
        return getSplittingNb(grid, [Sidx[1]])
    else: 
        dist = np.zeros(grid.shape[1], dtype=int)
        dist[Sidx[1]] = 1
        return getNbTimelines(grid, dist)

# Part 1: 1649 
# Part 2: 
