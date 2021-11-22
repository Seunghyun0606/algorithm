# BJ. 1016 제곱 ㄴㄴ 수
# 2 3 5 7 11 13 17... prime number의 제곱.
# min, max가 prime number의 제곱으로 안나눠지면 count

start, last = map(int, input().split())

prime = [2]
check = [0] * (last-start+1)
count = 0

for k in range(last-start+1):
    if check[k]:
        continue
    if (k + start) % (2 ** 2) == 0:
        check[k] = 1
        count += 1


if last < 4:
    print(last-start+1)
else:
    for i in range(3, last+1):  # 여기까지가 소수 구하는 것.
        for j in range(len(prime)):
            if i % prime[j] == 0:  # 나눠지면 더 볼 필요없다.
                break
        else:
            if i**2 >= last:
                break
            prime.append(i)

            for k in range(last-start+1):
                if check[k]:
                    continue
                if (k+start) % (i**2) == 0:
                    check[k] = 1
                    count += 1
print(last - start + 1 - count)

