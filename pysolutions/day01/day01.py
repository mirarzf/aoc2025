def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    dialnb = 50
    compteur1 = 0 
    compteur2 = 0
    for line in lines: 
        dir = 1 if line[0] == 'R' else -1 
        if dialnb != 0: 
            dialnb = dialnb + dir * (int(line[1:])%100)
            if dialnb % 100 == 0: 
                compteur1 += 1 
                print("on arrive à 0")
            else: 
                print(dialnb)
                if dialnb > 100 or dialnb < 0: 
                    compteur2 += 1 
                    print("on dépasse sur le côté")
        else: 
            dialnb += dir * (int(line[1:])%100)
        dialnb %= 100 
        compteur2 += int(line[1:])//100 
        print(line[:-1], dialnb, compteur2+compteur1)

    if puzzlepart == 1: 
        return compteur1
    else: 
        return compteur2+compteur1
