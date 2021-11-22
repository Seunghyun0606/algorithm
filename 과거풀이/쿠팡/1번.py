# 진법구하는 로직, 자릿수 곱이 최대가 되는 k 진법, 그때의 자릿수 곱을 구해야함.


def solution(N):
    answer = []
    k = 2
    ans = 1
    for i in range(3, 10):  # 2진법은 어차피 자릿수 곱 최대가 1
        n = N
        result = 1
        while n > 1:
            temp = n % i
            n = n // i
            if temp:
                result *= temp
        if result >= ans:
            ans = result
            k = i
    answer.append(k)
    answer.append(ans)

    return answer