import math

with open('input.txt') as infile:
    lines = infile.read().splitlines()
    instructions = lines[0].translate(str.maketrans('LR', '01'))
    data = {}
    start_nodes = []
    for line in lines[2:]:
        node = line[0:3]
        if node[-1] == 'A':
            start_nodes.append(node)
        data[node] = (line[7:10], line[12:15])

n = len(instructions)
times = []
# Find how many steps it takes for each starting node to reach the end
for start in start_nodes:
    steps = 0
    curr = start
    while curr[-1] != 'Z':
        curr = data[curr][int(instructions[steps % n])]
        steps += 1
    times.append(steps)

# Calculate the least common multiple of the times
print(math.lcm(*times))
