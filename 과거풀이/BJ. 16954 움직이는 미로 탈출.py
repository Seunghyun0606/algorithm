# BJ. 16954 움직이는 미로 탈출
# 벽이 내려온다. 다내려오면 끝남.
# 대각선 이동가능.
# 왼쪽 밑에서 시작해서 오른쪽 위가 도착지점.
# 어차피 우측위에 도착만하면되니깐 BFS로 돌리자.
# 맵이작으니깐 BFS로 맵도 같이넘겨주면될듯. 얼마안걸림.

from collections import deque


def down(wall_list):
    # 새로 지정안해주면 새로운 함수로 넘어가도 같은 id를 지정해버림.
    new_wall_list = []

    for i in range(len(wall_list)):
        wall_list[i][0] += 1
        new_wall_list.append(wall_list[i])
    # for문 돌려서 맵에 직접 표시하나 좌표로 for돌려서 검사하나 똑같다.
    # 오히려 더 적게들지. 좌표만 비교하니깐 n x n 이아니라 n만하면됨.
    return new_wall_list

def BFS(walls):

    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [1, 0, -1, 1, -1, 0, 1, 0, -1]

    que = deque()
    que2 = deque()
    que2.append([7, 0])
    time = 0

    while True:
        while que2:
            flag = False
            check_x, check_y = que2.popleft()

            if check_x == 0 and check_y == 7:
                print(1)
                return

            for wall_x, wall_y in walls:
                if wall_x == check_x and wall_y == check_y:
                    flag = True
                    break
            if flag:
                continue

            que.append([check_x, check_y])

        while que:
            x, y = que.popleft()

            for i in range(9):
                row = x + dx[i]
                col = y + dy[i]

                if time < 8:
                    if 8 > row > -1 and 8 > col > -1:
                        flag = False
                        for wall_x, wall_y in walls:
                            if wall_x == row and wall_y == col:
                                flag = True
                                break
                        if flag:
                            continue
                        que2.append([row, col])
                        check[row][col] = 1
                else:
                    print(1)
                    return

        walls = down(walls)
        time += 1

        if not que and not que2:
            print(0)
            return

board = [ list(input()) for _ in range(8) ]
check = [ [ 0 for _ in range(8)] for _ in range(8) ]
check[7][0] = 1
# 출발점은 (7, 0)
# 도착점은 (0, 7)

where = []

for i in range(8):
    for j in range(8):
        if board[i][j] == '#':
            where.append([i, j])

BFS(where)

