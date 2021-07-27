# n**2 의 기본 다익스트라 개념 ( 다익스트라가 아니어도 풀 수 있을 듯 )
# a, b, c, d 에서 a -> d로 가는 개념 구하는 것

# version 1. dfs X - 시작지점이 없는 경우 안됨. 예제 입력2 케이스

# a, b = map(lambda x: int(x) - 1, input().split())
# n, m = map(int, input().split())
# pairs = [ [] for _ in range(n) ]

# for i in range(m):
#     c, d = map(int, input().split())
#     pairs[c-1].append(d-1)

# visit = [0]*n
# result = float('inf')
# def dfs(start, cnt):
#     global result

#     if start == b:
#         result = min(result, cnt)
#         return

#     else:
#         for i in pairs[start]:
#             if not visit[i]:
#                 visit[i] = 1
#                 dfs(i, cnt + 1)
#                 visit[i] = 0
# dfs(a, 0)
# print(result)

# Version 2. 다익스트라
a, b = map(lambda x: int(x) - 1, input().split())
n, m = map(int, input().split())
adj_matrix = [ [0]*n for _ in range(n) ]
for i in range(m):
    c, d = map(int, input().split())
    adj_matrix[c-1][d-1] = 1

visit = [0]*n
# visit[a] = 1
min_distance = adj_matrix[a]
result = adj_matrix[a][b]

# 방문 안한 정점 중에, 최소 정점
def getSmallNode():
    min_index = 0
    min_value = float('inf')

    for i in range(n):
        if min_distance[i] < min_value and not visit[i]:
            min_value = min_distance[i]
            min_index = i

    return min_index

# 해당 정점이 갈 수 있는 점
# 총 n개의 node중 시작점과 끝점 제외하고 n-2번 확인한다.
for i in range(n-2):
    current = getSmallNode()
    visit[current] = 1
    # 정점이 도착하는 점
    for j in range(n):
        if not visit[j]:
            min_distance[j] = min(min_distance[j], min_distance[current] + adj_matrix[current][j])

print(min_distance)
print(adj_matrix)