# 같은 알파벳은 지나가지 못한다.
# dict를 사용해서 풀면 될듯 / DFS

# DFS 시간초과

from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [ input() for _ in range(n) ]

direc = [ (0, 1), (-1, 0), (0, -1), (1, 0), ]

alpha_dict = defaultdict(int)

result = 0
alpha_dict[board[0][0]] += 1
def dfs(r, c, cnt):
    global result    

    for dir_r, dir_c in direc:
        nr, nc = r + dir_r, c + dir_c

        if n > nr > -1 and m > nc > -1:
            if not alpha_dict[board[nr][nc]]:
                alpha_dict[board[nr][nc]] += 1
                result = max(dfs(nr, nc, cnt + 1), result)
                alpha_dict[board[nr][nc]] -= 1

    return cnt
dfs(0, 0, 1)
print(result)


