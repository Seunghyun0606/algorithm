import sys
input = sys.stdin.readline

#  6 12 18 24
# 1 7 19 37 61

num = int(input())
n = 1
total = 1
while total < num:
    total = 6*((n*(n-1))/2) + 1
    n += 1

if num == 1:
    print(1)
else:
    print(n-1)


# 좀 더 프로그래밍적인 관점, 위에는 수학적인 관점
# n = int(input())
# sum = 1
# for i in range(0, n):
#     if n == 1:
#         print(n)

#     else:
#         sum += i*6
#         if n <= sum:
#             print(i+1)
#             break