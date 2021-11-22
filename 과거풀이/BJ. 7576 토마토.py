# BJ. 7576 토마토 // 가로세로 // BFS

from collections import deque


def cabinet():
    que = deque()

    for k in where:
        que.append([k, 0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        idx, time = que.popleft()

        for i in range(4):
            row = idx[0] + dx[i]
            col = idx[1] + dy[i]
            if m > row > -1 and n > col > -1:
                if tomatoes[row][col]:
                    continue
                tomatoes[row][col] = 1
                que.append([[row, col], time + 1])

    for i in range(m):
        for j in range(n):
            if tomatoes[i][j] == 0:
                print(-1)
                return

    print(time)
    return


n, m = map(int, input().split())

tomatoes = []
where = []
cnt = 0
for i in range(m):
    temp = []
    for j, val in enumerate(map(int, input().split())):
        if val == 1:
            where.append([i, j])
            cnt += 1
        temp.append(val)
    tomatoes.append(temp)


