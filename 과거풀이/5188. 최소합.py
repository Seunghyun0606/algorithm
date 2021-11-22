# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
# 아래랑 오른쪽으로만 간다.


def dfs(x1, y1, sub_sum):
    if x1 == n-1 and y1 == n-1 :
        global result
        result = min(result, sub_sum)
        return

    elif sub_sum > result:
        return
    else:
        for i in range(2):
            row = x1 + dx[i]
            col = y1 + dy[i]
            if n > row > -1 and n > col > -1:
                dfs(row, col, sub_sum + board[row][col])


T = int(input())

for tc in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = 2**12
    dx = [0, 1]
    dy = [1, 0]
    dfs(0, 0, board[0][0])

    print('#{}'.format(tc+1), result)

