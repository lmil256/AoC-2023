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

with open('input.txt') as infile:
    grid = infile.read().splitlines()

# Make a clean grid twice the height and width
big_grid = []
big_height = len(grid) * 2
big_width = len(grid[0]) * 2
for i in range(big_height):
    big_grid.append(['.'] * big_width)

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
loop_count = 0
while True:
    tile = grid[pos_y][pos_x]
    # If we hit a corner, change direction
    if tile in 'LJ7F':
        dirs = tilekey[tile]
        heading = dirs[0] if flip(heading) == dirs[1] else dirs[1]
    dy, dx = offset_y[heading], offset_x[heading]
    # Draw the loop on the big grid
    big_grid[pos_y*2 + 1][pos_x*2 + 1] = '#'
    # Draw the extra tile
    big_grid[pos_y*2 + 1 + dy][pos_x*2 + 1 + dx] = '#'
    pos_y += dy
    pos_x += dx
    loop_count += 1
    if pos_y == start_y and pos_x == start_x:
        break

# Flood fill from the top left corner to find all outside tiles
queue = [0, 0]
outside = 0
while len(queue) > 0:
    curr_y, curr_x = queue.pop(0), queue.pop(0)
    # Count tiles which map to the original grid
    if curr_y % 2 == curr_x % 2 == 1:
        outside += 1
    for dy, dx in zip(offset_y, offset_x):
        next_y, next_x = curr_y + dy, curr_x + dx
        if -1 < next_y < big_height and -1 < next_x < big_width \
                and big_grid[next_y][next_x] == '.':
            big_grid[next_y][next_x] = ' '
            queue.append(next_y)
            queue.append(next_x)

print(len(grid)*len(grid[0]) - loop_count - outside)
