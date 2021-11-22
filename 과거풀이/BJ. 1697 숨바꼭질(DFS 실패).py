# BJ. 1697 숨바꼭질 DFS론 안됨

import sys
sys.setrecursionlimit(100000000)

def hide(subin, sister, t):
    if subin == sister:
        if t < min_t:
            min_t = t
    else:
        if sister > subin*2:
            subin *= 2
        elif abs((subin-1)*2 - sister) > abs((subin+1)*2 - sister):
            subin += 1
        else:
            subin -= 1
        hide(subin, sister, t + 1)


places = list(map(int, input().split()))
min_t = 10**10

hide(places[0], places[1], 0)
print(min_t)


