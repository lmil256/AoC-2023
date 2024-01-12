coords = [(0, 0)]
perimeter = 0
with open('input.txt') as infile:
    x = y = 0
    for line in infile:
        hexstring = line[line.find('#')+1:-1]
        heading = hexstring[5]
        count = int(hexstring[:5], base=16)
        match heading:
            case '0':
                x += count
            case '1':
                y -= count
            case '2':
                x -= count
            case '3':
                y += count
        coords.append((x, y))
        perimeter += count

s1 = s2 = 0
for i in range(len(coords)-1):
    s1 += coords[i][0]*coords[i+1][1]
    s2 += coords[i][1]*coords[i+1][0]

print(abs(s1-s2)//2 + perimeter//2 + 1)
