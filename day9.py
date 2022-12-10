f = open("inputs/day9", "r")

COORDINATES = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
MOVES = [(COORDINATES[x.split(" ")[0]], int(x.split(" ")[1].strip())) for x in f.readlines()]


def sign(x):
    return -1 if x < 0 else 0 if x == 0 else 1


def visit(knots, moves):
    k = [(0, 0)]*knots
    visited = set([(0, 0)])

    for (x,  y),m in moves:
        for _ in range(m):
            h = k[0]
            k[0] = (h[0]+x, h[1]+y)

            for i in range(len(k)-1):
                h, t = k[i], k[i+1]
                dx, dy = h[0]-t[0], h[1]-t[1]
                if abs(dx) >= 2 or abs(dy) >= 2:
                    k[i+1] = (t[0] + sign(dx), t[1]+sign(dy))
            visited.add(k[-1])
    
    return len(visited)


print(visit(2, MOVES))
print(visit(10, MOVES))
