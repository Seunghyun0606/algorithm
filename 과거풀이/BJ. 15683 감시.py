# BJ. 15683 감시
# 경우의 수.
# 1은 4 한방향  상하좌우
# 2는 2 양방향  상하/좌우
# 3은 4 직각    상하좌우
# 4는 4 삼방향  상하좌우
# 5는 1 전방향
# 경우의 수 다만들어야할듯.
# 하나씩줄이면서 그때 값이 3, 2, 1, 0 일때 상하좌우 라고 생각하고 하면될거같은데


def plus(what, x, y):
    cnt = 0
    if what == 'up':
        while x > -1:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] < 1:
                if room_backup[x][y] == 0:
                    cnt += 1
                room_backup[x][y] -= 1
            x -= 1

    elif what == 'down':

        while n > x:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] < 1:
                if room_backup[x][y] == 0:
                    cnt += 1
                room_backup[x][y] -= 1
            x += 1

    elif what == 'left':
        while y > -1:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] < 1:
                if room_backup[x][y] == 0:
                    cnt += 1
                room_backup[x][y] -= 1
            y -= 1
    else:
        while m > y:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] < 1:
                if room_backup[x][y] == 0:
                    cnt += 1
                room_backup[x][y] -= 1
            y += 1
    return cnt


def minus(what, x, y):
    if what == 'up':
        while x > -1:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] < 0:
                room_backup[x][y] += 1
            x -= 1

    elif what == 'down':
        while n > x:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] < 0:
                room_backup[x][y] += 1
            x += 1

    elif what == 'left':
        while y > -1:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] < 0:
                room_backup[x][y] += 1
            y -= 1
    else:
        while m > y:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] < 0:
                room_backup[x][y] += 1
            y += 1


def counting(depth1, c_type, x, y, cnt, li):  # direction 이 즉 경우의 수 갯수.

    if depth1 == 0:
        counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt, li)

    if depth1 == len(cctv)-1:
        global max_visible

        if cnt > max_visible:
            max_visible = cnt
        return

    else:
        if c_type == 0:
            return
        elif c_type == 1:
            for direction in range(4):
                temp = 0
                if direction == 3:
                    temp += plus('up', x, y)
                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)
                    minus('up', x, y)

                elif direction == 2:
                    temp += plus('down', x, y)
                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)
                    minus('down', x, y)

                elif direction == 1:
                    temp += plus('right', x, y)
                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)
                    minus('right', x, y)

                else:
                    temp += plus('left', x, y)
                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)
                    minus('left', x, y)

        elif c_type == 2:
            for direction in range(2):
                temp = 0
                if direction == 1:
                    temp += plus('up', x, y)
                    temp += plus('down', x, y)

                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)

                    minus('up', x, y)
                    minus('down', x, y)
                else:
                    temp += plus('left', x, y)
                    temp += plus('right', x, y)

                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)

                    minus('right', x, y)
                    minus('left', x, y)

        elif c_type == 3:
            for direction in range(4):
                temp = 0
                if direction == 3:
                    temp += plus('right', x, y)
                    temp += plus('up', x, y)

                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)

                    minus('right', x, y)
                    minus('up', x, y)
                elif direction == 2:
                    temp += plus('right', x, y)
                    temp += plus('down', x, y)

                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)

                    minus('down', x, y)
                    minus('right', x, y)
                elif direction == 1:
                    temp += plus('left', x, y)
                    temp += plus('up', x, y)

                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)

                    minus('left', x, y)
                    minus('up', x, y)
                else:
                    temp += plus('left', x, y)
                    temp += plus('down', x, y)

                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)

                    minus('left', x, y)
                    minus('down', x, y)
        elif c_type == 4:
            for direction in range(4):
                temp = 0
                if direction == 3:
                    temp += plus('up', x, y)
                    temp += plus('down', x, y)
                    temp += plus('left', x, y)

                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)

                    minus('up', x, y)
                    minus('down', x, y)
                    minus('left', x, y)
                elif direction == 2:
                    temp += plus('up', x, y)
                    temp += plus('down', x, y)
                    temp += plus('right', x, y)

                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)

                    minus('up', x, y)
                    minus('down', x, y)
                    minus('right', x, y)
                elif direction == 1:
                    temp += plus('left', x, y)
                    temp += plus('right', x, y)
                    temp += plus('up', x, y)

                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)

                    minus('up', x, y)
                    minus('left', x, y)
                    minus('right', x, y)
                else:
                    temp += plus('left', x, y)
                    temp += plus('right', x, y)
                    temp += plus('down', x, y)

                    counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt + temp, li)

                    minus('left', x, y)
                    minus('down', x, y)
                    minus('right', x, y)

        else:
            cnt += plus('left', x, y)
            cnt += plus('right', x, y)
            cnt += plus('down', x, y)
            cnt += plus('up', x, y)
            counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt, li)
            minus('up', x, y)
            minus('left', x, y)
            minus('right', x, y)
            minus('down', x, y)


n, m = map(int, input().split())

room_backup = []
zero_count = 0
cctv = [0]  # cctv 종류, 위치 저장해둠.
for row in range(n):
    room_backup.append([])
    for col, value in enumerate(list(map(int, input().split()))):
        room_backup[row].append(value)
        if value == 0:
            zero_count += 1
        elif value == 6:
            continue
        else:
            cctv.append([value, row, col])

cctv.append([0, 0, 0])

max_visible = 0
counting(0, 0, 0, 0, 0, room_backup)


print(zero_count - max_visible)

