# heap을 이용해서 각 과목에서 투자해야할 최대 마일리지를 다 쌓아놓고,
# 정렬하고, sum 해서 하나씩 빼버리자.

# 사실 정렬하고 append를 이용해서도 풀수있다.
# sys 쓰니간 88 -> 72ms가 된다.

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

max_point = []

for _ in range(n):
    np, nl = map(int, input().split())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    if np > nl:
        for _ in range(np-nl+1):
            temp_point = heapq.heappop(heap)
        else:
            max_point.append(temp_point)
    else:
        max_point.append(1)


max_point.sort()
total_point = sum(max_point)
cnt = len(max_point)
while total_point > m:
    total_point -= max_point.pop()
    cnt -= 1

else:
    print(cnt)


# 다른 사람 풀이. append와 정렬을 이용함. 64ms 로 88ms보다 빠르다.
# import sys
# input = sys.stdin.readline

# n, tM = map(int, input().split())
# MList = []

# for i in range(n):
#     pi, li = map(int, input().split())
#     arr = list(map(int, input().split()))
#     if pi < li :
#         MList.append(1)
#     else:
#         arr.sort(reverse = True)
#         MList.append(arr[li-1])

# while (sum(MList) > tM):
#     MList.remove(max(MList))
#     n -= 1


# print(n)
