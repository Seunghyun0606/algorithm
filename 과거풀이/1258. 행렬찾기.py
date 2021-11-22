# 1258. 행렬찾기

# 크기는 찾은 값 - 처음 값

import sys
sys.stdin = open('input.txt', 'r')


def search(x, y):
    x1 = x
    y1 = y

    while True:
        if x1 == n or chemies[x1][y] == 0:
            break
        x1 += 1

    while True:
        if y1 == n or chemies[x][y1] == 0:
            break
        y1 += 1

    for i in range(x, x1):
        for j in range(y, y1):
            chemies[i][j] = 0
    return x1-x, y1-y


T = int(input())

for tc in range(T):
    n = int(input())
    chemies = [ list(map(int, input().split())) for _ in range(n)]

    count = 0
    result = []
    mult = []
    for i in range(n):
        for j in range(n):
            if chemies[i][j]:
                row_c, col_c = search(i, j)
                count += 1
                result.append(row_c)
                result.append(col_c)
                mult.append(row_c*col_c)
    if count > 1:
        for i in range(count-1):
            for j in range(i+1, count):
                if mult[i] > mult[j]:
                    mult[i], mult[j] = mult[j], mult[i]
                    result[2*i], result[2*j] = result[2*j], result[2*i]
                    result[2*i+1], result[2*j+1] = result[2*j+1], result[2*i+1]

        for i in range(count-1):
            if mult[i] == mult[i+1]:
                if result[2*i] > result[2*(i+1)]:
                    result[2*i], result[2*(i+1)] = result[2*(i+1)], result[2*i]
                    result[2 * i + 1], result[2 * (i+1) + 1] = result[2 * (i+1) + 1], result[2 * i + 1]

    result = [count] + result

    print('#{}'.format(tc+1), *result)

