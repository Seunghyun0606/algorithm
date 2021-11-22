# BJ.1726 로봇
# 1, 2, 3, 4 동서남북

from collections import deque


def check_direction(a, b):
    if b == 1:
        if a == 2:
            return 2
        return 1
    elif b == 2:
        if a == 1:
            return 2
        return 1
    elif b == 3:
        if a == 4:
            return 2
        return 1
    else:
        if a == 3:
            return 2
        return 1


def robot():
    dx = [0, 0, 0, 1, -1]  # 동서남북
    dy = [0, 1, -1, 0, 0]

    que = deque()
    que.append(start[0:2])
    field[start[0]][start[1]] = 1

    while que:
        x, y, d = que.popleft()


        # if x == end[0] and y == end[1]:
        #     if d != end[2]:
        #         print(field[x][y] + check_direction(d, end[2]) - 1)
        #     else:
        #         print(field[x][y] - 1)
        #     return

        for i in range(1, 5):
            row = x + dx[i]
            col = y + dy[i]
            tc = 0
            while n > row > -1 and m > col > -1 and field[row][col] != -1 and tc < 3:
                temp_cnt = 0
                if i != d:
                    temp_cnt = check_direction(d, i)
                que.append([row, col, i])
                field[row][col] = min(field[x][y] + temp_cnt + 1, field[row][col])
                row += dx[i]
                col += dy[i]
                tc += 1


n, m = map(int, input().split())

field = []

for i in range(n):
    a = []
    for j in map(int, input().split()):
        if j:
            a.append(-j)
        else:
            a.append(200)
    field.append(a)

start = list(map(int, input().split()))  # 출발, 방향
end = list(map(int, input().split()))  # 도착, 방향

if start[0] > 0:
    start[0] = start[0]-1
if start[1] > 0:
    start[1] = start[1]-1
if end[0] > 0:
    end[0] = end[0]-1
if end[1] > 0:
    end[1] = end[1]-1


robot()
