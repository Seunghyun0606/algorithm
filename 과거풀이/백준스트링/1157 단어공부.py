# 152m // default dict 사용시 236ms

from collections import Counter

counter = Counter(input().upper())
check = counter.most_common()
if len(check) == 1:
    print(check[0][0])
elif check[0][1] == check[1][1]:
    print('?')
else:
    print(check[0][0])


# 깔끔한풀이 80ms 31240kb
# n = input()
# n = n.upper()
# alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# result = []
# for i in alpa:
#   result.append(n.count(i))
# if result.count(max(result)) > 1:
#   print("?")
# else:
#   print(alpa[result.index(max(result))])
# 풀이 2
# s,a=input().lower(),[]
# for i in range(97,123):
#  a.append(s.count(chr(i)))
# print('?'if a.count(max(a))>1 else chr(a.index(max(a))+97).upper())