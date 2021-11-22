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
            if visit[row][col] == 1:
                continue
            if iceberg[row][col]:
                melting(row, col)
            else:
                if iceberg[x][y]:
                    iceberg[x][y] -= 1

    if iceberg[x][y]:
        ice_count += 1


def melting2(x, y):
    global ice_count
    visit[x][y] = -1

    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if n > row > -1 and m > col > -1:
            if visit[row][col] == -1:
                continue
            if iceberg[row][col]:
                melting2(row, col)
            else:
                if iceberg[x][y]:
                    iceberg[x][y] -= 1

    if iceberg[x][y]:
        ice_count += 1


def connect(x, y):
    global count
    visit[x][y] = 2
    count += 1
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if n > row > -1 and m > col > -1:
            if visit[row][col] == 2:
                continue
            if iceberg[row][col]:
                connect(row, col)


n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 만들어진 빙하 갯수와 dfs돌렸을때 연결된 빙하 전체 갯수가 다르면 return. 그리고 만들어진 빙하갯수가 0이면 바로 리턴

time = 0
flag = True

while flag:
    time += 1
    ice_count = 0
    count = 0
    flag2 = True
    flag3 = True
    flag4 = True
    flag5 = True

    for i in range(1, n-1):

        if not flag3:
            break

        for j in range(1, m-1):
            if flag2:
                if iceberg[i][j]:
                    if time % 2:
                        melting(i, j)
                    else:
                        melting2(i, j)
                    flag2 = False
            if flag4:
                if iceberg[i][j] and visit[i][j]:
                    connect(i, j)
                    flag4 = False
                    if count != ice_count:
                        flag = False
                        flag3 = False
                        break
                    else:
                        flag5 = False
            if iceberg[i][j] and visit[i][j] == 0:
                time = 0
                flag3 = False
                flag = False
                break
    else:
        if flag5:
            time = 0
            break


print(time)

