# BJ. 15652 N과 M(4)


def dfs(start, li):

    if len(li) == m:
        print(*li)
    else:
        for i in range(start, n+1):
            dfs(i, li + [i])

n, m = map(int, input().split())

bin1 = []

dfs(1, bin1)

