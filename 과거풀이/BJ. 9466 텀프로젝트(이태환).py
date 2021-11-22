from collections import deque


def bfs(s_x):
    Q = deque()
    x = s_x
    Q.append(x)
    step = 1
    ans = 0
    while True:

        if not check_arr[x] and not dis_arr[x]:
            dis_arr[x] = step
        elif not check_arr[x] and dis_arr[x]:
            ans = step-dis_arr[x]
            break
        elif check_arr[x]:
            ans = 0
            break
        Q.append(x)
        step += 1
        x = arr[x]

    for i in range(len(Q)):
        check_arr[Q[i]] = True
    return ans


T = int(input())
for t in range(T):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    check_arr = [False]*(n+1)
    dis_arr = [0]*(n+1)
    result = n
    for i in range(1, 1+n):
        if not check_arr[i]:
            result -= bfs(i)
    print(result)