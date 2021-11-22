# BJ. 15650 N과 M(2)


def dfs(start, n1, li):
    stack[start] = 1

    if len(li) == m:
        print(*li)

    else:
        for i in range(1, n1):
            if stack[i]:
                continue
            dfs(i, n1, li + [i])
            stack[i] = 0


n, m = map(int, input().split())

stack = [0] * (n+1)
bin1 = []

dfs(0, n+1, bin1)

