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

verts = [(start_y, start_x)]
pos_y = start_y
pos_x = start_x
loop_count = 0
while True:
    tile = grid[pos_y][pos_x]
    # If we hit a corner, change direction
    if tile in 'LJ7F':
        dirs = tilekey[tile]
        heading = dirs[0] if flip(heading) == dirs[1] else dirs[1]
        verts.append((pos_y, pos_x))
    dy, dx = offset_y[heading], offset_x[heading]
    pos_y += dy
    pos_x += dx
    loop_count += 1
    if pos_y == start_y and pos_x == start_x:
        break

verts.append((start_y, start_x))
s1 = s2 = 0
for i in range(len(verts)-1):
    s1 += verts[i][0]*verts[i+1][1]
    s2 += verts[i][1]*verts[i+1][0]

print(abs(s1-s2)//2 - loop_count//2 + 1)
