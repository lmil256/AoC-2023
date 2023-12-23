with open('input.txt') as infile:
    lines = infile.read().splitlines()
    instructions = lines[0].translate(str.maketrans('LR', '01'))
    data = {}
    for line in lines[2:]:
        data[line[0:3]] = (line[7:10], line[12:15])

curr = 'AAA'
steps = 0
n = len(instructions)
while curr != 'ZZZ':
    curr = data[curr][int(instructions[steps % n])]
    steps += 1

print(steps)
