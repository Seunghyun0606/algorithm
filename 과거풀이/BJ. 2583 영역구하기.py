# BJ. 2583 영역구하기
# x가 열 y가 행

import sys
sys.setrecursionlimit(10000000)

def square(x, y):
    global count
    paper[x][y] = 0
    count += 1
    for i in range(4):
        row1 = x + dx[i]
        col1 = y + dy[i]
        if n > row1 > -1 and m > col1 > -1:
            if paper[row1][col1]:
                square(row1, col1)



n, m, k = map(int, input().split())

paper = [ [1 for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    rect = list(map(int, input().split()))
    for row in range(rect[1], rect[3]):
        for col in range(rect[0], rect[2]):
            paper[row][col] = 0

result = []

for i in range(n):
    for j in range(m):
        if paper[i][j]:
            count = 0
            square(i, j)
            result.append(count)
print(len(result))
print(*sorted(result))