# BJ. 1926 그림
import sys
sys.setrecursionlimit(100000000)

def painting(row, col):
    global size
    paints[row][col] = 0
    size += 1
    for k in range(4):
        row1 = row + dx[k]
        col1 = col + dy[k]
        if n > row1 > -1 and m > col1 > -1:
            if paints[row1][col1]:
                painting(row1, col1)


n, m = map(int, input().split())  # 행, 열
paints = [ list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 갯수, 그림 크기
count = 0
size_max = 0

for i in range(n):
    for j in range(m):
        size = 0
        if paints[i][j]:
            painting(i, j)
            count += 1
            if size > size_max:
                size_max = size

print(count, size_max, sep='\n')
