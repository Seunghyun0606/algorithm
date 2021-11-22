# BJ. 3190 뱀
# L은 왼쪽 D는 오른쪽

import sys
sys.setrecursionlimit(10**7)

def snake(length, when, direct, time):  # [[0, 0]], 0, 3, 0
    global flag, finished
    if flag:
        x = length[0][0]
        y = length[0][1]

        board[x][y] = -1

        if when < d and int(direct_info[when][0]) == time:
            if direct_info[when][1] == 'L':
                direct -= 1
                if direct == -1:
                    direct = 3
            elif direct_info[when][1] == 'D':
                direct += 1
                if direct == 4:
                    direct = 0
            when += 1

        row = x + dx[direct]
        col = y + dy[direct]

        if n > row > -1 and n > col > -1:
            if board[row][col] == 1:
                snake([[row, col]] + length, when, direct, time + 1)

            elif board[row][col] == -1:
                finished = time + 1
                flag = False
                return

            else:

                if len(length) > 1:
                    i, j = length.pop()
                    board[i][j] = 0
                    snake([[row, col]] + length, when, direct, time + 1)
                else:
                    board[x][y] = 0
                    snake([[row, col]], when, direct, time + 1)
        else:
            finished = time + 1
            flag = False
            return


n = int(input())  # 보드 크기
k = int(input())  # 사과 갯수
board = [ [0 for _ in range(n)] for _ in range(n)]

for _ in range(k):  # put_apple
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

d = int(input())  # 방향 전환 횟수
direct_info = [ list(input().split()) for _ in range(d)]

dx = [1, 0, -1, 0]  # 하 좌 상 우
dy = [0, -1, 0, 1]

flag = True
finished = 0
length_list = [[0, 0]]

snake(length_list, 0, 3, 0)

print(finished)

