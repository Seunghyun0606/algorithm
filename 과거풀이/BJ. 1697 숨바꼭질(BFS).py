# BJ. 1697 숨바꼭질(BFS)
# 걸으면 x +- 1
# 순간이동하면 2*x
from collections import deque

def hide():

    check = [0] * (k*2)
    que = deque()
    que.append([n, 0])

    if n >= k:
        print(n - k)
        return

    else:
        while que:
            x, time = que.popleft()
            my_num = [x - 1, x + 1, x * 2]

            for i in my_num:
                if i == k:
                    print(time + 1)
                    return

                else:
                    if -1 < i < k*2 - 1 and check[i] == 0:
                        que.append([i, time + 1])
                        check[i] = 1


n, k = map(int, input().split())
hide()
