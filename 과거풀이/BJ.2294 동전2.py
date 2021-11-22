# BJ.2294 동전2


n, k = map(int, input().split())

coins = set()

for i in range(n):
    coins.add(int(input()))

coins = sorted(list(coins))

dp_value = [0] + [10001] * k

for coin in coins:
    for j in range(coin, k+1):
        dp_value[j] = min(dp_value[j], dp_value[j - coin] + 1)

if dp_value[k] == 10001:
    print(-1)
else:
    print(dp_value[k])
