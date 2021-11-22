# BJ.2309 일곱난쟁이

height = [ int(input()) for _ in range(9) ]

all_sum = sum(height)
a1 = 0
a2 = 0

flag = False
result = 0
for i in range(9):
    if flag:
        break
    all_sum = sum(height)
    all_sum -= height[i]
    for j in range(9):
        if i == j:
            continue
        elif all_sum - height[j] == 100:
            result = all_sum - height[j]
            flag = True
            a1 = i
            a2 = j
            break

height1 = []
for k in range(9):
    if k == a1 or k == a2 :
        continue
    height1.append(height[k])

for l in sorted(height1):
    print(l)










