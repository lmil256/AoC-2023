import re

MAX = {
    'red': 12,
    'green' : 13,
    'blue': 14
    }

expr = re.compile('[0-9]+|red|green|blue')

with open('input.txt') as infile:
    total = 0
    gamenum = 1
    for line in infile:
        ispossible = True
        a = expr.findall(line, line.find(':'))
        # Iterate over (num, color) pairs
        for i in zip(a[0::2], a[1::2]):
            if MAX[i[1]] < int(i[0]):
                ispossible = False
                break
        if ispossible:
            total += gamenum
        gamenum += 1
    print(total)
