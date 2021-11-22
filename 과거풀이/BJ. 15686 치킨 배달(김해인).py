N, M = map(int, input().split())
city = []
houses = []
chickens = []
for n in range(N):
    row = list(map(int, input().split()))
    city.append(row)
    for i in range(N):
        if row[i] == 1:
            houses.append([n, i])
        elif row[i] == 2:
            chickens.append([n, i])
check = [0] * len(chickens)
mymin = []


def dist(check):
    total = 0
    for i in range(len(houses)):
        minval = 2 * N
        for j in range(len(check)):
            if check[j]:
                calc = abs(houses[i][0] - chickens[j][0]) + abs(houses[i][1] - chickens[j][1])
                minval = min(minval, calc)
        total += minval
    mymin.append(total)


def subset(k):
    if k == len(chickens):
        if check.count(1) == M:
            print(check)
            dist(check)
    else:
        check[k] = 0
        subset(k+1)
        check[k] = 1
        subset(k+1)


subset(0)
print(min(mymin))
print(mymin)