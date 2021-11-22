# 1974 스도쿠 검증

def my_sdoku(sdoku):
    for y in range(9):
        sum_x = 0
        sum_y = 0
        for x in range(9):
            sum_x += sdoku[x][y]
            sum_y += sdoku[y][x]
        if sum_x != 45 or sum_y != 45:
            return 0

    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            sum_x = 0
            sum_y = 0
            for y1 in range(3):
                for x1 in range(3):
                    sum_x += sdoku[x + x1][y + y1]
                    sum_y += sdoku[y + y1][x + x1]
            if sum_x != 45 or sum_y != 45:
                return 0
    return 1


T = int(input())

for tc in range(T):
    sdoku_map = [list(map(int, input().split())) for _ in range(9)]

    print('#{}'.format(tc + 1), my_sdoku(sdoku_map))
