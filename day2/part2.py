import re
from math import prod

expr = re.compile('[0-9]+|red|green|blue')

with open('input.txt') as infile:
    total = 0
    for line in infile:
        # Stores the largest largest value seen for each color
        colormax = { 'red': 0, 'green' : 0, 'blue': 0 }
        a = expr.findall(line, line.find(':'))
        # Iterate over (num, color) pairs
        for i in zip(a[0::2], a[1::2]):
            if colormax[i[1]] < int(i[0]):
                colormax[i[1]] = int(i[0])
        total += prod(colormax.values())
    print(total)
