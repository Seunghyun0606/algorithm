# 1167 트리의 지름과 동일하다.
# 특정노드부터 최대 거리의 노드를 구한 뒤,
# 그 노드부터 가장 먼 최대거리의 노드가 트리의 지름이 된다.

import sys
sys.setrecursionlimit(10**9)

n = int(input())

if n == 1:
    print(0)
else:

    nodes = [ [] for _ in range(n+1) ]
    check = [0]*(n+1)
    max_weight = 0
    farest_node = 0


    for _ in range(n-1):
        sn, en, w = map(int, input().split())

        nodes[sn].append([en, w])
        nodes[en].append([sn, w])


    def DFS(start_node, init_weight):
        global max_weight, farest_node
        check[start_node] = 1
        for end_node, weight in nodes[start_node]:
            if not check[end_node]:
                total_weight = init_weight + weight
                if total_weight > max_weight:
                    max_weight = total_weight
                    farest_node = end_node
                DFS(end_node, total_weight)
        check[start_node] = 0

    DFS(1, 0)
    DFS(farest_node, 0)
    print(max_weight)

# DFS한번으로 찾기

# import sys
# sys.setrecursionlimit(1234567)
# input = sys.stdin.readline

# N = int(input())
# g = [[] for i in range(N)]
# v = [-1] * N

# for i in range(N-1):
#     a, b, d = map(int, input().split())
#     g[a-1].append((b-1, d))
#     g[b-1].append((a-1, d))

# def DFS(cur, distance):
#     v[cur] = distance
#     for nxt, nd in g[cur]:
#         if v[nxt] != -1:
#             continue
#         DFS(nxt, distance + nd)

# DFS(0, 0)

# max_node = v.index(max(v))
# v = [-1] * N
# DFS(max_node, 0)
# print(max(v))