# 4008. 숫자만들기(모의테스트)
# + - * / 순서
import sys
sys.stdin = open('input.txt', 'r')

def operator(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    else:
        if num1 < 0:
            num1 *= -1
            return (num1 // num2) * (-1)
        return num1 // num2


def calculator(start, li):  # x = 0, cnt = 0, num은 첫 숫자
    global num_max, num_min

    visit[start] = 1
    if len(li) == n-1:
        num = nums[0]
        for i in range(n-1):
            num = operator(num, nums[i+1], li[i])

        if num > num_max:
            num_max = num
        if num_min > num:
            num_min = num

    else:
        x = ''
        for i in range(1, n):
            if visit[i]:
                continue
            if x == using_calc[i]:
                continue
            x = using_calc[i]

            calculator(i, li + [using_calc[i]])
            visit[i] = 0


T = int(input())

for tc in range(T):
    n = int(input())
    calc = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    num_max = -1000000000
    num_min = 1000000000

    using_calc = [0]
    visit = [0] * n

    visit2 = []
    empty = []


    for i in range(4):
        for j in range(calc[i]):
            if i == 0:
                using_calc.append('+')
            elif i == 1:
                using_calc.append('-')
            elif i == 2:
                using_calc.append('*')
            else:
                using_calc.append('/')

    calculator(0, empty)

    print('#{}'.format(tc+1), num_max-num_min)


