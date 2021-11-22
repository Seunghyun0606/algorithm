# BJ.2294 동전2

import sys
sys.setrecursionlimit(10**6)

def dp(coin1, j):
    if j > k:
        return
    else:
        dp_value[j] = min(dp_value[j], dp_value[j-coin1] + 1)
        dp(coin1, j+1)


n, k = map(int, input().split())

coins = set()

for i in range(n):
    coins.add(int(input()))

coins = sorted(list(coins))

dp_value = [0] + [10001] * k

for coin in coins:
    dp(coin, coin)

if dp_value[k] == 10001:
    print(-1)
else:
    print(dp_value[k])

# print(dp_value)
