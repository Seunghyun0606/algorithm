# 배낭문제랑은 다르다.

T = int(input())

for _ in range(T):
    n = int(input())
    coin_list = list(map(int, input().split()))

    result_amount = int(input())

    dp = [0] * (result_amount + 1)
    dp[0] = 1

    for coin in coin_list:

        for i in range(coin, result_amount + 1):
            dp[i] += dp[i - coin]

    print(dp[-1])

