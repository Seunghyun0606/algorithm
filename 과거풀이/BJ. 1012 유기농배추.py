# BJ. 1012 유기농배추

import sys
sys.setrecursionlimit(10000000)

def warms(row, col):
    farms[row][col] = 0
    for i in range(4):
        row1 = row + dx[i]
        col1 = col + dy[i]
        if n > row1 > -1 and m > col1 > -1:
            if farms[row1][col1]:
                warms(row1, col1)


T = int(input())

for _ in range(T):

    m, n, k = map(int, input().split())  # 가로(열), 세로(행), 배추 개수
    farms = [ [0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        farms[b][a] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    count = 0
    for y in range(m):
        for x in range(n):
            if farms[x][y]:
                warms(x, y)
                count += 1

    print(count)


