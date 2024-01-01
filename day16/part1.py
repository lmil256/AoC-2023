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

    history = {}
    queue = [0, 0, EAST]
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

    print(len(history))

main()
