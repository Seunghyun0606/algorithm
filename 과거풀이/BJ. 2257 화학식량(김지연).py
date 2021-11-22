
arr = list(input())
N = len(arr)
stack = []
result = tmp = tmp_result = t = k = 0

for i in range(N):
    if arr[i] in 'HCO':
        if len(stack) == 0:
            if arr[i] == 'H':
                tmp = 1
                result += 1
            elif arr[i] == 'C':
                tmp = 12
                result += 12
            elif arr[i] == 'O':
                tmp = 16
                result += 16
        else:
            stack.append(arr[i])
    elif arr[i] == '(':
        stack.append(arr[i])
    elif arr[i] == ')':
        tmp_result = 0
        while stack[-1] != '(':
            if stack[-1] == 'H':
                tmp_result += 1
                stack.pop()
            elif stack[-1] == 'C':
                tmp_result += 12
                stack.pop()
            elif stack[-1] == 'O':
                tmp_result += 16
                stack.pop()
            else:
                if stack[-2] == 'H':
                    t = 1
                elif stack[-2] == 'C':
                    t = 12
                elif stack[-2] == 'O':
                    t = 16
                tmp_result += t * int(stack[-1])
                stack.pop()
                stack.pop()
        k += tmp_result
        stack.pop()
        if len(stack) == 0:
            if i+1 < N and arr[i+1] not in '23456789':
                result += k
                k = 0
                tmp_result = 0
            elif i == N - 1:
                result += k
                k = 0
                tmp_result = 0
    else:
        if len(stack) == 0 and k == 0:
            result += tmp * (int(arr[i]) - 1)
        elif len(stack) > 0 and tmp_result != 0:
            tmp_result *= (int(arr[i]) - 1)
            k += tmp_result
            tmp_result = 0
        elif len(stack) == 0 and k != 0:
            result += k * int(arr[i])
            k = 0
        elif len(stack) > 0:
            stack.append(arr[i])

print(result)


