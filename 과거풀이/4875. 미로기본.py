# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로


def dfs(vx, vy):
    visit[vx][vy] = 1

    if maze[vx][vy] == '3':
        return 1
    else:
        for i in range(4):
            x1 = vx + dx[i]
            y1 = vy + dy[i]

            if n > x1 > -1 and n > y1 > -1:
                if visit[x1][y1]:
                    continue
                if maze[x1][y1] == '1':
                    continue

                if dfs(x1, y1):
                    return 1
    return 0

T = int(input())
for tc in range(T):

    n = int(input())

    maze = [ list(input()) for _ in range(n) ]
    visit = [ [0 for _ in range(n) ] for _ in range(n) ]


    p_x = 0
    p_y = 0
    flag = False
    for x in range(n):
        if flag:
            break
        for y in range(n):
            if maze[x][y] == '2':
                p_x = x
                p_y = y
                flag = True
                break

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    print('#{}'.format(tc+1), dfs(p_x, p_y))










