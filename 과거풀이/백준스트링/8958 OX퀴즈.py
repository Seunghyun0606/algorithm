T = int(input())

for _ in range(T):
    score = input()
    result = 0
    temp = 1
    for s in score:
        if s == 'O':
            result += temp
            temp += 1
        elif s == 'X':
            temp = 1
    print(result)
        