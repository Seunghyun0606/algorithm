# 5185.[파이썬 S/W 문제해결구현] 1일차 - 이진수 D2
# 1. 내장함수사용
# 2. dic로 ABCDEF 값 넣어서 구한다.
# 3. ord로 0~9, A~F 의 아스키코드 값 구해서 해도된다.

T = int(input())

for tc in range(T):

    n, number = input().split()
    number = int('0x' + number, 16)  # 10진수로 바꿈
    binary = format(number, 'b')  # 2진수로 바꿈, str임

    for _ in range(int(n)*4 - len(binary)):
        binary = '0' + binary

    print('#{}'.format(tc+1), binary)

# print(format(0x47F4, 'b'))
# a = 0x47F4
# b = int('0x'+'47F4', 16)
# print(ord('1'))
# print(bin(4))
# print(type(format(b, 'b')))