with open('input.txt') as infile:
    grid = [list(line) for line in infile.read().splitlines()]

weights = []
hashes = []
while True:
    # North
    for y in range(1, len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                dest_y = y
                # Scan up
                for i in range(y-1, -1, -1):
                    if grid[i][x] == '.':
                        dest_y = i
                    else:
                        break
                if dest_y != y:
                    grid[y][x] = '.'
                    grid[dest_y][x] = 'O'

    # West
    for y in range(len(grid)):
        for x in range(1, len(grid[0])):
            if grid[y][x] == 'O':
                dest_x = x
                # Scan left
                for i in range(x-1, -1, -1):
                    if grid[y][i] == '.':
                        dest_x = i
                    else:
                        break
                if dest_x != x:
                    grid[y][x] = '.'
                    grid[y][dest_x] = 'O'

    # South
    for y in range(len(grid)-2, -1, -1):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                dest_y = y
                # Scan down
                for i in range(y+1, len(grid)):
                    if grid[i][x] == '.':
                        dest_y = i
                    else:
                        break
                if dest_y != y:
                    grid[y][x] = '.'
                    grid[dest_y][x] = 'O'

    # East
    weight = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])-1, -1, -1):
            if grid[y][x] == 'O':
                dest_x = x
                # Scan right
                for i in range(x+1, len(grid[0])):
                    if grid[y][i] == '.':
                        dest_x = i
                    else:
                        break
                if dest_x != x:
                    grid[y][x] = '.'
                    grid[y][dest_x] = 'O'
                weight += len(grid)-y

    cur_hash = hash(''.join([''.join(line) for line in grid]))
    try:
        index = hashes.index(cur_hash)
        break
    except ValueError:
        weights.append(weight)
        hashes.append(cur_hash)

print(weights[index + (999999999-index)%(len(weights)-index)])
