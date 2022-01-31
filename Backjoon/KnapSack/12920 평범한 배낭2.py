# 배낭 문제, 0-1, 중복가능( 갯수 한정 ), 최대 만족도

import sys
input = sys.stdin.readline

# 물건 종류 수, 가방 최대무게
n, m = map(int, input().split())

# 물건 무게, 만족도, 물건 개수
stuffs = [ list(map(int, input().split())) for _ in range(n) ]

# 가방 무게를 기준으로 만족도 dp
dp_weight = [0] * ( m + 1 )

# 개수별로 2의 승수의 합 개념이용.
# 예를 들어, 7은 1, 2, 4의 합
# 이진수로 7을 만들 수 있고, 그에 따라 각 승수별로 DP를 만들 수 있다.

for t_weight, t_satisfaction, k in stuffs:
    i = 0

    while k:
        temp = min(k, 1 << i)
        weight = temp * t_weight
        satisfaction = temp * t_satisfaction

        for w in range(m - weight, -1, -1):
            dp_weight[w + weight] = max( dp_weight[w] + satisfaction, dp_weight[w + weight] )

        k -= temp
        i += 1

print(max(dp_weight))