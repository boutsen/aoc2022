f = open("inputs/day9", "r")

COORDINATES = { 'U': (0,1), 'D': (0,-1), 'L': (-1,0), 'R': (1,0) }
MOVES = [ (COORDINATES[x.split(" ")[0]],int(x.split(" ")[1].strip())) for x in f.readlines() ]

def sign(x):
    return -1 if x < 0 else 0 if x == 0 else 1

def visit(knots,moves):
    K = [(0,0)]*knots
    VISITED = set([(0,0)])

    for (x,y),m in moves:
        for _ in range(m):
            H = K[0]
            K[0] = (H[0]+x,H[1]+y)

            for i in range(len(K)-1):
                H, T = K[i], K[i+1]
                dx,dy = H[0]-T[0],H[1]-T[1]
                if  abs(dx) >=  2 or abs(dy) >= 2:
                    K[i+1] = (T[0] + sign(dx),T[1]+sign(dy))
            VISITED.add(K[-1])
    
    return len(VISITED)


print(visit(2,MOVES))
print(visit(10,MOVES))