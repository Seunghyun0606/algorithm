from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())
arr = [-1]*10001
coins = []
Q = deque()
for i in range(n):
    tmp = int(input())
    if tmp<=10000 and arr[tmp] == -1:
        arr[tmp] = 1
        coins.append(tmp)
        Q.append(tmp)

while Q:
    x = Q.popleft()
    for i in range(len(coins)):
        if x+coins[i] <= 10000 and arr[x+coins[i]] == -1:
            arr[x+coins[i]] = arr[x] + 1
            Q.append(x+coins[i])

print(arr[k])