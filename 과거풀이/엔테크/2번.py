# 피보나치

def solution(N):
    answer = 0

    check = [0] + [1] + [2] + [0]*43

    for i in range(1, 44):
        check[i+2] = check[i+1] + check[i]

    answer = check[N]
    return answer
