while True:
    spells = input()
    if len(spells) == 1:
        break
    stack = []
    flag = False
    for spell in spells:
        if spell in '([':
            stack.append(spell)
        elif spell == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            else:
                flag = True
                break
        elif spell == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    break
            else:
                flag = True
                break
    if stack or flag:
        print('no')
    else:
        print('yes')