# BJ. 15649 N과 M(1)


def dfs(start, n1, bin1):
    stack[start] = 1
    if len(bin1) == m:
        print(*bin1)

    else:
        for i in range(1, n1):
            if stack[i]:
                continue
            dfs(i, n1, bin1 + [i])
            stack[i] = 0


n, m = map(int, input().split())
stack = [0] * (n+1)  # 0번은 안쓸거다.
bin2 = []

dfs(0, n+1, bin2)

