import sys
from collections import defaultdict
input = sys.stdin.readline

word = input().upper().strip()
dict = defaultdict(int)
dict_list = defaultdict(list)

for w in word:
    dict[w] += 1
# maxkey = max(dict, key=dict.get)
max_val = 1
for k,v in dict.items():
    if v > max_val:
        max_val = v
    dict_list[v].append(k)

if len(dict_list[max_val]) > 1:
    print('?')
else:
    print(''.join(dict_list[max_val]))


# from collections import defaultdict

# word = input().upper()

# how_many = defaultdict(int)

# for w in word:
#     how_many[w] += 1

# answer = max(how_many.values())
# cnt = 0
# for i in how_many.values():
#     if i == answer:
#         cnt += 1
#     if cnt == 2:
#         print('?')
#         break

# else:
#     print(max(how_many.keys(), key=(lambda x: how_many[x])))