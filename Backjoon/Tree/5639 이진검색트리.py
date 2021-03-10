# 전위순회 결과로 후위순회 알아내기
# 전위순회 결과를 바탕으로 본 노드의 간선을 꾸며내자.

# 이런식으로 풀면안된다. 이진 검색 트리의 개념을 이용해서 풀어야한다.
nodes = []
try:
    while True:
        num = int(input())
        nodes.append(num)
except:
    pass

counted_nodes = len(nodes)
check_node = [1]*counted_nodes
edges = [ [0, 0] for _ in range(counted_nodes)]

def preorder(start_node):
    try:
        for i in range(start_node + 1, counted_nodes):
            if check_node[i]:
                if nodes[start_node] > nodes[i]:
                    edges[start_node][0] = i
                    check_node[i] = 0
                    preorder(i)
                else:
                    edges[start_node][1] = i
                    check_node[i] = 0

    except:
        return

preorder(0)
print(check_node)
print(edges)