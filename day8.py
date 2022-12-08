f = open("inputs/day8", "r")

DATA =[list(map(int, line.strip())) for line in f.readlines()]

w = len(DATA)
h = len(DATA[0])

VISIBLE = [[0 for x in range(w)] for y in range(h)]
SCENE_SCORE = []

for i in range(w):
    for j in range(h):
        score = 1
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            ii, jj = i+dx, j+dy
            tmp_score = 1
            while 0 <= ii < w and 0 <= jj < h and DATA[ii][jj] < DATA[i][j]:
                ii, jj = ii+dx, jj+dy
                tmp_score += 1
            if not( 0 <= ii < w and 0 <= jj < h):
                VISIBLE[i][j] = 1
                tmp_score -= 1
            score *= tmp_score
        SCENE_SCORE.append(score)

print(sum(map(sum, VISIBLE)))
print(max(SCENE_SCORE))