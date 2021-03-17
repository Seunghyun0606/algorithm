# 자연수 A를 B번 곱한 수를 C로 나눈 나머지
# pow에 대해서 알아보던 중 pow( A, B, C ) 이렇게 3개의 변수를 pow에 넣어주면
# A를 B번 제곱한 값을 C로 나눈 나머지를 반환해 준다. pow(A, B, C)
# 하지만 이 문제의 의도는 분할정복이므로, 분할정복으로 풀어본다.

# b의 값이 짝수인지 홀수인지 파악
# b의 값이 짝수라면 10**12 -> (10**6)**2 형태로 변환
# b의 값이 홀수라면 10**11 -> (10**5)**2*10 형태로 변환

A, B, C = map(int, input().split())

def power(a, b):
    if b == 1:
        return a % C
    else:
        temp_b = power(a, b // 2)
        if b % 2:
            return ( temp_b ** 2 ) * a % C  # 홀수인 경우
        else:
            return ( temp_b ** 2 ) % C  # 짝수인 경우

print(power(A, B))