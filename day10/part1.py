NORTH = 0
WEST = 1
EAST = 2
SOUTH = 3
def flip(n): return 3 - n

offset_y = (-1, 0, 0, 1)
offset_x = (0, -1, 1, 0)
tilekey = {
    '|': (NORTH, SOUTH),
    '-': (EAST, WEST),
    'L': (NORTH, EAST),
    'J': (NORTH, WEST),
    '7': (SOUTH, WEST),
    'F': (SOUTH, EAST)
    }

with open('testinput.txt') as infile:
    grid = infile.read().splitlines()

# Find starting position
for i in range(len(grid)):
    if (t := grid[i].find('S')) != -1:
        start_y, start_x = i, t
        break

# Find starting direction
for direction in range(4):
    dy, dx = offset_y[direction], offset_x[direction]
    neighbor = grid[start_y+dy][start_x+dx]
    if neighbor != '.' and flip(direction) in tilekey[neighbor]:
        heading = direction
        break

pos_y = start_y
pos_x = start_x
steps = 0
while True:
    tile = grid[pos_y][pos_x]
    # If we hit a corner, change direction
    if tile in 'LJ7F':
        dirs = tilekey[tile]
        heading = dirs[0] if flip(heading) == dirs[1] else dirs[1]
    pos_y += offset_y[heading]
    pos_x += offset_x[heading]
    steps += 1
    if pos_y == start_y and pos_x == start_x: break

print(steps // 2)
