# BJ. 15654 N과 M(5)

def dfs(start, n1, li):
    stack[start] = 1

    if len(li) == m:
        print(*li)

    else:
        for i in range(1, n1):
            if stack[i]:
                continue
            dfs(i, n1, li + [li1[i]])
            stack[i] = 0


n, m = map(int, input().split())
li1 = [0] + sorted(list(map(int, input().split())))
ept_li = []
stack = [0] * (n+1)

dfs(0, n+1, ept_li)
