from itertools import combinations as comb

n, m = map(int, input().split())
possi = input().split()

for c in comb(sorted(possi), n):
    flag1 = False
    flag2 = 0
    for i in c:
        if i in 'aeiou':
            flag1 = True
        else:
            flag2 += 1
    if flag1 and flag2 >  1:
        print(''.join(c))


# BJ. 1759 암호만들기

# def dfs(start, words):
#     if len(words) == n:
#         count = 0
#         for word in words:
#             if word in vowels:
#                 count += 1
#         if 0 < count < len(words) - 1:
#             print(words)

#     else:
#         for i in range(start, m):
#             dfs(i+1, words + char[i])


# n, m = map(int, input().split())

# char = sorted(list(input().split()))
# vowels = ['a', 'e', 'i', 'o', 'u']

# dfs(0, '')


