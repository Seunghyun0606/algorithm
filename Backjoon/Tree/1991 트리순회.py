# 전위 순회, 중위 순회, 후위 순회 모두 재귀로 푼다.
n = int(input())

# 전처리
binary_tree = [ [False for _ in range(2)] for _ in range(n) ]
for _ in range(n):
    middle, left, right = map(lambda x: ord(x) - 65, input().split())
    binary_tree[middle][0] = left
    binary_tree[middle][1] = right

# 전위 순회 (루트, 왼쪽, 오른쪽)
preorder_result = []
def preorder(start_node):
    preorder_result.append(chr(start_node + 65))
    for i in range(2):
        if binary_tree[start_node][i] >= 0:
            preorder(binary_tree[start_node][i])

# 중위 순회 (왼쪽, 루트, 오른쪽)
inorder_result = []
def inorder(start_node):
    for i in range(2):
        if i == 1:
            inorder_result.append(chr( start_node + 65 ))
        if binary_tree[start_node][i] >= 0:
            inorder(binary_tree[start_node][i])

# 후위 순회 (왼쪽, 오른쪽, 루트)
postorder_result = []
def postorder(start_node):
    for i in range(2):
        if binary_tree[start_node][i] >= 0:
            postorder(binary_tree[start_node][i])
    postorder_result.append(chr(start_node + 65))


preorder(0)
inorder(0)
postorder(0)

print(''.join(preorder_result))
print(''.join(inorder_result))
print(''.join(postorder_result))
