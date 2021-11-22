# BJ. 5397 키로거(스택)
# insert 하나해보고 스택 만들어서 하나해보자.
# 일단 문제의도는 연결리스트 만들라는거 같긴하다.

T = int(input())

for tc in range(T):

    result = []
    stack = []
    for password in list(input()):
        if password == '<':
            if result:
                stack.append(result.pop())
        elif password == '>':
            if stack:
                result.append(stack.pop())
        elif password == '-':
            if result:
                result.pop()
        else:
            result.append(password)

    result += stack[::-1]

    print(*result, sep='')


