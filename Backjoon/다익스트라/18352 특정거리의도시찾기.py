# n개의 도시와 m개의 단방향 도로 ( 거리는 모두 1 )
# x에서 시작해서 최단거리가 k인 모든 도시를 출력 x에서 x는 0
# bfs로 풀면 더 빨리 풀기 가능
# x 에서 임의 도시 p 까지 가는데 k이기만 하면 되기때문

import heapq, sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

roads = [ [] for _ in range(n + 1) ]

for i in range(m):
    s, e = map(int, input().split())
    roads[s].append(e)

heap = []

distance = [float('inf')] * ( n + 1 )
distance[x] = 0
heapq.heappush(heap, (0, x))

while heap:
    current_distance, current_city = heapq.heappop(heap)

    if distance[current_city] >= current_distance:
        for next_city in roads[current_city]:
            if distance[next_city] > current_distance + 1:
                distance[next_city] = current_distance + 1
                heapq.heappush(heap, (distance[next_city], next_city))

result = [ i for i in range(len(distance)) if distance[i] == k]

print(*sorted(result), sep = '\n') if result else print('-1')