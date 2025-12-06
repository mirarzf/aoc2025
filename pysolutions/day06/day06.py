def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()
    ops = lines[-1].split()

    nb_terms = [] 
    terms_size = 0 
    for e in lines[-1][1:]: 
        if e == ' ': 
            terms_size += 1 
        else: 
            nb_terms.append(terms_size)
            terms_size = 0 
    nb_terms.append(terms_size+1)

    terms = []
    if puzzlepart == 1: 
        terms = [[] for i in range(len(ops))]
        for line in lines[:-1]: 
            for i, e in enumerate(line.split()): 
                terms[i].append(int(e))

    else: # puzzleplart == 2 
        terms_per_op = []
        curr_nb_terms = 1 
        nb_terms_idx = 0 
        for i in range(len(lines[0])-1): 
            new_term = ''
            for j in range(len(lines)-1): 
                if lines[j][i] != '': 
                    new_term += lines[j][i] 
            if len(new_term.split()) != 0: 
                terms_per_op.append(int(new_term))
                curr_nb_terms += 1 
            else: 
                terms.append(terms_per_op)
                terms_per_op = []
                nb_terms_idx += 1
                curr_nb_terms = 1
        terms.append(terms_per_op)

    total = 0 
    for i, op in enumerate(ops): 
        if op == '+': 
            total += sum(terms[i])
        else: # op == '*': 
            multotal = 1
            for factor in terms[i]: 
                multotal *= factor
            total += multotal
    return total
            
# Part 1: 5346286649122
# Part 2: 10389131401929
