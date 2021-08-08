# 항상 내리막길로 가야하고, 최단 경로가 아니라, 경로의 개수이므로 DFS로 풀면된다.

import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

down_road = [ list(map(int, input().split())) for _ in range(n)]

direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]

check = [ [0]*m for _ in range(n) ]

result = 0
def dfs(r, c):
    global result

    if (r, c) == (n-1, m-1):
        result += 1
    else:
        for i in range(4):
            nr = r + direc[i][0]
            nc = c + direc[i][1]
            if n > nr > -1 and m > nc > -1:
                if down_road[r][c] > down_road[nr][nc]:
                    check[nr][nc] = 1
                    dfs(nr, nc)
                    check[nr][nc] = 0
dfs(0, 0)
print(result)
    