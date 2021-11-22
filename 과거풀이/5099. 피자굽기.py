# 5099. 피자굽기

import queue as Q

T = int(input())

for tc in range(T):

    n, k = map(int, input().split())

    cheese = list(map(int, input().split()))

    que = Q.Queue()

    i = 0
    while i < n:
        que.put([i, cheese[i]])
        i += 1

    while que.qsize() != 1 :

        j, temp = que.get()
        temp = temp//2
        if temp:
            que.put([j, temp])
        else:
            if i < k:
                que.put([i, cheese[i]])
                i += 1

    print('#{}'.format(tc+1), que.get()[0] + 1)







