coords = [(0, 0)]
perimeter = 0
with open('input.txt') as infile:
    x = y = 0
    for line in infile:
        splitline = line.split(' ')
        heading, count = splitline[0], int(splitline[1])
        match heading:
            case 'U':
                y += count
            case 'D':
                y -= count
            case 'L':
                x -= count
            case 'R':
                x += count
        coords.append((x, y))
        perimeter += count

s1 = s2 = 0
for i in range(len(coords)-1):
    s1 += coords[i][0]*coords[i+1][1]
    s2 += coords[i][1]*coords[i+1][0]

print(abs(s1-s2)//2 + perimeter//2 + 1)
