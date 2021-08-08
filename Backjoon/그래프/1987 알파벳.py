# 같은 알파벳은 지나가지 못한다.
# dict를 사용해서 풀면 될듯 / DFS / BFS
# dict를 사용할 경우 Worst는 O(n)이다.
# https://www.acmicpc.net/board/view/56580

# from collections import deque

# n, m = map(int, input().split())

# board = [ list(map(lambda x : ord(x) - 65, input())) for _ in range(n) ]

# direc = [ (0, 1), (-1, 0), (0, -1), (1, 0) ]

# alpha_list = [0]*26

# result = 0
# alpha_list[board[0][0]] = 1

# que = deque()
# que.append([0, 0, 1])

# while que:
#     r, c, cnt = que.popleft()

#     for dr, dc in direc:
#         nr, nc = r + dr, c + dc
#         if n > nr > -1 and m > nc > -1 and not alpha_list[board[nr][nc]]:
#             alpha_list[board[nr][nc]] = 1
#             que.append([nr, nc, cnt + 1])
#             result = max(result, cnt + 1)

# print(result)






# DFS dict 사용시 시간초과 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [ list(map(lambda x : ord(x) - 65, input())) for _ in range(n) ]
direc = [ (0, 1), (-1, 0), (0, -1), (1, 0) ]

alpha_list = [0]*26

result = 0
alpha_list[board[0][0]] = 1

def dfs(r, c, cnt):
    global result
    # max 체크를 하는게 for문 안에 있으면 그 만큼 n번만큼 max체크를 더 하는 셈이므로, 시간이 더 오래걸린다,
    # 따라서 밖에 쓰는게 맞다.
    result = max(cnt, result)

    for dir_r, dir_c in direc:
        nr, nc = r + dir_r, c + dir_c

        if n > nr > -1 and m > nc > -1:
            if not alpha_list[board[nr][nc]]:
                alpha_list[board[nr][nc]] = 1
                dfs(nr, nc, cnt + 1)
                alpha_list[board[nr][nc]] = 0
dfs(0, 0, 1)
print(result)


# def solve(x, y, l):
#     global ans
#     ans = max(ans, l)
#     for d in range(4):
#         i, j = x + dx[d], y + dy[d]
#         if 0<=i<r and 0<=j<c and alpha[table[i][j]] == 0:
#             alpha[table[i][j]] = 1
#             solve(i, j, l+1)
#             alpha[table[i][j]] = 0
# r, c = map(int, input().split())
# table = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(r)]
# dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
# alpha = [0] * 26
# ans = 0
# alpha[table[0][0]] = 1
# solve(0, 0, 1)
# print(ans)
