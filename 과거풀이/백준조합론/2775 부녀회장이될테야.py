def my_calc(depth, prev):
    next = [0]*(n+1)
    if depth == k:
        print(prev[n])
    else:
        for i in range(1, n+1):
            next[i] = prev[i] + next[i-1]
        my_calc(depth+1, next)

T = int(input())

for _ in range(T):
    k = int(input())  # 높이
    n = int(input())  # 너비 i호에는 i명이 산다

    zero = [ i for i in range(n+1) ]

    my_calc(0, zero)
