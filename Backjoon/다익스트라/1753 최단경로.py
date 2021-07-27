# 다익스트라, 기본 풀이, 이러면 메모리초과 뜬다.

v, e = map(int, input().split())
k = int(input())

adj_matrix = [ [float('INF')]*v for _ in range(v) ]

for _ in range(e):
    u, v, w = map(int, input().split())
    adj_matrix[u-1][v-1] = w
    # adj_matrix[v][u] = w  # 양방향일 경우

# 자기 자신의 간선은 0
for i in range(v):
    adj_matrix[i][i] = 0

# visit
visit = [0]*v
visit[k-1] = 1  # 시작점 k = 1 ( 인덱스 0 )

# distance
distance = adj_matrix[k-1]

# 미방문, 최소 거리
def getSmallNode():
    min_value = float('inf')
    index = 0

    for i in range(v):
        if not visit[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

# 다익스트라

for i in range(v-2):
    current = getSmallNode()
    visit[current] = 1

    for j in range(v):
        if not visit[j]:
            distance[j] = min(distance[j], distance[current] + adj_matrix[current][j] )

print(*distance, sep="\n")