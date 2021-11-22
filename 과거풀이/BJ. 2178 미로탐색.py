# BJ. 2178 미로탐색  Dfs로는 못푸는 문제. BFS로 풀어야함. 답은 맞으나 시간초과뜸

import queue as Q


def my_maze():
    que = Q.Queue()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    que.put([0, 0])
    check[0][0] = 1
    while que:
        if check[n-1][m-1]:
            return maze[n-1][m-1]
        x, y = que.get()

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
            if n > row > -1 and m > col > -1:
                if maze[row][col] == 0:
                    continue
                if check[row][col]:
                    continue
                check[row][col] = 1
                maze[row][col] = maze[x][y] + 1
                que.put([row, col])


n, m = map(int, input().split())

maze = [ list(map(int, input())) for _ in range(n) ]
check = [ [ 0 for _ in range(m)] for _ in range(n) ]

print(my_maze())