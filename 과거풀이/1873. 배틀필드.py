# 1873. 상호의 배틀필드
# * 벽돌벽, . 평지, # 강철벽, - 물, < 전차가 보는 방향(전차 위치)


def my_up(x, y):
    game_map[x][y] = '^'
    if game_map[x-1][y] == '.':
        game_map[x-1][y] = '^'
        game_map[x][y] = '.'
        p_x = x-1


def my_down(x, y):
    game_map[x][y] = 'v'
    if game_map[x+1][y] == '.':
        game_map[x+1][y] = 'v'
        game_map[x][y] = '.'
        p_x = x+1


def my_left(x, y):
    game_map[x][y] = '<'
    if game_map[x][y-1] == '.':
        game_map[x][y-1] = '<'
        game_map[x][y] = '.'
        p_y = y-1


def my_right(x, y):
    game_map[x][y] = '>'
    if game_map[x][y+1] == '.':
        game_map[x][y+1] = '>'
        game_map[x][y] = '.'
        p_y = y+1


def my_shoot(direc, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x1 = x
    y1 = y
    if direc == '<':
        i = 0
        x1 += dx[i]
        while h > x1 > -1 and w > y1 > -1:
            if game_map[x1][y1] == '*':
                game_map[x1][y1] = '.'
            elif game_map[x1][y1] == '#':
                break
            x1 += dx[i]

    elif direc == '>':
        i = 1
        x1 += dx[i]
        while h > x1 > -1 and w > y1 > -1:
            if game_map[x1][y1] == '*':
                game_map[x1][y1] = '.'
            elif game_map[x1][y1] == '#':
                break
            x1 += dx[i]
    elif direc == '^':
        i = 2
        y1 += dy[i]
        while h > x1 > -1 and w > y1 > -1:
            if game_map[x1][y1] == '*':
                game_map[x1][y1] = '.'
            elif game_map[x1][y1] == '#':
                break
            y1 += dy[i]
    else:
        i = 3
        y1 += dy[i]
        while h > x1 > -1 and w > y1 > -1:
            if game_map[x1][y1] == '*':
                game_map[x1][y1] = '.'
            elif game_map[x1][y1] == '#':
                break
            y1 += dy[i]


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):

    h, w = map(int, input().split())

    game_map = [list(input()) for _ in range(h)]

    n = int(input())

    commends = input()

    p_x, p_y = 0, 0

    flag = False
    for x1 in range(h):
        if flag:
            break
        for y1 in range(w):
            a = game_map[x1][y1]
            if a == '<' or a == '>' or a == '^' or a == 'v':
                p_x, p_y = x1, y1
                flag = True
                break

    for com in commends:
        if com == 'U':
            my_up(p_x, p_y)
        elif com == 'L':
            my_left(p_x, p_y)
        elif com == 'R':
            my_right(p_x, p_y)
        elif com == 'D':
            my_down(p_x, p_y)
        else:
            my_shoot(game_map[p_x][p_y], p_x, p_y)

    print('#{}'.format(tc+1), end='')
    for m in game_map:
        print(*m)







