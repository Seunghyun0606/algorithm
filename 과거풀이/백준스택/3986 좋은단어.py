# 스택 문제, 선이 겹치지 않게 만들어야한다. ABBA 는 BB 위로 AA곡선이 지나니깐 겹치지 않는 것이라고 보는것.
# A와 B로만 이루어져있음.
# str안쓰고 list로 바꾸는 것만으로도 메모리가 늘어난다.

n = int(input())
result = 0
for _ in range(n):
    spells = input()
    stack = []
    for spell in spells:
        if stack and stack[-1] == spell:
            stack.pop()
        else:
            stack.append(spell)
    if not stack:
        result += 1
print(result)