# 한번에 이동할수 있는 중량의 '최댓값'을 구하기. => 여러 경로를 거치는 와중에서 최대값을 가진 경로
# 즉, a -> b로 갈 때, 각 경로를 거쳐서 가는 최종적인 최소거리가 2, 7, 3 이 있었다고 하면, 이 중에서 최대거리인 7을 뽑는 것
# 그래프 노드 형태로 나타냄.
# 모든 다리는 양방향

import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())

# node 좌표
node = [ [] for _ in range(n+1) ]

for _ in range(m):
    s_n, e_n, weight = map(int, input().split())
    node[s_n].append((weight, e_n))
    node[e_n].append((weight, s_n))

# 마지막 결과 노드
a, b = map(int, input().split())

# 최소 중량을 위한 dp 및, 해당 dp를 만들기 위한 각 경로의 값
weight_dp = [ float('-inf') ]*(n+1)
weight_dp[a] = 0

# heap 생성, weight, 다음 node, 거쳐간 모든 경로
heap = []
heapq.heappush(heap, (-float('inf'), a))

# 다익스트라 시작
# 최소힙으로 만들어서 모든 경우를 돌리면 시간초과 난다.
# 따라서 최대힙으로 만들어야한다.
while heap:
    current_w, current_n = heapq.heappop(heap)
    current_w = -current_w
    # 이미 최대중량일 경우 넘어가야함. ( 이 경로에서는 더이상 늘릴 수 없는 경우 )
    if weight_dp[current_n] > current_w:
        continue
    for next_w, next_n in node[current_n]:

        # 다음 도착지에 저장 되어있는 최대 하중 ( 그 도착지까지 가기 위한 하중 중에서 최대 하중 ) 보다 현재 하중이 크면서
        # 다음 도착지에 저장 되어있는 최대 하중 보다 다음 도착지로 가기 위한 다리의 하중이 더 크면
        # 다음 도착지의 하중은 현재 하중 과 다음 도착지로 가기위한 다리의 하중 중 작은 것 선택.
        if weight_dp[next_n] < current_w and weight_dp[next_n] < next_w:
            weight_dp[next_n] = min(current_w, next_w)
            heapq.heappush(heap, (-weight_dp[next_n], next_n))

print(weight_dp[b])