# 배낭문제, 다만, 여러개 물품을 넣을 수 있다.

import sys
input = sys.stdin.readline

def get_param(num):
    # candy, price = map(float, input().split())
    # candy = int(candy)
    # price = int(price*100 + 0.5)
    # return [candy, price]
    return int(num.replace('.', '')) 

while True:
    # n, money = get_param()
    n, money = map(get_param, input().split())

    if n:
        # candies = [ get_param() for _ in range(n) ]
        candies = [ list(map(get_param, input().split())) for _ in range(n) ]
        
        dp = [0] * ( money + 1 )

        # 여기서 인덱스로 찾는거보다, candies에서 꺼내서 찾는게 훨씬 빠르다.
        # 2중 리스트다보니 내부적으로 찾는데 시간이 걸리나 보다.
        # index로 찾으면 2436 //  꺼내서 찾으면 880 으로 3배정도 차이난다.

        # for i in range(n):

        #     for j in range(candies[i][1], money + 1):
        #         dp[j] = max(dp[j - candies[i][1]] + candies[i][0], dp[j])
        for candy, price in candies:

            for j in range(price, money + 1):
                dp[j] = max(dp[j - price] + candy, dp[j])

        print(max(dp))
    else:
        break
