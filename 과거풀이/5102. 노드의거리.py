# 5102. 노드의거리

from collections import deque


T = int(input())

for tc in range(T):

    vertex, edge = map(int, input().split())

    nodes = [ [] for _ in range(vertex+1) ]
    check = [0]*(vertex+1)

    for i in range(edge):
        start, last = map(int, input().split())
        nodes[start].append(last)
        nodes[last].append(start)

    start, last = map(int, input().split())

    que = deque()
    que.append([start, 0])
    while que:

        temp, cnt = que.popleft()

        if temp == last:
            print('#{}'.format(tc + 1), cnt)
            break

        for i in nodes[temp]:
            if check[i]:
                continue
            que.append([i, cnt+1])
            check[i] = 1
    else:
        print('#{}'.format(tc + 1), 0)


