import numpy as np 

def getNbPaths(grid, dist, puzzlepart=1):
    if grid.shape[0] == 1: 
        if puzzlepart == 1: 
            return 0
        else: # puzzlepart == 2 
            return np.sum(dist)
    
    next_dist = np.zeros(grid.shape[1], dtype=int)
    nb_splits = 0 
    for j in range(grid.shape[1]): 
        if dist[j] > 0: 
            if grid[0,j] == 1: 
                if j-1 >= 0: 
                    next_dist[j-1] += dist[j]
                if j+1 < grid.shape[1]: 
                    next_dist[j+1] += dist[j]
                nb_splits += 1 
            else: 
                next_dist[j] += dist[j]
    
    if puzzlepart == 1: 
        return nb_splits + getNbPaths(grid[1:], next_dist, puzzlepart)
    else: 
        return getNbPaths(grid[1:], next_dist, puzzlepart)

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()
    
    grid = np.zeros((len(lines), len(lines[0])), dtype=int)

    Sidx = 0, 0 
    for i in range(grid.shape[0]): 
        for j in range(grid.shape[1]): 
            if lines[i][j] == 'S': 
                Sidx = j 
            elif lines[i][j] == '^': 
                grid[i][j] = 1 
    
    dist = np.zeros(grid.shape[1], dtype=int)
    dist[Sidx] = 1

    if puzzlepart == 1: 
        return getNbPaths(grid, dist, 1)
    else: 
        return getNbPaths(grid, dist, 2)

# Part 1: 1649 
# Part 2: 16937871060075
