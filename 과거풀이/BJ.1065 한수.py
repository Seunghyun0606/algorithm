def solve(n):

    if n < 100:
        return True

    check = []
    number = n
    while n:
        check.append(n % 10)
        n = n//10

    temp = check[0] - check[1]
    for i in range(1, len(check)-1):
        if temp != (check[i] - check[i+1]):
            return False

    return True



number = int(input())
count = 0

for i in range(1, number+1):
    if solve(i):
        count += 1

print(count)

