# 다익스트라, 총걸린 최소시간들 중 가장 큰 값

import heapq, sys
input = sys.stdin.readline

n, m, x = map(int, input().split())

# node들 간의 인접리스트
adj_list = [ [] for _ in range(n+1) ]

for _ in range(m):
    s, e, t = map(int, input().split())
    adj_list[s].append((t, e))
    # adj_list[e].append((t, s))

all_time = [0]*(n+1)

def commute_time(node):    
    # 각 노드들 까지의 최대시간 dp를 위한 time list
    time = [float('inf')]*(n+1)
    time[node] = 0

    # heap 생성
    heap = []
    heapq.heappush(heap, (0, node))

    while heap:
        now_t, now_node = heapq.heappop(heap)

        if time[now_node] >= now_t:
            for next_t, next_node in adj_list[now_node]:
                total_time = next_t + now_t

                if time[next_node] > total_time:
                    time[next_node] = total_time
                    heapq.heappush(heap, (total_time, next_node))
    all_time[node] += time[x]
    if node == x:
        for i in range(1, n+1):
            all_time[i] += time[i]

# 가는데 걸리는 시간 + 오는데 걸리는 시간 따로 구한다.

# 가는게 걸리는 시간 - 학생들 각각이 X까지 가는데 걸리는 시간을 구한다.

# 오는데 걸리는 시간 - X에서 각 학생들 집까지 시간을 구한다.

for i in range(1, n+1):
    commute_time(i)
print(max(all_time))
    

