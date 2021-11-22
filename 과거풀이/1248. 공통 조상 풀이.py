# 1248 공통조상 풀이

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_LCA(root, p, q):
    if root in (p, q, None):
        return root
    left = find_LCA(root.left, p, q)
    right = find_LCA(root.right, p, q)
    return root if (left and right) else (left or right)


def count_children(root):
    if root:
        left = count_children(root.left)
        right = count_children(root.right)
        return 1 + left + right
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E, P, Q = map(int, input().split())
    nodes = [Node(x) for x in range(V+1)]
    edges = list(map(int, input().split()))
    for i in range(0, 2*E, 2):
        parent = nodes[edges[i]]
        child = nodes[edges[i+1]]
        if not parent.left:
            parent.left = child
        else:
            parent.right = child
    lca = find_LCA(nodes[1], nodes[P], nodes[Q])
    count = count_children(lca)
    print('#{} {} {}'.format(tc, lca.val, count))