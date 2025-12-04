import numpy as np 

def isInGrid(i,j,gridshape): 
    if i >= gridshape[0]: 
        return False 
    if i < 0: 
        return False 
    if j >= gridshape[1]: 
        return False 
    if j < 0: 
        return False 
    return True 

def nbNeighbours(grid, i, j): 
    n_nb = 0 
    for nbi in range(i-1,i+2): 
        for nbj in range(j-1,j+2): 
            if isInGrid(nbi, nbj, grid.shape) and (nbi != i or nbj != j): 
                if grid[nbi, nbj] == 1: 
                    n_nb += 1 
    return n_nb 

def updateGrid(grid): 
    newgrid = np.zeros(grid.shape, dtype=int)

    for i in range(grid.shape[0]): 
        for j in range(grid.shape[1]): 
            if grid[i,j] == 1 and nbNeighbours(grid, i, j) >= 4: 
                newgrid[i,j] = 1
    
    return newgrid 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    grid = np.ones((len(lines), len(lines[0])-1), dtype=int)
    
    i = 0 
    for line in lines: 
        for j in range(grid.shape[1]): 
            if line[j] == ".": 
                grid[i,j] = 0 
        i += 1 
    initial_nb_of_rolls = np.sum(grid)

    old_nb_of_rolls = np.sum(grid)
    nb_of_rolls = 0
    if puzzlepart == 1: 
        grid = updateGrid(grid)
    else: 
        while old_nb_of_rolls != nb_of_rolls: 
            grid = updateGrid(grid)
            old_nb_of_rolls = nb_of_rolls
            nb_of_rolls = np.sum(grid)

    return initial_nb_of_rolls-np.sum(grid) 

# Part 1: 1527 
# Part 2: 8690 
