# BJ. 1965 상자넣기(LCS)
# dp 배열을 만들고, boxes[i] 일때보다 작은 수의 갯수를 세서 dp[i]에 넣는것.
# dp 는 기본적으로 1로 시작(왜냐면 자기자신을 포함해야하니깐)
# 주의해야할점은, i 보다 작은 dp[:i]의 값중 제일 큰 값을 dp[i]에 더해넣는것이란 점 기억.

n = int(input())

boxes = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if boxes[i] > boxes[j] and dp[i] < dp[j] + 1:
            # i번째 있는 수보다 작은 값이면서 쌓여진 상자가 제일 많은 것을 골라야한다.
            # 그러니깐 계속 dp[i] 값은 i번째 있는 수보다 작을 값이면서 상자의 갯수를 보면서 업데이트 되는 셈이지.
            # 마지막에는 제일 많이 쌓여진 상자를 더하게 될 것이다.
            dp[i] = dp[j] + 1
print(max(dp))

