# BJ. 7569 토마토
# [행, 높이, 열]

from collections import deque
from sys import stdin
input = stdin.readline


def cabinets():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    que = deque()

    for i in where:
        que.append([i, 0])

    while que:
        idx, time = que.popleft()

        for i in range(6):
            height = idx[0] + dz[i]
            row = idx[1] + dx[i]
            col = idx[2] + dy[i]
            # if row >= n or row < 0 or col >= m or col < 0 or height >= h or height < 0 or tomatoes[height][row][col]:
            #     continue

            if n > row > -1 and m > col > -1 and h > height > -1:
                if tomatoes[height][row][col]:
                    continue
                tomatoes[height][row][col] = 1
                que.append([[height, row, col], time + 1])

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






