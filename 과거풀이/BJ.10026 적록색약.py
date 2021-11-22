def dfs(vx, vy, cr):
    visit[vx][vy] = 1

    for i in range(4):
        x = vx + dx[i]
        y = vy + dy[i]

        if n > x > -1 and n > y > -1:
            if visit[x][y]:
                continue
            if pan[x][y] != cr:
                continue
            dfs(x, y, cr)

import sys
sys.stdin = open('input.txt', 'r')


n = int(input())
pan = [ list(input()) for _ in range(n) ]
visit = [ [0 for _ in range(n)] for _ in range(n) ]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
for x1 in range(n):
    for y1 in range(n):
        for co in 'RGB':
            if pan[x1][y1] == co and not visit[x1][y1]:
                dfs(x1, y1, co)
                count += 1

for x1 in range(n):
    for y1 in range(n):
        if pan[x1][y1] == 'G':
            pan[x1][y1] = 'R'

visit = [ [0 for _ in range(n)] for _ in range(n) ]

count2 = 0
for x1 in range(n):
    for y1 in range(n):
        for co in 'RB':
            if pan[x1][y1] == co and not visit[x1][y1]:
                dfs(x1, y1, co)
                count2 += 1

print(count, count2)

