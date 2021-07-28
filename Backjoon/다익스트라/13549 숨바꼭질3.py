# 다익스트라 이용 가능 - 노드 개념으로 가져갈 필요 없이, 이동시 코스트로 계산
# -1, 1, 0인 셈
# visit배열 쓸 거면 사실상 BFS써도 무관했을듯 하다

import heapq, sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 각 x 좌표 옮기기 위한 시간
move_time = [(1, -1), (1, 1), (0, 0)]

# 각 거리까지의 최소 시간
distance_time = [float('inf')] * 100001
distance_time[n] = 0

# heap 준비
heap = []
heapq.heappush(heap, (0, n))

while heap:
    current_w, current_x = heapq.heappop(heap)

    if distance_time[current_x] >= current_w:
        for next_w, next_x in move_time:
            total_time = next_w + current_w
            if next_x:
                last_x = current_x + next_x
            else:
                last_x = current_x*2
            if -1 < last_x <= 100000 and distance_time[last_x] > total_time:
                distance_time[last_x] = total_time
                heapq.heappush(heap, (total_time, last_x))
print(distance_time[k])