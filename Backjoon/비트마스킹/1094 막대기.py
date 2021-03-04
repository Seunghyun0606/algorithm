# 비트마스크 이용하는 문제

bar = int(input())

# 자리수 확인
k = 0
# bit 개수
bit = 0

while bar >= ( 1 << k):
    if bar & ( 1 << k ):
        bit += 1
    k += 1
print(bit)