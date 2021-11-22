# BJ. 1799 비숍(DFS)


def check_on(x1, y1):
    board_check[x1][y1] += 1
    for i in range(4):
        row = x1 + dx[i]
        col = y1 + dy[i]
        while n > row > -1 and n > col > -1:
            board_check[row][col] += 1
            row += dx[i]
            col += dy[i]


def check_off(x1, y1):
    board_check[x1][y1] -= 1
    for i in range(4):
        row = x1 + dx[i]
        col = y1 + dy[i]
        while n > row > -1 and n > col > -1:
            board_check[row][col] -= 1
            row += dx[i]
            col += dy[i]


def bishop_black(depth):
    global count_max_b, cnt

    for i in range(depth, mb):
        x, y = where_black[i]
        if mb-depth+cnt < count_max_b:  # 앞으로 놓을 비숍의 수가 적으면 더 하지말고 넘김
            return
        if black_check[i]:
            continue
        if board_check[x][y]:
            continue

        black_check[i] = 1
        cnt += 1
        check_on(x, y)
        bishop_black(i+1)
        cnt -= 1
        black_check[i] = 0
        check_off(x, y)
        bishop_black(i+1)
    else:
        count_max_b = max(count_max_b, cnt)


def bishop_white(depth):
    global count_max_w, cnt

    for i in range(depth, mw):
        x, y = where_white[i]
        if mw - depth + cnt < count_max_w:  # 앞으로 놓을 비숍의 수가 적으면 더 하지말고 넘김
            return
        if white_check[i]:
            continue
        if board_check[x][y]:
            continue

        white_check[i] = 1
        cnt += 1
        check_on(x, y)
        bishop_white(i + 1)
        cnt -= 1
        white_check[i] = 0
        check_off(x, y)
        bishop_white(i + 1)
    else:
        count_max_w = max(count_max_w, cnt)



n = int(input())

board = []

board_check = [[0 for _ in range(n)] for _ in range(n)]

count_max_b = 0
count_max_w = 0
cnt = 0

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

bishop_black(0)
bishop_white(0)
print(count_max_b + count_max_w)
