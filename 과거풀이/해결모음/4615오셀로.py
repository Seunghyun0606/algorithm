# 4615. 재미있는 오셀로 게임 D3

# 한변의 길이 N, 돌 놓는 횟수 M
# 좌표, 흑돌 1 백돌 2

T = int(input())

for tc in range(T):

    n, m = map(int, input().split())

    places = [ list(map(int, input().split())) for _ in range(m) ]

    # 게임판 시작
    game_map = [ [0 for __ in range(n)] for _ in range(n) ]
    game_map[n//2-1][n//2-1] = 2
    game_map[n//2][n//2] = 2
    game_map[n//2-1][n//2] = 1
    game_map[n//2][n//2-1] = 1

    dx = [1, -1, 0, 0, 1, 1, -1, -1]  # 상 하
    dy = [0, 0, -1, 1, 1, -1, 1, -1]  # 좌 우

    # 놓는 경우의 수
    for x in range(len(places)):  # 턴 당 놓는 위치 // 0번째는 열, 1번째는 행
        if places[x][2] == 1:  # 1(흑돌)이면
            game_map[places[x][1]-1][places[x][0]-1] = 1  # 놓은걸 흑돌로 바꾸고 game_map의 행, 열
            # 좌우 상하에 백돌이 있는 쪽을 찾고, 그 방향으로 흑돌이나올때까지 찾자.
            for i in range(len(dx)):
                temp_x = places[x][1]-1 + dx[i]
                temp_y = places[x][0]-1 + dy[i]
                if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= n:
                    continue
                else:
                    if game_map[temp_x][temp_y] == 2:  # 상하 좌우 검색해서 백돌이면
                        while game_map[temp_x][temp_y] != 0:  # 백돌 방향으로 먼저 0을 찾아
                            temp_x += dx[i]
                            temp_y += dy[i]
                            if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= n:  # 1(흑돌)을 만나기전에 경계를 벗어나면 0만 있었던거니깐 while break시켜
                                break
                            if game_map[temp_x][temp_y] == 1:
                                temp_x = places[x][1] - 1 + dx[i]  # 좌표 초기화시켜서 백돌을 흑돌로 바꾸는 과정
                                temp_y = places[x][0] - 1 + dy[i]
                                while game_map[temp_x][temp_y] != 1:  # 흑돌이 아니면 계속 전진하면서 흑돌로 바꿔
                                    game_map[temp_x][temp_y] = 1
                                    temp_x += dx[i]
                                    temp_y += dy[i]
                                break

        if places[x][2] == 2:  # 2(백돌)이면
            game_map[places[x][1]-1][places[x][0]-1] = 2  # 놓은걸 백돌로 바꿈 game_map의 행, 열
            # 좌우 상하에 흑돌이 있는 쪽을 찾고, 그 방향으로 백돌이나올때까지 찾자.
            for i in range(len(dx)):
                temp_x = places[x][1]-1 + dx[i]
                temp_y = places[x][0]-1 + dy[i]
                if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= n:
                    continue
                else:
                    if game_map[temp_x][temp_y] == 1:  # 상하 좌우 검색해서 흑돌이면
                        while game_map[temp_x][temp_y] != 0: # 흑돌 방향으로 먼저 0을 찾아
                            temp_x += dx[i]
                            temp_y += dy[i]
                            if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= n:  # 2(백돌)을 만나기전에 경계를 벗어나면 0만 있었던거니깐 while break시켜
                                break
                            if game_map[temp_x][temp_y] == 2:
                                temp_x = places[x][1] - 1 + dx[i]  # 좌표 초기화시켜서 흑돌을 백돌로 바꾸는 과정
                                temp_y = places[x][0] - 1 + dy[i]
                                while game_map[temp_x][temp_y] != 2:  # 백돌이 아니면 계속 전진하면서 백돌로 바꿔
                                    game_map[temp_x][temp_y] = 2
                                    temp_x += dx[i]
                                    temp_y += dy[i]
                                break

    count_black = 0
    count_white = 0

    for x in range(len(game_map)):
        for y in range(len(game_map[x])):
            if game_map[x][y] == 1:
                count_black += 1
            elif game_map[x][y] == 2:
                count_white += 1

    print('#{}'.format(tc+1), count_black, count_white)