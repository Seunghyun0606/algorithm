# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# Invalid : 가장 긴변의 길이보다 나머지 두변의 길이의 합이 더 길어야한다.

# pool = ['A', 'B', 'C']
# print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
# print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

import sys
import itertools
input = sys.stdin.readline

def calc(num):
    a, b = num
    return 1 if a==b else 0

# 각 변은 양의 정수가 입력됨

while True:
    abc = list(map(int, input().split()))
    if sum(abc) == 0:
        break
    abc.sort()
    a,b,c = abc
    if a+b <= c:
        print("Invalid")
        continue
    comb = list(map(calc, itertools.combinations(abc,2)))
    result = sum(comb)
    if result == 3:
        print("Equilateral")
    elif result == 0:
        print("Scalene")
    else:
        print("Isosceles")
