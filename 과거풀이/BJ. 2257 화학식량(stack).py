# BJ. 2257 화학식량(stack)
# 처음에 stack에 다저장해두고 다더하면됨.
# 연산자랑 비슷하게하면될듯
# 런타임에러가뜬다. 왜지?
# (H(O2)3)2 이러경우 안된다 지금.


chemi = list(input())

stack = [0]  # 숫자형태로변형된 값들을 stack에 저장한뒤 꺼내서 계산할거다.
result = 0
flag = False

for i in range(len(chemi)-1, -1, -1):
    if 58 > ord(chemi[i]) > 49:
        stack.append(int(chemi[i]))

    elif chemi[i] == ')':
        temp = 0
        flag = True
        stack.append(')')

    elif chemi[i] == '(':
        stack.pop()
        flag = False
        if temp:
            if stack[-1]:
                result += temp * stack.pop()
            else:
                result += temp

    elif chemi[i] == 'H':
        if stack[-1] == ')':
            temp += 1
        elif stack[-1] == 0:
            result += 1
        else:
            if flag:
                temp += stack.pop() * 1
            else:
                result += stack.pop() * 1

    elif chemi[i] == 'C':
        if stack[-1] == ')':
            temp += 12
        elif stack[-1] == 0:
            result += 12
        else:
            if flag:
                temp += stack.pop() * 12
            else:
                result += stack.pop() * 12

    elif chemi[i] == 'O':
        if stack[-1] == ')':
            temp += 16
        elif stack[-1] == 0:
            result += 16
        else:
            if flag:
                temp += stack.pop() * 16
            else:
                result += stack.pop() * 16

print(result)

