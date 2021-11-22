# 브루트 포스로 다구해버리자
from itertools import permutations as p
from collections import defaultdict

s = input()
my_per = p(s, len(s))

answer = defaultdict(int)
for per in my_per:
    for i in range(len(per)-1):
        if per[i] == per[i+1]:
            break
    else:
        if not answer[per]:
            answer[per] += 1
print(len(answer))
