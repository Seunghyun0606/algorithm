# 106764kb	3128ms

from collections import deque

n, m = map(int, input().split())

farms = [ list(map(int, input().split())) for _ in range(m) ]

riped = deque()

# -1 인 지점빼고 m*n 개수만큼이면 다 익을 수 있다.
# BFS가 끝났는데도 개수가 다르면, -1 출력, 모두 익었으면 0 출력 
riped_tomatoes = 0
blocked_place = 0
result_day = 0

for i in range(m):
    for j in range(n):
        if farms[i][j] == 1:
            riped_tomatoes += 1
            riped.append([i, j])
        elif farms[i][j] == -1:
            blocked_place += 1

# deque 날짜 구분자
riped.append([-1, -1])

# 모두 익은상황
if n*m - blocked_place == riped_tomatoes:
    print(0)
# 익어야하거나, 모두 익을수 없는 상황
else:
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while riped:
        x, y = riped.popleft()
        if x < 0:
            if not riped:
                # 익을 수 없는 상황 구분
                if n*m - blocked_place == riped_tomatoes:
                    print(result_day)
                else:
                    print(-1)
                break
            else:
                result_day += 1
                riped.append([-1, -1])
        else:
            for k in range(4):
                row = x + dx[k]
                col = y + dy[k]
                if m > row > -1 and n > col > -1 and not farms[row][col]:
                    riped.append([row, col])
                    farms[row][col] = 1
                    riped_tomatoes += 1


# BJ. 7576 토마토 // 가로세로 // BFS
# 226876kb	3212ms 큐에 time까지 넣어서 메모리를 많이 잡아먹는듯하다.

# from collections import deque


# def cabinet():
#     que = deque()

#     for k in where:
#         que.append([k, 0])

#     dx = [1, -1, 0, 0]
#     dy = [0, 0, -1, 1]

#     while que:
#         idx, time = que.popleft()

#         for i in range(4):
#             row = idx[0] + dx[i]
#             col = idx[1] + dy[i]
#             if m > row > -1 and n > col > -1:
#                 if tomatoes[row][col]:
#                     continue
#                 tomatoes[row][col] = 1
#                 que.append([[row, col], time + 1])

#     for i in range(m):
#         for j in range(n):
#             if tomatoes[i][j] == 0:
#                 print(-1)
#                 return

#     print(time)
#     return


# n, m = map(int, input().split())

# tomatoes = []
# where = []
# cnt = 0
# for i in range(m):
#     temp = []
#     for j, val in enumerate(map(int, input().split())):
#         if val == 1:
#             where.append([i, j])
#             cnt += 1
#         temp.append(val)
#     tomatoes.append(temp)

# if cnt == n*m:
#     print(0)
# else:
#     cabinet()

