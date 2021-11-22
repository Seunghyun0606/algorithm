# BJ.1726 로봇
# 1, 2, 3, 4 동서남북
# 먼저 전진명령내린다음에 방향회전해야한다.
# 왜냐면 맨마지막에 end지점에서 안움직이고 회전하기때문.
# 따라서 회전부터하면안된다.
# 3차원으로 만들어서 각 회전당 움직이는 횟수를 생각하는게 중요. 벽부수기랑 비슷한거같기도하고.

from collections import deque


def check_direction(a, b):
    if b == 0:
        if a == 1:
            return 2
        return 1
    elif b == 1:
        if a == 0:
            return 2
        return 1
    elif b == 2:
        if a == 3:
            return 2
        return 1
    else:
        if a == 2:
            return 2
        return 1


def robot():
    dx = [0, 0, 1, -1]  # 동서남북
    dy = [1, -1, 0, 0]

    que = deque()
    que.append([start_x-1, start_y-1, start_d-1])

    while que:

        x, y, d = que.popleft()

        if x == end_x - 1 and y == end_y - 1 and d == end_d - 1:
            print(visit[x][y][d])
            return

        row = x
        col = y
        for _ in range(3):  # 전진 3번 먼저함.
            row += dx[d]
            col += dy[d]
            if row > n-1 or row < 0 or col > m-1 or col < 0 or field[row][col] == 1:
                break
            if not visit[row][col][d]:  # 비어있으면
                que.append([row, col, d])
                visit[row][col][d] = visit[x][y][d] + 1

        for i in range(4):  # 방향전환
            if d == i:
                continue
            k = check_direction(d, i)

            if not visit[x][y][i]:  # 비어있으면
                que.append([x, y, i])
                visit[x][y][i] = visit[x][y][d] + k


n, m = map(int, input().split())

field = [ list(map(int, input().split())) for _ in range(n)]
visit = [ [[0]*4 for _ in range(m)] for _ in range(n) ]
start_x, start_y, start_d = list(map(int, input().split()))  # 출발, 방향
end_x, end_y, end_d = list(map(int, input().split()))  # 도착, 방향

robot()
