# BJ. 7569 토마토
# [행, 높이, 열]
# 왜 이게 더 빠른거지? if를 손수 다쓰니깐 2초정도 빨라짐. 이건 2초
# for 돌린경우 4초.

from collections import deque
from sys import stdin
input = stdin.readline


def cabinets():

    que = deque()

    for i in where:
        que.append([i, 0])

    while que:
        idx, time = que.popleft()
        h1 = idx[0]
        n1 = idx[1]
        m1 = idx[2]
        if m1 > 0 and tomatoes[h1][n1][m1 - 1] == 0:
            tomatoes[h1][n1][m1-1] = 1
            que.append([[h1, n1, m1-1], time+1])

        if m1 < m - 1 and tomatoes[h1][n1][m1 + 1] == 0:
            tomatoes[h1][n1][m1 + 1] = 1
            que.append([[h1, n1, m1 + 1], time + 1])

        if n1 > 0 and tomatoes[h1][n1 - 1][m1] == 0:
            tomatoes[h1][n1 - 1][m1] = 1
            que.append([[h1, n1 - 1, m1], time + 1])

        if n1 < n - 1 and tomatoes[h1][n1 + 1][m1] == 0:
            tomatoes[h1][n1+1][m1] = 1
            que.append([[h1, n1+1, m1], time + 1])

        if h1 > 0 and tomatoes[h1 - 1][n1][m1] == 0:
            tomatoes[h1 - 1][n1][m1] = 1
            que.append([[h1 - 1, n1, m1], time + 1])

        if h1 < h - 1 and tomatoes[h1 + 1][n1][m1] == 0:
            tomatoes[h1+1][n1][m1] = 1
            que.append([[h1+1, n1, m1], time + 1])

    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomatoes[k][i][j] == 0:
                    print(-1)
                    return
    print(time)
    return


m, n, h = map(int, input().split())

tomatoes = []
where = []
cnt = 0

for k in range(h):
    temp_h = []
    for i in range(n):
        temp_i = []
        for j, val in enumerate(map(int, input().split())):
            if val == 1:
                where.append([k, i, j])
                cnt += 1
            temp_i.append(val)
        temp_h.append(temp_i)
    tomatoes.append(temp_h)

if cnt == n*m*h:
    print(0)
else:
    cabinets()






