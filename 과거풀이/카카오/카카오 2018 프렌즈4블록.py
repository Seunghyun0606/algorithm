# 0,0 부터, n-1, m-1 까지  모두 조사, 4개블럭 확인.
# 몇 개 지워졌는지 확인해야함.
# 한번 다지우고나서 지울게 리셋하고 지울게 없어질때까지 없앰.


def solution(m, n, board):

    board = list(map(list, board))
    answer = 0
    # 하, 우, 우하 3가지만 검색
    dr = [1, 0, 1]
    dc = [0, 1, 1]

    # m 이 row, n이 col


    while True:
        # 4개인 프렌즈 확인
        locations = []
        for row in range(m-1):
            for col in range(n-1):
                who = board[row][col]
                temp = []
                if who:
                    temp.append((row, col))  # list는 unhashable해서 tuple로 만든 뒤, set 사용한다.
                    for i in range(3):
                        check_row = row + dr[i]
                        check_col = col + dc[i]
                        if who != board[check_row][check_col]:
                            break
                        temp.append((check_row, check_col))
                    else:
                        locations += temp
        
        if not locations:
            break

        set_locations = set(locations)
        answer += len(set_locations)

        # 프렌즈 없애기

        for r, c in set_locations:
            board[r][c] = 0
        
        # 좌표 내리기 스택에 넣고, 0은 없애고, 다시 넣자.
        stack = []
        for c in range(n):
            for r in range(m):
                if board[r][c]:
                    stack += [board[r][c]]
            else:
                for i in range(m-1, -1, -1):
                    if stack:
                        board[i][c] = stack.pop()
                    else:
                        board[i][c] = 0

    return answer