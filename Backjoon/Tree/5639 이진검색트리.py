# 전위순회 결과로 후위순회 알아내기
# 전위순회 결과를 바탕으로 본 노드의 간선을 꾸며내자.

# 이런식으로 풀면안된다. 이진 검색 트리의 개념을 이용해서 풀어야한다.
# nodes = []
# try:
#     while True:
#         num = int(input())
#         nodes.append(num)
# except:
#     pass

# counted_nodes = len(nodes)
# check_node = [1]*counted_nodes
# edges = [ [0, 0] for _ in range(counted_nodes)]

# def preorder(start_node):
#     try:
#         for i in range(start_node + 1, counted_nodes):
#             if check_node[i]:
#                 if nodes[start_node] > nodes[i]:
#                     edges[start_node][0] = i
#                     check_node[i] = 0
#                     preorder(i)
#                 else:
#                     edges[start_node][1] = i
#                     check_node[i] = 0

#     except:
#         return

# preorder(0)
# print(check_node)
# print(edges)


# 전위 순회는 항상 맨 앞이 루트고, 후위 순회는 항상 맨 뒤가 루트이다.
# 이 문제의 경우, 루트의 왼쪽은 항상 작고, 오른쪽은 항상 크기 때문에 이진 탐색 로직을 사용해야한다.

import sys

sys.setrecursionlimit(10**9)

preorder = []

try:
    while True:
        temp = int(input())
        preorder.append(temp)
except:
    pass

def postorder(start, end):
    
    if start > end:
        return
    division_index = end + 1
    for i in range(start + 1, end + 1):
        if preorder[start] < preorder[i]:
            division_index = i
            break
    postorder(start+1, division_index - 1)
    postorder(division_index, end)

    print(preorder[start])


postorder(0, len(preorder) - 1)

