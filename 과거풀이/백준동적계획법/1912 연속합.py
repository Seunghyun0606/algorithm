# 종만북에 나오는 dpFastestMaxSum 활용하면 될듯하다.

n = int(input())
nums = list(map(int, input().split()))
result = float('-inf')
psum = 0
for i in range(n):
    psum = max(psum, 0) + nums[i]
    result = max(result, psum)
print(result)


# 다른사람 풀이 1
# arr_size = int(input())
# arr = list(map(int, input().split()))
# dp = arr

# for i in range(1, arr_size):
#     if dp[i - 1] > 0:
#         dp[i] += dp[i - 1]

# print(max(dp))

# 다른사람 풀이 2
# import sys

# n = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split(" ")))

# for i in range(1, len(numbers)):
#     if numbers[i] + numbers[i-1] > numbers[i]:
#         numbers[i] += numbers[i-1]

# print(max(numbers))