import numpy as np 

def eudist(v1, v2): 
    return np.sum([(v2[i]-v1[i])**2 for i in range(3)])

def appendSorted(liste, newelement, lenlistemax = None): 
    if lenlistemax == None: 
        lenlistemax = len(liste)+1
    if len(liste) == 0 or newelement[0] <= liste[0][0]: 
        return [newelement] + liste[:lenlistemax-1]
    for i in range(len(liste)-1): 
        if liste[i][0] <= newelement[0] and liste[i+1][0] >= newelement[0]: 
            return liste[:i+1] + [newelement] + liste[i+1:lenlistemax-1]
    return liste 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    vertices = []
    for line in lines: 
        if line != "": 
            vertices.append([float(e) for e in line.split(',')])
    vertices = np.array(vertices)

    all_dists = []
    if puzzlepart == 1: 
        n_connexions = 1000
    else: 
        n_connexions = None
    index = 0
    for i in range(vertices.shape[0]): 
        for j in range(i+1, vertices.shape[0]): 
            dist = eudist(vertices[i], vertices[j])
            all_dists = appendSorted(all_dists, (dist, i, j), lenlistemax=n_connexions)
            index += 1 
    
    # print(all_dists)
    print(len(all_dists))

    components = {}
    circuits_lengths = {0:1}
    i_dist = 0 
    continueWhileLoop = True
    while i_dist < len(all_dists) and continueWhileLoop: 
        e = all_dists[i_dist] 
        i, j = e[1], e[2]
        if i in components.keys() and j not in components.keys(): 
            components[j] = components[i]
            circuits_lengths[components[i]] += 1 
        
        elif j in components.keys(): 
            if i not in components.keys(): 
                components[i] = i 
                circuits_lengths[i] = 1

            if components[i] != components[j]: 
                new_circuit_r = components[i]
                ex_circuit_r = components[j]

                for vertex in components.keys(): 
                    if components[vertex] == ex_circuit_r: 
                        components[vertex] = new_circuit_r 

                circuits_lengths[new_circuit_r] += circuits_lengths[ex_circuit_r]
                circuits_lengths[ex_circuit_r] = 0 
            
        else: # i not in components.keys() and j not in components.keys()
            components[i] = i
            components[j] = i
            circuits_lengths[i] = 2
        
        continueWhileLoop = puzzlepart == 1 or (max(circuits_lengths.values()) < len(vertices))
        i_dist += 1 
    
    if puzzlepart == 1: 
        retval = 1 
        circuits_lengths_liste = [circuits_lengths[key] for key in circuits_lengths.keys()]
        circuits_lengths_liste.sort(reverse=True)
        for e in circuits_lengths_liste[:3]: 
            retval *= e
        print(circuits_lengths_liste[:3])
        
        return retval

    else: 
        u = all_dists[i_dist-1][1]
        v = all_dists[i_dist-1][2]
        print(vertices[u], vertices[v])
        retval = vertices[u][0]*vertices[v][0]
        return retval 

# Part 1: 330786
# Part 2: 
