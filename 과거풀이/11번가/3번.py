# 이풀이는안됨, 반례가있음
# 2, 2, 2, 2 가 대표적 사례


def solution(A):

    n = len(A)
    number = sum(A)

    check_number = n*(n+1)//2

    result = abs(check_number - number)

    if result > 10**9:
        return -1

    return result
