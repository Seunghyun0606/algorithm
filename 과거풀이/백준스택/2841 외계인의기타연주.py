# stack 문제

import sys
input = sys.stdin.readline
n, p = map(int, input().split())

guitar = [ [] for _ in range(6) ]
result = 0
for _ in range(n):
    line, flat = map(int, input().split())
    flag = False
    while guitar[line-1] and guitar[line-1][-1] >= flat:
        if guitar[line-1][-1] == flat:
            flag = True
            break
        guitar[line-1].pop()
        result += 1
    if flag:
        continue
    guitar[line-1].append(flat)
    result += 1
print(result)