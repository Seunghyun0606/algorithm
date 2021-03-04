# 남동북서 8 4 2 1
# 1011의 경우 동쪽이 뚫려있는거임.
# 체크할 맵을 그리고, 맵을 기준으로 BFS돌리면된다.
# BFS돌린 이후에 각 방의 개수를 구한다.
# 각 방 중 가장 넓은 방 구한다.
# 붙어있는 방 2개의 합 중 가장 큰 것을 구한다.
# -> 각 방을 구분할 수 있어야한다. 맵에다가 표시하자.

from collections import deque

n, m = map(int, input().split())

bit_map = [ list(map(int, input().split())) for _ in range(m) ]
check_map = [ [ 0 for _ in range(n) ] for _ in range(m)]

max_room_size = 0
room_size_list = []

# 서북동남
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

# 방 사이즈 구하기
def measure_size(i, j, room_number):
    go_que = deque()
    go_que.append([i, j])
    room_size = 1
    check_map[i][j] = room_number

    while go_que:
        r, c = go_que.popleft()

        for k in range(4):
            if not (bit_map[r][c] & ( 1 << k )) and not check_map[r + dr[k]][c + dc[k]]:
                go_que.append([ r + dr[k], c + dc[k]])
                room_size += 1
                check_map[r + dr[k]][c + dc[k]] = room_number

    return room_size

# 방 갯수 구하기
for i in range(m):
    for j in range(n):
        if not check_map[i][j]:
            temp_room_size = measure_size(i, j, len(room_size_list) + 1)
            room_size_list.append(temp_room_size)
            max_room_size = max(max_room_size, temp_room_size)

# 벽 하나 제거시 최대 방 크기

well_place = deque()
room_size_set = set()

for i in range(m):
    for j in range(n):
        if check_map[i][j]:
            well_place.append([i, j])
            bit_map[i][j] = 0

            while well_place:
                r, c = well_place.popleft()

                for k in range(4):
                    row = r + dr[k]
                    col = c + dc[k]
                    if m > row > -1 and n > col > -1 and bit_map[row][col]:
                        if check_map[r][c] == check_map[row][col]:
                            well_place.append([row, col])
                            bit_map[row][col] = 0
                        else:
                            room_size_set.add((check_map[r][c], check_map[row][col]))

max_room_no_well = 0
for room1, room2 in room_size_set:
    max_room_no_well = max(max_room_no_well, room_size_list[room1-1] + room_size_list[room2-1])

print(len(room_size_list), max_room_size, max_room_no_well, sep='\n')


# 메모리 초과 코드.
# BFS 돌때 방문체크를 똑바로안해서, BFS에 너무 많은 중복된 값이 쌓여서 발생한 문제인 것으로 보임

# from collections import deque

# n, m = map(int, input().split())

# bit_map = [ list(map(int, input().split())) for _ in range(m) ]
# check_map = [ [ 0 for _ in range(n) ] for _ in range(m)]

# max_room_size = 0
# room_size_list = []

# # 서북동남
# dr = [0, -1, 0, 1]
# dc = [-1, 0, 1, 0]

# # 방 사이즈 구하기
# def measure_size(i, j, room_number):
#     go_que = deque()
#     go_que.append([i, j])
#     room_size = 1

#     while go_que:
#         r, c = go_que.popleft()

#         for k in range(4):
#             if not (bit_map[r][c] & ( 1 << k )) and bit_map[r + dr[k]][c + dc[k]]:
#                 go_que.append([ r + dr[k], c + dc[k]])
#                 room_size += 1

#         bit_map[r][c] = 0
#         check_map[r][c] = room_number
#     return room_size

# # 방 갯수 구하기
# for i in range(m):
#     for j in range(n):
#         if bit_map[i][j]:
#             temp_room_size = measure_size(i, j, len(room_size_list) + 1)
#             room_size_list.append(temp_room_size)
#             max_room_size = max(max_room_size, temp_room_size)

# # 벽 하나 제거시 최대 방 크기

# well_place = deque()
# room_size_set = set()

# for i in range(m):
#     for j in range(n):
#         if check_map[i][j]:
#             well_place.append([i, j])

#             while well_place:
#                 r, c = well_place.popleft()

#                 for k in range(4):
#                     row = r + dr[k]
#                     col = c + dc[k]
#                     if m > row > -1 and n > col > -1 and check_map[r][c] and check_map[row][col]:
#                         if check_map[r][c] == check_map[row][col]:            
#                             well_place.append([row, col])
#                         else:
#                             room_size_set.add((check_map[r][c], check_map[row][col]))

#                 check_map[r][c] = 0


# max_room_no_well = 0
# for room1, room2 in room_size_set:
#     max_room_no_well = max(max_room_no_well, room_size_list[room1-1] + room_size_list[room2-1])

# print(len(room_size_list), max_room_size, max_room_no_well, sep='\n')
