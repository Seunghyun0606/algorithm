# 5097. 회전, BFS 기초

import queue as q

T = int(input())

for tc in range(T):

    n, k = map(int, input().split())

    num_list = list(map(int, input().split()))
    my_q = q.Queue()

    for i in range(n):
        my_q.put(num_list[i])

    for i in range(k):
        my_q.put(my_q.get())

    print('#{}'.format(tc+1), my_q.get())



