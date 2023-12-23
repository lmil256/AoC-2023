import re

zeroexpr = re.compile('(?=[1-9]|one|two|three|four|five|six|seven|eight|nine)')
digitexpr = re.compile('[1-9]|one|two|three|four|five|six|seven|eight|nine')
digitmap = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
    }

with open('input.txt') as infile:
    total = 0
    for line in infile:
        digitstring = ''
        # Zero-width match to find overlapping digits
        l = list(zeroexpr.finditer(line))
        # Get first and last matches
        for i in (0, -1):
            matchstr = digitexpr.search(line, l[i].start()).group(0)
            digitstring += matchstr if matchstr.isdigit() else digitmap[matchstr]
        total += int(digitstring)
        print(digitstring)
    print(total)
