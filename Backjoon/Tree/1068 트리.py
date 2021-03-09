# 제거한 노드 이하는 모두 없앤다.

n = int(input())

tree = [ [] for _ in range(n) ]

# 해당 노드 리스트는 부모리스트이기 때문에 해당 노드에 존재하지 않으면
# leaf node가 된다.
node_parent = list(map(int, input().split()))

deleted_node_number = int(input())

# node 하위의 연결된 node들을 모두 지워버려야한다.
def delete_node(start_delete_node):
    node_parent[start_delete_node] = -2
    for i in range(len(node_parent)):
        if node_parent[i] == start_delete_node:
            delete_node(i)

delete_node(deleted_node_number)

result = 0
# 삭제된 노드가 아니고, parent node가 아니면 leaf node 이다.
for i in range(len(node_parent)):
    if node_parent[i] != -2 and i not in node_parent:
        result += 1

print(result)