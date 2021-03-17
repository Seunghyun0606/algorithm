# 무조건 DFS로 풀어야한다. BFS로 풀면, 최대깊이에서의 최대 값을 못구한다.
# 아니다, BFS로도 트리의 지름을 구하는 개념을 알면 가능하다.

# 노드에 가는 값과 가중치를 넣어주며 하나씩 꺼내서 max값을 알아내야한다.

# 이 문제의 핵심은, 트리의 지름을 구하는 개념을 아느냐 였다.
# 임의의 한 노드부터 최대 거리를 가지는 노드를 구한 뒤,
# 그 노드로 부터 최대 거리를 가지는 노드가 트리의 지름에 해당된다.
# 나의 경우, 1이 항상 최상단 노드라고 생각해서 틀렸었고,
# farest_node를 추가해서 답을 구했다.

# input을 readline으로 안하면 5500ms, 하면 900ms
import sys
input = sys.stdin.readline

n = int(input())

tree = [ [] for _ in range(n+1) ]
check = [0]*(n+1)
max_weight = 0
farest_node = 0

for _ in range(n):
    temp_input = list(map(int, input().split()))

    for i in range(1, len(temp_input) - 2, 2):
        # 어차피 중복되는 값이 있으니, 양 쪽 노드 모두에 집어넣을 필요 없다.
        tree[temp_input[0]].append([temp_input[i], temp_input[i+1]])

def DFS(start_node, init_weight):
    global max_weight, farest_node
    check[start_node] = 1
    for end_node, weight in tree[start_node]:
        if not check[end_node]:
            total_weight = init_weight + weight
            if total_weight > max_weight:
                max_weight = total_weight
                farest_node = end_node
            DFS(end_node, total_weight)
    check[start_node] = 0


DFS(1, 0)
DFS(farest_node, 0)
print(max_weight)

# 8
# 1 2 1 -1
# 2 1 1 3 1 -1
# 3 2 1 4 1 -1
# 4 3 1 5 1 8 2 -1
# 5 4 1 6 1 -1
# 6 5 1 7 1 -1
# 7 6 1 -1
# 8 4 2 -1