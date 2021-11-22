# 두가지방법이있다. 정렬을 두번하거나, https://copy-driven-dev.tistory.com/entry/%EB%B0%B1%EC%A4%80Python1931%EA%B7%B8%EB%A6%AC%EB%94%94-%ED%9A%8C%EC%9D%98%EC%8B%A4%EB%B0%B0%EC%A0%95
# 우선순위 큐를 쓰거나 하는 방법이다. https://covenant.tistory.com/129
# 둘다 써보자.



import heapq, sys
input = sys.stdin.readline

n = int(input())

time_set = []

for _ in range(n):
    time_set.append(list(map(int, input().split())))

# 시작시간을 기준으로 정렬해놓고, 우선순위 큐 비교.
time_set.sort(key=lambda x : x[0])

heap = [time_set[0][1]]
# (빨리 끝나는 시간) 최소힙을 구해야함
# 가장 빨리시작하는 수업먼저 넣고 끝나는 시간과 다음 시작시간을 비교.
# 이후에는 쌓인 강의실중에서 가장 늦은 시간과 다음 시작시간을 비교한다.
# 즉, 여러개의 강의실이 필요하다면 몇개가 필요한지를 구하는 문제이다.

for i in range(1, n):
    if heap[0] <= time_set[i][0]:
        heapq.heappop(heap)
        heapq.heappush(heap, time_set[i][1])
    else:
        heapq.heappush(heap, time_set[i][1])
print(len(heap))


# 정렬하는 방법은 안된다.

# import sys
# input = sys.stdin.readline

# n = int(input())

# time_set = []

# for _ in range(n):
#     time_set.append(list(map(int, input().split())))

# # 가장 늦게끝나는 시간 기준으로 정렬하고, 같으면 시작하는 시간 기준으로 정렬
# time_set.sort(key=lambda x : (x[1], x[0]))

# latest = 0
# count = 0

# for i in range(n):
#     if time_set[i][0] >= latest:
#         latest = time_set[i][1]
#         count += 1
# print(count)
