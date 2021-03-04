# # 인접 정점의 색이 정점의 색과 다른 그래프. 2가지 색으로 그래프를 그릴 수 있는 그래프를 이분 그래프라 한다.
# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(k):
#     global color

#     for next_v in edge[k]:
#         if not visit[next_v]:
#             bfs_list.append(next_v)
#             visit[next_v] = -color
#         elif visit[next_v] == color:
#             print('NO')
#             return False
#     color *= -1
#     return True



# T = int(input())

# for _ in range(T):
#     v, e = map(int, input().split())

#     # 정점 방문 체크 (1 검은색, -1 빨간색, 0 미방문)
#     visit = [0]*(v + 1)

#     # 간선 정보
#     edge = [ [] for _ in range(v + 1) ]

#     for _ in range(e):
#         vs, ve = map(int, input().split())
#         edge[vs].append(ve)
#         edge[ve].append(vs)
    
#     # 정점 색깔
#     color = 1

#     # BFS 시행
#     # 정점이 이어지지 않는 경우도 있으니, 모두 확인해야해서 for 사용
#     bfs_list = deque()
#     flag = True
#     for i in range(1, v + 1):
#         if not visit[i]:
#             visit[i] = color
#             bfs(i)
#         while bfs_list and flag:
#             next_bfs = bfs_list.popleft()
#             flag = bfs(next_bfs)

#         # NO일 경우
#         if not flag:
#             break
#     else:
#         print("YES")



# 인접 정점의 색이 정점의 색과 다른 그래프. 2가지 색으로 그래프를 그릴 수 있는 그래프를 이분 그래프라 한다.
# 위에 코드는 틀렸는데, color를 지정하면안되고, 무조건 이전 정점이랑 비교하는 코드로 가야한다.
from collections import deque
import sys
input = sys.stdin.readline

def bfs(k):

    bfs_list = deque()
    # 정점색깔
    visit[k] = 1
    bfs_list.append(k)

    while bfs_list:
        next_k = bfs_list.popleft()
        for next_v in edge[next_k]:
            if not visit[next_v]:
                bfs_list.append(next_v)
                visit[next_v] = -visit[next_k]
            elif visit[next_v] == visit[next_k]:
                print('NO')
                return False
    return True



T = int(input())

for _ in range(T):
    v, e = map(int, input().split())

    # 정점 방문 체크 (1 검은색, -1 빨간색, 0 미방문)
    visit = [0]*(v + 1)

    # 간선 정보
    edge = [ [] for _ in range(v + 1) ]

    for _ in range(e):
        vs, ve = map(int, input().split())
        edge[vs].append(ve)
        edge[ve].append(vs)

    # BFS 시행
    # 정점이 이어지지 않는 경우도 있으니, 모두 확인해야해서 for 사용
    flag = True
    for i in range(1, v + 1):
        if not visit[i]:
            flag = bfs(i)

        # NO일 경우
        if not flag:
            break
    else:
        print("YES")
        
