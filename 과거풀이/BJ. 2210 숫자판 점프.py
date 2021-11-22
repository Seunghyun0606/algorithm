# BJ. 2210 숫자판 점프


def all_inone(x, y, num):

    if len(num) == 6:
        nums.add(num)

    else:
        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
            if 5 > row > -1 and 5 > col > -1:
                all_inone(row, col, num + board[row][col])


board = [ list(input().split()) for _ in range(5) ]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

nums = set()

for i in range(5):
    for j in range(5):
        all_inone(i, j, board[i][j])

print(len(nums))

