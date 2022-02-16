# # 0,0, n,n 이 시작과 끝이라서 방문자리 초기화가 필요없다.
# # 왜냐면 우선순위 큐에 넣을 때, 벽을 부수면 후순위로 밀리기 때문.
# # 벽을 부수고 간 자리가 먼저가는 경우는 생각할 필요 없다.

# import heapq, sys
# input = sys.stdin.readline

# n = int(input())
# maze = [ list(map(int, list(input().rstrip()))) for _ in range(n) ]

# check = [ [ 0 for _ in range(n)] for _ in range(n) ]


# heap = []
# heapq.heappush(heap, (0, 0, 0))
# check[0][0] = 1

# tr = [1, -1, 0, 0]
# tc = [0, 0, 1, -1]

# while heap:
#     cnt_wall, r, c = heapq.heappop(heap)

#     if r == n-1 and c == n-1:
#         print(cnt_wall)
#         break
    
#     for i in range(4):
#         nr = r + tr[i]
#         nc = c + tc[i]

#         if n > nr > -1 and n > nc > -1 and not check[nr][nc]:
#             check[nr][nc] = 1
#             if not maze[nr][nc]:
#                 heapq.heappush(heap, (cnt_wall + 1, nr, nc))
#             else:
#                 heapq.heappush(heap, (cnt_wall, nr, nc))
            
            
# deque 로 구현

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maze = [ list(map(int, list(input().rstrip()))) for _ in range(n) ]

check = [ [ 0 for _ in range(n)] for _ in range(n) ]

que = deque()
que.append([0, 0, 0])
check[0][0] = 1

tr = [1, -1, 0, 0]
tc = [0, 0, 1, -1]

while que:
    cnt_wall, r, c = que.popleft()

    if r == n-1 and c == n-1:
        print(cnt_wall)
        break
    
    for i in range(4):
        nr = r + tr[i]
        nc = c + tc[i]

        if n > nr > -1 and n > nc > -1 and not check[nr][nc]:
            check[nr][nc] = 1
            if not maze[nr][nc]:
                que.append([cnt_wall + 1, nr, nc])
            else:
                que.appendleft([cnt_wall, nr, nc])
            
            
