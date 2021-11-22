# BJ. 15656 N과 M(7)

def dfs(start, n1, li1):
    stack[start] = 1
    if len(li1) == m:
        print(*li1)

    else:
        for i in range(1, n1):
            if stack[i]:
                continue
            dfs(start, n1, li1 + [li[i]])


n, m = map(int, input().split())
li = [0] + sorted(list(map(int, input().split())))
ept_li = []
stack = [0] * (n+1)

dfs(0, n+1, ept_li)

