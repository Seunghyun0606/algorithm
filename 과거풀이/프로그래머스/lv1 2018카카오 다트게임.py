def solution(dartResult):
    answer = 0
    stack = []
    cnt = 0
    for dart in dartResult:

        if dart == 'S':
            temp = stack.pop()
            if cnt > 1:
                temp = stack.pop() + temp
            cnt = 0
            stack.append(int(temp))
        elif dart == 'D':
            temp = stack.pop()
            if cnt > 1:
                temp = stack.pop() + temp
            cnt = 0
            stack.append(int(temp)**2)
        elif dart == 'T':
            temp = stack.pop()
            if cnt > 1:
                temp = stack.pop() + temp
            cnt = 0
            stack.append(int(temp)**3)
        elif dart == '#':
            temp = stack.pop()
            stack.append(temp*(-1))
            # stack.append(-temp)
        
        elif dart == '*':
            temp_stack = []
            count = 0
            while stack and count < 2:
                temp = stack.pop()
                temp_stack.append(temp*2)
                count += 1
            while temp_stack:
                stack.append(temp_stack.pop())            
        else:
            cnt += 1
            stack.append(dart)
    return sum(stack)