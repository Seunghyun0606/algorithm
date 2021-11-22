# 9/1 12/3 15/6 18/10
# 3   4    5    6
# 2, 3 ,4 등차수열 만들어버리자 그냥

n = int(input())
DP = [0, 1, 1, 1]  # 3의 몫일때 인덱스 값 = 분해방법갯수
# 1000개 배열.
for i in range(2, 1001):
    DP.append(DP[-1] + i)
print(DP[n//3])

# n = int(input())
# n = n // 3 - 2
# answer = 0
# for i in range(1, n + 1):
#     answer += i
# print(answer)

# x = int(input()) // 3 - 1
# print(x * (x-1) // 2)