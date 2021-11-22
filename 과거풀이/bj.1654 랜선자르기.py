# 이분탐색, 2^31 -1 이 최대니깐, n으로 잡고, 이 n을 찾아가면됨

import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lines = [ int(input()) for _ in range(K) ]

right = 2**31 - 1
left = 1
real_result = 0
while left <= right:
    n = ( right + left ) // 2
    result = 0
    for line in lines:
        result += line // n
    
    if result >= N:
        real_result = max(n, real_result)
        left = n + 1
    else:
        right = n - 1
print(real_result)
