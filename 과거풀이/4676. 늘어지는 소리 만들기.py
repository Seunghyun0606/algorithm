# 4676. 늘어지는 소리 만들기

T = int(input())

for tc in range(T):

    words = input()
    check = [0] * (len(words)+1)

    n = int(input())
    many = list(map(int, input().split()))

    for i in many:
        check[i] += 1

    new = ''
    for i in range(len(words)):
        if check[i]:
            new += '-' * check[i]
        new += words[i]

    if check[-1]:
        new += '-' * check[-1]

    print('#{}'.format(tc+1), new)
