# bfs 사용해서 일단 제일가까운 놈 고른다음에, 없애고 초기화 시킨다.
# 즉, 한마리씩만 먹고 다음 턴을 진행하자. 어차피 map자체가 작아서 계속 돌려도 큰 지장없을듯.
# sys 붙여도 별 큰 차이없네, 로직자체가 느린가보다.

from collections import deque
# import sys

# input = sys.stdin.readline

n = int(input())


sea = []
start = []

for i in range(n):
    temp = []
    for j, k in enumerate(list(map(int, input().split()))):
        if k == 9:
            start = [i, j, 0]
        temp.append(k)
    sea.append(temp)


dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

current_size = 2

def find_fish(start):
    que = deque()
    que.append(start)
    can_eat = []
    check_sea[start[0]][start[1]]

    while que:
        r, c, d = que.popleft()

        for i in range(4):
            row = r + dr[i]
            col = c + dc[i]

            if n > row > -1 and n > col > -1 and sea[row][col] <= current_size and not check_sea[row][col]:
                if 0 < sea[row][col] < current_size:
                    can_eat.append([row, col, d+1])
                que.append([row, col, d+1])
                check_sea[row][col] = 1
    if can_eat:
        can_eat.sort(key = lambda x : (x[2], x[0], x[1]))
        return (can_eat[0][0], can_eat[0][1], can_eat[0][2])
    else:
        return []


time = 0
exp = 0

sea[start[0]][start[1]] = 0

while True:
    check_sea = [ [ 0 for _ in range(n) ] for _ in range(n) ]

    eat_fish = find_fish(start)
    if eat_fish:
        exp += 1
    
    else:
        print(time)
        break

    if exp == current_size:
        current_size += 1
        exp = 0

    time += eat_fish[2]
    sea[eat_fish[0]][eat_fish[1]] = 0
    start = [eat_fish[0], eat_fish[1], 0]
