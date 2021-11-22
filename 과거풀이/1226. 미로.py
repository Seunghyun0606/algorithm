# 1226. 미로 D4


T = 10

for _ in range(T):

    tc = int(input())

    maze = [list(map(int, input())) for _ in range(16)]

    start = []
    flag = False
    for y in range(16):
        if flag:
            break
        for x in range(16):
            if maze[x][y] == 2:
                start += [x]
                start += [y]  # 2일때의 행과 열 위치
                flag = True
    # 여기까지 시작지점을 찾았다.

    visit = [ [ 0 for _ in range(16) ] for _ in range(16) ]

    def dfs(vx, vy):  # 맨처음 start지점 넣었음
        visit[vx][vy] = 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        new_xy = []
        for i in range(4):
            new_xy.append([vx+dx[i], vy+dy[i]])

        for w in new_xy:
            if maze[w[0]][w[1]] == 3:
                return 1
            elif maze[w[0]][w[1]] == 1:
                continue
            if visit[w[0]][w[1]]:
                continue
            if dfs(w[0], w[1]):
                return 1

        return 0

    print('#{}'.format(tc), dfs(start[0], start[1]))
