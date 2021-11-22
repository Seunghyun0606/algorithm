# BJ. 2573 빙산

import sys
sys.setrecursionlimit(10000000)


def melting(x, y):
    global ice_count
    visit[x][y] = 1
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if n > row > -1 and m > col > -1:
            if visit[row][col]:
                continue
            if mountain[row][col]:
                melting(row, col)
            else:
                if mountain[x][y]:
                    mountain[x][y] -= 1
    if mountain[x][y]:
        ice_count += 1



def connect(x, y, cnt):
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if n > row > -1 and m > col > -1:
            if mountain[row][col]:
                connect(row, col, cnt+1)



n, m = map(int, input().split())
mountain = [ list(map(int, input().split())) for _ in range(n) ]
visit = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

time = 0
flag2 = True
while flag2:
    flag = False
    time += 1
    ice_count = 0
    for i in range(1, n-1):
        if flag:
            break
        for j in range(1, m-1):
            if mountain[i][j]:
                melting(i, j)
                flag = True
                break

    count = 0
    for i in range(1, n-1):
        if not flag2:
            break
        for j in range(1, m-1):
            if mountain[i][j]:
                connect(i, j)
                count += 1
                if count > 1:
                    flag2 = False
                    break

    if count == 0:
        flag2 = False
        time = 0
print(time)


# 5 7
# 0 0 0 0 0 0 0
# 0 3 3 3 0 0 0
# 0 3 0 3 0 0 0
# 0 3 3 3 0 0 0
# 0 0 0 0 0 0 0
