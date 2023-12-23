import re

schematic = []
with open('input.txt') as infile:
    for line in infile:
        schematic.append(line.rstrip('\n'))

total = 0

# Find numbers in the line that overlap the horizontal range
def find_overlap(line, lbound, rbound):
    result = []
    for nummatch in re.finditer('[0-9]+', line):
        if nummatch.start() <= rbound and nummatch.end() - 1 >= lbound:
            result.append(nummatch.group(0))
    return result

for linenum in range(len(schematic)):
    for gearmatch in re.finditer('\*', schematic[linenum]):
        adjacent_nums = []
        lbound = gearmatch.start() - 1
        rbound = gearmatch.end()
        if linenum > 0:
            adjacent_nums += find_overlap(schematic[linenum-1], lbound, rbound)
        if linenum < len(schematic) - 1:
            adjacent_nums += find_overlap(schematic[linenum+1], lbound, rbound)
        adjacent_nums += find_overlap(schematic[linenum], lbound, lbound)
        adjacent_nums += find_overlap(schematic[linenum], rbound, rbound)
        if len(adjacent_nums) == 2:
            total += int(adjacent_nums[0]) * int(adjacent_nums[1])

print(total)
