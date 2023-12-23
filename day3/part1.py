import re

schematic = []
with open('input.txt') as infile:
    for line in infile:
        schematic.append(line.rstrip('\n'))

total = 0
for linenum in range(len(schematic)):
    for nummatch in re.finditer('[0-9]+', schematic[linenum]):
        left = max(nummatch.start() - 1, 0)
        right = min(nummatch.end() + 1, len(schematic[0]) - 1)
        s = ''
        if linenum > 0:
            s += schematic[linenum-1][left:right]
        if linenum < len(schematic) - 1:
            s += schematic[linenum+1][left:right]
        s += schematic[linenum][left:right]
        if re.search('[^0-9\.]', s) is not None:
            total += int(nummatch.group(0))
print(total)
