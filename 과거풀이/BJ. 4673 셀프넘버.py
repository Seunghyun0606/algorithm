# 셀프넘버는 생성자가 없는 숫자.
# 각 자릿수만 더한다. 111 이면 111 + 1 + 1 + 1

def solve(n):

    number = n
    while n:
        number += n % 10
        n = n // 10
    return number


check = [0]*10001

for i in range(1, 10001):
    selfNumber = solve(i)

    if selfNumber < 10001:
        check[selfNumber] = 1
    
for j in range(1, 10001):
    if not check[j]:
        print(j)

