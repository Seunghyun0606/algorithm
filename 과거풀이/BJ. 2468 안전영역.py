# BJ. 2468 안전영역

import sys
sys.setrecursionlimit(10000000)

def rain(row, col):
    visit[row][col] = 0
    for i in range(4):
        row1 = row + dx[i]
        col1 = col + dy[i]
        if n > row1 > -1 and n > col1 > -1:
            if visit[row1][col1]:
                rain(row1, col1)


n = int(input())
safe = [ list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
flag = True
max_count = 0

while flag:
    visit = [ [1 for _ in range(n)] for _ in range(n)]
    if safe == visit:
        print(1)
        break
    for x in range(n):
        for y in range(n):
            if safe[x][y] > 0:
                safe[x][y] -= 1
            if safe[x][y] == 0:
                visit[x][y] = 0
    count = 0
    for x in range(n):
        for y in range(n):
            if visit[x][y]:
                rain(x, y)
                count += 1
    if count:
        if count > max_count:
            max_count = count
    else:
        flag = False
        print(max_count)



