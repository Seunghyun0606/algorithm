# 1486. 장훈이의 높은 선반
# 값을 변수로 넣어서 가져가면서 더해나가자

import sys
sys.stdin = open('input.txt', 'r')

def shelve(start, h_sum):
    global h_min, flag

    if flag:
        visit[start] = 1

        if h_sum > h_min:
            return

        if h_sum == h:
            flag = False
            h_min = h
            return

        if h_sum > h:
            if h_min > h_sum:
                h_min = h_sum

        else:
            for i in range(1, n+1):
                if visit[i]:
                    continue
                shelve(i, h_sum + heights[i])
                visit[i] = 0




T = int(input())

for tc in range(T):

    n, h = map(int, input().split())

    heights = [0] + list(map(int, input().split()))
    visit = [0] * (n+1)

    flag = True
    h_min = 20 * 10 ** 4

    shelve(0, 0)

    print('#{}'.format(tc+1), h_min-h)