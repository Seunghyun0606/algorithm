n = 1

for i in range(3):
    n *= int(input())

check = [0]*10

for j in str(n):
    check[int(j)] += 1
print(*check, sep='\n')