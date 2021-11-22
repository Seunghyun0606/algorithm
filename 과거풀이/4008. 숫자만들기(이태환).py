import sys
sys.stdin = open('input.txt', 'r')

def dfs(depth):
    if depth == m:
        tmp = arr_num[0]
        for i in range(m):
            if arr_dfs[i] == 0:
                tmp = tmp+arr_num[i+1]
            elif arr_dfs[i] == 1:
                tmp = tmp-arr_num[i+1]
            elif arr_dfs[i] == 2:
                tmp = tmp*arr_num[i+1]
            elif arr_dfs[i] == 3:
                if tmp<0:
                    tmp *= -1
                    tmp = tmp//arr_num[i+1]
                    tmp *= -1
                else:
                    tmp = tmp//arr_num[i+1]
        global val_max, val_min
        # print(tmp)
        if tmp<val_min:
            val_min = tmp
        if tmp>val_max:
            val_max = tmp
        return

    for i in range(4):
        if arr_operator[i]:
            arr_operator[i] -= 1
            arr_dfs[depth] = i
            dfs(depth+1)
            arr_operator[i] += 1


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr_operator = list(map(int, input().split()))
    arr_num = list(map(int, input().split()))
    m = n-1
    arr_dfs = [0]*m
    val_max = -100000000
    val_min = 100000000

    dfs(0)
    print('#{} {}'.format(t, val_max-val_min))