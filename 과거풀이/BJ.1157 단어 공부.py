from collections import defaultdict

word = input().upper()

how_many = defaultdict(int)

for w in word:
    how_many[w] += 1

answer = max(how_many.values())
cnt = 0
for i in how_many.values():
    if i == answer:
        cnt += 1
    if cnt == 2:
        print('?')
        break

else:
    print(max(how_many.keys(), key=(lambda x: how_many[x])))