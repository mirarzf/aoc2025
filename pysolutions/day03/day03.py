def getHighestDigit(line): 
    for highest_digit in range(9,0,-1): 
        for i in range(len(line)): 
            if int(line[i]) == highest_digit: 
                return i, highest_digit

def getMaximumVoltage(line, n_batteries): 
    voltage_digits = []
    left_idx = 0 
    n_line = len(line)
    for i in range(n_batteries): 
        line_to_check = line[left_idx:n_line-n_batteries+1+i]
        idx, digit = getHighestDigit(line_to_check)
        voltage_digits.append(digit) 
        left_idx += idx+1
    return sum([voltage_digits[i]*10**(n_batteries-1-i) for i in range(n_batteries)])

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    retval = 0

    if puzzlepart == 1: 
        n_batteries = 2 
    else: 
        n_batteries = 12 
    for line in lines: 
        retval += getMaximumVoltage(line[:-1], n_batteries)

    return retval 
# Part 1: 17432
# Part 2: 173065202451341
