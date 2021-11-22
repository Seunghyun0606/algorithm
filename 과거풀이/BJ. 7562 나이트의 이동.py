# BJ. 7562 나이트의 이동 // BFS문제.

from collections import deque

def chess():
    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]

    que = deque()
    que.append([start[0], start[1], 0])

    while que:
        x, y, time = que.popleft()

        for i in range(8):
            row = x + dx[i]
            col = y + dy[i]

            if n > row > -1 and n > col > -1:
                if board[row][col]:
                    continue
                if row == end[0] and col == end[1]:
                    print(time + 1)
                    return
                board[row][col] = 1
                que.append([row, col, time+1])

T = int(input())
for _ in range(T):
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    if start == end:
        print(0)
    else:
        chess()
