import functools

@functools.cache
def count(diagram, groups):
    diagram = diagram.lstrip('.')
    if len(diagram) == 0:
        return 1 if len(groups) == 0 else 0
    if len(groups) == 0:
        return 1 if '#' not in diagram else 0
    if diagram[0] == '?':
        return count(diagram[1:], groups)+count('#'+diagram[1:], groups)
    # Try to place the current group
    if '.' not in diagram[:groups[0]]:
        if len(diagram) > groups[0] and diagram[groups[0]] != '#':
            return count(diagram[groups[0]+1:], groups[1:])
        elif len(diagram) == groups[0]:
            return count('', groups[1:])
    return 0

with open('input.txt') as infile:
    total = 0
    for line in infile:
        pair = line.rstrip('\n').split(' ')
        diagram = '?'.join([pair[0]]*5)
        groups = tuple([int(x) for x in pair[1].split(',')]*5)
        total += count(diagram, groups)

print(total)
