# BJ. 2206 벽부수고 이동하기4
# 3차원 배열 // 메모리랑 시간을 더 많이먹네? 2차원 배열 두개보다.


from collections import deque

def breaking():

    que = deque()
    que.append([0, 0, 0])  # 0이면 false 1이면 True

    distance = [ [ [0, 0] for _ in range(m)] for _ in range(n) ]
    distance[0][0][0] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        x, y, status = que.popleft()

        if x == n-1 and y == m-1:
            return distance[x][y][status]

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]

            if n > row > -1 and m > col > -1:
                if distance[row][col][status]:
                    continue
                if walls[row][col] and status == 0:
                    distance[row][col][1] = distance[x][y][status] + 1
                    que.append([row, col, 1])
                if walls[row][col] == 0:
                    distance[row][col][status] = distance[x][y][status] + 1
                    que.append([row, col, status])

    return -1


n, m = map(int, input().split())

walls = [ list(map(int, input())) for _ in range(n)]

print(breaking())