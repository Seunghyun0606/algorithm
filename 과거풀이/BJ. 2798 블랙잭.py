# BJ. 2798 블랙잭
# 3장

def blackjack(depth, idx, my_sum):
    global flag, my_num
    if flag:
        check[idx] = 1
        if my_sum > m:
            return

        if depth == 3:
            # for i in range(1, n+1):
            #     if check[i]:
            #         print(cards[i], end='')
            # print()
            if my_sum == m:
                my_num = m
                flag = False
                return

            if my_sum > my_num:
                my_num = my_sum
            return

        else:
            a = []
            for i in range(idx+1, n+1):
                if check[i]:
                    continue
                if cards[i] in a:
                    continue
                a.append(cards[i])

                blackjack(depth+1, i, my_sum + cards[i])
                check[i] = 0

n, m = map(int, input().split())
cards = [0] + list(map(int, input().split()))

my_num = 0
check = [0] * (n+1)
flag = True

blackjack(0, 0, 0)

print(my_num)

