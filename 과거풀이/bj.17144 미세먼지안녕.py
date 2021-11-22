# dict 활용.
# bfs쓰려하니깐, 값까지 넣어주려하니, 다른방향에서 온 미세먼지 값을 못 더해주네 ( 더해주려면 맵을 만들어야하는데 맵을 안만들려고하는중 )
# 방법 1
# 맨처음 Q에 좌표와 값을 넣어준다.
# 미세먼지는 동시에 확산되어야하므로, 값을 넣어서 큐에 넣어야하는 것.
# 또한, 4방향 확인후, 자기 자신 위치에서의 값도 큐에 넣어줘야함.
# 확산 이후, 한칸씩 옮겨가야함.
# 위에처럼 값을 큐에 넣어주면, 이동을 확인하기 힘들다.
# 따라서 확산하는 동시에 반영해야한다.
# T초가 지난 후에 남아있는 미세먼지양을 구한다.

# 이렇게 푸니깐 느리네, 2400ms, 단순하게 for문 돌려서 푸는게 더빠르다.
# bfs도 느림, 단순히 맵 여러개 그리는게 나을듯. 아마도 50x50이라서 그런가봄
# 쉽게풀수록 빠름, 그리고 deepcopy 하는것보다 for 2개돌려서 대입하는게 더 빠름. -> 김원호 풀이참조

from collections import defaultdict

def ventilate(row, col, r, c):
    new_row = row
    new_col = col

    # 아래, 위 청소기
    if 0 <= row <= cleaner[0]:
        if row == 0:
            if 0 < col <= c-1:
                new_col = col - 1  # 위, 우측 상단 모서리
            elif col == 0:
                new_row = row + 1  # 좌측 상단 모서리
        elif row == cleaner[0]:
            if 0 < col < c-1:
                new_col = col + 1
            elif col == c-1:
                new_row = row - 1  # 우측 하단 모서리
        else:
            if col == 0:
                new_row = row + 1
            elif col == c-1:
                new_row = row - 1
    else:
        if row == r-1:
            if 0 < col <= c-1:
                new_col = col - 1  # 아래, 아래 하단 모서리
            elif col == 0:
                new_row = row - 1
        elif row == cleaner[1]:
            if 0 < col < c-1:
                new_col = col + 1
            elif col == c-1:
                new_row = row + 1  # 우측 상단 모서리
        else:
            if col == 0:
                new_row = row - 1
            elif col == c-1:
                new_row = row + 1

    return (new_row, new_col)

r, c, limit = map(int, input().split())

where_dust = defaultdict(int)

cleaner = []

for i in range(r):
    for j, dust in enumerate(map(int, input().split())):
        if dust > 0:
            where_dust[(i, j)] += dust
        elif dust < 0:
            cleaner.append(i)  # j는 어차피 0

x = [1, -1, 0, 0]
y = [0, 0, 1, -1]

time = 0
while time < limit:
    temp = defaultdict(int)

    for where, value in where_dust.items():
        if value == 0:
            continue
        r1, c1 = where
        cnt = 0
        for i in range(4):
            row = r1 + x[i]
            col = c1 + y[i]

            if r > row > -1 and c > col > -1:
                if (row, 0) == (cleaner[0], col) or (row, 0) == (cleaner[1], col):
                    continue
                # 일단 쪼개고 움직인다
                row, col = ventilate(row, col, r, c)
                temp[(row, col)] += value // 5
                cnt += 1
        r1, c1 = ventilate(r1, c1, r, c)
        temp[(r1, c1)] += value - (value // 5)*cnt

    # 청소기에 빨려들어간놈들없앰
    if temp[(cleaner[0], 0)]:
        del temp[(cleaner[0], 0)]
    if temp[(cleaner[1], 0)]:
        del temp[(cleaner[1], 0)]
    where_dust = temp.copy()

    time += 1
else:
    print(sum(where_dust.values()))