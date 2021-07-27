# # 다익스트라 방식, 각 점을 node로 보고 푼다. (실패)
# # BFS 방식도 가능할듯 하다.

# # 1차원으로 변환하면 안된다. 2차원으로 해야한다.

# import heapq, sys
# input = sys.stdin.readline

# m, n = map(int, input().split())

# if m == 1:
#     cnt = 0
#     for i in range(n):
#         if input().rstrip() == '1':
#             cnt += 1
#     print(cnt)
# else:

#     # 2차원 maze개념이아니라, adj_list이며, 각각의 좌표점을 node라고 생각한다.
#     maze = [ [] for _ in range(n*m) ]

#     # 벽 유무
#     wall = []
#     for i in range(n):
#         for j in input().rstrip():
#             wall.append(j)

#     # 좌표를 1차원 변환을 위한 list ( 좌, 우, 하, 상)
#     trans = [-1, 1, m, -m]

#     # 벽 없이 가면 0, 벽 부수고가면 1
#     for i in range(n):
#         for j in range(m):
#             temp = i*m + j
#             for k in trans:
#                 if temp >= m-1 and (( temp % ((i+1)*m-1) == 0 and k == 1 ) or ( temp % (i*m-1) == 1 and k == -1 )):
#                     continue
#                 if n*m > temp + k > -1:
#                     if wall[temp + k] == '1':
#                         maze[temp].append((1, temp + k))
#                     else:
#                         maze[temp].append((0, temp + k))

#     # dp를 위한 distance list ( 해당 maze에선 각 좌표들이 node이다 )
#     distance = [float('inf')]*(n*m)
#     distance[0] = 0

#     # 우선순위 큐, 시작 위치는 0 (1, 1), weight는 0
#     heap = []
#     heapq.heappush(heap, (0, 0))

#     while heap:
#         current_w, current_i = heapq.heappop(heap)

#         if distance[current_i] >= current_w:
            
#             for next_w, next_i in maze[current_i]:
#                 total_w = current_w + next_w
#                 if total_w < distance[next_i]:
#                     distance[next_i] = total_w
#                     heapq.heappush(heap, (total_w, next_i))
#     print(str(distance[n*m-1])[0])


# version 2. 각 좌표를 힙에 넣는다

import heapq, sys
input = sys.stdin.readline


m, n = map(int, input().split())

wall = [ list(map(int, input().rstrip())) for _ in range(n) ]
# print(wall)
# 중복으로 갈수도 있기 때문에, visit여부는 체크하지 않는다.

# x, y좌표
x = [1, -1, 0, 0]
y = [0, 0, -1, 1]

# dp를 위한 distance
distance = [ [float('inf')]*m for _ in range (n) ]
distance[0][0] = 0

# heap 생성, weight 및 x, y좌표
heap = []

heapq.heappush(heap, (0, 0, 0))

while heap:
    w, y1, x1 = heapq.heappop(heap)

    for i in range(4):
        xx = x1 + x[i]
        yy = y1 + y[i]
        if m > xx > -1 and n > yy > -1 and distance[yy][xx] > wall[yy][xx] + w:
            distance[yy][xx] = wall[yy][xx] + w
            heapq.heappush(heap, (distance[yy][xx], yy, xx))

print(distance[n-1][m-1])