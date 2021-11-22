# 5189. 전자카트

def dfs(depth, sub_sum):

    if depth == n-1:
        global result
        temp = 0
        sub_sum.append(0)
        for j in range(n):
            temp += carts[sub_sum[j]][sub_sum[j+1]]
        result = min(result, temp)
        sub_sum.pop()
        return

    else:
        for i in range(1, n):
            if check[i]:
                continue
            check[i] = 1
            sub_sum.append(i)
            dfs(depth+1, sub_sum)
            check[i] = 0
            sub_sum.pop()


T = int(input())

for tc in range(T):
    n = int(input())

    carts = [ list(map(int, input().split())) for _ in range(n)]
    result = 2 << 15
    check = [0] * n
    dfs(0, [0])
    print('#{}'.format(tc+1), result)

