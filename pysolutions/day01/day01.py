import numpy as np 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    dialnb = 50
    compteur1 = 0 
    compteur2 = 0
    for line in lines: 
        dir = 1 if line[0] == 'R' else -1 
        if puzzlepart == 2: 
            print(line[:-1])
            compteur2 += int(line[1:]) // 100 
            if dialnb != 0 and (dialnb + dir*int(line[1:]) > 100 or dialnb + dir*int(line[1:]) < 0): 
                compteur2 += 1 
            print("ahoy", dialnb + dir*int(line[1:]), int(line[1:]) // 100 + 1)
        dialnb = (dialnb + dir * int(line[1:])) % 100
        if puzzlepart == 1: 
            if dialnb == 0: 
                compteur1 += 1 
        print(dialnb, compteur2)

    if puzzlepart == 1: 
        return compteur1
    else: 
        return compteur2+compteur1
