# 힙정렬 순서가 아마도, 튜플로 넣으면 0, 1, 2, 3로 작은 순으로 알아서 정렬될것이다.

import sys, heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    temp = int(input())

    if temp:
        heapq.heappush(heap, (abs(temp), temp))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    