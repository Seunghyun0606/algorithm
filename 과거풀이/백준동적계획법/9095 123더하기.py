# 1 - 1
# 2 - 2
# 3 - 4
# 4 - 7
# 5 - 13
# 6 - 24
# 앞에 3개 더하기.

n = int(input())

init = [0, 1, 2, 4]

for i in range(4, 11):
    init.append(sum(init[i-3:i]))

for _ in range(n):
    num = int(input())
    print(init[num])
