# BJ. 9466 텀프로젝트, 시간초과.

import sys
sys.setrecursionlimit(10000000)


def team(start):  # 맨처음에 0, 빈리스트 넣고 시작.
    visited[start] = 1
    if pointing[start] in li:
        return len(li) - li.index(pointing[start])  # 그룹되어진 사람 수
    if visited[pointing[start]]:
        return 0
    li.append(pointing[start])
    return team(pointing[start])


T = int(input())
for _ in range(T):

    n = int(input())
    pointing = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    count = 0
    for i in range(1, n+1):
        if visited[i]:
            continue
        li = [i]
        count += team(i)

    print(n-count)


# 2
# 7
# 3 1 3 7 3 4 6
# 8
# 1 2 3 4 5 6 7 8

# 1
# 4
# 2 3 4 4
