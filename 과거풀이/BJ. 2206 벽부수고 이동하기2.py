# BJ. 2206 벽부수고 이동하기2
# check 배열 하나 필요하다.
# distance 배열 하나.

from collections import deque
import sys
sys.stdin = open('test.txt', 'r')


def breaking2(x, y, check, distance, dx, dy):
    que2 = deque()
    que2.append([x, y])

    distance2 = []

    for i1 in range(n):
        a = []
        for j1 in range(m):
            a.append(distance[i1][j1])
        distance2.append(a)

    while que2:
        x1, y1 = que2.popleft()
        for i in range(4):
            row = x1 + dx[i]
            col = y1 + dy[i]
            if n > row > -1 and m > col > -1:
                if walls[row][col]:
                    continue
                if check[row][col] == 1:
                    continue
                if distance2[row][col] < distance2[x1][y1] + 1:
                    continue
                

                check[row][col] = 1
                distance2[row][col] = distance2[x1][y1] + 1

                que2.append([row, col])


def breaking():

    que = deque()
    que.append([0, 0, -1])  # -1이면 false 1이면 True
    check = [ [ 0 for _ in range(m)] for _ in range(n)]
    distance = [ [ n*m for _ in range(m)] for _ in range(n) ]
    distance[0][0] = 0
    check[0][0] = -1

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        x, y, status = que.popleft()

        if status == -1:
            for i in range(4):
                row = x + dx[i]
                col = y + dy[i]
                if n > row > -1 and m > col > -1:
                    if check[row][col] == -1:
                        continue
                    if distance[row][col] < distance[x][y] + 1:
                        continue
                    if walls[row][col]:
                        check[row][col] = 1
                        distance[row][col] = distance[x][y] + 1

                        que.append([row, col, 1])
                        continue

                    check[row][col] = -1
                    distance[row][col] = distance[x][y] + 1

                    que.append([row, col, -1])

        else:
            breaking2(x, y, check, distance, dx, dy)

    return distance[n-1][m-1]


n, m = map(int, input().split())

walls = [ list(map(int, input())) for _ in range(n)]

result = breaking()


if result == n*m:
    print(-1)
else:
    print(result+1)


# 8 4
# 0000
# 0110
# 1110
# 0000
# 0111
# 0000
# 1110
# 0000

# 6 5
# 01100
# 11110
# 10110
# 00110
# 01100
# 00000

# 5 3
# 000
# 010
# 010
# 010
# 000