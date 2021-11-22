# BJ. 15683 감시2

# BJ. 15683 감시
# 경우의 수.
# 1은 4 한방향  상하좌우
# 2는 2 양방향  상하/좌우
# 3은 4 직각    상하좌우
# 4는 4 삼방향  상하좌우
# 5는 1 전방향
# 경우의 수 다만들어야할듯.
# 하나씩줄이면서 그때 값이 3, 2, 1, 0 일때 상하좌우 라고 생각하고 하면될거같은데


def back_up():

    room_backup1 = []
    for i in range(n):
        a = []
        for j in range(m):
            a.append(room[i][j])
        room_backup1.append(a)
    return room_backup1


def plus(what, x, y, cnt, room_backup):
    if what == 'up':
        i = 0
        while x > -1:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] == 0:
                room_backup[x][y] -= 1
                cnt += 1
            i += 1
            x -= i

    elif what == 'down':
        i = 0
        while n > x:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] == 0:
                room_backup[x][y] -= 1
                cnt += 1
            i += 1
            x += i

    elif what == 'left':
        i = 0
        while y > -1:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] == 0:
                room_backup[x][y] -= 1
                cnt += 1
            i += 1
            y -= i
    else:
        i = 0
        while m > y:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] == 0:
                room_backup[x][y] -= 1
                cnt += 1
            i += 1
            y += i
    return cnt


def minus(what, x, y, cnt, room_backup):
    if what == 'up':
        i = 0
        while x > -1:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] == 0:
                room_backup[x][y] = 1
                cnt += 1
            i += 1
            x -= i

    elif what == 'down':
        i = 0
        while n > x:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] == 0:
                room_backup[x][y] = 1
                cnt += 1
            i += 1
            x += i

    elif what == 'left':
        i = 0
        while y > -1:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] == 0:
                room_backup[x][y] = 1
                cnt += 1
            i += 1
            y -= i
    else:
        i = 0
        while m > y:
            if room_backup[x][y] == 6:
                break
            elif room_backup[x][y] == 0:
                room_backup[x][y] = 1
                cnt += 1
            i += 1
            y += i
    return cnt


def counting(depth1, c_type, x, y, cnt, li):  # direction 이 즉 경우의 수 갯수.
    visit[depth1] = 1

    if depth1 == 1:
        li = back_up()

    if depth1 == len(cctv):
        global temp
        temp = cnt

        return

    else:
        for i in range(depth1, len(cctv)):
            if visit[i]:
                continue
            if cctv[i][0]
            for direction in range(4):
                if direction == 3:
                    cnt += plus('up', x, y, cnt, li)
                elif direction == 2:
                    cnt += plus('down', x, y, cnt, li)
                elif direction == 1:
                    cnt += plus('right', x, y, cnt, li)
                else:
                    cnt += plus('left', x, y, cnt, li)
                counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt, li)
        elif c_type == 2:
            for direction in range(2):
                if direction == 1:
                    cnt += plus('up', x, y, cnt, li)
                    cnt += plus('down', x, y, cnt, li)
                else:
                    cnt += plus('left', x, y, cnt, li)
                    cnt += plus('right', x, y, cnt, li)
                counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt, li)
        elif c_type == 3:
            for direction in range(4):
                if direction == 3:
                    cnt += plus('right', x, y, cnt, li)
                    cnt += plus('up', x, y, cnt, li)
                elif direction == 2:
                    cnt += plus('right', x, y, cnt, li)
                    cnt += plus('down', x, y, cnt, li)
                elif direction == 1:
                    cnt += plus('left', x, y, cnt, li)
                    cnt += plus('up', x, y, cnt, li)
                else:
                    cnt += plus('left', x, y, cnt, li)
                    cnt += plus('down', x, y, cnt, li)
                counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt, li)
        elif c_type == 4:
            for direction in range(4):
                if direction == 3:
                    cnt += plus('up', x, y, cnt, li)
                    cnt += plus('down', x, y, cnt, li)
                    cnt += plus('left', x, y, cnt, li)
                elif direction == 2:
                    cnt += plus('up', x, y, cnt, li)
                    cnt += plus('down', x, y, cnt, li)
                    cnt += plus('right', x, y, cnt, li)
                elif direction == 1:
                    cnt += plus('left', x, y, cnt, li)
                    cnt += plus('right', x, y, cnt, li)
                    cnt += plus('up', x, y, cnt, li)
                else:
                    cnt += plus('left', x, y, cnt, li)
                    cnt += plus('right', x, y, cnt, li)
                    cnt += plus('down', x, y, cnt, li)
                counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt, li)

        elif c_type == 0:
            counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt, [])
        else:
            cnt += plus('left', x, y, cnt, li)
            cnt += plus('right', x, y, cnt, li)
            cnt += plus('down', x, y, cnt, li)
            cnt += plus('up', x, y, cnt, li)
            counting(depth1 + 1, cctv[depth1 + 1][0], cctv[depth1 + 1][1], cctv[depth1 + 1][2], cnt, li)


n, m = map(int, input().split())

room = []
zero_count = 0
cctv = [0]  # cctv 종류, 위치 저장해둠.
for row in range(n):
    room.append([])
    for col, value in enumerate(list(map(int, input().split()))):
        room[row].append(value)
        if value == 0:
            zero_count += 1
        elif value == 6:
            continue
        else:
            cctv.append([value, row, col])

back_up()

visit = [0] * len(cctv)

max_visible = 0
temp = counting(0, 0, 0, 0, 0, [])

if temp > max_visible:
    max_visible = temp


print(zero_count - max_visible)
