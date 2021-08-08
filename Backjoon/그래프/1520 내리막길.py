# 항상 내리막길로 가야하고, 최단 경로가 아니라, 경로의 개수이므로 DFS로 풀면된다.
# 그냥 풀면 시간초과가 뜬다. 따라서 DP를 사용해야한다.

import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

down_road = [ list(map(int, input().split())) for _ in range(n)]

direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# DP 사용
check = [ [-1]*m for _ in range(n) ]


# check 배열에서 0이면 목적지까지 갈 수 없음. -1이면 한 번도 가본 적 없음. 1 이상의 값이면 한번 이상 가본적 있음.
def dfs(r, c):

    if (r, c) == (n-1, m-1):
        return 1
    if check[r][c] != -1:
        return check[r][c]
    check[r][c] = 0
    for i in range(4):
        nr = r + direc[i][0]
        nc = c + direc[i][1]
        if n > nr > -1 and m > nc > -1:
            if down_road[r][c] > down_road[nr][nc]:
                check[r][c] += dfs(nr, nc)
    return check[r][c]

print(dfs(0, 0))