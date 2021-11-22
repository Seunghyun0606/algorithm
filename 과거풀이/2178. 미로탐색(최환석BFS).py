from collections import deque


def bfs(x, y):
    Q = deque()
    visit[x][y] = 1
    D[x][y] = 1
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or ty < 0 or tx == N or ty == M or visit[tx][ty] or not maze[tx][ty]:
                continue

            visit[tx][ty] = 1
            D[tx][ty] = D[x][y] + 1

            Q.append((tx, ty))

    return D[N - 1][M - 1]


N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
D = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = bfs(0, 0)

print(result)