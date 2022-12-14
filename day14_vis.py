import re
f = open("inputs/day14", "r")

ROCKS = set()

for line in f.readlines():
    path = [(int(r), int(l)) for (r, l) in re.findall(r"(\d+),(\d+)", line)]
    for i in range(len(path)-1):
        (c1, r1), (c2, r2) = path[i], path[i+1]
        for c in range(min(c1, c2), max(c1, c2)+1):
            for r in range(min(r1, r2), max(r1, r2)+1):
                ROCKS.add((c, r))


def get_resting_place(rocks, sand, floor):
    prev, (x, y) = (-1, -1), (500, 0)
    while prev != (x, y):
        prev = (x, y)
        for (dx, dy) in [(x, y+1), (x-1, y+1), (x+1, y+1)]:
            if (dx, dy) not in rocks and (dx, dy) not in sand and y < floor:
                (x, y) = (dx, dy)
                break
    return x, y


def run_sand(rocks, floor, target):
    sand = set()
    (x, y) = get_resting_place(rocks, sand, floor)
    while y != target:
        sand.add((x, y))
        (x, y) = get_resting_place(rocks, sand, floor)
    return sand


FLOOR = max(y for _, y in ROCKS)
ROWS = [x for x, _ in ROCKS]
COLS = [y for _, y in ROCKS]

SAND = run_sand(ROCKS, FLOOR, FLOOR)
for j in range(max(COLS)+1):
    line = ""
    for i in range(min(ROWS), max(ROWS)+1):
        if (i, j) in ROCKS:
            line += "#"
        elif (i, j) in SAND:
            line += "O"
        elif (i, j) == (500, 0):
            line += "+"
        else:
            line += "."
    print(line)