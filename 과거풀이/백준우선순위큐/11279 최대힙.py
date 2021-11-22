# heapify_max라는걸 지원한다는데, 음수로 계산하면 힙성질을 반대로 이용가능.
# tuple로 (-1, 1) 형태로도 가능. 다른데에 응용도 가능할듯

import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    temp = int(input())

    if temp:
        heapq.heappush(heap, -temp)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
