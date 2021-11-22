# BJ. 1759 암호만들기


def dfs(start, words):
    if len(words) == n:
        count = 0
        for word in words:
            if word in vowels:
                count += 1
        if 0 < count < len(words) - 1:
            print(words)

    else:
        for i in range(start, m):
            dfs(i+1, words + char[i])


n, m = map(int, input().split())

char = sorted(list(input().split()))
vowels = ['a', 'e', 'i', 'o', 'u']

dfs(0, '')


