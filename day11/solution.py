import bisect
import sys

with open('input.txt') as infile:
    grid = infile.read().splitlines()

try: expansion = int(sys.argv[1])
except IndexError: expansion = 2
height = len(grid)
width = len(grid[0])
empty_rows = list(range(height))
empty_cols = list(range(width))
galaxies = []

# Find galaxies and delist non-empty rows/columns
for row in range(height):
    for col in range(width):
        if grid[row][col] == '#':
            try: empty_rows.remove(row)
            except ValueError: pass
            try: empty_cols.remove(col)
            except ValueError: pass
            galaxies.append([row, col])

# Adjust galaxy coordinates by the number of empty rows above and empty columns
# to the left
for galaxy in galaxies:
    galaxy[0] += bisect.bisect(empty_rows, galaxy[0])*(expansion - 1)
    galaxy[1] += bisect.bisect(empty_cols, galaxy[1])*(expansion - 1)

# Add up the distances between each pair of galaxies
result = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        start_y = min(galaxies[i][0], galaxies[j][0])
        start_x = min(galaxies[i][1], galaxies[j][1])
        dest_y = max(galaxies[i][0], galaxies[j][0])
        dest_x = max(galaxies[i][1], galaxies[j][1])
        result += dest_y - start_y + dest_x - start_x

print(result)
