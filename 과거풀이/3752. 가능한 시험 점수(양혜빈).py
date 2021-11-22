for t in range(int(input())):
    N = int(input())
    Q_score = list(map(int, input().split()))
    ans, max_val = 0, 0
    numbers = [0] * (sum(Q_score) + 1)
    numbers[0] = 1
    for i in Q_score:
        max_val += i
        for j in range(max_val, -1, -1):
            if numbers[j]:
                numbers[i + j] = 1
        numbers[i] = 1
    for i in numbers:
        if i: ans += 1
    print(numbers)
    print('#{} {}'.format(t+1, ans))
