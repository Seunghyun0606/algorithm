import copy
R, C, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if board[i][0] == -1:
        clear_machine = i
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for t in range(T):
    tmp_board = copy.deepcopy(board)
    for x in range(R):
        for y in range(C):
            cnt = 0
            if board[x][y] >= 5:
                for d in range(4):
                    tx = x + dx[d]
                    ty = y + dy[d]
                    if 0 <= tx < R and 0 <= ty < C:
                        if board[tx][ty] == -1: continue
                        cnt += 1
            if cnt:
                for d in range(4):
                    tx = x + dx[d]
                    ty = y + dy[d]
                    if 0 <= tx < R and 0 <= ty < C:
                        if board[tx][ty] == -1: continue
                        tmp_board[tx][ty] += board[x][y] // 5
                tmp_board[x][y] -= cnt * (board[x][y] // 5)
    board = copy.deepcopy(tmp_board)
    for i in range(1, clear_machine-1):
        board[i][0] = tmp_board[i-1][0]
    for i in range(0, clear_machine - 1):
        board[i][C-1] = tmp_board[i+1][C-1]
    for j in range(2, C):
        board[clear_machine-1][j] = tmp_board[clear_machine-1][j-1]
        board[clear_machine][j] = tmp_board[clear_machine][j-1]
    for j in range(C-1):
        board[0][j] = tmp_board[0][j+1]
        board[R-1][j] = tmp_board[R-1][j+1]
    for i in range(clear_machine+1, R-1):
        board[i][0] = tmp_board[i+1][0]
    for i in range(clear_machine+1, R):
        board[i][C-1] = tmp_board[i-1][C-1]
    board[clear_machine][1] = 0
    board[clear_machine-1][1] = 0
print(sum(map(sum, board)) + 2)

# deep copy가 1250, 그냥이 724, 심지어 deep copy가 메모리를 더먹는다.

import copy
R, C, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if board[i][0] == -1:
        clear_machine = i
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for t in range(T):
    tmp_board = [[0 for _ in range(C)] for __ in range(R)]
    for x in range(R):
        for y in range(C):
            cnt = 0
            if board[x][y] >= 5:
                for d in range(4):
                    tx = x + dx[d]
                    ty = y + dy[d]
                    if 0 <= tx < R and 0 <= ty < C:
                        if board[tx][ty] == -1: continue
                        cnt += 1
            if cnt:
                for d in range(4):
                    tx = x + dx[d]
                    ty = y + dy[d]
                    if 0 <= tx < R and 0 <= ty < C:
                        if board[tx][ty] == -1: continue
                        tmp_board[tx][ty] += board[x][y] // 5
                tmp_board[x][y] -= cnt * (board[x][y] // 5)
    for i in range(R):
        for j in range(C):
            board[i][j] += tmp_board[i][j]
            tmp_board[i][j] = board[i][j]
    for i in range(1, clear_machine-1):
        board[i][0] = tmp_board[i-1][0]
    for i in range(0, clear_machine - 1):
        board[i][C-1] = tmp_board[i+1][C-1]
    for j in range(2, C):
        board[clear_machine-1][j] = tmp_board[clear_machine-1][j-1]
        board[clear_machine][j] = tmp_board[clear_machine][j-1]
    for j in range(C-1):
        board[0][j] = tmp_board[0][j+1]
        board[R-1][j] = tmp_board[R-1][j+1]
    for i in range(clear_machine+1, R-1):
        board[i][0] = tmp_board[i+1][0]
    for i in range(clear_machine+1, R):
        board[i][C-1] = tmp_board[i-1][C-1]
    board[clear_machine][1] = 0
    board[clear_machine-1][1] = 0
print(sum(map(sum, board)) + 2)