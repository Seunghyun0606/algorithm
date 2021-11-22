# 정점 갯수 4, 간선갯수 5, 시작 1 (n, m, v)

import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

node_list = [ [] for _ in range(n+1) ]

for _ in range(m):
    s, e = map(int, input().split())

    node_list[s].append(e)
    node_list[e].append(s)

node_list = list(map(sorted, node_list))

# DFS 순서
def DFS(start):
    check[start] = 1
    for node in node_list[start]:
        if check[node]:
            continue
        dfs_answer.append(node)
        DFS(node)

check = [0]*(n+1)
dfs_answer = [v]
DFS(v)

print(*dfs_answer)


# BFS 순서
from collections import deque


check = [0]*(n+1)

que = deque()

for node in node_list[v]:
    que.append(node)
check[v] = 1
bfs_answer = [v]
while que:
    node = que.popleft()
    if check[node]:
        continue
    check[node] = 1
    bfs_answer.append(node)

    for temp_node in node_list[node]:
        que.append(temp_node)

print(*bfs_answer)

# visited = [False] * N

# q = deque()
# q.append(V - 1)
# visited[V - 1] = True

# while len(q):
#     curr = q.popleft()
#     print(curr + 1, end=' ')

#     for i in range(0, len(graph[curr])):
#         if not visited[graph[curr][i]]:
#             visited[graph[curr][i]] = True
#             q.append(graph[curr][i])