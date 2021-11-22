# BJ. 2231 분해합
# N이 100만 이니깐 자릿수는 6개, 즉 커봐야 999999 -> 54. 한 최대 55개만 세면되겠네.
# 처음 입력받을때 자릿수 몇갠지 세고 * 9 개 밑에서부터 세보자.

n = input()
N = int(n)
length = len(n)

check = N-(length*9)
if check <= 0:
    check = 1

for i in range(check, N):
    temp_sum = 0
    temp_sum += i
    k = i
    for j in range(length-1, -1, -1):
        a = k // (10**j)
        b = k % (10**j)
        k = b
        temp_sum += a
    if temp_sum == N:
        print(i)
        break
else:
    print(0)




