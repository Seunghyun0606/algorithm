n = int(input())


for i in range(n):
    m, word = input().split()

    repeat = ''
    for w in word:
        for k in range(int(m)):
            repeat += w
    print(repeat)