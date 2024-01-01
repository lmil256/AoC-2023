NORTH = 0
WEST = 1
EAST = 2
SOUTH = 3
OFFSET_Y = (-1, 0, 0, 1)
OFFSET_X = (0, -1, 1, 0)
MIRRORS = {
    '/': (EAST, SOUTH, NORTH, WEST),
    '\\': (WEST, NORTH, SOUTH, EAST)
    }

def main():
    with open('input.txt') as infile:
        grid = infile.read().splitlines()
    highest = 0
    for start_y in range(len(grid)):
        highest = max(highest, max(run(grid, start_y, 0, EAST),
                                    run(grid, start_y, len(grid[0])-1, WEST)))
    for start_x in range(len(grid[0])):
        highest = max(highest, max(run(grid, 0, start_x, SOUTH),
                                    run(grid, len(grid)-1, start_x, NORTH)))
    print(highest)

def run(grid, start_y, start_x, start_heading):
    history = {}
    queue = [start_y, start_x, start_heading]
    while len(queue) > 0:
        pos_y = queue.pop(0)
        pos_x = queue.pop(0)
        heading = queue.pop(0)
        while 0 <= pos_y < len(grid) and 0 <= pos_x < len(grid[0]):
            try:
                if heading in history[(pos_y, pos_x)]:
                    break
            except KeyError:
                history[(pos_y, pos_x)] = [heading]

            tile = grid[pos_y][pos_x]
            if tile in MIRRORS:
                heading = MIRRORS[tile][heading]
            elif tile == '|' and (heading == EAST or heading == WEST):
                queue.append(pos_y+OFFSET_Y[NORTH])
                queue.append(pos_x+OFFSET_X[NORTH])
                queue.append(NORTH)
                heading = SOUTH
            elif tile == '-' and (heading == NORTH or heading == SOUTH):
                queue.append(pos_y+OFFSET_Y[WEST])
                queue.append(pos_x+OFFSET_X[WEST])
                queue.append(WEST)
                heading = EAST
            pos_y += OFFSET_Y[heading]
            pos_x += OFFSET_X[heading]

    return len(history)

main()
