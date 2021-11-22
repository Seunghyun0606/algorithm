# BJ. 5575 타임카드


a = []

for i in range(3):
    a.append(list(map(int, input().split())))

result = [ [] for _ in range(3)]

for k in range(3):
    for i in range(2, -1, -1):
        if a[k][i] > a[k][i+3]:
            a[k][i+2] -= 1
            temp = 60 - (a[k][i] - a[k][i+3])
            result[k] = [temp] + result[k]
        else:
            temp = a[k][i+3] - a[k][i]
            result[k] = [temp] + result[k]

for i in range(3):
    print(*result[i])