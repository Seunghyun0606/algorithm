# BFS써서 별자리 탐색 완료하면 +1

from collections import deque


def find_star(x1, y1):

    stars[x1][y1] = 0
    que = deque()
    que.append([x1, y1])

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    while que:
        x, y = que.popleft()

        for k in range(8):
            row = x + dx[k]
            col = y + dy[k]

            if 10 > row > -1 and 10 > col > -1 and stars[row][col]:
                stars[row][col] = 0
                que.append([row, col])

T = int(input())

for tc in range(T):

    stars = [ list(map(int, input().split())) for _ in range(10) ]
    count = 0

    for i in range(10):
        for j in range(10):
            if stars[i][j]:
                find_star(i, j)
                count += 1

    print('#{}'.format(tc+1), count)