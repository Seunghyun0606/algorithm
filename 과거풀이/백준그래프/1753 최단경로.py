# 1. 갈수있는 경로와 값을 저장하는 리스트
# 2. DFS로 끝까지 갔을 경우,

import sys
sys.setrecursionlimit(100000000)

V, E = map(int, input().split())
start = int(input())

where_you_go = [ [] for _ in range(V+1) ]

def find_min(start, end, weight):
    global result
    for v, w in where_you_go[start]:
        if result < weight + w:
            return

        if v == end:
            if result > weight + w:
                result = weight + w
            return
        find_min(v, end, weight + w)

for _ in range(E):
    u, v, w = map(int, input().split())
    where_you_go[u].append([v, w])

for i in range(1, V+1):
    result = float('inf')

    if i == start:
        print(0)
    else:
        find_min(start, i, 0)
        print(result) if float(result).is_integer() else print('INF')
