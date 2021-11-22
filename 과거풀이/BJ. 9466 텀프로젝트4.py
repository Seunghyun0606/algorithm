# BJ. 9466 텀프로젝트, 성공

import sys
sys.setrecursionlimit(10000000)


def team(start):  # 맨처음에 0, 빈리스트 넣고 시작.
    global count
    visited[start] = 1
    if start == pointing[start]:  # Self Circle인경우
        count += 1
        return 0, 0
    if visited[pointing[start]]:
        return 2, pointing[start]  # 그룹되어진 경우 사람 수
    cnt, trace_confirm = team(pointing[start])
    if trace_confirm == start:
        count += cnt
        return 0, 0
    else:
        return cnt+1, trace_confirm


T = int(input())
for _ in range(T):

    n = int(input())
    pointing = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    count = 0
    for i in range(1, n+1):
        if visited[i]:
            continue
        team(i)

    print(n-count)


# 2
# 7
# 3 1 3 7 3 4 6
# 8
# 1 2 3 4 5 6 7 8

# 1
# 4
# 2 3 4 2
