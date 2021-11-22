# BJ. 2206 벽부수고 이동하기
# 최단거리 모두

from collections import deque


def dfs(row, col, check, dx, dy, x1, y1):
    global check_cnt
    check_cnt -= 1
    que1 = deque()
    distance[row][col] = distance[x1][y1] + 1
    check[row][col] = 1
    que1.append([row, col])
    while que1:
        x, y = que1.popleft()

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
            if row == n-1 and col == m-1:
                if distance[row][col] > distance[x][y] + 1:
                    distance[row][col] = distance[x][y] + 1
                return
            if n > row > -1 and m > col > -1:
                if check[row][col] == 1 or check[row][col] == check_cnt:
                    continue
                if maze[row][col]:
                    continue
                if 0 < distance[row][col] < distance[x][y] + 1:
                    continue

                distance[row][col] = distance[x][y] + 1
                check[row][col] = check_cnt
                que1.append([row, col])


def breaking():
    check = [ [0]*m for _ in range(n)]
    distance[n-1][m-1] = n*m

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()
    que.append([0, 0])
    check[0][0] = 1
    while que:
        x, y = que.popleft()

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
            if row == n-1 and col == m-1:
                if distance[row][col] > distance[x][y] + 1:
                    distance[row][col] = distance[x][y] + 1
                return
            if n > row > -1 and m > col > -1:
                if check[row][col] == 1:
                    continue
                if maze[row][col]:
                    dfs(row, col, check, dx, dy, x, y)
                    continue
                if 0 < distance[row][col] < distance[x][y] + 1:
                    continue

                distance[row][col] = distance[x][y] + 1
                check[row][col] = 1
                que.append([row, col])


n, m = map(int, input().split())

maze = [ list(map(int, input())) for _ in range(n) ]
distance = [[0] * m for _ in range(n)]
check_cnt = 0

breaking()
if distance[n-1][m-1] == n*m:
    if distance[n-1][m-1] == 1:
        print(1)
    else:
        print(-1)
else:
    print(distance[n-1][m-1]+1)
# print(distance)


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
# 00110
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
