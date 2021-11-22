# BJ.14502 연구소

n, m = map(int, input().split())

lab = [ list(map(int, input().split())) for _ in range(n)]

check = [[ 0 for _ in range(m)] for _ in range(n)]

def dfs(row, col):

    if row == n and col == m:
        return

    for i in range(row, n):
        for j in range(col, m):
            if lab[i][j]:
                continue
            if check[i][j]:
                continue
            check[i][j] = 1
            dfs(i+1, j+1)
            check[i][j] = 0






