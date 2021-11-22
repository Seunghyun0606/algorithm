# BJ. 2573 빙산  BFS배우고 풀자.

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
            if iceberg[row][col]:
                melting(row, col)
            else:
                if mountain[x][y]:
                    mountain[x][y] -= 1

    visit[x][y] = 0
    if mountain[x][y]:
        ice_count += 1


def connect(x, y):
    global count
    visit[x][y] = 1
    count += 1
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if n > row > -1 and m > col > -1:
            if visit[row][col]:
                continue
            if mountain[row][col]:
                connect(row, col)
    visit[x][y] = 0


n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 만들어진 빙하 갯수와 dfs돌렸을때 연결된 빙하 전체 갯수가 다르면 return. 그리고 만들어진 빙하갯수가 0이면 바로 리턴

time = 0
flag2 = True
while flag2:
    mountain = [[iceberg[i][j] for j in range(m)] for i in range(n)]

    time += 1
    flag = True
    flag1 = True
    count = 0
    ice_count = 0

    for i in range(1, n-1):
        if not flag1:
            break
        for j in range(1, m-1):
            if mountain[i][j] and flag:
                melting(i, j)
                flag = False
                if ice_count == 0:
                    flag1 = False
                    flag2 = False
                    break
            if mountain[i][j]:
                connect(i, j)
                if ice_count != count:
                    flag1 = False
                    flag2 = False
                    break
                flag1 = False
                break
    if flag2:
        iceberg = [[mountain[i][j] for j in range(m)] for i in range(n)]


print(time)
