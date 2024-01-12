import minheap

NORTH = 0
WEST = 1
EAST = 2
SOUTH = 3
OFFSET_Y = (-1, 0, 0, 1)
OFFSET_X = (0, -1, 1, 0)
def flip(n): return 3-n

def main():
    with open('input.txt') as infile:
        grid = [[int(c) for c in line] for line in infile.read().splitlines()]

    graph = {}
    start = (0, 0, -1, 0)
    graph[start] = [((0, 1, EAST, 1), grid[0][1]), ((1, 0, SOUTH, 1), grid[1][0])]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for heading in range(4):
                for consecutive in range(1, 11):
                    if node_valid(grid, y, x, heading, consecutive):
                        l = graph[(y, x, heading, consecutive)] = []
                        for next_heading in range(4):
                            if next_heading == flip(heading): continue
                            if next_heading != heading and consecutive < 4: continue
                            dy, dx = OFFSET_Y[next_heading], OFFSET_X[next_heading]
                            node = (y+dy, x+dx, next_heading, consecutive+1 if next_heading == heading else 1)
                            if node_valid(grid, *node):
                                l.append((node, grid[y+dy][x+dx]))

    dist = {}
    heap = minheap.MinHeap(key=lambda x: dist[x])
    for node in graph:
        dist[node] = 10*len(grid)*len(grid[0])
        heap.insert(node)
    dist[start] = 0
    while len(heap) > 0:
        cur = heap.extract_min()
        for neighbor, weight in graph[cur]:
            if dist[neighbor] > dist[cur]+weight:
                dist[neighbor] = dist[cur]+weight
                heap.priority_decreased(neighbor)

    end_nodes = []
    for node in graph:
        if node[0] == len(grid)-1 and node[1] == len(grid[0])-1:
            end_nodes.append(node)
    print(dist[min(end_nodes, key=lambda x: dist[x])])

def node_valid(grid, y, x, heading, consecutive):
    border_distances = (y, x, len(grid[0])-1-x, len(grid)-1-y)
    dist_ahead = border_distances[heading]
    dist_behind = border_distances[flip(heading)]
    return dist_behind >= consecutive\
            and dist_ahead >= max(0, 4-consecutive)\
            and consecutive <= 10
main()
