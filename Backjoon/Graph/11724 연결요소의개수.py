# 방향 없는 그래프 (양방향), 연결 요소의 개수 구하기
# 연결 요소란, 각 그래프가 연결되어있는 한 그룹
# 즉, DFS 혹은 BFS한번 다 돌면 되고, 방문 정점 Check해주면됨

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nodes = [ [] for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

check = [0]*(n+1)

# BFS
bfs = deque()
count = 0
for i in range(1, n+1):
    if not check[i]:
        bfs.append(i)
        check[i] = 1
        while bfs:
            node = bfs.popleft()

            for next_node in nodes[node]:
                if not check[next_node]:
                    bfs.append(next_node)
                    check[next_node] = 1
        count += 1
print(count)