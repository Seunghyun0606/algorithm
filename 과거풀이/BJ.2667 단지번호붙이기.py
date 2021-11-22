# BJ.2667 단지번호붙이기
def search(vx, vy):
    global count
    visit[vx][vy] = 1
    danji[vx][vy] = 0
    for i in range(4):
        x = vx + dx[i]
        y = vy + dy[i]
        if n > x > -1 and n > y > -1:
            if danji[x][y] == 0:
                continue
            elif visit[x][y]:
                continue
            count += 1
            search(x, y)

import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000000)


n = int(input())
danji = [ list(map(int, input())) for _ in range(n) ]
visit = [ [ 0 for _ in range(n)] for _ in range(n) ]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

my_count = []
for x1 in range(n):
    for y1 in range(n):
        count = 1
        if danji[x1][y1] == 1:
            search(x1, y1)
            my_count += [count]

print(len(my_count))
for k in sorted(my_count):
    print(k)

