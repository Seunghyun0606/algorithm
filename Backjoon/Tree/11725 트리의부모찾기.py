# 루트가 1 각 노드의 부모 구하기
# 입력으로 edge, 출력으로 각 노드의 부모
# readline 입력 사용안하면 4380ms 사용시 352ms
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

edges = [ [] for _ in range(n+1) ]

for i in range(n-1):
    s, e = map(int, input().split())

    edges[s].append(e)
    edges[e].append(s)

check_node = [0]*(n+1)

# 너비우선 검색
node_place = deque()
node_place.append(1)

while node_place:
    start_node = node_place.popleft()

    for node in edges[start_node]:
        if not check_node[node]:
            node_place.append(node)
            check_node[node] = start_node

for result in check_node[2:]:
    print(result)