# stack 문제, 맨뒤에서부터 인덱스체크, 자기보다 낮으면 넘어가고, 높거나 같으면 거기서 멈춘다.
# 맨뒤에서부터하면 10**10 이라서 시간초과가뜬다.
# 따라서 앞에서부터 탐색해야한다.

n = int(input())
towers = list(map(int, input().split()))
stack = []
result = []

for i in range(n):
    while stack:
        if stack[-1][1] >= towers[i]:
            result.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    stack.append((i, towers[i]))
print(*result)

# 시간초과 코드
# n = int(input())
# towers = list(map(int, input().split()))
# check = [0]*n
# for i in range(n-1, 0, -1):
#     k = i-1

#     while k > -1:
#         if towers[k] >= towers[i]:
#             check[i] = k + 1
#             break
#         k -= 1
# print(*check)

