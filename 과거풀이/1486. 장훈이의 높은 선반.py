# 1486. 장훈이의 높은 선반
# 값을 변수로 넣어서 가져가면서 더해나가자

import sys
sys.stdin =open('input.txt', 'r')


def shelve(start, idx, h_sum):
    global h_min, flag

    if flag:

        if start == n:
            if h_min > h_sum > h:
                h_min = h_sum
            elif h_sum == h:
                flag = False
                h_min = h
            return
        if h_sum > h_min:
            return
        if h_sum == h:
            flag = False
            h_min = h
            return
        if h_sum > h:
            if h_min > h_sum:
                h_min = h_sum
                return

        else:
            # for i in range(idx, n):
            #     shelve(start+1, i+1, h_sum + heights[i+1])

            # 매개벼수를 더잡아먹어서 그런지모르겠지만 for가 더 느리다. 305ms vs 185 ms
            # 아래는 010101 트리의 부분 집합을 만들기위한 로직

            # shelve(start+1, h_sum + heights[start+1])
            # shelve(start+1, h_sum)




T = int(input())

for tc in range(T):

    n, h = map(int, input().split())

    heights = [0] + list(map(int, input().split()))
    visit = [0] * (n+1)

    flag = True
    h_min = 20 * 10 ** 4

    shelve(0, 0, 0)

    print('#{}'.format(tc+1), h_min - h)