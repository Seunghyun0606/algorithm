# knapSack algo, 여기엔 분할가능 or 0-1 knapSack이 있는데, 이 문제는 0-1
# 즉, 넣냐 마냐의 문제

n, k = map(int, input().split())

wanted_stuff = [[0, 0]] + [ list(map(int, input().split())) for _ in range(n) ]

dp = [ [ 0 for _ in range(k + 1) ] for _ in range(n + 1) ]

for i in range(1, n+1):
    for possible_weight in range(1, k+1):
        now_weight = wanted_stuff[i][0]
        now_value = wanted_stuff[i][1]

        if possible_weight < now_weight:
            dp[i][possible_weight] = dp[i-1][possible_weight]
        else:
            dp[i][possible_weight] = max(now_value + dp[i-1][possible_weight - now_weight], dp[i-1][possible_weight] )

print(dp[n][k])

# 다른 사람 풀이. 불필요한 메모이제이션을 하지 않는다.
# ver 3: dp by list - 기존 방식보다 4배정도 빠르다.

N, K = map(int, input().split())
stuffs = [(map(int, input().split())) for _ in range(N)]
dp = [0] * (K+1)
dp[0] = 1
for w, v in stuffs:
    for i in range(K-w, -1, -1):
        if dp[i]:
            dp[i+w] = max(dp[i+w], dp[i]+v)

print(max(dp)-1)

# 다른 사람 풀이. 불필요한 메모이제이션을 하지 않는다. ( dictionary 이용 )
# ver 2 메모리를 더먹지만 더 빠르다.
N, K = map(int, input().split())
stuffs = [(map(int, input().split())) for _ in range(N)]
dp = {0: 0}
for w, v in stuffs:
    temp_dp = {}
    for key, value in dp.items():
        temp_dp[key + w] = value + v

    for key, value in temp_dp.items():
        if key > K:
            continue

        dp[key] = max(dp.get(key, 0), value)

print(max(dp.values()))
