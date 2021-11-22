# "100-200*300-500+20"	60420
# 딕셔너리로 연산자의 가중치를 주면 더 쉬울거같은데?
# { '*': 2, '+': 1, '-': 0 } 식으로

# 숫자 리스트, operator 리스트 ( 여기서 인덱스 뽑고, 2n + 1 번째마다 넣어준다 )
# 후위 연산자로 만들어서 만들어둔 우선순위를 바탕으로 계산한다.


def posfix(expression, operator):
    result = []
    operator_stack = []

    for express in expression:
        if express in '*+-':
            if operator_stack:
                if operator[operator_stack[-1]] < operator[express]:
                    operator_stack.append(express)
                else:
                    while len(operator_stack) > 0 and operator[operator_stack[-1]] >= operator[express]:
                        result.append(operator_stack.pop())
                    operator_stack.append(express)
            else:
                operator_stack.append(express)
        else:
            result.append(express)
    else:
        while operator_stack:
            result.append(operator_stack.pop())

    stack = []
    for res in result:
        if res in '*+-':
            b = int(stack.pop())
            a = int(stack.pop())
            if res == '*':
                stack.append(a*b)
            elif res == '+':
                stack.append(a+b)
            else:
                stack.append(a-b)
        else:
            stack.append(res)
    return abs(stack[0])


def solution(expression):

    answer = 0

    new_express = []
    operators = ['*', '+', '-']
    given_operators = []        # 연산자 중에서 중복 제거 (우선순위 매기기용)
    # given_operators_all = []  # 1, 3, 5 모든 주어진 연산자 2n + 1 이후에 후위연산자 만들어서 계산하면될듯
    # 그냥 new_express 에 모든 값들 넣고, 이것을 후위연산식으로 변환하고, 새로 받은 딕셔너리 우선순위 바탕으로 계산

    temp_num = ''
    for i in expression:
        if ord(i) < 48:
            if i not in given_operators:
                given_operators.append(i)
            new_express.append(temp_num)  # 숫자 넣고,
            new_express.append(i)              # 연산자 넣고,
            temp_num = ''

        else:
            temp_num += i
    else:
        new_express.append(temp_num)

    kind_given_operators = []
    # # 연산자 우선순위를 모아둔 것들, 딕셔너리형태, 하나씩 꺼내서 for문 돌리면서 우선순위할때 쓰면될듯

    num_given_operators = len(given_operators)
    check = [0]*num_given_operators

    def get_kind_operators(c, k, bin):
        nonlocal check
        bin2 = bin.copy()
        if len(bin) == k:
            kind_given_operators.append(bin)

        else:
            for i in range(k):
                if check[i]:
                    continue
                check[i] = 1
                bin2[given_operators[c]] = i
                get_kind_operators(c+1, k, bin2)
                check[i] = 0

    get_kind_operators(0, num_given_operators, {})

    for operator_set in kind_given_operators:
        a = posfix(new_express, operator_set)
        answer = max(a, answer)
    return answer
