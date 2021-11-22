# BJ. 2589 보물섬

from collections import deque


def hunting():
    que = deque()
    que.append((i, j))
    check[i][j] = dist_count
    distance[i][j] = 0
    while que:
        x, y = que.popleft()
        for k in range(4):
            row = x + dx[k]
            col = y + dy[k]
            if n > row > -1 and m > col > -1:  # and gold[row][col] == 'L' and check[row][col] != dist_count
                if gold[row][col] == 'W':
                    continue
                if check[row][col] == dist_count:
                    continue
                check[row][col] = dist_count
                distance[row][col] = distance[x][y] + 1
                que.append((row, col))

    return distance[x][y]

n, m = map(int, input().split())
gold = [ list(input()) for _ in range(n) ]
check = [[0] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]

max_count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dist_count = 1

for i in range(n):
    for j in range(m):
        if gold[i][j] == 'L':
            temp = hunting()
            dist_count += 1
            if temp > max_count:
                max_count = temp

print(max_count)



