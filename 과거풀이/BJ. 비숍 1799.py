# BJ. 비숍 1799 (실패)
# 가지치기.
# 하나의 행에서 다 뽑을라 했는데 그건 안됨. 반례가 있음. 하나의 행을 다 안쓰는 경우가 생길수 도있음.


from sys import stdin
input = stdin.readline


def bishop():
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]

    new = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0

    for i in where:
        for j in i:
            x, y = j
            if new[x][y]:
                continue
            new[x][y] = 1
            cnt += 1

            for k in range(4):
                row = x+dx[k]
                col = y+dy[k]

                while n > row > -1 and n > col > -1:
                    new[row][col] = 1
                    row += dx[k]
                    col += dy[k]

    return cnt


n = int(input())

board = []
where = []

for i in range(n):
    temp = []
    where_temp = []
    for j, val in enumerate(map(int, input().split())):
        if val:
            where_temp.append([i, j])
        temp.append(val)
    where.append(where_temp)
    board.append(temp)

count_max = 0

for tc in range(n):

    count_max = max(count_max, bishop())

    start = where.pop()  # 순서만 바꿈. 왜냐면 하나의 행에서는 어차피 다 뽑을수 있으니깐.
    where = [start] + where

print(count_max)



