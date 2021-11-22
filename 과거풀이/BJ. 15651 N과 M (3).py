# BJ. 15651 N과 M (3)


def dfs(start, n, li):
    stack[start] = 1

    if len(li) == m1:
        print(*li)
    else:
        for i in range(1, n):
            if stack[i]:
                continue
            dfs(start, n, li + [i])


n1, m1 = map(int, input().split())

stack = [0] * (n1+1)

bin1 = []
dfs(0, n1+1, bin1)
