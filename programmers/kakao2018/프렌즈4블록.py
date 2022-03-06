# 2x2 블록 4개가붙을경우 사라지면서 점수 얻는다.
# 초기 배열 이후에 지워지는 블록의 갯수 구하기.
# 높이 m 폭n, board 주어짐
# 더 이상 지워지지 않을때까지 완전탐색.

board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
m = 4
n = 5

board = [ list(s) for s in board ]

dr = [1, 0, 1]
dc = [0, 1, 1]

answer = 0

# 제거하면서 여러 라운드 진행
while True:
    # 제거할 목록
    remove_list = set()
    # 세로
    for i in range(m-1):
        # 가로
        for j in range(n-1):
            block = board[i][j]
            # 값이 있으면
            if block:
                cnt = 1
                temp_list = [(i, j)]
                for k in range(3):
                    row = dr[k] + i
                    col = dc[k] + j

                    if block == board[row][col]:
                        cnt += 1
                        temp_list.append((row, col))
                if cnt == 4:
                    remove_list.update(temp_list)
    if not remove_list:
        print(answer)
        break

    # 제거 시작
    for remove in remove_list:
        i, j = remove
        board[i][j] = 0
        answer += 1

    # 하강 시작
    for j in range(n-1, -1, -1):
        for i in range(m-1, -1, -1):
            block = board[i][j]

            if not block:
                k = i - 1
                while k > -1:
                    
                    if board[k][j]:
                        board[i][j] = board[k][j]
                        board[k][j] = 0
                        break
                    k -= 1
    







            
