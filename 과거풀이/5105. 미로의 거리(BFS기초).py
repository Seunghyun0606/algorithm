# 5105. 미로의거리 BFS기초

import queue as Q


T = int(input())

for tc in range(T):
    n = int(input())
    maze = [ list(map(int, input())) for _ in range(n) ]
    que = Q.Queue()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    flag = False
    for x in range(n):
        if flag:
            break
        for y in range(n):
            if maze[x][y] == 2:
                maze[x][y] = -1
                que.put([x, y])
                flag = True
                break
    count = 0
    while que:
        if not flag:
            break
        if que.empty():
            break
        x, y = que.get()
        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
            if n > row > -1 and n > col > -1:
                if maze[row][col] == 0:
                    que.put([row, col])
                    maze[row][col] = maze[x][y] - 1
                elif maze[row][col] == 3:
                    count = -maze[x][y] - 1
                    flag = False
                    break

    print('#{}'.format(tc+1), count)


