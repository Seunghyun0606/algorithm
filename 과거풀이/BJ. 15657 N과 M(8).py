# BJ. 15657 N과 M(8)


def dfs(start, li1):
    if len(li1) == m:
        print(*li1)

    else:
        for i in range(start, n):
            dfs(i, li1 + [li[i]])


n, m = map(int, input().split())

li = sorted(list(map(int, input().split())))
ept_li = []

dfs(0, ept_li)
