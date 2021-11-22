# 6485. 삼성시의 버스 노선
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):

    n = int(input())
    routes = []

    for i in range(n):
        routes.append(list(map(int, input().split())))

    p = int(input())
    stops = []

    for i in range(p):
        stops.append(int(input()))

    results = [0] * p
    
    for i in range(n):
        for k in range(p):
            if routes[i][1]+1 > stops[k] >= routes[i][0]:
                results[k] += 1

    print('#{}'.format(tc+1), *results)


