# 이분탐색, 시간 초과, 최적화하면 풀수있으나, 느림.
# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     n = int(input())
#     num1 = list(map(int, input().split()))
#     m = int(input())
#     num2 = list(map(int, input().split()))

#     num1.sort()

#     for num in num2:
#         left, right = 0, n - 1
#         while right >= left:
#             mid = ( right + left ) // 2
            
#             if num1[mid] > num:
#                 right = mid -1
#             elif num1[mid] == num:
#                 print(1)
#                 break
#             else:
#                 left = mid + 1
#         else:
#             print(0)

import sys
from collections import defaultdict
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    num1 = set(map(int, input().split()))
    m = int(input())
    num2 = list(map(int, input().split()))

    my_dict1 = defaultdict(int)
    for i in num1:
        my_dict1[i] = 1
    for j in num2:
        print(1) if my_dict1[j] else print(0)