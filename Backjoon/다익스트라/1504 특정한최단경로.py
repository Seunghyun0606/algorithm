# 방향성이 없는 그래프(양방향), 다익스트라
# 1 -> N으로 갈 때, 주어진 두 정점을 반드시 거쳐야 한다.
# a랑 b에서 두번만 다익스트라 거치면된다.
# 왜냐면 1 a b a 2 여도, b에서 2까지 가는데,
# a를 통과한 시간을 포함해서 2로 바로가는것 보다 짧은 시간이 DP에 저장되기 때문이다.

import heapq, sys
input = sys.stdin.readline

n, e = map(int, input().split())

# 노드 개수만큼 간선 확보
adj_list = [ [] for _ in range(n+1) ]

for _ in range(e):
    s, e, d = map(int, input().split())
    adj_list[s].append((d, e))
    adj_list[e].append((d, s))

v1, v2 = map(int, input().split())

def dijkstra(v):
    distance = [float('inf')]*(n+1)
    distance[v] = 0

    heap = []
    heapq.heappush(heap, (0, v))

    while heap:
        current_w, current_node = heapq.heappop(heap)

        if distance[current_node] >= current_w:

            for next_w, next_node in adj_list[current_node]:
                total_weight = next_w + current_w
                if distance[next_node] > total_weight:
                    distance[next_node] = total_weight
                    heapq.heappush(heap, (total_weight, next_node))
    return distance

v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

result = min(v1_distance[1] + v1_distance[v2] + v2_distance[n], v2_distance[1] + v2_distance[v1] + v1_distance[n] )
print( -1 if result == float('inf') else result )