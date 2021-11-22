# 2805. 농작물 수확하기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    n = int(input())

    farms = [list(map(int, input())) for _ in range(n)]

    result = 0

    for x in range(n):
        if x <= n//2 :
            for i in range(n//2 - x, n//2 + x + 1):
                result += farms[x][i]
        else:
            for m in range(1, n//2 + 1):
                for j in range(m, n-m):
                    result += farms[x+m-1][j]
            break

    print('#{}'.format(tc+1), result)



