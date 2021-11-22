# 1974. 스도쿠 검증
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):

    sdoku = [list(map(int, input().split())) for _ in range(9)]
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    flag = False
    result = 1
    for y in range(9):
        if flag:
            break
        sum_x = 0
        sum_y = 0
        for x in range(9):
            sum_x += sdoku[x][y]
            sum_y += sdoku[y][x]
        if sum_x != 45 or sum_y != 45:
            result = 0
            flag = True
            break

    if result != 0:
        for y in range(0, 9, 3):
            if flag:
                break
            for x in range(0, 9, 3):
                if flag:
                    break
                sum_x = 0
                for i in range(3):
                    for j in range(3):
                        sum_x += sdoku[x+i][y+j]
                if sum_x != 45:
                    result = 0
                    flag = True
                    break

    print('#{}'.format(tc+1), result)








