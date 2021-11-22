# BJ.10711 모래성

from collections import deque

n, m = map(int, input().split())

sand = [ list(input()) for _ in range(n) ]
check = [ [0]*m for _ in range(n) ]

dx = [1, -1, 1, -1, 1, -1, 0, 0]
dy = [0, 0, 1, -1, -1, 1, 1, -1]
waves = 0

que = deque()

for i in range(1, n-1):
    for j in range(1, m-1):
        if sand[i][j] == '9':
            continue
        if sand[i][j] != '.':
            cnt = 0
            for k in range(8):
                row = i + dx[k]
                col = j + dy[k]
                if n > row > -1 and m > col > -1 and sand[row][col] == '.':
                    cnt += 1
            if cnt >= int(sand[i][j]):
                check[i][j] = 1
            else:
                que.append([i, j, 1])

while que:
    waves += 1
    x, y, visit = que.popleft()
    cnt = 0
    for k in range(8):
        row = x + dx[k]
        col = y + dy[k]
        if n > row > -1 and m > col > -1:
            if sand[row][col] == '.' or check[row][col]:
                cnt += 1
    if cnt >= int(sand[x][y]):
        check[x][y] = visit + 1
    else:
        que.append([x, y, visit + 1])


print(waves)

