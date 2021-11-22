# BJ. 9466 텀프로젝트, 메모리초과.

import sys
sys.setrecursionlimit(10000000)

def team(start, li1):  # 맨처음에 0, 빈리스트 넣고 시작.
    global count
    visited[start] = 1
    if pointing[start] in li1:
        count += len(li1) - li1.index(pointing[start])  # 그룹되어진 사람 수
        return
    if visited[pointing[start]]:
        return
    team(pointing[start], li1 + [pointing[start]])


T = int(input())
for _ in range(T):

    n = int(input())
    pointing = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    count = 0
    li = []
    for i in range(1, n+1):
        if visited[i]:
            continue
        team(i, li + [i])

    print(n-count)


# 2
# 7
# 3 1 3 7 3 4 6
# 8
# 1 2 3 4 5 6 7 8

# 1
# 4
# 2 3 4 1
