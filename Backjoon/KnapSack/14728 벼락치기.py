# 배낭 문제랑 똑같다.
# 총 시간을 기준으로 메모이제이션

n, t = map(int, input().split())

studies = [ list(map(int, input().split())) for _ in range(n) ]

dp = [0] * ( t + 1 )
dp[0] = 1

for i in range(n):

    for j in range( len(dp) - studies[i][0] - 1, -1, -1):
        
        if dp[j]:
            dp[j + studies[i][0] ] = max(dp[j] + studies[i][1], dp[j + studies[i][0]])
    
print(max(dp) - 1)