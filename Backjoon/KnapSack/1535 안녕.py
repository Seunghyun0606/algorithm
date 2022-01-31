# 배낭문제, 체력이 담을 수 있는 최대 무게, 기쁨이 최대 가치
# 체력이 100이상 소진되면 죽어서 기쁨을 얻을 수 없다.

n = int(input())

lose_healthy = list(map(int, input().split()))
get_happiness = list(map(int, input().split()))

dp = [0] * 101
dp[0] = 1

for i in range(n):
    lose, happiness = lose_healthy[i], get_happiness[i]

    if 100 > lose:
        for j in range(99 - lose, -1, -1):
            if dp[j]:
                dp[j + lose] = max( dp[j + lose], happiness + dp[j] )
        
print(max(dp) - 1)

