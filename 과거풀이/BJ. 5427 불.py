# BJ. 5427 불
# 불 붙였을때와 사람 이동시킬때 걸러내는 조건에 따라서 횟수가 몇번 더 도는 경우가 생길수 있는데 그것때매 시간초과 난다.

from collections import deque


def Fire():

    for _ in range(len(fire)):
        x1, y1 = fire.popleft()
        for i in range(4):
            row1 = x1 + dx[i]
            col1 = y1 + dy[i]
            if n > row1 > -1 and m > col1 > -1:
                if structure[row1][col1] == '.' or structure[row1][col1] == '@':  # 조건문을 조금 바꾸면 시간초과남. 주의해야함.
                    structure[row1][col1] = '*'
                    fire.append([row1, col1])


def fire_exit():

    que = deque()
    que.append(place[0])
    time_check = 0
    while que:
        x, y, time = que.popleft()

        if time == time_check:
            Fire()
            time_check += 1

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]

            if n > row > -1 and m > col > -1:
                if structure[row][col] == '.':
                    structure[row][col] = '@'
                    que.append([row, col, time+1])
            else:
                print(time+1)
                return

    else:
        print('IMPOSSIBLE')


T = int(input())

for tc in range(T):
    m, n = map(int, input().split())

    fire = deque()
    place = []
    structure = []

    for i in range(n):
        temp = list(input())
        for j, val in enumerate(temp):
            if val == '*':
                fire.append([i, j])
            elif val == '@':
                place.append([i, j, 0])
        structure.append(temp)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    fire_exit()
