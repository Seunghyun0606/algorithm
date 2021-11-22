# BJ. 2257 화학식량
# H = 1, C = 12, O = 16
# 2 ~ 9 // 50 ~ 57
# C(CO(CO))2
import sys
sys.setrecursionlimit(10**7)

def my_chemi(start, temp):

    for i in range(start, -1, -1):  # start는 len(chemi) - 1 로 시작.
        if using[i]:
            continue
        using[i] = 1
        if chemi[i] == 'H':
            if stack[-1] == ')':
                temp += 1
            elif stack[-1] == 0:
                temp += 1
            else:
                temp += 1 * stack.pop()

        elif chemi[i] == 'C':
            if stack[-1] == ')':
                temp += 12
            elif stack[-1] == 0:
                temp += 12
            else:
                temp += 12 * stack.pop()

        elif chemi[i] == 'O':
            if stack[-1] == ')':
                temp += 16
            elif stack[-1] == 0:
                temp += 16
            else:
                temp += 16 * stack.pop()

        elif chemi[i] == '(':
            stack.pop()
            return temp
        elif chemi[i] == ')':
            stack.append(chemi[i])
            a = my_chemi(i-1, 0)
            if a:
                if stack[-1] == 0 or stack[-1] == ')':
                    temp += a
                else:
                    temp += a * stack.pop()
        # C(CO(CO))2
        else:
            stack.append(int(chemi[i]))
    return temp


chemi = list(input())

using = [0] * len(chemi)
stack = [0]


result = my_chemi(len(chemi)-1, 0)

print(result)

