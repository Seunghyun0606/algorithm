# 새로운 메모리를 적재할 때, 들어가는 비용 최소화
# 꺼야하는 메모리의 양에서 최소 비용 == 새로키는 메모리의 양에서 최소 비용

n, m = map(int, input().split())

memories = list(map(int, input().split()))

costs = list(map(int, input().split()))

dp = [0] * ( sum(costs) + 1 )
dp[0] = 1
result = float('inf')
for i in range(n):
    memory = memories[i]
    cost = costs[i]

    for j in range(len(dp) - cost - 1, -1, -1):
        if dp[j]:
            dp[j + cost] = max(dp[j + cost], dp[j] + memory)
            if dp[j + cost] -1 >= m:
                result = min(j + cost, result)
print(result)