with open('input.txt') as infile:
    grid = [list(line) for line in infile.read().splitlines()]

result = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'O':
            dest_y = y
            for i in range(y-1, -1, -1):
                if grid[i][x] == '.':
                    dest_y = i
                else:
                    break
            if dest_y != y:
                grid[y][x] = '.'
                grid[dest_y][x] = 'O'
            result += len(grid)-dest_y

print(result)
