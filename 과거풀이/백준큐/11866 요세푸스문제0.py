from collections import deque
n, k = map(int, input().split())

nums = [ i for i in range(1, n+1)]

que = deque(nums)
result = []
while que:
    for _ in range(k-1):
        que.append(que.popleft())
    result.append(que.popleft())
print('<', end='')
print(*result, sep=', ', end='>')

# 수학적으로 풀기
# N, K = map(int, input().split())
# l = list(range(1, N+1))
# p = list()
# i = 0
# while l:
#     i = (i+K-1) % len(l)
#     p.append(str(l.pop(i)))

# print('<'+', '.join(p)+'>')

# n, k = map(int, input().split())
# lst = list()
# ans = list()
# for i in range(1, n + 1):
#   lst.append(int(i))

# idx = k - 1
# while True:
#   ans.append(lst[idx])
#   del lst[idx]
#   if not lst:
#     break
#   idx = (idx + k - 1) % len(lst)

# print ('<', end = '')
# for i in range(0, len(ans)):
#   if i == len(ans) - 1:
#     print(ans[i], end = '')
#   else:
#     print("%d, "%ans[i], end = '')
# print ('>')

# n, k = map(int, input().split())
# q = [i for i in range(1, n+1)]
# ans = []
# temp = k-1

# for i in range(n):
#     if len(q) > temp: #위치가 리스트를 넘지 않으면
#         ans.append(q.pop(temp))
#     else: #위치가 리스트를 넘으면
#         temp %= len(q)
#         ans.append(q.pop(temp))
#     temp += (k-1)
    
# print('<', end = '')
# for i in range(n):
#     if i == n-1: print(ans[-1], end = '')
#     else: print(str(ans[i])+ ', ', end = '')
# print('>', end = '')