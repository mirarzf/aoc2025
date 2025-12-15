import numpy as np 

def eudist(v1, v2): 
    return np.sum([(v1[i]-v2[i])**2 for i in range(3) ])

def fusionner(gauche, droite): 
    if len(gauche) == 0: 
        return droite 
    if len(droite) == 0: 
        return gauche 
    if gauche[0][0] <= droite[0][0]: 
        return [gauche[0]] + fusionner(gauche[1:], droite)
    else: 
        return [droite[0]] + fusionner(gauche, droite[1:])


def trifusion(liste): 
    if len(liste) == 1: 
        return liste 
    
    milieu = len(liste)//2 
    gauche = trifusion(liste[:milieu])
    droite = trifusion(liste[milieu:])
    
    return fusionner(gauche, droite)
    

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    vertices = []
    for line in lines: 
        if line != "": 
            vertices.append([int(e) for e in line.split(',')])
    vertices = np.array(vertices)

    v_dists = [ [] for i in range(len(lines)) ]
    all_dists = []
    
    index = 0
    for i in range(vertices.shape[0]): 
        for j in range(i+1, vertices.shape[0]): 
            dist = eudist(vertices[i], vertices[j])
            all_dists.append((dist, index))
            v_dists[i].append(index)
            v_dists[j].append(index)
            index += 1 

    all_dists_sorted = trifusion(all_dists)
    

    return 0 

# Part 1:  
# Part 2: 
