import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    temp = int(input())
    if temp:
        heapq.heappush(heap, temp)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)