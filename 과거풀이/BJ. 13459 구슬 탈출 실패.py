# BJ. 13459 구슬 탈출
# 1, 2, 3, 4 상하좌우. DFS or BFS(위치정보, times) 쓰면 될듯
# 제약조건 10번.

# 4 6
######
##BR##
#O...#
######

# 아래 오른쪽 위 왼쪽 하면 된다
# time이 옮겨갈때마다 그때의 새로운 체크맵을 사용해야함.


def DFS(red_w, blue_w, time, r_time_map, b_time_map):
    new_r_map = r_time_map[:]
    new_b_map = b_time_map[:]

    print(*board, sep='\n')
    print()

    if time == 10:
        print(0)
        return False

    for i in range(4):
        moved_red_w, r_state = Move(red_w, i, new_r_map)
        moved_blue_w, b_state = Move(blue_w, i, new_b_map)
        if moved_red_w != red_w:
            if r_state and not b_state:
                print(1)
                return False
            elif r_state and b_state:
                print(0)
                return False
            if not DFS(moved_red_w, moved_blue_w, time+1, r_time_map, b_time_map):
                return False
            else:
                board, clone_board = clone_board, board
        Check_back(red_w, moved_red_w, i, new_r_map)
        Check_back(blue_w, moved_blue_w, i, new_b_map)
    return True

# 움직이면서 체크하고 체크 취소도 해야함.
def Move(where, direction, check):
    x, y = where
    color = board[x][y]
    clone_board[x][y] = '.'
    flag = False
    check[x][y] = 0
    while n-1 > x > 0 and m-1 > y > 0 and board[x][y] == '.' and not check[x][y]:
        check[x][y] = 1
        x += dx[direction]
        y += dy[direction]
        flag = True
        if board[x][y] == 'O':
            if color == 'B':
                x -= dx[direction]
                y -= dy[direction]
                clone_board[x][y] = color
                return [x, y], True
            return [0, 0], True

    if flag:
        x -= dx[direction]
        y -= dy[direction]
    clone_board[x][y] = color
    return [x, y], False


def Check_back(start, end, direction, check):

    # if direction & 1:  # 홀수면 -1 짝수면 +1 // 상하좌우 0123
    #     direction -= 1
    # else:
    #     direction += 1
    sx, sy = start
    ex, ey = end
    color = board[ex][ey]
    board[ex][ey] = '.'
    board[sx][sy] = color

    while sx != ex or sy != ey:
        check[sx][sy] = 0
        sx += dx[direction]
        sy += dy[direction]
    check[ex][ey] = 0
    return


n, m = map(int, input().split())
# n = row, m = col

board = []
clone_board = board[:]
r_check = [ [0]*m for _ in range(n) ]
b_check = [ [0]*m for _ in range(n) ]
blue_p = []
red_p = []
goal_p = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    temp = list(input())
    for j in range(m):
        if temp[j] == 'B':
            blue_p.append(i)
            blue_p.append(j)
        elif temp[j] == 'R':
            red_p.append(i)
            red_p.append(j)
        elif temp[j] == 'O':
            goal_p.append(i)
            goal_p.append(j)
    board.append(temp)

if DFS(red_p, blue_p, 0, r_check, b_check):
    print(0)
