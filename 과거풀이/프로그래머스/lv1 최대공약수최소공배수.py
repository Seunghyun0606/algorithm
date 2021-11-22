# https://brownbears.tistory.com/454
# 최대공약수, 최소공배수 개념 체크하기.
# 유클리드호제법. 계속 큰수를 작은수로 나누고 큰수 = 작은수, 작은수 = 큰수 % 작은수

def solution(n, m):  # n > m 이란 가정
    answer = []
    a, b = n, m
    if n < m:
        n, m = m, n
    
    while m:
        n, m = m, n % m  # 최대공약수
    answer.append(n)
    answer.append(a*b // n)  # 최소공배수
    

    return answer