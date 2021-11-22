# BJ. 1325 효율적인 해킹
# n은 nodes 수 m은 간선수
# 시간제한이 빡빡한 문제. pypy3로 해야함.

from collections import deque
# import sys
# input = sys.stdin.readline  없는게 더빠름. pypy라서그런가?


def computer(k):
    cnt = 1
    check = [0] * (n+1)
    que = deque()
    que.append(k)
    check[k] = 1

    while que:
        num = que.popleft()

        for i in nodes[num]:
            if not check[i]:
                que.append(i)
                check[i] = 1
                cnt += 1

    return cnt



n, m = map(int, input().split())

nodes = [ [] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    nodes[b].append(a)

max_hack = 0
result = []

for i in range(1, n+1):
    if nodes[i]:
        temp = computer(i)
        if temp > max_hack:
            max_hack = temp
            result = [i]
        elif temp == max_hack:
            result.append(i)

print(*result)
