# 다익스트라 풀이

import heapq, sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 인접 리스트 생성
adj_list = [ []*(n+1) for _ in range(n+1) ]

for _ in range(m):
    s_node, e_node, weight = map(int, input().split())
    adj_list[s_node].append((weight, e_node))

# 도착 지점
s, e = map(int, input().split())

# 우선순위 큐 생성
heap = []

# DP용 distance list (weight)
distance = [float('inf')]*(n+1)
distance[s] = 0

# 다익스트라
heapq.heappush(heap, (0, s))

while heap:
    w, i = heapq.heappop(heap)

    if distance[i] >= w:

        for next_w, next_i in adj_list[i]:
            total_w = next_w + w
            if total_w < distance[next_i]:
                distance[next_i] = total_w
                heapq.heappush(heap, (total_w, next_i))
# 결과 도출
print(distance[e])