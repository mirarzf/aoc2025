def getMirror(nb:int): 
    dec_length = len(str(nb))
    return nb * (1 + 10**dec_length)

def hasRepeats(nb:int): 
    nb_str = str(nb)
    n_half_str = len(nb_str)//2 
    for l in range(n_half_str, 0,-1): 
        if len(nb_str)%l == 0: 
            pattern_to_repeat = nb_str[:l]
            repeated_pattern = pattern_to_repeat*(len(nb_str)//l)
            if repeated_pattern == nb_str: 
                return True 
    return False 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    line = lines[0].split(',')
    retval = 0 

    for range_of_ids in line: 
        ids = range_of_ids.split('-')

        if puzzlepart == 1: 
            len_lowest_to_mirror = len(ids[0])//2
            if len_lowest_to_mirror == 0: 
                to_mirror = 1
            else: 
                to_mirror = int(ids[0][:len_lowest_to_mirror]) 
            mirror = getMirror(to_mirror)
            while mirror <= int(ids[1]): 
                if mirror >= int(ids[0]) and mirror <= int(ids[1]): 
                    retval += mirror
                to_mirror += 1 
                mirror = getMirror(to_mirror)   
        
        if puzzlepart == 2: 
            for i in range(int(ids[0]), int(ids[1])+1): 
                if hasRepeats(i): 
                    retval += i


    if puzzlepart == 1: 
        return retval # 12850231731 
    else: 
        return retval # 24774350364 
