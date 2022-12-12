from collections import deque
f = open("inputs/day12", "r")

def char_to_num(input):
    if input == "S": return 0
    if input == "E": return 26
    return ord(input)-ord('a')+1


START = char_to_num("S")
STOP = char_to_num("E")

HEIGHTMAP = [list(map(char_to_num, list(line.strip()))) for line in f.readlines()]


def BFS(heightmap, sp):
    h, w = len(heightmap), len(heightmap[0])
    queue, visited = deque(), set()
    queue.append((sp[0], sp[1], 0))

    while queue:
        (x, y, c) = queue.popleft()
        if heightmap[x][y] == STOP: return c
        if (x, y) in visited: continue

        visited.add((x, y))
        for (x1, y1) in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            if 0 <= x1 < h and 0 <= y1 < w and (heightmap[x1][y1] - heightmap[x][y]) <= 1:
                queue.append((x1, y1, c+1))
    return -1


SP = [(ix, iy) for ix, row in enumerate(HEIGHTMAP) for iy, i in enumerate(row) if i == START][0]
EP = [(ix, iy) for ix, row in enumerate(HEIGHTMAP) for iy, i in enumerate(row) if i == STOP][0]

print(BFS(HEIGHTMAP, SP))

RESULTS = []
for i in [(ix, iy) for ix, row in enumerate(HEIGHTMAP) for iy, i in enumerate(row) if i == char_to_num('a')]:
    t = BFS(HEIGHTMAP, i)
    if t > 0:
        RESULTS.append(t)

print(sorted(RESULTS)[0])
