# 14728 벼락치기랑 문제가 같음 // 배낭문제
max_time, k = map(int, input().split())

# 중요도, 필요한 공부시간
studies = [ list(map(int, input().split())) for _ in range(k) ]

# 최대 시간 한계 초과 X
dp_time = [0] * (max_time + 1)
dp_time[0] = 1

for score, time in studies:

    for t in range( max_time - time, -1, -1):
        if dp_time[t]:
            dp_time[t + time] = max( dp_time[t + time], dp_time[t] + score )
print(max(dp_time) - 1)

