# 컴퓨터가 감염되는 시간이 중요하다.
# 다익스트라 개념 이용 가능

import heapq, sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())

    nodes = [ [] for _ in range(n+1) ]
    
    for _ in range(d):
        a, b, s = map(int, input().split())

        nodes[b].append((s, a))
    
    check_node = [float('inf')] * ( n + 1 )
    check_node[c] = 0

    heap = []
    heapq.heappush(heap, (0, c))

    while heap:
        cur_time, infested = heapq.heappop(heap)
        
        if check_node[infested] < cur_time:
            continue
        for node in sorted(nodes[infested]):
            next_time, next_infested = node
            next_sum_time = next_time + check_node[infested]
            if check_node[next_infested] > next_sum_time:
                check_node[next_infested] = next_sum_time
                heapq.heappush(heap, (next_sum_time, next_infested)) 

    result_list = list(filter(lambda x: x != float('inf'), check_node))
    print(len(result_list) , max(result_list))