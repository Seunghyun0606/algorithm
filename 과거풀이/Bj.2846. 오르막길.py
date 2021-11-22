# Bj.2846 오르막길

n = int(input())

asc = list(map(int, input().split()))
asc += [0]

height = 0
start = asc[0]
i = 0

while True:
    if i + 1 < n+1:
        i += 1
        if asc[i] > asc[i-1]:
            continue
        else:
            end = asc[i-1]
            if end-start > height:
                height = end-start
            start = asc[i]
    else:
        break

print(height)


