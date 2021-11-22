# 힙을 이용한 풀이

import heapq

n, m = map(int, input().split())

heap = list(map(int, input().split()))

heapq.heapify(heap)

for _ in range(m):
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)

    heapq.heappush(heap, first+second)
    heapq.heappush(heap, first+second)
print(sum(heap))
