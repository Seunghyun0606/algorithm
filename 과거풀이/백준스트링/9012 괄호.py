n = int(input())


for _ in range(n):
    stack = []
    ps = input()

    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')