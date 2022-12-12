f = open("inputs/day10", "r")

OPERATIONS, LIGHT, DARK = [], "##", ".."

for line in f.readlines():
    OPERATIONS.append(0)
    if "addx" in line:
        OPERATIONS.append(int(line.split(" ")[1]))

print("Part1:", sum([(1 + sum([OPERATIONS[cycle] for cycle in range(n-1)]))*n for n in [20, 60, 100, 140, 180, 220]]))

register, CRT = 1, ""
for cycle, operation in enumerate(OPERATIONS):
    if cycle % 40 == 0: CRT += "\n"
    CRT += LIGHT if abs((cycle % 40)-register) < 2 else DARK
    register += operation

print("Part2:", "".join(CRT))
