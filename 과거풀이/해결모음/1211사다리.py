# 1211. [S/W 문제해결 기본] 2일차 - Ladder2

import sys
sys.stdin = open('ladder_input.txt', 'r')

T = 10
for t in range(T):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    count_min = 10000
    result = 0
    dy_list = [1, -1]  # 좌우 탐색

    for y in range(100):  # y는 열검색
        my_y = y
        count = 0
        for x in range(100):  # x는 행검색
            flag = False
            if ladder[x][my_y] == 0:  # 시작할때 값이 0이면 열 방향으로 이동.
                break
            else:
                for bridge in dy_list:  # 1, -1
                    dy = my_y + bridge  # 양쪽 옆의 값을 봐야하니 열방향으로 검사
                    if dy >= 100 or dy < 0:
                        continue
                    while ladder[x][dy] == 1:
                        my_y = dy  # 현재 나의 열 위치정보
                        if bridge == 1:
                            dy += 1
                        else:
                            dy -= 1
                        count += 1
                        flag = True
                        if dy == 100 or dy == -1:
                            break
                    if flag:  # 여기서 좌측으로는 가지 않는 것이 문제였는데 flag를 만들어서 해결햇다.
                        break
            count += 1
        if count != 0 and count < count_min:
            count_min = count
            result = y  # min값이 나올때의 y 값이 시작점(구하고자하는값)

    print('#{}'.format(tc), result)
